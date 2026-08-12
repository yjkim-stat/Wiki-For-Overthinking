"""Folding finished readings into the records.

The queue hands back an answer; this is what turns it into archive. It is the
last step at which a reading is still a *result* rather than a record, so every
judgement about which of two sources wins lives here -- most of it in
``_apply_bibliography``, where a reader's reading of a hand-filed PDF competes
with metadata an index may have supplied since.

It sits under ``enrich/`` because it writes to ``data/``. Rendering reads the
records this produces and never changes them; keeping the two apart is what
lets the code be replaced while the archive keeps accumulating.
"""

from __future__ import annotations

from ..common.config import Config
from ..common.log import get
from ..common.schema import PaperSummary, VideoSummary, utcnow
from ..common.store import RecordStore
from .concepts import slug_for
from .queue import Queue

_LOG = get(__name__)


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


def _reading_basis(task: dict, result: dict) -> str:
    """What a reading was based on, from the answer or from the task.

    The reader's own answer wins, and the validator has already refused the one
    version of it that could be checked. Two cases remain:

    A task that attached no document had nothing to open, so ``abstract`` is not
    an assumption about the reader — it is the only thing the task made possible.

    A task that attached one and came back silent predates this field, and there
    is no way to recover which it was. That stays empty. Recording a guess would
    make an unknown reading indistinguishable from a declared one, and the whole
    point of the field is that the difference is visible.
    """
    declared = str(result.get("read_from") or "").strip()
    if declared:
        return declared
    attachments = task.get("attachments")
    if isinstance(attachments, dict) and not attachments.get("pdf_path"):
        return "abstract"
    return ""


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
        read_from=_reading_basis(task, result),
        generated_by=task.get("completed_by") or "queue",
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
    # The reader's links go to `related_authored`, never to `related`. The
    # latter is derived and the next harvest rebuilds it from scratch, so an
    # answer written there is discarded within the same render — which is
    # exactly what used to happen, silently, with every counter reporting
    # success. See docs/commit/0045.
    if "related" in result:
        concept.related_authored = _authored_links(slug, result["related"])
    store.save_concept(concept)
    return True


def _authored_links(slug: str, names: object) -> list[str]:
    """The reader's `related` answer as slugs.

    Replaces rather than accumulates, so answering again with a shorter list
    retracts. An authored link is a ruling over the whole neighbourhood, and
    without replacement the only way to take one back would be editing `data/`
    by hand — which is the thing the queue exists to prevent.

    A result that omits the key entirely leaves the stored links alone: absent
    is not the same answer as `[]`.
    """
    links: list[str] = []
    for name in names or []:
        other = slug_for(str(name))
        if other and other != slug and other not in links:
            links.append(other)
    return links


_APPLIERS = {"paper": _apply_paper, "video": _apply_video, "concept": _apply_concept}


def completed(cfg: Config) -> dict[str, int]:
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
