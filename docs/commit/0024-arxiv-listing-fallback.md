# 0024 — Read arXiv's listing pages when the API will not answer

| | |
| --- | --- |
| **Commit** | `feat(collect): fall back to the arXiv listing pages when the API is unavailable` |
| **Scope** | `pipelines/collect/arxiv_listing.py`, `pipelines/collect/arxiv.py`, `pipelines/common/html.py`, `pipelines/collect/virtual_site.py`, `config/sources.yaml`, `tests/test_arxiv_listing.py` |
| **Kind** | feature |

## What changed

A second way into arXiv: `arxiv.org/list/<category>/recent`, paginated, parsed
from the definition list the page has used for years. `arxiv.listing.mode`
governs it — `auto` (default) uses it only when the API returned nothing,
`always` uses it instead of the API, `never` turns it off.

Also, and this is a correctness fix that reaches further than the new
collector: every structural HTML parse now strips comments first.

## Why it is built this way

**The API and the website are different hosts.** `export.arxiv.org` is the
right way to read arXiv and stays the default. But a network policy, a
corporate proxy or an arXiv-side rate limit can block one and leave the other
readable, and when that happens the collector's failure is total and silent —
the run reports a quiet day. This is the same shape as OpenReview answering 403
to every venue lookup from a blocked host, which the archive already lives with.

**`auto`, not `always`, and this is the substantive design decision.** The
listing sees *strictly less* than the API: it carries titles, authors and
subjects, and no abstracts. So a paper whose keywords appear only in its
abstract is invisible to it, where the API's `all:` search would have found it.
That is a real loss of recall, not a rounding error, and it is why the fallback
only runs when the alternative is nothing at all. A deployment that is
permanently blocked from the API sets `always` and accepts the trade knowingly.

**Titles are scored before abstracts are fetched**, the same arrangement as the
conference programme collector, and for the same reason: reading a day's
announcements costs a handful of requests, while fetching every abstract would
cost thousands. Because adding text can only add keyword matches, a title-only
score is a lower bound — nothing that would have cleared a threshold is dropped
by the gate.

**The crawl is bounded and says so.** `max_pages`, `page_size`, a 5s floor of
its own, and a stop as soon as the page's declared total is covered. arXiv asks
not to be crawled hard, and scoring locally is what makes politeness and
usefulness the same choice rather than opposed ones. The circuit breaker from
[0018](0018-give-up-on-a-dead-host.md) composes on top: a blocked `arxiv.org`
costs five failures and then nothing.

**Entries are anchored on a `<dt>`/`<dd>` pair.** The page links to `/abs/`
from its browse-context sidebar as well, so matching bare `/abs/` links would
invent papers — the same failure the conference collector had with a login link
in [0020](0020-programme-listings-read-the-noscript-block.md).

**Comments are stripped before structural matching, everywhere.** This was
found by a test rather than reasoned out: a fixture whose *comment* read "this
block carries no `<dt>`" handed the parser a false entry, and it took the
sidebar's identifier with it. Real pages carry commented-out markup, so this
was not a fixture artefact — it was the fixture doing its job. `virtual_site`
had the same exposure and is fixed by the same helper.

**Records carry an `arxiv:` id.** Deduplication merges them onto whatever the
archive already holds, so a paper found by the listing and later by the API is
one record.

## Trade-offs and rejected alternatives

**Rejected: make the listing the primary source.** It cannot search abstracts
and cannot honour a `--days 90` backfill — `/recent` is arXiv's announcement
window, not a date range a caller chooses. It is a fallback because it is
worse, not because it is newer.

**Rejected: fetch every announcement's abstract to close the recall gap.** That
is one request per announced paper — thousands a day for a busy category — to
recover papers whose titles say nothing relevant. The cap exists so this cannot
happen by accident.

**Cost: recall is title-limited while the fallback is in use.** Stated in the
module docstring and in `config/sources.yaml` so nobody discovers it from a
thin archive.

**Cost: this is scraping, and it can break.** A page shape change yields zero
entries and a warning rather than wrong records, which is the best available
outcome, but it is still a page that can be redesigned without notice.

## What a reviewer should check

The two traps, both of which are tested because both have bitten this
repository:

```bash
python3 -m unittest tests.test_arxiv_listing -v
```

`test_a_sidebar_abs_link_is_not_an_announcement` guards the false-entry case.
`test_max_pages_bounds_the_crawl` asserts the request count, not just the
result — a bound that is not observed in the call count is not a bound.
`test_never_means_the_api_result_stands` confirms the fallback cannot fire when
it is switched off.

Then check the mode logic in `arxiv.collect`: `auto` must not run the listing
when the API returned anything at all, or a blocked-abstract-search path
silently becomes the normal one.

**Not validated against a live page.** Every arXiv host is blocked from this
environment — `arxiv.org`, `export.arxiv.org` and `rss.arxiv.org` alike — so the
parser is written against the documented page shape and tested against fixtures,
exactly as [0009](0009-venue-programme-pages.md) was before a field report
corrected it. The fixture in `tests/test_arxiv_listing.py` is the file to
correct first once a real page can be fetched.

## Downstream impact

`config/sources.yaml` gains an `arxiv.listing` block. Behaviour is unchanged
while the API works, because `auto` only fires when the API returned nothing —
a deployment that pulls this and never notices it is a deployment whose API
access is fine.

A deployment permanently blocked from `export.arxiv.org` sets `mode: always`
and should expect lower recall than it had before the block, not equal recall.
