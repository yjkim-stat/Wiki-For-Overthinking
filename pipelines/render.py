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
from .common import paths as P
from .common.config import Config
from .common.llm import get_summarizer
from .common.store import RecordStore, read_json
from .enrich import apply as apply_mod
from .enrich import concepts as concepts_mod
from .enrich.queue import Queue
from .publish import archive as archive_mod
from .publish import lecture_note, report, slides, wiki

_LOG = log.get(__name__)


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


def queue_missing_summaries(cfg: Config) -> dict[str, int]:
    """File a task for any stored record that still has no summary.

    Collection queues a task when it first sees an item, but a task can be lost
    — deleted by hand, dropped when the queue was at its cap, or belonging to a
    record that was added some other way. Without this the item would sit in the
    archive unread forever, so the check is repeated on every render and the
    queue heals itself.

    Returns three numbers that used to be one, and the one was wrong. What was
    reported as `summaries_queued` counted *records without a summary* — the
    backlog — because a queue backend defers every item it is handed and the
    count was taken from that. It therefore read the same on every render
    however little was filed, which is how a defect that filed nothing for weeks
    went unnoticed. `unread` is that number, under its own name; `queued` and
    `refreshed` are what the queue actually wrote.
    """
    store = RecordStore(cfg.layout)
    queue, summarizer = _queue_and_summarizer(cfg)
    unread = 0

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
            unread += 1

    for video in store.iter_videos():
        if not video.topics or store.video_summary_path(video.id).exists():
            continue
        if summarizer.summarize_video(
            video,
            store.load_transcript(video.id),
            cfg.topic_context(video.topics),
            cfg.language,
        ) is None:
            unread += 1

    counts = {"unread": unread, "queued": queue.filed, "refreshed": queue.refreshed}
    if queue.filed or queue.refreshed:
        _LOG.info(
            "summary tasks: %d filed, %d refreshed (%d record(s) still unread)",
            queue.filed,
            queue.refreshed,
            unread,
        )
    return counts


def queue_missing_definitions(cfg: Config) -> dict[str, int]:
    """Ask for a definition for every promoted entity that still lacks one.

    This is what makes the wiki extend itself: a concept that turns up in a
    second independent source stops being a bare name and becomes a note with
    an actual definition, without anyone requesting it.
    """
    store = RecordStore(cfg.layout)
    queue, summarizer = _queue_and_summarizer(cfg)

    concepts = {c.slug: c for c in store.iter_concepts()}
    live = concepts_mod.promoted(cfg, concepts)

    undefined = 0
    for concept in concepts_mod.undefined_concepts(cfg, live):
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
            undefined += 1

    counts = {
        "undefined": undefined,
        "queued": queue.filed,
        "refreshed": queue.refreshed,
    }
    if queue.filed or queue.refreshed:
        _LOG.info(
            "definition tasks: %d filed, %d refreshed (%d entity/entities still "
            "undefined)",
            queue.filed,
            queue.refreshed,
            undefined,
        )
    return counts


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


def queue_stale_definitions(cfg: Config) -> dict[str, int]:
    """Ask again for a definition whose evidence has outgrown it.

    `stale_definitions` reports; this is the step that does something about it,
    and the distinction it has to preserve is the one `CLAUDE.md` states: **a
    counter must not discard written work on arithmetic alone.**

    So nothing is rewritten and nothing is cleared. The concept keeps its
    definition, and a task is filed carrying that definition back to a reader
    with the question "what has changed" rather than "what is this". A refresh
    nobody answers leaves the archive exactly as it was, which is the property
    that makes it safe to file one automatically at all.

    Two bounds, because staleness is a standing condition rather than an event
    and an unbounded response to it would refill the queue every render:

    **A ratio, not any growth at all.** A definition written against three
    sources standing at nine is describing a third of its evidence; one written
    against forty standing at forty-six is not. Re-asking on every new mention
    would spend a reader's night on definitions that are still true.

    **A cap per render**, so a long-neglected archive drains over several
    passes, worst first, instead of producing a backlog nobody can face.
    """
    settings = cfg.settings.get("wiki", {}) or {}
    ratio = float(settings.get("refresh_definition_at", 0) or 0)
    counts = {"stale": 0, "eligible": 0, "queued": 0}
    if ratio <= 0:
        # Off by default is deliberate. A deployment that has never seen this
        # feature should not have its queue grow because it upgraded.
        return counts

    cap = int(settings.get("max_refresh_tasks", 5) or 0)
    store = RecordStore(cfg.layout)
    queue, summarizer = _queue_and_summarizer(cfg)

    rows = stale_definitions(cfg)
    counts["stale"] = len(rows)
    for row in rows:  # already sorted: most outgrown first
        # `written_for` of zero would make any ratio pass; a definition is
        # written against at least one source or it is not written.
        written_for = max(1, int(row["written_for"]))
        if row["sources_now"] < written_for * ratio:
            continue
        counts["eligible"] += 1
        if counts["queued"] >= cap:
            continue

        concept = store.load_concept(row["slug"])
        if concept is None or not concept.definition.strip():
            continue
        sources = [
            {
                "kind": item.get("kind", ""),
                "title": item.get("title", ""),
                "note": item.get("note", ""),
                "topics": concept.topics,
            }
            for item in concept.evidence
        ]
        summarizer.define_concept(
            concept.name, sources, cfg.language, previous=concept.definition
        )
        counts["queued"] += 1

    if counts["queued"]:
        _LOG.info(
            "asked again for %d definition(s) their evidence has outgrown "
            "(%d eligible of %d stale)",
            counts["queued"],
            counts["eligible"],
            counts["stale"],
        )
    elif counts["eligible"]:
        _LOG.info(
            "%d definition(s) eligible for a refresh; none filed (cap %d)",
            counts["eligible"],
            cap,
        )
    return counts


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
        result["applied"] = apply_mod.completed(cfg)
        # After applying, so a reading finished this run files its document too.
        result["documents"] = shelve_documents(cfg)
        result["archive"] = rebuild_archive(cfg)
        if not skip_queueing:
            summaries = queue_missing_summaries(cfg)
            result["summaries_queued"] = summaries["queued"]
            result["summaries_refreshed"] = summaries["refreshed"]
            result["summaries_unread"] = summaries["unread"]

    if only in (None, "wiki"):
        # Derive first, draw second. The renderer is handed the entities rather
        # than deriving them, so this is the only place in the wiki stage that
        # writes to `data/`.
        concepts, live = concepts_mod.rebuild(cfg)
        result["wiki"] = wiki.update(cfg, concepts, live)
        if not skip_queueing:
            definitions = queue_missing_definitions(cfg)
            result["definitions_queued"] = definitions["queued"]
            result["definitions_refreshed"] = definitions["refreshed"]
            result["definitions_undefined"] = definitions["undefined"]
            # After the missing ones. An entity with no definition at all is a
            # worse gap than one whose definition is behind its evidence, and
            # they share the queue's cap.
            result["definitions_reasked"] = queue_stale_definitions(cfg)["queued"]
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
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
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
