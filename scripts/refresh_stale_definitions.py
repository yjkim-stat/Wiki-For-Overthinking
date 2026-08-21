#!/usr/bin/env python3
"""Re-queue wiki definitions that their own evidence has outgrown.

`pipelines.render` reports how many definitions were written against fewer
sources than now exist, and deliberately does not act on it: re-deriving a
definition means reading its sources again, and a counter must not discard
written work on arithmetic alone. The documented way to re-queue one is to clear
`definition` in `data/concepts/<slug>.json` and render again. This does that in
bulk, with a threshold, so the judgement stays with the person running it.

    python3 scripts/refresh_stale_definitions.py                  # dry run, all
    python3 scripts/refresh_stale_definitions.py --min-growth 6
    python3 scripts/refresh_stale_definitions.py --min-growth 6 --apply

**Growth, not staleness, is the thing to threshold on.** A definition written
against 2 sources when there are now 3 is stale by the counter and is almost
certainly still correct; one written against 3 when there are now 20 is a
different claim about a different body of evidence. Sorting by
`sources_now - written_for` puts the definitions that are actually wrong first,
and `--min-growth` is how you decline to rewrite the rest.

Only the `definition` field is cleared. Aliases, related links and the kind a
definition task ruled on are left alone, because those do not go stale the way a
summary of the evidence does — and the kind in particular is defended against
being reverted by harvest.

Nothing here writes a definition. It queues the work; the reader does it.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.common import config as config_mod  # noqa: E402
from pipelines.common.store import RecordStore  # noqa: E402
from pipelines.render import stale_definitions  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--min-growth",
        type=int,
        default=1,
        help="only re-queue definitions whose source count grew by at least this much",
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="stop after this many, largest growth first"
    )
    parser.add_argument(
        "--apply", action="store_true", help="clear the definitions (default is a dry run)"
    )
    args = parser.parse_args()

    cfg = config_mod.load()
    store = RecordStore(cfg.layout)

    rows = stale_definitions(cfg)
    if not rows:
        print("every definition is current with its evidence")
        return 0

    rows.sort(key=lambda r: r["sources_now"] - r["written_for"], reverse=True)
    chosen = [r for r in rows if r["sources_now"] - r["written_for"] >= args.min_growth]
    if args.limit:
        chosen = chosen[: args.limit]

    skipped = len(rows) - len(chosen)
    if not chosen:
        print(f"{len(rows)} stale, none with growth >= {args.min_growth}")
        return 0

    print(f"{'growth':>7}  {'was':>4} {'now':>4}  name")
    for row in chosen:
        print(
            f"{row['sources_now'] - row['written_for']:>7}  "
            f"{row['written_for']:>4} {row['sources_now']:>4}  {row['name']}"
        )
    if skipped:
        print(f"\n({skipped} stale definition(s) below the threshold, left alone)")

    if not args.apply:
        print(f"\n{len(chosen)} definition(s) would be re-queued. Re-run with --apply.")
        return 0

    cleared = 0
    for row in chosen:
        concept = store.load_concept(row["slug"])
        if concept is None:
            print(f"  missing concept record: {row['slug']}")
            continue
        concept.definition = ""
        store.save_concept(concept)
        cleared += 1

    print(f"\ncleared {cleared} definition(s)")
    print("run `python3 -m pipelines.render` to file the tasks, then drain the queue")
    return 0


if __name__ == "__main__":
    sys.exit(main())
