# A PDF that no record claims is reported by nothing

**Status:** solved 2026-08-14 — see [Resolution](#resolution) at the foot of this
file and [note 0053](../commit/0053-the-other-direction-of-the-same-question.md).
**Kind:** feature · reporting
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

---

## Resolution

`migrate status` now prints the symmetric line, naming up to twenty examples.
Commit `feat(migrate): report documents that no record claims`, note
[0053](../commit/0053-the-other-direction-of-the-same-question.md).

The two questions this document left open, decided:

- **`migrate status` only, not `render`.** `render` runs constantly and a count
  that does not change until somebody acts becomes noise; the `stale` block earns
  its place by reporting things that *moved*. And the reason an orphan matters is
  that it inflates a bundle's `irreplaceable` tier, so the command you run when
  that matters is where it belongs.
- **`data/pdfs/read/` counts, `inbox/` does not.** A shelved document whose
  record has gone is an orphan by the same definition, so the scan uses `rglob`.
  A file in the inbox is unclaimed on purpose — it is on its way in and has no
  record yet. The transient this document worried about, a re-read paper leaving
  a file behind for a moment, shows up as a *missing* document on the other line
  rather than as an orphan, and `shelve_documents` repairs it on the next render.

It deletes nothing, as specified. The line appears only when the count is
non-zero, because a standing zero on every run is how a number stops being read —
which is the failure this feature exists to correct rather than repeat.

`migration/README.md` carries the new output and a troubleshooting row, since it
is the authority for what `status` prints.
