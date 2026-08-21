# 0030 — One topic with results hid the others

| | |
| --- | --- |
| **Commit** | `fix(collect): gate the arXiv listing fallback per topic, not per run` |
| **Scope** | `pipelines/collect/arxiv.py`, `tests/test_arxiv_listing.py` |
| **Kind** | fix |

## What changed

`arxiv.collect` now records which topics the API answered with nothing and, in
`auto` mode, runs the listing fallback for exactly those. Previously the gate
was `not collected` — a single dict accumulated across every topic — so the
fallback ran only when the API returned nothing for the entire run.

## Why it is built this way

**The condition was inverted against its own purpose.** The fallback exists for
the case where the API does not answer. With five topics sharing four
categories, some topic almost always matches something, so `not collected` was
almost never true, and the topics that most needed the fallback were the ones
guaranteed not to get it. It had never fired in a scheduled run: `grep`ping two
days of logs for the message it emits returns nothing, while calling
`arxiv.collect` with a single unanswered topic returns sixteen papers from the
listing, ten of which were absent from the archive.

**The gate belongs at topic granularity because that is what the fallback
consumes.** `arxiv_listing.collect` derives its categories from the topics it is
given and keeps only titles those topics score, so passing the barren subset
narrows the crawl and the filter at once. Passing all topics would re-crawl
categories on behalf of topics that were already answered.

**"Answered" means this topic's queries returned entries, not that the shared
dict grew.** Topics overlap heavily here, so a topic whose every result was
already contributed by an earlier topic still had its queries answered. Counting
dict growth marks such a topic barren and sends it to the fallback for nothing.
This is not hypothetical — the first implementation did exactly that, and the
test `test_no_listing_request_when_every_topic_was_answered` is what caught it.

**A topic whose queries all errored is barren, deliberately.** The existing code
logs an `HTTPError` and continues, contributing no papers; such a topic now
reaches the fallback, which is the case the fallback was written for — the API
host is blocked and the website is not.

## Trade-offs and rejected alternatives

- *Set `listing.mode: always`.* Rejected: the listing cannot search abstracts,
  so it sees strictly less than the API. Running it unconditionally spends
  requests on categories the API already covered, and the config comment
  already says `auto` is the intended setting.
- *Keep the run-level gate and widen the lookback instead.* Rejected — it
  addresses a different failure. A wider window helps when the API answers; it
  does nothing when the API returns nothing for a topic, which is the case here.
- *Count papers rather than entries per topic.* Rejected for the overlap reason
  above; `_parse_entry` returning `None` for a malformed entry would also make
  a genuinely answered topic look barren.
- The cost accepted: a run where the API answers four of five topics now makes
  listing requests it did not make before — a handful per category for the one
  barren topic, at the listing's slower interval. That is the intended expense.

## What a reviewer should check

- `answered` is set from `_parse_entry` succeeding, not from `entries` being
  non-empty. Those differ when a page parses to entries that all fail to yield
  a paper, and treating that topic as answered would hide a parse regression.
- Topics skipped for other reasons — `source_enabled("arxiv")` false, or no
  query built — are `continue`d before the flag is set, so they are not in
  `barren` and do not pull the listing in. That is deliberate: a topic that
  opted out of arXiv should not be collected from arXiv by another route.
- The log line now names the barren topics. If it ever reports every topic on a
  normal day, the API is failing rather than the window being narrow.

## Downstream impact

Runs will collect more, and on a day when the API answers unevenly they will
make listing requests they did not make before. Any deployment that had
concluded the fallback was dead code should expect it to start firing. Papers it
recovers now carry announcement dates, per
[0029](0029-a-listing-record-with-no-date-is-second-class.md); without that
change they would arrive undated and be filed under an unknown year.
