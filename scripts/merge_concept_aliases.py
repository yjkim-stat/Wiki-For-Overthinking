#!/usr/bin/env python3
"""Retire the concept records that `config/concept-aliases.yaml` has orphaned.

Declaring an alias redirects the *harvest*: from the next render on, a summary
naming `AIME24` files its evidence under `AIME 2024`. It does nothing to the
`data/concepts/aime24.json` already on disk -- and that record has a definition,
so the harvest's carry-over rule resurrects it every pass. Two notes, one
benchmark, for ever.

Retiring it destroys authored text, which is why it is a one-off with an audit
trail rather than a step in `render`. Nothing here runs by accident: `--apply`
is required, and every retired record is written to `data/concepts/retired/`
before it is removed, so the definition that was dropped can still be read.

    python3 scripts/merge_concept_aliases.py                # what would happen
    python3 scripts/merge_concept_aliases.py --apply
    python3 scripts/merge_concept_aliases.py --candidates   # what is not ruled on

**The definition is not carried across.** When the retired record has one and
the canonical does too, the canonical's is cleared as well, so the merged entity
is re-queued and re-derived against the union of the evidence -- which is the
point, since neither definition was written against more than a fraction of it.
Moving a definition instead would be worse than it looks: `render` reads how
many sources a definition was written against from the archived queue task,
keyed by the concept's *name*, so a definition that changes names loses its
staleness count and reads as current for ever.

    python3 -m pipelines.render     # re-queues the cleared definitions

`--candidates` lists the other direction: names that some reader declared as an
alias in a summary and that are separate records here. That list is not a merge
plan. Readers use `aliases` for spelling variants and for neighbours alike, so
it holds `GPQA` under `gpqa-diamond` (a subset), `MATH` under `math500` (a
superset) and `causal tracing` under `activation-patching` (a different
measurement). It is a worklist for a person; what survives review goes in the
config file.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipelines.common import config as config_mod  # noqa: E402
from pipelines.common.paths import slugify  # noqa: E402
from pipelines.common.store import RecordStore  # noqa: E402
from pipelines.local import aliases as aliases_mod  # noqa: E402


def _write(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def retire(cfg, apply: bool) -> int:
    """Fold every declared alias's record into its canonical. Returns exit code."""
    store = RecordStore(cfg.layout)
    mapping = aliases_mod.mapping()
    if not mapping:
        print("no alias map installed; nothing to retire")
        return 0

    records = {c.slug: c for c in store.iter_concepts()}
    retired_dir = cfg.layout.data / "concepts" / "retired"

    folded = 0
    # A set, not a counter: an entity with two aliases reaches this branch
    # twice, and only the first clearing is a clearing. Counting the visits
    # made the dry run promise more work than `--apply` then did.
    cleared: set[str] = set()
    for alias, canonical in sorted(mapping.items()):
        old = records.get(alias)
        if old is None:
            continue
        new = records.get(canonical)
        where = f"{alias} -> {canonical}"
        if new is None:
            # The canonical has no record yet, which happens when every summary
            # used the alias spelling. The harvest will build it on the next
            # render from the same evidence; the alias record is still stale.
            print(f"{where}: canonical has no record yet (harvest will build it)")
        print(
            f"{where}: {len(old.evidence)} source(s), "
            f"definition {'yes' if old.definition else 'no'}"
            + (
                f"  |  canonical {len(new.evidence)} source(s), "
                f"definition {'yes' if new.definition else 'no'}"
                if new is not None
                else ""
            )
        )

        if apply:
            _write(retired_dir / f"{alias}.json", old.to_dict())
            store.concept_path(alias).unlink(missing_ok=True)
        folded += 1

        if new is None:
            continue

        # Authored links are carried; `aliases` is not, because the harvest
        # rebuilds it from the surface names it sees.
        added = [s for s in old.related_authored if s not in new.related_authored]
        if added:
            print(f"    carrying {len(added)} authored link(s) to {canonical}")
            if apply:
                new.related_authored.extend(added)

        # Decided before the mutation below, not after. Re-testing
        # `new.definition` in the write condition made it false the moment the
        # clearing succeeded, so the record was cleared in memory and never
        # written -- a silent no-op that `--apply` reported as done.
        clearing = bool(old.definition and new.definition)
        if clearing:
            print(
                f"    both are defined; clearing {canonical}'s definition so it "
                f"re-derives against all {len(old.evidence) + len(new.evidence)} "
                f"source(s) (upper bound; overlap is folded at harvest)"
            )
            cleared.add(canonical)
            if apply:
                new.definition = ""
        elif old.definition:
            print(
                f"    {alias} was defined and {canonical} is not; the text is in "
                f"{retired_dir.name}/ and the merged entity will be queued fresh"
            )

        if apply and (added or clearing):
            _write(store.concept_path(canonical), new.to_dict())

    verb = "retired" if apply else "would retire"
    print(f"\n{verb} {folded} record(s); {len(cleared)} definition(s) cleared for re-derivation")
    if not apply and folded:
        print("re-run with --apply to write, then `python3 -m pipelines.render`")
    return 0


def candidates(cfg) -> int:
    """Names a reader declared as an alias that are separate records here."""
    store = RecordStore(cfg.layout)
    records = {c.slug: c for c in store.iter_concepts()}
    ruled = aliases_mod.mapping()

    rows = []
    for concept in records.values():
        for name in concept.aliases:
            alias = slugify(name)
            if alias == concept.slug or alias in ruled or alias not in records:
                continue
            other = records[alias]
            rows.append((len(other.evidence), alias, other, concept))

    # Sorted on the two comparable fields only: a tie would otherwise fall
    # through to comparing Concepts, which have no ordering.
    for count, alias, other, claimant in sorted(rows, key=lambda r: (-r[0], r[1])):
        print(
            f"{alias:38s} {count:3d} src  def={'y' if other.definition else 'n'}"
            f"   claimed by {claimant.slug} ({len(claimant.evidence)} src)"
        )
    print(f"\n{len(rows)} unruled candidate(s)")
    print("Not a merge plan: `aliases` holds spelling variants and neighbours alike.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=None, help="deployment root")
    parser.add_argument("--apply", action="store_true", help="write; without it, report")
    parser.add_argument(
        "--candidates",
        action="store_true",
        help="list alias-field collisions nobody has ruled on, and stop",
    )
    args = parser.parse_args()

    cfg = config_mod.load(args.root)
    if args.candidates:
        return candidates(cfg)
    return retire(cfg, args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
