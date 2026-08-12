# 0028 — The ledger waited for the part that never finished

| | |
| --- | --- |
| **Commit** | `fix(collect): record the coverage ledger before the backfill, not after it` |
| **Scope** | `pipelines/collect/arxiv_listing.py`, `tests/test_arxiv_listing.py` |
| **Kind** | fix |

## What changed

`arxiv_listing.sweep` now writes the coverage ledger immediately after the
listing pass, in addition to writing it at the end. Three tests cover the
ordering.

The sweep has two passes with very different costs. The listing pass walks each
category's recent pages — a handful of requests — and produces arXiv's own
per-day announcement count, which is the entire reason the sweep exists. The
backfill pass then fetches one abstract per announced paper, up to
`max_abstracts_per_run`, at the listing's request interval. With this
deployment's settings that second pass is on the order of ten minutes.

The ledger was written only after both. So a run that did not survive the
backfill recorded nothing at all, including the cheap half it had already
finished.

## Why it is built this way

**The symptom is indistinguishable from the feature being off.** `sweep.enabled`
has been `true` here since it landed, and `data/index/coverage.jsonl` had never
been created — every run reported `coverage: {days: 0, ...}` and no error. That
is exactly the confusion [0025](0025-re-queue-what-the-evidence-outgrew.md) and
the sweep's own docstring say the per-day count exists to prevent: a small
number with no error means either a quiet day or a failed read, and without the
ledger there is nothing that can tell them apart. The ledger being absent for
the same reason is the failure eating its own remedy.

**Writing twice is nearly free, because the ledger merges on a high-water
mark.** `coverage.record` takes the maximum of `announced`, `listed` and
`captured` per category-day, so an early write can only be improved on by the
later one, never contradicted. The cost is one extra rewrite of a file that
holds a few hundred rows.

**The cheap half is the valuable half.** `announced` is the only number in this
pipeline that does not come from our own parsing. `captured` is useful and
recoverable — a later run pays the abstract debt down. Ordering the write so
that an interruption keeps the irreplaceable number and loses only the
recoverable one is the whole change.

## Trade-offs and rejected alternatives

- *Make the sweep cheap enough to always finish.* Rejected as the fix rather
  than as a separate question: lowering `max_abstracts_per_run` shrinks the
  window but does not close it, and the right budget is a deployment choice that
  should not be load-bearing for whether bookkeeping survives.
- *Write the ledger incrementally, per category.* Rejected for now — it would
  rewrite the file once per category for a marginal gain, since the listing pass
  is the fast part and rarely dies midway through.
- *Record inside `coverage.record` with an append-only log.* Rejected: the
  ledger is a merged high-water mark by design, and an append log would need the
  same merge on read plus compaction.
- The cost accepted: the file is rewritten twice per sweep, and a run that dies
  between the two writes leaves `captured` understated until the next sweep
  corrects it upward.

## What a reviewer should check

- The regression is genuinely covered. Removing the added `coverage.record`
  call makes `test_the_day_count_is_on_disk_before_the_first_abstract_request`
  fail with an empty ledger; a test that only checked the end state would pass
  either way, which is why that test inspects the ledger from inside the first
  `/abs/` request rather than after the sweep returns.
- `coverage.record` still merges upward, so the early write cannot lower a count
  established by an earlier run — see the `max` calls in `enrich/coverage.py`.
- `data/index/coverage.jsonl` appears in this commit for the first time. It is
  meant to be committed; `data/abstracts/` is not, and is still ignored.

## Downstream impact

None for a deployment that already had a working ledger. For one that did not —
which was every deployment running this sweep to a timeout — the ledger starts
appearing after the next run, and the first entries will show large listing gaps
because the debt was never recorded before. That number is the sweep working,
not failing.
