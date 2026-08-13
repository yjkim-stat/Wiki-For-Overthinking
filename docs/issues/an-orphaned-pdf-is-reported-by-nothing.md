# A PDF that no record claims is reported by nothing

**Status:** open · **Kind:** feature · reporting
**Found:** 2026-08-13, splitting option C out of
[the merge defect](../solved/a-hand-filed-pdf-is-lost-when-its-record-merges.md)
**Touches:** `pipelines/migrate.py`, `pipelines/render.py`, `tests/`

A file in `data/pdfs/` that no paper's `local_path` points at is invisible.
`render.shelve_documents` files documents *by record*, so it never sees one; the
day's digest counts what was collected, not what is on disk; and `migrate status`
reports documents in the other direction only — how many records claim a document
that is missing, never how many documents are claimed by nobody.

[Note 0047](../commit/0047-a-filed-document-survives-its-merge.md) removed the
cause that was known to produce them. It did not add a way to notice the next one,
and it deliberately did not delete the ones already there.

## Why it is worth having anyway

The defect 0047 fixed was found by reading code, not by running anything. An
orphan report would have surfaced it in a day. Orphans can also arise without any
bug: an interrupted run, a hand-edited record, a restore from a bundle packed at a
narrower tier.

They are not harmless. `migrate.build_plan` cannot establish provenance for a file
no record claims, so it correctly refuses to call it re-fetchable and files it as
`irreplaceable` — the tier a migration bundle guarantees to carry. Orphans
therefore inflate the one number that decides how large a bundle has to be, in the
direction that makes it larger.

## What it should do

Count and name them, and nothing else.

- `migrate status` already prints `documents: N record(s) claim one, M missing on
  disk`. The symmetric line is the whole feature: how many files are on disk that
  no record claims.
- Naming a few examples matters more than the count, the way the existing
  `missing` line names them — a count alone cannot be acted on.
- **It must not delete anything.** Nothing in this repository removes a file under
  `data/` from code, and an orphan is exactly the case where the safe reading of
  "unknown provenance" is the one that keeps the bytes. Report; let a person
  decide.

## Open

- Whether `render` should report it too, or only `migrate status`. `render`'s
  result dict already carries a `stale` block for things that are wrong while
  looking fine, which is the same category. Against: `render` runs constantly and
  a number that never changes becomes noise.
- Whether `data/pdfs/read/` counts. A shelved document whose record vanished is an
  orphan by the same definition, and a re-read paper legitimately leaves one
  behind for a moment.

## Tests

- A file in `data/pdfs/` claimed by no record is counted and named.
- A file claimed by a record is not.
- The report writes nothing — assert the directory is byte-identical afterwards,
  the way `tests/test_layering.py` snapshots `data/`.
