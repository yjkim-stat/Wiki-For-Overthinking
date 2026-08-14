# 0053 — The other direction of the same question

| | |
| --- | --- |
| **Commit** | `feat(migrate): report documents that no record claims` |
| **Scope** | `pipelines/migrate.py`, `tests/test_migrate.py`, `migration/README.md`, `docs/issues/`, `docs/solved/` |
| **Kind** | feature |

## What changed

`migrate status` already answered "how many records claim a document that is not
on disk". It now also answers the reverse, which nothing could see:

```
documents: 1140 record(s) claim one, 0 missing on disk
  3 file(s) on disk that no record claims -- carried as `irreplaceable`, since
  nothing can show them re-fetchable
  orphan   data/pdfs/local-ba6b91360ccccfd7.pdf
```

This is option C, split out of [note 0047](0047-a-filed-document-survives-its-merge.md)
when that fixed the cause of the orphans it left behind.

## Why it is built this way

**An orphan is invisible to everything else.** `shelve_documents` files
documents *by record*, so it never visits a file no record names; the day's
digest counts what was collected, not what is on disk. The defect 0047 fixed was
found by reading code, and this is what would have found it by running something.

**They are not free.** `build_plan` cannot establish provenance for a file nobody
claims, so it correctly refuses to call it re-fetchable and tiers it
`irreplaceable` — the tier a bundle guarantees to carry. Orphans inflate the one
number that decides how large a migration has to be, in the direction that makes
it larger. On the archive where this was found, one run took that tier from
7 files / 169.5 MB to 11 / 235.5 MB.

**It reports and deletes nothing.** Nothing in this repository removes a file
under `data/` from code, and an orphan is precisely the case where the safe
reading of "provenance unknown" is the one that keeps the bytes. The tiering rule
that makes orphans expensive is the same rule that makes deleting them
unsafe automatically.

**`migrate status` only, not `render`.** Both were open in the issue. `render`
runs constantly and a count that does not change until somebody acts becomes
noise — the `stale` block earns its place by reporting things that *moved*. And
the reason an orphan matters is that it inflates a bundle, so the command you run
when that matters is the right place to say so.

**`pdfs/read/` counts; `inbox/` does not.** A shelved document whose record has
gone is an orphan by the same definition, so the scan uses `rglob`. A file in the
inbox is unclaimed *on purpose* — it is on its way in, and has not been given a
record yet.

**The line appears only when the count is non-zero.** A standing zero on every
run is how a number stops being read, which is the failure this feature exists to
correct rather than repeat.

## Trade-offs and rejected alternatives

**It cannot tell an orphan from a document whose record is merely stale.** Both
look the same from the filesystem, and the difference matters when deciding
whether to delete: the guidance in `migration/README.md` says to check the record
that ought to claim the file first. Distinguishing them automatically would mean
guessing at provenance, which is the thing `build_plan` deliberately refuses to
do.

**Twenty examples, then a count.** The same bound the `missing` line uses. An
archive with hundreds of orphans has one problem, not hundreds, and a page of
paths would bury the tier totals above it.

**No exit code changes.** `status` still exits 0 always. An orphan is a thing to
look at, not a reason to refuse to pack — and packing carries it correctly today.

## What a reviewer should check

- The four mutations: drop the orphan collection, narrow `rglob` to `glob` (the
  shelf stops being scanned), stop recording claimed paths (every document
  becomes an orphan), and widen the scan to `inbox/` (undrained files are
  reported as faults). Each takes down one to three tests.
- `test_both_directions_are_reported_at_once`. A record with no file and a file
  with no record are different faults and must both survive in one report.
- `test_the_report_writes_nothing` snapshots `data/` around `check_documents` and
  `status`, the way `tests/test_layering.py` does. A reporting feature that
  writes is the worst version of this.

## Downstream impact

`check_documents` gains two keys, `orphaned` and `orphan_examples`; `status`
gains lines when there is something to say. Nothing else changes, no exit code
moves, and an archive with no orphans prints exactly what it printed before.

Deployments that ran a version with the merge defect (before note 0047) will see
a non-zero count on the first run. Those files are inert duplicates and safe to
remove by hand once the record that should claim each one has been checked.
