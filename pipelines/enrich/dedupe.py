"""Cross-source deduplication.

The same paper arrives as an arXiv preprint, an OpenReview submission and a
DBLP proceedings entry. All three must collapse onto one record, and the
mapping has to survive across runs — which is why it lives in SQLite rather
than a per-run set.
"""

from __future__ import annotations

from ..common.log import get
from ..common.schema import Paper, Video, strip_arxiv_version, title_fingerprint
from ..common.store import RecordStore, SeenStore, read_json
from .queue import Queue

_LOG = get(__name__)


def paper_keys(paper: Paper) -> list[str]:
    """Every identifier this paper could also be known by."""
    keys: list[str] = []
    if paper.arxiv_id:
        keys.append(f"arxiv:{strip_arxiv_version(paper.arxiv_id)}")
    if paper.doi:
        keys.append(f"doi:{paper.doi.strip().lower()}")
    if paper.title:
        keys.append(f"title:{title_fingerprint(paper.title)}")
    if paper.id and paper.id not in keys:
        keys.append(paper.id)
    return keys


def merge_records(cfg, survivor_id: str, absorbed_id: str, *, dry_run: bool = False) -> dict:
    """Fold one stored paper into another, once a person has named the survivor.

    `reconcile_identifiers` reports two records claiming one identifier and
    stops there, because choosing between them is a merge and this repository
    does not make merges quietly. This is the other side of that stop line: the
    survivor is an argument, so the machine still chooses nothing.

    **Why it cannot be automatic**, in one measured example. A paper filed by
    hand and also collected from arXiv ended up with the *reading* on one record
    and the *document* on the other — the arXiv record held the PDF and had no
    summary, sitting unread in the queue; the hand-filed record had been read and
    had no document. Any rule preferring the richer record, or the older, or the
    one with more topics, discards something real. Only somebody who knows what
    the two records are for can say which survives.

    What moves, and what deliberately does not:

    ``data/papers/`` — folded by `merge_papers`, then the absorbed file is
    deleted. ``data/summaries/`` — the reading moves only if the survivor has
    none; two readings of one paper is a judgement, not a merge, and the second
    is kept where it is rather than silently dropped. ``data/findings/`` — a
    finding naming the absorbed id is repointed, because it is authored and its
    validator would reject the id once the record is gone.
    ``data/index/seen.sqlite`` — every key that resolved to the absorbed record
    now resolves to the survivor. ``data/queue/`` — a pending task that can never
    be applied is removed.

    **`data/concepts/` is not touched, and that is not an omission.** Evidence is
    derived: `harvest` rebuilds it from the summaries on every render, so moving
    the reading *is* how the entities are repointed. Editing those records here
    would write derived data by hand and be undone by the next pass.
    ``archive/`` is not touched for the same reason — `rebuild_archive` clears
    and regenerates it, so a ghost page disappears on its own.
    """
    from ..common.store import write_json

    store = RecordStore(cfg.layout)
    survivor = store.load_paper(survivor_id)
    absorbed = store.load_paper(absorbed_id)
    plan: dict = {
        "survivor": survivor_id,
        "absorbed": absorbed_id,
        "dry_run": dry_run,
        "problems": [],
        "summary_moved": False,
        "summary_kept_apart": False,
        "document_taken": False,
        "findings_repointed": [],
        "keys_repointed": 0,
        "tasks_removed": [],
        "topics_added": [],
    }

    if survivor is None:
        plan["problems"].append(f"no such record: {survivor_id}")
    if absorbed is None:
        plan["problems"].append(f"no such record: {absorbed_id}")
    if survivor_id == absorbed_id:
        plan["problems"].append("a record cannot absorb itself")
    if plan["problems"]:
        return plan

    merged = merge_papers(survivor, absorbed)
    merged.id = survivor_id

    # `merge_papers` deliberately leaves `topics` alone: at collection time the
    # two records were scored separately and the stored one's answer stands.
    # Here a person has said they are one paper, so both taggings describe it,
    # and dropping either would lose exactly what this command exists to
    # preserve — one measured pair had the wider tagging only on the record
    # that was about to be absorbed.
    for slug in absorbed.topics:
        if slug not in merged.topics:
            merged.topics.append(slug)
    for slug, score in absorbed.scores.items():
        if score > merged.scores.get(slug, 0.0):
            merged.scores[slug] = score
    for word in absorbed.matched_keywords:
        if word not in merged.matched_keywords:
            merged.matched_keywords.append(word)
    plan["topics_added"] = [s for s in absorbed.topics if s not in survivor.topics]
    if not survivor.local_path and absorbed.local_path:
        plan["document_taken"] = True

    survivor_summary = store.paper_summary_path(survivor_id)
    absorbed_summary = store.paper_summary_path(absorbed_id)
    if absorbed_summary.exists():
        if survivor_summary.exists():
            # Two readings of one paper. Which is better is a judgement about
            # their content, and this command has a person for identity only.
            plan["summary_kept_apart"] = True
        else:
            plan["summary_moved"] = True

    for finding in store.iter_findings():
        if absorbed_id in finding.papers:
            plan["findings_repointed"].append(finding.id)

    queue = Queue(cfg.layout)
    for task_id in queue.pending_ids():
        task = queue.load(task_id) or {}
        if task.get("item_id") == absorbed_id:
            plan["tasks_removed"].append(task_id)
    if plan["summary_moved"] or survivor_summary.exists():
        # The survivor is read once this lands, so a task asking for it to be
        # read can never be applied and would sit pending for ever.
        survivor_task = Queue.task_id("paper", survivor_id)
        if queue.pending_path(survivor_task).exists():
            plan["tasks_removed"].append(survivor_task)

    with SeenStore(cfg.layout.seen_db) as seen:
        plan["keys_repointed"] = len(seen.keys_for(absorbed_id))

    if dry_run:
        return plan

    if plan["summary_moved"]:
        data = read_json(absorbed_summary) or {}
        data["paper_id"] = survivor_id
        write_json(survivor_summary, data)
    absorbed_summary.unlink(missing_ok=True)

    store.save_paper(merged)
    store.paper_path(absorbed_id).unlink(missing_ok=True)

    for finding_id in plan["findings_repointed"]:
        finding = store.load_finding(finding_id)
        papers = [survivor_id if p == absorbed_id else p for p in finding.papers]
        finding.papers = list(dict.fromkeys(papers))
        store.save_finding(finding)

    for task_id in plan["tasks_removed"]:
        queue.pending_path(task_id).unlink(missing_ok=True)

    with SeenStore(cfg.layout.seen_db) as seen:
        seen.repoint(absorbed_id, survivor_id)

    _LOG.info(
        "merged %s into %s: %s",
        absorbed_id,
        survivor_id,
        {k: v for k, v in plan.items() if k not in ("problems", "dry_run")},
    )
    return plan


def reconcile_identifiers(cfg) -> dict[str, int]:
    """Register identifiers a record gained after it was first registered.

    Deduplication resolves an incoming paper against keys recorded at
    *collection* time. A hand-filed PDF has none worth having then: the record
    is created before anything opens the document — deliberately, because a
    Python parser guessing at a title poisons the archive quietly — so the only
    key available is a fingerprint of the filename.

    The arXiv id arrives later, at `queue complete`, and nothing re-registered
    the keys. So the record sat in the archive with `arxiv_id: 2503.20314` and
    no `arxiv:2503.20314` key, and the day the arXiv collector returned that
    paper it forked instead of folding: two records for one paper, two archive
    pages, and every entity counting it twice. Measured on one deployment,
    **17 of 22 hand-filed papers carrying an arXiv id were in that state.**

    Self-healing rather than event-driven, for the reason `shelve_documents` is:
    a fix that only ran at apply time would prevent the next duplicate and close
    none of the ones already waiting to happen, because those readings were
    applied long ago. Re-deriving from the records every pass costs a handful of
    indexed lookups and needs nothing remembered.

    **A key already held by another record is reported, never repointed.** That
    is a duplicate that already exists, and choosing which of the two survives
    is a merge — a decision with a human in it, and the one thing this
    repository is most careful never to make quietly.
    """
    store = RecordStore(cfg.layout)
    counts = {"registered": 0, "papers": 0, "conflicts": 0}
    examples: list[str] = []

    with SeenStore(cfg.layout.seen_db) as seen:
        for paper in store.iter_papers():
            added = 0
            for key in paper_keys(paper):
                holder = seen.canonical_for([key])
                if holder is None:
                    # `mark` would repoint an existing key, so it is only ever
                    # reached for one nothing holds.
                    seen.mark(
                        key, kind="paper", canonical=paper.id, source=paper.source
                    )
                    added += 1
                elif holder != paper.id:
                    counts["conflicts"] += 1
                    if len(examples) < 10:
                        examples.append(f"{key}: {holder} and {paper.id}")
            if added:
                counts["registered"] += added
                counts["papers"] += 1

    if counts["registered"]:
        _LOG.info(
            "registered %d identifier(s) for %d record(s) that gained them after "
            "collection",
            counts["registered"],
            counts["papers"],
        )
    if counts["conflicts"]:
        _LOG.warning(
            "%d identifier(s) are claimed by two records — duplicates that "
            "already exist; merging them is a decision for a person",
            counts["conflicts"],
        )
        for example in examples:
            _LOG.warning("  duplicate  %s", example)
    return counts


def merge_papers(existing: Paper, incoming: Paper) -> Paper:
    """Fold ``incoming`` into ``existing``, preferring richer values.

    A venue from a proceedings entry and an abstract from arXiv both matter, so
    fields are filled in rather than overwritten. The stored record wins on
    identity; the newcomer wins only where the stored record is empty or
    thinner.
    """
    merged = Paper.from_dict(existing.to_dict())

    for field_name in ("abstract", "venue", "doi", "arxiv_id", "pdf_url", "url"):
        current = getattr(merged, field_name) or ""
        candidate = getattr(incoming, field_name) or ""
        if len(candidate) > len(current):
            setattr(merged, field_name, candidate)

    if len(incoming.authors) > len(merged.authors):
        merged.authors = incoming.authors
    if incoming.year and not merged.year:
        merged.year = incoming.year
    if incoming.published and (
        not merged.published or incoming.published < merged.published
    ):
        # The earliest sighting is the real publication date; a proceedings
        # entry should not push a preprint's date forward.
        merged.published = incoming.published
    if incoming.updated > merged.updated:
        merged.updated = incoming.updated

    for category in incoming.categories:
        if category not in merged.categories:
            merged.categories.append(category)

    if incoming.source not in merged.source.split("+"):
        merged.source = f"{merged.source}+{incoming.source}"

    # A document is not merged on richness like every field above. There is no
    # "longer" path, and the two candidates are not two descriptions of one
    # thing — they are two files.
    #
    # The stored path wins when there is one, because it may already have been
    # shelved into `data/pdfs/read/` and replacing it would point the record at
    # a file that is no longer there. Otherwise the newcomer's is taken.
    # Dropping it is what left a hand-filed PDF orphaned on disk while the
    # pipeline downloaded the same paper again, having concluded that the record
    # it had just merged held no document. `source` *is* merged, so the record
    # still read as hand-filed — it simply could not say where the file was.
    if incoming.local_path and not merged.local_path:
        merged.local_path = incoming.local_path

    merged.last_seen = incoming.last_seen
    return merged


class Deduplicator:
    """Resolves incoming records onto canonical stored ones."""

    def __init__(self, seen: SeenStore, store: RecordStore) -> None:
        self.seen = seen
        self.store = store

    def resolve_paper(self, paper: Paper) -> tuple[Paper, bool]:
        """Return ``(record, is_new)`` for ``paper``.

        ``record`` is the canonical, possibly merged paper as it should be
        stored. ``is_new`` is True only the first time the work is seen at all.
        """
        keys = paper_keys(paper)
        canonical = self.seen.canonical_for(keys) or paper.id
        is_new = canonical == paper.id and not self.seen.has(paper.id)

        existing = self.store.load_paper(canonical)
        if existing is not None:
            paper.id = canonical
            record = merge_papers(existing, paper)
            is_new = False
        else:
            paper.id = canonical
            record = paper

        for key in keys:
            self.seen.mark(
                key, kind="paper", canonical=canonical, source=paper.source
            )
        return record, is_new

    def resolve_video(self, video: Video) -> tuple[Video, bool]:
        """Videos have a single stable id, so this only tracks first sighting."""
        existing = self.store.load_video(video.id)
        is_new = self.seen.mark(
            video.id, kind="video", canonical=video.id, source=video.source
        )
        if existing is not None:
            merged = Video.from_dict(existing.to_dict())
            for field_name in ("description", "title", "channel", "url"):
                if not getattr(merged, field_name):
                    setattr(merged, field_name, getattr(video, field_name))
            merged.duration_s = merged.duration_s or video.duration_s
            merged.transcript_available = (
                merged.transcript_available or video.transcript_available
            )
            merged.transcript_chars = max(
                merged.transcript_chars, video.transcript_chars
            )
            merged.last_seen = video.last_seen
            return merged, False
        return video, is_new


def main(argv: list[str] | None = None) -> int:
    """`merge` only. Deduplication itself has no command: it happens inside a run."""
    import argparse
    import json
    import sys
    from pathlib import Path

    from ..common import config as config_mod
    from ..common import paths as P

    parser = argparse.ArgumentParser(
        prog="python -m pipelines.enrich.dedupe",
        description="Fold one stored paper into another, survivor named by you.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_merge = sub.add_parser(
        "merge", help="fold one paper record into another (you name the survivor)"
    )
    p_merge.add_argument("survivor", help="the id that stays")
    p_merge.add_argument("absorbed", help="the id that is folded in and deleted")
    p_merge.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would move and change nothing",
    )

    sub.add_parser("conflicts", help="identifiers claimed by two records")

    args = parser.parse_args(argv)
    cfg = config_mod.load(args.root)
    cfg.layout.ensure()

    if args.command == "conflicts":
        counts = reconcile_identifiers(cfg)
        print(json.dumps(counts, indent=2))
        return 0

    plan = merge_records(cfg, args.survivor, args.absorbed, dry_run=args.dry_run)
    if plan["problems"]:
        for problem in plan["problems"]:
            print(problem, file=sys.stderr)
        return 1
    print(json.dumps(plan, indent=2, ensure_ascii=False))
    if plan["summary_kept_apart"]:
        print(
            "\nboth records carry a reading. The survivor keeps its own; the "
            "other is discarded with the record it was on. Check that is what "
            "you meant before running without --dry-run.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
