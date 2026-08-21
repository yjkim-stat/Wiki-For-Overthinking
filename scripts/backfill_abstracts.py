#!/usr/bin/env python3
"""Fetch abstracts for records already stored without one.

The conference collector now fills in a missing abstract before it returns, but
that is forward-looking: a record collected before it did stays title-only
forever, because nothing re-visits a stored record. This is the counterpart, in
the same spirit as `scripts/retopic.py` — collection-time behaviour has to be
applicable to what collection already produced.

    python3 scripts/backfill_abstracts.py            # dry run
    python3 scripts/backfill_abstracts.py --apply
    python3 scripts/backfill_abstracts.py --apply --limit 20

It reuses the collector's own resolvers rather than reimplementing them, so a
venue that works during collection works here and there is one place to fix.

Filling an abstract changes what scoring would see — a title-only record is
judged on a title hit worth 3.0 and nothing else. Run `scripts/retopic.py`
afterwards to let the new evidence assign topics it could not reach before;
that script only ever adds, so this cannot cost a record a topic it already has.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.local.abstracts import fill_missing  # noqa: E402
from pipelines.common import config as config_mod  # noqa: E402
from pipelines.common.http import from_settings  # noqa: E402
from pipelines.common.store import RecordStore  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help="save what is fetched (default is a dry run)"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="stop after this many lookups"
    )
    args = parser.parse_args()

    cfg = config_mod.load()
    store = RecordStore(cfg.layout)

    missing = [
        p
        for p in store.iter_papers()
        if not (p.abstract or "").strip() and p.doi
    ]
    without_doi = [
        p
        for p in store.iter_papers()
        if not (p.abstract or "").strip() and not p.doi
    ]
    if without_doi:
        # Said out loud rather than counted silently: nothing here can resolve
        # these, so they stay title-only until another index supplies the work.
        print(f"{len(without_doi)} record(s) have no abstract and no DOI; skipping")

    if not missing:
        print("every stored record with a DOI has an abstract")
        return 0

    print(f"{len(missing)} record(s) need an abstract")
    if not args.apply:
        for paper in missing[:20]:
            print(f"  - {paper.id:38} {paper.title[:56]}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")
        print("\nRe-run with --apply to fetch them.")
        return 0

    if args.limit:
        missing = missing[: args.limit]

    # One request per paper against a throttled client, so this is slow on
    # purpose; the collector's own cap does not apply here because the whole
    # point is to work through a backlog the cap was designed to spread out.
    client = from_settings(cfg.settings, min_interval_s=1.0)
    block = cfg.sources.setdefault("conferences", {}).setdefault("abstracts", {})
    block["enabled"] = True
    block["max_lookups"] = len(missing)

    filled = fill_missing(cfg, missing, client)

    saved = 0
    for paper in missing:
        if (paper.abstract or "").strip():
            store.save_paper(paper)
            saved += 1

    print(f"\nfetched {filled}, saved {saved} record(s)")
    if saved:
        print("run `python3 scripts/retopic.py` to re-score against the new text,")
        print("then `python3 -m pipelines.render`")
    return 0


if __name__ == "__main__":
    sys.exit(main())
