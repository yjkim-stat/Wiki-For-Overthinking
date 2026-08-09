# 0025 — Know what a day held, not just what we found

| | |
| --- | --- |
| **Commit** | `feat(collect): record arXiv's own per-day count and pay down what is missing` |
| **Scope** | `pipelines/enrich/coverage.py`, `pipelines/collect/arxiv_listing.py`, `pipelines/common/store.py`, `pipelines/common/paths.py`, `pipelines/run_daily.py`, `config/sources.yaml`, `.gitignore`, `CLAUDE.md`, `README.md`, `tests/test_coverage.py` |
| **Kind** | feature |

## What changed

A run now records, per category and announcement day, three counts:
`announced` (what arXiv says the day held), `listed` (identifiers we have seen)
and `captured` (identifiers we hold an abstract for). The ledger lives in
`data/index/coverage.jsonl` and the abstracts in `data/abstracts/<cat>/<day>.jsonl`
— every announced paper, not only the ones a topic currently wants.

Where the counts are short, the shortfall is carried as a debt and paid down
over later runs, relevance first.

## Why it is built this way

**`announced` is the only number in this pipeline that we did not compute.**
Every other counter reports what a collector found, which means none of them
can distinguish "arXiv announced nothing today" from "we failed to read what
arXiv announced today". Those two look identical in a log — a small number, no
error — and this repository has now been bitten by that shape of failure four
separate times. arXiv publishes its own per-day count in the listing's day
headings, and comparing against it is the first integrity check here that does
not grade its own homework.

**Three counts, not one, because the two gaps cost different amounts to close.**
A short `listed` means we never saw the identifiers — pagination stopped early,
a host died mid-crawl — and closing it means more listing requests. A short
`captured` means we know exactly which identifiers we are missing abstracts
for, which is the cheap and precise repair. Collapsing them into one "missing"
number would hide which kind of work a day needs.

**A gap is a debt, not an error.** It is recorded and reported, and a bounded
budget of it is paid each run. A day that is never completed is telling you
something real about the source; retrying it silently forever would hide that,
and repairing everything in one run would mean a single run issuing hundreds of
requests to a host that asks not to be crawled hard.

**Backfill is ordered by title relevance, and that ordering is doing two jobs.**
The group gets abstracts for what it is likely to want on the first run, and
the tail still drains on later ones. Ordering by date instead would spend the
budget on whatever happened to be announced first.

**Counts only ever go up.** The ledger is a high-water mark of what has been
seen, not a snapshot of the last run — otherwise a run that paginated one page
would erase the knowledge that a previous run had walked ten.

**`data/abstracts/` is separate from `data/papers/`, and that separation is the
point.** `papers/` is what the group tracks; `abstracts/` is what was
published. Keeping the second out of the first is what lets a threshold or a
keyword list be revisited later against the real record rather than against
what an old threshold happened to admit. It is committed, because re-fetching
costs one request per paper and losing it on a fresh clone would cost days.

**The listing pass files every identifier with an empty abstract.** That is
what makes the day's file its identifier list as well as its abstract store, so
`listed` and `captured` are both answerable from one place, and a backfill knows
precisely what to ask for.

## Trade-offs and rejected alternatives

**Rejected: fetch every abstract for a short day immediately, as first
proposed.** A busy category announces a few hundred papers a day; at a five
second floor that is half an hour of requests for one category-day, and a
backlog would compound into runs measured in hours. The budget plus the ledger
gets the same end state without any single run behaving badly.

**Rejected: infer completeness from our own entry count.** That is exactly the
self-grading this commit exists to escape.

**Rejected: keep abstracts only for papers above a lower threshold.** Cheaper,
and it reintroduces the problem — a re-scored archive could only ever see what
the old threshold let through.

**Cost: repository weight.** Roughly 1.5 KB per abstract; a four-category year
is on the order of 100 MB before git compresses it. Stated in
`config/sources.yaml` and `.gitignore`, with the escape hatch named: ignore the
directory and the ledger will report the resulting gap honestly rather than
pretending.

**Cost: a first sweep on a busy deployment reports a large debt.** That is the
true state, arrived at for the first time.

## What a reviewer should check

That the ledger reports a gap where the pipeline used to report a quiet day:

```bash
python3 -m unittest tests.test_coverage -v
```

`test_the_ledger_records_arxivs_own_count_against_ours` is the whole idea in one
test — two entries parsed against an announced 213. `test_counts_only_ever_go_up`
guards the high-water-mark property, without which a small run silently erases a
large one. `test_a_second_run_does_not_refetch_what_it_holds` is what keeps the
budget from being spent on work already done.

**Not validated against a live page.** Every arXiv host is blocked from this
environment, so the day-heading shape is written from the documented format and
tested against fixtures. `test_a_page_without_day_headings_degrades_to_one_undated_day`
is the guard for being wrong about it: the sweep loses the day split, not the
entries.

## Downstream impact

`run_daily`'s result gains a `coverage` block. `data/abstracts/` and
`data/index/coverage.jsonl` are new and committed.

A deployment pulling this should expect its first sweep to report a large debt
and its repository to start growing. Set `arxiv.listing.sweep.enabled: false` to
opt out entirely, or gitignore `data/abstracts/` to keep the ledger without the
weight.
