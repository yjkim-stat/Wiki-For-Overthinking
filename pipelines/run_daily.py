"""Daily collection run.

    python -m pipelines.run_daily [--days N] [--topic slug] [--source arxiv] [--dry-run]

Collects, scores, deduplicates, stores, and files a summarization task for
everything that cleared its topic threshold. It deliberately stops there: the
summaries themselves are produced by whatever backend ``summarize.backend``
names, and applied by ``pipelines/render.py``. Splitting the two means a failed
or slow summarization step never costs a day of collection.

Every source is optional at runtime. If arXiv is unreachable the run still
completes with whatever the other sources returned, and the failure is recorded
in the day's digest.
"""

from __future__ import annotations

import argparse
import logging
import re
from datetime import date, timedelta
from pathlib import Path

from .collect import (
    arxiv,
    arxiv_listing,
    conferences,
    curated,
    local_pdf,
    pdf_fetch,
    youtube,
)
from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config, Topic
from .common.llm import get_summarizer
from .common.schema import Paper, Video, strip_arxiv_version
from .common.store import RecordStore, SeenStore, append_jsonl, write_json
from .enrich import coverage
from .enrich.dedupe import Deduplicator
from .enrich.queue import Queue
from .enrich.score import score_against_topics
from .publish import archive as archive_mod

_LOG = log.get(__name__)

_ARXIV_ID = re.compile(r"(?:arxiv:)?(\d{4}\.\d{4,5})(v\d+)?$", re.IGNORECASE)


def _snapshot(cfg: Config, day: date, name: str, records: list) -> None:
    """Keep the raw collector output so a parsing bug can be replayed later."""
    if not records:
        return
    write_json(
        cfg.layout.raw / day.isoformat() / f"{name}.json",
        [r.to_dict() for r in records],
    )


def _seed_papers(
    cfg: Config,
    topics: list[Topic],
    store: RecordStore,
    errors: list[str] | None = None,
) -> list[Paper]:
    """Fetch a topic's anchor papers once, on the first run that needs them."""
    wanted: list[str] = []
    for topic in topics:
        for seed in topic.seed_papers:
            match = _ARXIV_ID.match(seed.strip())
            if not match:
                _LOG.info(
                    "seed '%s' for topic '%s' is not an arXiv id; add it by hand",
                    seed,
                    topic.slug,
                )
                continue
            arxiv_id = strip_arxiv_version(match.group(1))
            if store.load_paper(f"arxiv:{arxiv_id}") is None:
                wanted.append(arxiv_id)

    if not wanted:
        return []
    _LOG.info("fetching %d seed paper(s)", len(wanted))
    return arxiv.fetch_by_id(cfg, sorted(set(wanted)), errors=errors)


def _score_paper(cfg: Config, paper: Paper, topics: list[Topic]) -> bool:
    scores, matched, accepted = score_against_topics(
        topics,
        title=paper.title,
        body=paper.abstract,
        authors=paper.authors,
        settings=cfg.settings,
    )
    paper.scores = scores
    paper.matched_keywords = matched
    paper.topics = accepted
    return bool(accepted)


def _score_video(cfg: Config, video: Video, topics: list[Topic]) -> bool:
    scores, matched, accepted = score_against_topics(
        topics,
        title=video.title,
        body=video.description,
        settings=cfg.settings,
    )
    video.scores = scores
    video.matched_keywords = matched
    video.topics = accepted
    return bool(accepted)


def run(
    cfg: Config,
    *,
    days: int = 2,
    topic_slugs: list[str] | None = None,
    sources: list[str] | None = None,
    dry_run: bool = False,
) -> dict:
    """Execute one collection run. Returns a summary of what happened."""
    cfg.layout.ensure()

    topics = cfg.topics
    if topic_slugs:
        topics = [t for t in topics if t.slug in set(topic_slugs)]
    if not topics:
        _LOG.warning(
            "no topics to run. Add one with `scripts/new_topic.sh \"Name\"` "
            "or check --topic."
        )
        return {"papers": 0, "videos": 0, "queued": 0, "errors": ["no topics defined"]}

    sources = sources or ["arxiv", "conferences", "curated", "youtube", "local"]
    today = date.today()
    since = today - timedelta(days=max(1, days))
    errors: list[str] = []

    store = RecordStore(cfg.layout)
    # One budget for the whole run. Documents are fetched a paper at a time, as
    # each task is filed, so the cap has to outlive the call that spends it.
    pdf_budget = pdf_fetch.Budget.from_settings(cfg)

    # -- collect ------------------------------------------------------------
    papers: list[Paper] = []
    videos: list[Video] = []

    if "arxiv" in sources:
        try:
            found = arxiv.collect(cfg, topics, since, errors=errors)
            _snapshot(cfg, today, "arxiv", found)
            papers += found
        except Exception as exc:  # noqa: BLE001 - a dead source is not fatal
            _LOG.exception("arxiv collection failed")
            errors.append(f"arxiv: {exc}")

    if "conferences" in sources:
        try:
            found = conferences.collect(cfg, topics, since, errors=errors)
            _snapshot(cfg, today, "conferences", found)
            papers += found
        except Exception as exc:  # noqa: BLE001
            _LOG.exception("conference collection failed")
            errors.append(f"conferences: {exc}")

    if "curated" in sources:
        try:
            found = curated.collect(cfg, topics, since, store=store, errors=errors)
            _snapshot(cfg, today, "curated", found)
            papers += found
        except Exception as exc:  # noqa: BLE001
            _LOG.exception("curated list collection failed")
            errors.append(f"curated: {exc}")

    if "youtube" in sources:
        try:
            found = youtube.collect(cfg, topics, since, errors=errors)
            _snapshot(cfg, today, "youtube", found)
            videos += found
        except Exception as exc:  # noqa: BLE001
            _LOG.exception("youtube collection failed")
            errors.append(f"youtube: {exc}")

    if "local" in sources:
        try:
            found = local_pdf.collect(
                cfg, topics, since, dry_run=dry_run, errors=errors
            )
            _snapshot(cfg, today, "local", found)
            papers += found
        except Exception as exc:  # noqa: BLE001
            _LOG.exception("local pdf ingestion failed")
            errors.append(f"local: {exc}")

    # Independent of collection: the sweep records what each announcement day
    # held and keeps an abstract for all of it, so a threshold can be revisited
    # later without re-collecting. It files nothing and queues nothing.
    if "arxiv" in sources and not dry_run:
        try:
            arxiv_listing.sweep(cfg, topics, store, errors=errors)
        except Exception as exc:  # noqa: BLE001 - bookkeeping must not sink a run
            _LOG.exception("arxiv sweep failed")
            errors.append(f"arxiv_sweep: {exc}")

    try:
        papers += _seed_papers(cfg, topics, store, errors)
    except Exception as exc:  # noqa: BLE001
        _LOG.exception("seed paper lookup failed")
        errors.append(f"seeds: {exc}")

    _LOG.info("collected %d paper(s), %d video(s)", len(papers), len(videos))

    if dry_run:
        accepted_papers = [
            p for p in papers if _score_paper(cfg, p, topics) or p.is_local
        ]
        accepted_videos = [v for v in videos if _score_video(cfg, v, topics)]
        _LOG.info(
            "dry run: %d paper(s) and %d video(s) would be archived",
            len(accepted_papers),
            len(accepted_videos),
        )
        return {
            "papers": len(accepted_papers),
            "videos": len(accepted_videos),
            "queued": 0,
            "errors": errors,
            "dry_run": True,
        }

    # -- score, deduplicate, store -----------------------------------------
    queue = Queue(
        cfg.layout,
        max_pending=int(
            (cfg.settings.get("summarize", {}) or {}).get("max_pending_tasks", 0)
        )
        or None,
    )
    summarizer = get_summarizer(cfg.settings, enqueue=queue.enqueue)

    new_papers: list[Paper] = []
    new_videos: list[Video] = []
    rejected: list[dict] = []
    queued = 0

    with SeenStore(cfg.layout.seen_db) as seen:
        deduper = Deduplicator(seen, store)

        for paper in papers:
            # Filing a PDF by hand *is* the editorial decision that scoring
            # exists to approximate, so a local paper is kept whatever its
            # keywords say. Scoring still runs: the topics it happens to match
            # are worth recording, and the reader can add the ones it missed.
            if not _score_paper(cfg, paper, topics) and not paper.is_local:
                rejected.append(
                    {
                        "id": paper.id,
                        "title": paper.title,
                        "source": paper.source,
                        "scores": paper.scores,
                        "day": today.isoformat(),
                    }
                )
                continue

            record, is_new = deduper.resolve_paper(paper)
            store.save_paper(record)
            if is_new:
                new_papers.append(record)

            if not store.paper_summary_path(record.id).exists():
                # Fetch the document before filing the task, so the reader is
                # handed the paper rather than a claim about it. Failure is
                # ordinary: the task is filed either way, with an abstract.
                try:
                    pdf_fetch.fetch_for(
                        cfg, [record], errors=errors, budget=pdf_budget
                    )
                except Exception as exc:  # noqa: BLE001 - never block a reading
                    _LOG.exception("pdf fetch failed for %s", record.id)
                    errors.append(f"pdf[{record.id}]: {exc}")
                else:
                    if record.local_path:
                        store.save_paper(record)

                # A hand-filed PDF has not been read yet, so which topics it
                # belongs to is the reader's question. Show them all of them.
                slugs = record.topics
                if record.is_local and not slugs:
                    slugs = [t.slug for t in cfg.topics]
                if summarizer.summarize_paper(
                    record, cfg.topic_context(slugs), cfg.language
                ) is None:
                    queued += 1

        fetch_transcripts = bool(
            (cfg.sources.get("youtube", {}) or {}).get("fetch_transcripts", True)
        )
        for video in videos:
            if not _score_video(cfg, video, topics):
                rejected.append(
                    {
                        "id": video.id,
                        "title": video.title,
                        "source": video.source,
                        "scores": video.scores,
                        "day": today.isoformat(),
                    }
                )
                continue

            record, is_new = deduper.resolve_video(video)

            transcript = store.load_transcript(record.id)
            if fetch_transcripts and not transcript:
                transcript = youtube.fetch_transcript(record.source_id)
                if transcript:
                    store.save_transcript(record.id, transcript)
            record.transcript_available = bool(transcript)
            record.transcript_chars = len(youtube.transcript_text(transcript))

            store.save_video(record)
            if is_new:
                new_videos.append(record)

            if not store.video_summary_path(record.id).exists():
                if summarizer.summarize_video(
                    record, transcript, cfg.topic_context(record.topics), cfg.language
                ) is None:
                    queued += 1

        seen.commit()

    if rejected:
        append_jsonl(cfg.layout.index / "rejected.jsonl", rejected)

    # -- render what we can already show ------------------------------------
    for paper in new_papers:
        archive_mod.write_paper_page(cfg.layout, paper, store.load_paper_summary(paper.id))
    for video in new_videos:
        archive_mod.write_seminar_page(
            cfg.layout,
            video,
            store.load_video_summary(video.id),
            store.load_transcript(video.id),
        )

    store.rebuild_indexes()
    archive_mod.write_daily_digest(
        cfg,
        today,
        papers=new_papers,
        videos=new_videos,
        queue_stats=queue.stats(),
        errors=errors,
    )
    archive_mod.write_archive_index(cfg)

    result = {
        "papers": len(new_papers),
        "videos": len(new_videos),
        "rejected": len(rejected),
        "queued": queued,
        # What each announcement day held, against what we hold of it. A short
        # day is a debt to pay down, not a quiet day.
        "coverage": coverage.summarize(cfg.layout),
        "errors": errors,
    }
    _LOG.info("run complete: %s", result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.run_daily",
        description="Collect today's papers and seminars for every tracked topic.",
    )
    parser.add_argument(
        "--days", type=int, default=None, help="lookback window (default from settings)"
    )
    parser.add_argument(
        "--topic", action="append", dest="topics", help="restrict to a topic slug"
    )
    parser.add_argument(
        "--source",
        action="append",
        dest="sources",
        choices=["arxiv", "conferences", "curated", "youtube", "local"],
        help="restrict to one or more sources",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="collect and score, but write nothing and queue nothing",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    log.setup(cfg.layout.logs, logging.DEBUG if args.verbose else logging.INFO)

    days = args.days
    if days is None:
        days = int((cfg.settings.get("collect", {}) or {}).get("lookback_days", 2))

    result = run(
        cfg,
        days=days,
        topic_slugs=args.topics,
        sources=args.sources,
        dry_run=args.dry_run,
    )
    return 1 if result.get("errors") and not result.get("papers") else 0


if __name__ == "__main__":
    raise SystemExit(main())
