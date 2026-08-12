# 0023 — A title is not enough to score a paper

| | |
| --- | --- |
| **Commit** | `feat(collect): fetch the abstracts DBLP does not carry` |
| **Scope** | `pipelines/collect/conferences.py`, `config/sources.yaml`, `scripts/backfill_abstracts.py`, `tests/test_collect.py` |
| **Kind** | feature · **changes what scoring sees** |

## What changed

The conference collector now fills in a missing abstract before returning, using
two resolvers: ACL Anthology for `10.18653/` DOIs, and Semantic Scholar by DOI
for everything else. `scripts/backfill_abstracts.py` applies the same resolvers
to records already stored. New config block `conferences.abstracts` with
`enabled`, `max_lookups` and `acl_anthology_url`.

In this deployment all 60 DBLP records — 100% of them — had no abstract, and all
60 now do.

## Why this had to exist

DBLP is a bibliographic index. It carries authors, venue, year and DOI, and no
abstract at all; the module docstring has said so since the collector was
written. What was not followed through is that everything downstream assumes the
abstract is present.

**Scoring is the expensive part.** A title hit is weighted 3.0 and an abstract
hit 1.0, and `min_score: 0.35` was chosen to mean "in the title once, or in the
abstract twice". A record with no abstract cannot reach the second of those, so
it is judged on strictly less evidence than the same paper arriving from an
index that supplies one — and whether a paper is archived depends on which index
happened to find it first. That is not a threshold that can be tuned around,
because the two populations are being measured differently.

**And the reader is handed a task with no source material.** The task file is
supposed to be self-contained. For these it contained a title. Answering one
meant leaving the queue, finding the paper by hand, and fetching the abstract —
which happened 59 times in a single sitting before this existed.

## Why it is built this way

**After deduplication, not inside the DBLP collector.** A paper that Semantic
Scholar and DBLP both return already has an abstract from whichever arrived
first. Filling per-collector would spend a request on a field about to be
discarded; filling once over the merged set spends none.

**Keyed on the missing field, not on the source.** The step asks "does this
record have an abstract" rather than "did this come from DBLP". A future index
with patchy coverage is handled without being named.

**ACL gets its own resolver because it needs no lookup.** An Anthology DOI's
suffix *is* the Anthology identifier, so the page URL is derivable from the DOI
alone — one request, no search step, no ambiguity about which paper matched.
Semantic Scholar is the general fallback and reuses the API key already
configured for the search collector.

**`max_lookups` bounds a run, not the backlog.** Each lookup is a throttled
request, which makes this the slowest step in a run. A record left unfilled
keeps its empty abstract and is retried tomorrow, and the backlog only grows by
a day's collection at a time, so a low cap costs latency and never coverage.

**Best-effort, like every other query here.** A failed lookup leaves the
abstract empty, which is exactly the state before the attempt. Only a *total*
failure reaches the run's error list, because partial misses are normal — not
every venue publishes an abstract anywhere machine-readable.

## The bug worth knowing about

**DBLP reports DOIs uppercased**: `10.18653/V1/2026.ACL-LONG.1034`. A DOI is
case-insensitive by specification, so that is correct of DBLP. An ACL Anthology
URL *path* is case-sensitive, so the uppercase form 404s.

The first version of this did not lowercase, and the result was not a visible
failure: every ACL paper fell through to the Semantic Scholar fallback, and the
run reported 16 of 60 filled instead of an error. 61 of the 62 DOIs in this
store are uppercase, so the resolver written specifically for the venue that
supplies most of the archive was doing nothing at all. The lowercasing happens
in the resolver rather than at ingestion, so the stored record stays faithful to
what the index reported. `test_dblp_uppercases_dois_and_anthology_urls_are_lowercase`
pins it.

## Trade-offs and rejected alternatives

- *Crossref as the general fallback.* Rejected: abstracts are publisher-deposited
  and frequently absent, and it would be a fourth service to configure. Semantic
  Scholar is already here.
- *Fetching the PDF and extracting the abstract.* Rejected: far more expensive,
  and brittle across layouts, for a field both services publish as text.
- *Normalizing the DOI to lowercase at ingestion.* Tempting and rejected — the
  record should say what the index said. Consumers that need a specific case can
  ask for it, and exactly one does.
- *Skipping DBLP entirely now that Semantic Scholar works again (note 0017).*
  Rejected: DBLP is the reason 59 of this drain's papers were in the archive at
  all. It has the coverage; it just lacks one field.
- *One commit for the collector and one for the backfill script.* Considered and
  rejected: the script is four lines of argument parsing around the collector's
  own function, and splitting them would put a caller in a different commit from
  the thing it calls.

## What a reviewer should check

- `python3 -m unittest discover -s tests -t .` — 202 tests, eight new in
  `MissingAbstractTests`, all against a stub client. Nothing here touches the
  network during tests.
- The uppercase-DOI test above. It is the one that catches a silent fallthrough
  rather than a failure.
- `python3 scripts/backfill_abstracts.py` with no flags must print a plan and
  fetch nothing.
- That a record with no DOI is reported and skipped rather than counted as a
  failure — nothing here can resolve one.

## Downstream impact

**This changes what scoring sees, so it changes what is archived.** A deployment
using DBLP has been scoring those papers on titles alone; after this they are
scored on title and abstract, which will admit papers that were below the bar and
can push previously matched keywords into a different total. Re-check
`min_score` and `data/index/rejected.jsonl` after pulling.

For a store collected before this, run `scripts/backfill_abstracts.py --apply`,
then `scripts/retopic.py` to let the new text assign topics that title-only
scoring could not reach, then re-render. In this deployment that was 60 records
filled and 16 gaining a topic. Those 16 have no `relevance` entry for the new
slug — the same known gap note 0012 describes, and still out of scope here.

Collection runs get slower by roughly one throttled request per abstract-less
paper, bounded by `max_lookups`. Set `conferences.abstracts.enabled: false` to
opt out entirely.
