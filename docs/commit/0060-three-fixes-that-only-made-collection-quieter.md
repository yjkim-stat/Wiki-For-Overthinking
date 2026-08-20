# 0060 — Three fixes that only made collection quieter

| | |
| --- | --- |
| **Commit** | `fix(collect): gate the listing fallback per topic, date what it finds, record the ledger first` |
| **Scope** | `pipelines/collect/arxiv.py`, `collect/arxiv_listing.py`, `tests/test_local_collection.py` |
| **Kind** | fix |

## What changed

Three defects in arXiv collection, each of which made a run collect less while
reporting success.

1. **The listing fallback is gated per topic.** `collect()` tracked whether the
   API answered *this topic*, and reaches for the listing pages only for the
   topics it answered with nothing. It previously tested a dict accumulated
   across every topic, so one paper returned for any topic suppressed the
   fallback for all the others.
2. **A listing-derived record carries the day it was announced under.** `Entry`
   gained `announced`, filled by `parse_days`; `_to_paper` puts it in `published`
   and derives `year`; `collect()` reads the page through `parse_days` rather
   than `parse_listing` so the day heading reaches the entries beneath it.
3. **The coverage ledger is written before the abstract backfill**, as well as
   after.

## Why it is built this way

All three share one shape, and it is the reason they are one commit: **a
collector that returns fewer results than it should looks exactly like a quiet
day.** There is no error, no exception, no unusual count — just a smaller number,
which is also what a genuinely quiet day produces. None of the three would ever
have surfaced through the run's own reporting.

Per topic, not per run, because the listing is read per category and filtered by
the topics it is given — the topic is the unit the fallback can act on. With five
topics sharing four categories some topic almost always matches something, so the
whole-run gate meant the fallback had never fired in a scheduled run. The topics
that most needed it were exactly the ones that never got it.

The announcement day is the only date a listing page offers, and arXiv announces
the evening after the cutoff, so it is close enough to be the right value for
`published`. Leaving it empty is not a neutral choice: `publish/archive.py` files
a dateless paper under `archive/papers/unknown/` and every index sorts it last,
so a fallback record would be second-class purely because of where it came from.
When a page carries no day heading the field stays empty, which is the honest
answer rather than a guessed one.

The ledger is written first because the listing pass is a handful of requests and
the backfill is minutes of throttled ones. Holding the write until the end means
an interrupted run records nothing at all — and a run that is always interrupted
is indistinguishable from a sweep that was never enabled. `coverage.record`
merges on a high-water mark, so writing twice costs one rewrite and cannot
regress.

## Trade-offs and rejected alternatives

The per-topic gate can fetch the same listing page for several barren topics in
one run. That is bounded by the category set rather than the topic set, and the
client's per-host interval already throttles it, so the cost is small against a
fallback that fires when it should.

**The tests live in a file of their own**, `tests/test_local_collection.py`,
rather than in `tests/test_arxiv_listing.py` where they would naturally sit. This
is the load-bearing part of the commit. These three fixes existed once before and
were lost when the files holding them were replaced with newer versions of
themselves — silently, because the replacement's own tests passed. A test inside
a file that gets replaced cannot guard against the file being replaced.

## What a reviewer should check

- `python3 -m unittest tests.test_local_collection` — nine tests, one class per
  defect. The class name says which fix it guards.
- `test_the_day_count_is_on_disk_before_the_first_abstract_request` asserts the
  *ordering*, not the end state; that is the whole of defect 3.
- That the fallback still does not fire when every topic was answered:
  `test_no_listing_request_when_every_topic_was_answered`.

## Downstream impact

A deployment on `listing.mode: auto` will see the fallback fire where it did not
before, and will collect more — that is the fix, not a regression. Listing-derived
records now land under `archive/papers/<year>/` instead of
`archive/papers/unknown/`; the next render moves them, since page paths are
derived from the record. Existing dateless records keep their path until
re-collected, because nothing invents a date for a record that has none.
