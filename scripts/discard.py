#!/usr/bin/env python3
"""Remove records that a scoring mistake let into the archive.

Collection is a keyword rule, and a keyword rule is sometimes wrong. When it
admits something the archive should not hold — an analog-circuit design paper
that matched on the word "circuit" — the archive has, until now, had no way to
say so. Editing `data/` by hand is forbidden and would leave no record of the
judgement; leaving the item in corrupts the topic outputs built from it.

This is the destructive counterpart to `scripts/retopic.py`, and it is
deliberately harder to use.

    python3 scripts/discard.py --rescore                      # what no topic wants
    python3 scripts/discard.py --rescore --apply
    python3 scripts/discard.py --id arxiv:2608.04999 --apply

**Dry run is the default.** Nothing is removed without `--apply`.

**Hand-filed PDFs are never touched.** A PDF in `inbox/` bypasses scoring by
design — filing it is the editorial decision scoring exists to approximate — so
a local record with no topics is a reader's judgement, not a scoring error.
`--rescore` skips them entirely; removing one requires naming its id.

What a discard removes, per record: the record in `data/papers/`, its summary
in `data/summaries/papers/` if one exists, and any pending or done queue task
for it. The flat indexes are then rebuilt from what remains, and `archive/` is
regenerated on the next render, which clears the tree first.

What it deliberately does **not** touch is `data/index/seen.sqlite`. That is the
dedup alias map, and forgetting an id there would let the next run collect the
same item again. A discarded record should stay discarded.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.common import config as config_mod  # noqa: E402
from pipelines.common.store import RecordStore  # noqa: E402
from pipelines.enrich.queue import Queue  # noqa: E402
from pipelines.enrich.score import score_against_topics  # noqa: E402


def _queue_files(layout, paper_id: str) -> list[Path]:
    """Every queue task file belonging to this paper, in any state.

    The id is asked of ``Queue`` rather than reconstructed here. Rebuilding the
    transform by hand missed that dots are replaced as well as colons, which
    left the tasks behind after the records were gone.
    """
    task_id = Queue.task_id("paper", paper_id)
    found = []
    for state in ("pending", "done", "archive"):
        directory = layout.queue / state
        if directory.exists():
            found.extend(directory.glob(f"{task_id}*.json"))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--rescore",
        action="store_true",
        help="select collected records that no current topic accepts",
    )
    group.add_argument(
        "--id", action="append", metavar="PAPER_ID", help="discard this id; repeatable"
    )
    group.add_argument(
        "--orphans",
        action="store_true",
        help="remove queue tasks whose record no longer exists",
    )
    parser.add_argument(
        "--apply", action="store_true", help="actually remove (default is a dry run)"
    )
    args = parser.parse_args()

    cfg = config_mod.load()
    store = RecordStore(cfg.layout)

    if args.orphans:
        # A task whose record is gone can never be completed: `complete` looks
        # the record up to apply the result. Left alone it sits in the queue
        # forever and the next reader tries to answer it.
        import json

        stranded = []
        for state in ("pending", "done"):
            directory = cfg.layout.queue / state
            for path in sorted(directory.glob("*.json")) if directory.exists() else []:
                task = json.loads(path.read_text(encoding="utf-8"))
                if task.get("kind") != "paper":
                    continue
                if store.load_paper(task["item_id"]) is None:
                    stranded.append((path, task))
        if not stranded:
            print("no orphaned tasks")
            return 0
        for path, task in stranded:
            print(f"  - {task['task_id']:28} {task['payload']['title'][:60]}")
        if not args.apply:
            print(f"\n{len(stranded)} orphaned task(s). Re-run with --apply.")
            return 0
        for path, _ in stranded:
            path.unlink()
        print(f"\nremoved {len(stranded)} orphaned task(s)")
        return 0

    if args.rescore:
        if not cfg.topics:
            print("no topics defined; refusing to discard everything")
            return 2
        targets = []
        for paper in store.iter_papers():
            if paper.source == "local":
                continue  # a reader filed it; scoring does not get a vote
            _, _, accepted = score_against_topics(
                cfg.topics,
                title=paper.title,
                body=paper.abstract,
                authors=paper.authors,
                settings=cfg.settings,
            )
            if not accepted:
                targets.append(paper)
    else:
        targets = []
        for paper_id in args.id:
            paper = store.load_paper(paper_id)
            if paper is None:
                print(f"unknown paper id: {paper_id}")
                return 2
            targets.append(paper)

    if not targets:
        print("nothing to discard")
        return 0

    for paper in targets:
        print(f"  - {paper.id:26} {paper.title[:66]}")
        if paper.source == "local":
            print("      (hand-filed PDF — named explicitly, so removing it)")

    if not args.apply:
        print(f"\n{len(targets)} record(s) would be discarded. Re-run with --apply.")
        return 0

    removed = 0
    for paper in targets:
        for path in [
            store.paper_path(paper.id),
            store.paper_summary_path(paper.id),
            *_queue_files(cfg.layout, paper.id),
        ]:
            if path.exists():
                path.unlink()
        removed += 1

    counts = store.rebuild_indexes()
    print(f"\ndiscarded {removed} record(s); indexes rebuilt {counts}")
    print("run `python3 -m pipelines.render` to rebuild the archive and wiki")
    return 0


if __name__ == "__main__":
    sys.exit(main())
