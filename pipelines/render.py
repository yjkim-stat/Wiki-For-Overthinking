"""Apply completed summaries and rebuild every generated artifact.

    python -m pipelines.render [--topic slug] [--only archive|wiki|outputs]

This is the deterministic half of the system. It reads ``data/``, applies
anything waiting in ``data/queue/done/``, and rewrites the archive, the wiki and
the outputs. It never fetches and never calls a model, so it is safe to run as
often as you like — and rerunning it after changing a template or a renderer
rebuilds everything from the records already on disk.
"""

from __future__ import annotations

import argparse
import logging
import re
import shutil
from pathlib import Path

from .common import config as config_mod
from .common import log
from .common.config import Config
from .common.llm import get_summarizer
from .common.schema import PaperSummary, VideoSummary, utcnow
from .common.store import RecordStore, read_json
from .enrich.queue import Queue
from .publish import archive as archive_mod
from .publish import lecture_note, report, slides, wiki

_LOG = log.get(__name__)


# ---------------------------------------------------------------------------
# Applying queue results
# ---------------------------------------------------------------------------


def _apply_bibliography(cfg: Config, store: RecordStore, paper, result: dict) -> None:
    """Fold a reader-supplied bibliography into a hand-filed paper.

    Only a local PDF reaches this: it arrives knowing nothing but its filename,
    so the reading step is the only thing that can say what the document is.

    Whether the reading wins depends on what else the record has been seen
    from. While the inbox is its *only* source, everything it holds is a guess
    from a filename — including the title — so the reading replaces it
    outright. Once the same work has also arrived from an index, that metadata
    is better evidence than a reading, and the reading may only fill blanks.
    """
    biblio = result.get("bibliography") or {}
    if not isinstance(biblio, dict):
        return

    guessed = paper.source == "local"

    def take(field_name: str, value) -> bool:
        return bool(value) and (guessed or not getattr(paper, field_name, None))

    for field_name in ("title", "venue", "doi", "arxiv_id", "abstract"):
        value = str(biblio.get(field_name) or "").strip()
        if take(field_name, value):
            setattr(paper, field_name, value)

    authors = [str(a).strip() for a in (biblio.get("authors") or []) if str(a).strip()]
    if take("authors", authors):
        paper.authors = authors

    year = biblio.get("year") or 0
    if isinstance(year, int) and not isinstance(year, bool) and take("year", year):
        paper.year = year
        if take("published", year):
            paper.published = f"{year}-01-01"

    # Topic assignment is the reader's judgement for a hand-filed PDF, but an
    # unknown slug would silently vanish from every output, so it is dropped
    # loudly instead.
    known = {topic.slug for topic in cfg.topics}
    claimed = [str(s).strip() for s in (result.get("topics") or []) if str(s).strip()]
    for slug in claimed:
        if slug not in known:
            _LOG.warning("result for %s claims unknown topic '%s'", paper.id, slug)
        elif slug not in paper.topics:
            paper.topics.append(slug)

    store.save_paper(paper)


def _apply_paper(cfg: Config, store: RecordStore, task: dict) -> bool:
    result = task.get("result") or {}
    paper_id = task["item_id"]
    paper = store.load_paper(paper_id)
    if paper is None:
        _LOG.warning("result for unknown paper %s; skipping", paper_id)
        return False

    if paper.is_local:
        _apply_bibliography(cfg, store, paper, result)

    summary = PaperSummary(
        paper_id=paper_id,
        one_liner=result.get("one_liner", ""),
        problem=result.get("problem", ""),
        contributions=list(result.get("contributions") or []),
        method=result.get("method", ""),
        results=result.get("results", ""),
        limitations=result.get("limitations", ""),
        relevance=dict(result.get("relevance") or {}),
        concepts=list(result.get("concepts") or []),
        methods=list(result.get("methods") or []),
        datasets=list(result.get("datasets") or []),
        tags=list(result.get("tags") or []),
        generated_by=task.get("completed_by", task.get("kind", "")) or "queue",
        generated_at=task.get("completed_at") or utcnow(),
    )
    store.save_paper_summary(summary)
    return True


def _apply_video(cfg: Config, store: RecordStore, task: dict) -> bool:
    result = task.get("result") or {}
    video_id = task["item_id"]
    if store.load_video(video_id) is None:
        _LOG.warning("result for unknown video %s; skipping", video_id)
        return False

    summary = VideoSummary(
        video_id=video_id,
        one_liner=result.get("one_liner", ""),
        abstract=result.get("abstract", ""),
        chapters=list(result.get("chapters") or []),
        key_points=list(result.get("key_points") or []),
        referenced_papers=list(result.get("referenced_papers") or []),
        concepts=list(result.get("concepts") or []),
        methods=list(result.get("methods") or []),
        datasets=list(result.get("datasets") or []),
        tags=list(result.get("tags") or []),
        generated_by=task.get("completed_by", "queue"),
        generated_at=task.get("completed_at") or utcnow(),
    )
    store.save_video_summary(summary)
    return True


def _apply_concept(cfg: Config, store: RecordStore, task: dict) -> bool:
    from .publish.wiki import slug_for

    result = task.get("result") or {}
    name = task["item_id"]
    slug = slug_for(name)
    concept = store.load_concept(slug)
    if concept is None:
        _LOG.warning("definition for unknown entity '%s'; skipping", name)
        return False

    concept.definition = result.get("definition", "").strip()
    declared = result.get("kind")
    if declared in ("concept", "method", "dataset"):
        concept.kind = declared
    for alias in result.get("aliases") or []:
        if alias and alias not in concept.aliases:
            concept.aliases.append(alias)
    for related in result.get("related") or []:
        related_slug = slug_for(related)
        if related_slug and related_slug not in concept.related:
            concept.related.append(related_slug)
    store.save_concept(concept)
    return True


_APPLIERS = {"paper": _apply_paper, "video": _apply_video, "concept": _apply_concept}


def apply_completed(cfg: Config) -> dict[str, int]:
    """Fold every finished task into the records, then archive the task file."""
    store = RecordStore(cfg.layout)
    queue = Queue(cfg.layout)
    applied = {"paper": 0, "video": 0, "concept": 0, "skipped": 0}

    for task in list(queue.iter_done()):
        applier = _APPLIERS.get(task.get("kind", ""))
        if applier is None:
            _LOG.warning("unknown task kind in %s", task.get("task_id"))
            applied["skipped"] += 1
            continue
        try:
            ok = applier(cfg, store, task)
        except Exception:  # noqa: BLE001 - one bad result must not block the rest
            _LOG.exception("failed to apply %s", task.get("task_id"))
            applied["skipped"] += 1
            continue
        if ok:
            applied[task["kind"]] += 1
            queue.archive(task["task_id"])
        else:
            applied["skipped"] += 1

    if any(applied.values()):
        _LOG.info("applied queue results: %s", applied)
    return applied


# ---------------------------------------------------------------------------
# Rebuilding
# ---------------------------------------------------------------------------


def rebuild_archive(cfg: Config) -> dict[str, int]:
    store = RecordStore(cfg.layout)
    papers = videos = 0

    # Clear before regenerating, so the claim that `archive/` is a pure
    # function of `data/` is actually true. A paper's page path contains its
    # year, and a year can arrive after the page does — from a deduplication
    # merge, or from reading a hand-filed PDF that had no metadata at all.
    # Without this the old path survives as a second, stale copy.
    # `archive/daily/` is left alone: digests are dated records of a run, not
    # derived from the store, and nothing regenerates them.
    for directory in (cfg.layout.archive_papers, cfg.layout.archive_seminars):
        shutil.rmtree(directory, ignore_errors=True)
        directory.mkdir(parents=True, exist_ok=True)

    for paper in store.iter_papers():
        archive_mod.write_paper_page(
            cfg.layout, paper, store.load_paper_summary(paper.id)
        )
        papers += 1

    for video in store.iter_videos():
        archive_mod.write_seminar_page(
            cfg.layout,
            video,
            store.load_video_summary(video.id),
            store.load_transcript(video.id),
        )
        videos += 1

    store.rebuild_indexes()
    archive_mod.write_archive_index(cfg)
    _LOG.info("archive rebuilt: %d paper page(s), %d seminar page(s)", papers, videos)
    return {"papers": papers, "videos": videos}


def _queue_and_summarizer(cfg: Config):
    queue = Queue(
        cfg.layout,
        max_pending=int(
            (cfg.settings.get("summarize", {}) or {}).get("max_pending_tasks", 0)
        )
        or None,
    )
    return queue, get_summarizer(cfg.settings, enqueue=queue.enqueue)


def queue_missing_summaries(cfg: Config) -> int:
    """File a task for any stored record that still has no summary.

    Collection queues a task when it first sees an item, but a task can be lost
    — deleted by hand, dropped when the queue was at its cap, or belonging to a
    record that was added some other way. Without this the item would sit in the
    archive unread forever, so the check is repeated on every render and the
    queue heals itself.
    """
    store = RecordStore(cfg.layout)
    queue, summarizer = _queue_and_summarizer(cfg)
    queued = 0

    for paper in store.iter_papers():
        if store.paper_summary_path(paper.id).exists():
            continue
        # A collected paper with no topic matched nothing and is not worth
        # reading. A hand-filed one has not been read yet, so it has no topics
        # *because* nobody has looked at it — that is the task, not a reason to
        # skip it, and the reader is shown every topic to choose from.
        if paper.is_local:
            context = cfg.topic_context(paper.topics or [t.slug for t in cfg.topics])
        elif paper.topics:
            context = cfg.topic_context(paper.topics)
        else:
            continue
        if summarizer.summarize_paper(paper, context, cfg.language) is None:
            queued += 1

    for video in store.iter_videos():
        if not video.topics or store.video_summary_path(video.id).exists():
            continue
        if summarizer.summarize_video(
            video,
            store.load_transcript(video.id),
            cfg.topic_context(video.topics),
            cfg.language,
        ) is None:
            queued += 1

    if queued:
        _LOG.info("re-queued %d missing summary task(s)", queued)
    return queued


def queue_missing_definitions(cfg: Config) -> int:
    """Ask for a definition for every promoted entity that still lacks one.

    This is what makes the wiki extend itself: a concept that turns up in a
    second independent source stops being a bare name and becomes a note with
    an actual definition, without anyone requesting it.
    """
    store = RecordStore(cfg.layout)
    _, summarizer = _queue_and_summarizer(cfg)

    concepts = {c.slug: c for c in store.iter_concepts()}
    live = wiki.promoted(cfg, concepts)

    queued = 0
    for concept in wiki.undefined_concepts(cfg, live):
        sources = [
            {
                "kind": item.get("kind", ""),
                "title": item.get("title", ""),
                "note": item.get("note", ""),
                "topics": concept.topics,
            }
            for item in concept.evidence
        ]
        if summarizer.define_concept(concept.name, sources, cfg.language) is None:
            queued += 1

    if queued:
        _LOG.info("queued %d definition task(s)", queued)
    return queued


def _relative(cfg: Config, path: Path) -> str:
    try:
        return path.relative_to(cfg.layout.root).as_posix()
    except ValueError:
        return path.as_posix()


def shelve_documents(cfg: Config) -> dict[str, int]:
    """File each paper's document by whether its reading is done.

    ``data/pdfs/`` holds what is still waiting to be read and
    ``data/pdfs/read/`` holds what has been. The point is that the backlog
    becomes visible on disk: before this, both populations sat in one directory
    and the only way to tell them apart was to consult the queue.

    The pass is **self-healing rather than transactional**, which matters
    because a move and a record update cannot be made atomic together. Every run
    re-derives where each file belongs from the one fact that decides it — does
    a summary exist — and corrects whatever it finds. A crash between the move
    and the save leaves a record pointing at the old path; the next render
    notices the file at the other path and repairs the pointer. Nothing has to
    be rolled back.

    A missing file is left alone. PDFs are not committed, so a fresh clone has
    records whose documents are simply not here yet, and rewriting their paths
    would turn an absence into corruption.
    """
    store = RecordStore(cfg.layout)
    counts = {"shelved": 0, "returned": 0, "repaired": 0}

    for paper in store.iter_papers():
        if not paper.local_path:
            continue
        name = Path(paper.local_path).name
        read = store.paper_summary_path(paper.id).exists()
        belongs = (cfg.layout.pdfs_read if read else cfg.layout.pdfs) / name
        elsewhere = (cfg.layout.pdfs if read else cfg.layout.pdfs_read) / name
        current = cfg.layout.root / paper.local_path

        if belongs.exists():
            wanted = _relative(cfg, belongs)
            if paper.local_path != wanted:
                paper.local_path = wanted
                store.save_paper(paper)
                counts["repaired"] += 1
            continue

        source = current if current.exists() else (
            elsewhere if elsewhere.exists() else None
        )
        if source is None:
            continue

        belongs.parent.mkdir(parents=True, exist_ok=True)
        source.replace(belongs)
        paper.local_path = _relative(cfg, belongs)
        store.save_paper(paper)
        # A reading can be withdrawn by clearing its summary, so the move runs
        # both ways: what is in `pdfs/` is exactly what is unread.
        counts["shelved" if read else "returned"] += 1

    if any(counts.values()):
        _LOG.info("documents filed: %s", counts)
    return counts


# A hand-written section may declare how many sources it was written against.
_ANALYSIS_SOURCES_RE = re.compile(r"<!--\s*analysis-sources:\s*(\d+)\s*-->")


def _definition_source_count(queue: Queue, name: str) -> int | None:
    """How many sources the definition task for ``name`` was written against."""
    task_id = Queue.task_id("concept", name)
    for path in (queue.archive_path(task_id), queue.done_path(task_id)):
        task = read_json(path)
        if task:
            count = ((task.get("payload") or {}).get("source_count"))
            return count if isinstance(count, int) else None
    return None


def stale_definitions(cfg: Config) -> list[dict]:
    """Definitions whose evidence has grown since they were written.

    Every counter in this system measures whether something is *unwritten*.
    None measured whether it was *out of date* — so a definition was written
    once and never revisited, however far its evidence outgrew it. The result
    is a note that reads as complete while describing a subset of its own
    sources: "in all three sources" standing at nine, or a claim a later source
    flatly contradicts. Not thin. Wrong, and confidently so.

    The consequence governs how the archive is operated, so it is worth stating
    plainly: **an empty queue means nothing is unwritten. It does not mean
    nothing is out of date.**

    The recorded count is used rather than a phrase match because it also
    catches the more dangerous kind — a definition that enumerates its sources
    by name reads as exhaustive while describing four of ten.
    """
    store = RecordStore(cfg.layout)
    queue = Queue(cfg.layout)

    stale: list[dict] = []
    for concept in store.iter_concepts():
        if not concept.definition.strip():
            continue
        written_for = _definition_source_count(queue, concept.name)
        now = len(concept.evidence)
        if written_for is not None and now > written_for:
            stale.append(
                {
                    "slug": concept.slug,
                    "name": concept.name,
                    "written_for": written_for,
                    "sources_now": now,
                }
            )
    return sorted(stale, key=lambda row: row["written_for"] - row["sources_now"])


def stale_analysis(cfg: Config) -> list[dict]:
    """Hand-written sections that declared a source count and have been outgrown.

    The same rot reaches the prose under ``auto:end``, which is where the
    archive's actual reasoning lives — and there it is *structurally*
    undetectable. A definition has a countable evidence base and a recorded
    count, so staleness is arithmetic; prose declares no dependency on anything.

    So this lets it declare one. A section ending with ``<!-- analysis-sources:
    40 -->`` is checked against the note's evidence count. Opt-in, because some
    prose genuinely does not depend on the count.

    This is the weaker half and should be read as such: it relies on authors
    maintaining the marker. It is still better than the alternative, which is
    that the most valuable artifact in the repository is the only one with no
    integrity check at all.
    """
    store = RecordStore(cfg.layout)
    concepts = {c.slug: c for c in store.iter_concepts()}
    _, end_marker = wiki._markers(cfg)

    stale: list[dict] = []
    for kind in wiki.KINDS:
        for path in sorted(cfg.layout.wiki_kind_dir(kind).glob("*.md")):
            concept = concepts.get(path.stem)
            if concept is None:
                continue
            match = _ANALYSIS_SOURCES_RE.search(wiki._preserved_tail(path, end_marker))
            if match is None:
                continue
            written_for = int(match.group(1))
            now = len(concept.evidence)
            if now > written_for:
                stale.append(
                    {
                        "slug": concept.slug,
                        "path": str(path),
                        "written_for": written_for,
                        "sources_now": now,
                    }
                )
    return stale


def report_staleness(cfg: Config) -> dict[str, int]:
    """Count what has been outgrown, and say so. Never rewrites anything.

    Reporting only, deliberately. Re-deriving a definition means reading its
    sources; a counter must not discard written work on arithmetic alone. To
    re-queue one, clear ``definition`` in ``data/concepts/<slug>.json`` and
    render again.
    """
    definitions = stale_definitions(cfg)
    analysis = stale_analysis(cfg)

    for row in definitions[:10]:
        _LOG.warning(
            "definition for '%s' was written against %d source(s); there are now %d",
            row["name"],
            row["written_for"],
            row["sources_now"],
        )
    if len(definitions) > 10:
        _LOG.warning("... and %d more stale definition(s)", len(definitions) - 10)
    for row in analysis:
        _LOG.warning(
            "analysis in %s declares %d source(s); there are now %d",
            row["path"],
            row["written_for"],
            row["sources_now"],
        )

    return {"definitions": len(definitions), "analysis": len(analysis)}


def rebuild_outputs(cfg: Config, topic_slugs: list[str] | None = None) -> dict[str, int]:
    from .publish.material import gather

    topics = cfg.topics
    if topic_slugs:
        topics = [t for t in topics if t.slug in set(topic_slugs)]

    counts = {"lecture_notes": 0, "slides": 0, "reports": 0}
    for topic in topics:
        material = gather(cfg, topic)
        if topic.wants("lecture_note"):
            lecture_note.build(cfg, topic, material)
            counts["lecture_notes"] += 1
        if topic.wants("slides"):
            slides.build(cfg, topic, material)
            counts["slides"] += 1
        if topic.wants("report"):
            report.build(cfg, topic, material)
            counts["reports"] += 1
    return counts


def run(
    cfg: Config,
    *,
    topic_slugs: list[str] | None = None,
    only: str | None = None,
    skip_queueing: bool = False,
) -> dict:
    """Apply results and rebuild. ``only`` limits which stage runs."""
    cfg.layout.ensure()
    result: dict = {}

    if only in (None, "archive"):
        result["applied"] = apply_completed(cfg)
        # After applying, so a reading finished this run files its document too.
        result["documents"] = shelve_documents(cfg)
        result["archive"] = rebuild_archive(cfg)
        if not skip_queueing:
            result["summaries_queued"] = queue_missing_summaries(cfg)

    if only in (None, "wiki"):
        result["wiki"] = wiki.update(cfg)
        if not skip_queueing:
            result["definitions_queued"] = queue_missing_definitions(cfg)
        # Reported, never acted on: an empty queue means nothing is unwritten,
        # not that nothing is out of date.
        result["stale"] = report_staleness(cfg)

    if only in (None, "outputs"):
        result["outputs"] = rebuild_outputs(cfg, topic_slugs)

    _LOG.info("render complete: %s", result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.render",
        description="Apply completed summaries and rebuild every artifact.",
    )
    parser.add_argument(
        "--topic", action="append", dest="topics", help="restrict outputs to a topic"
    )
    parser.add_argument(
        "--only",
        choices=["archive", "wiki", "outputs"],
        help="run a single stage instead of all three",
    )
    parser.add_argument(
        "--no-queue",
        action="store_true",
        dest="no_queue",
        help="rebuild only; do not file any new summary or definition tasks",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root", type=Path, default=None, help="repository root (for testing)"
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    log.setup(cfg.layout.logs, logging.DEBUG if args.verbose else logging.INFO)

    run(
        cfg,
        topic_slugs=args.topics,
        only=args.only,
        skip_queueing=args.no_queue,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
