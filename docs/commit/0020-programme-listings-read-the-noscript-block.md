# 0020 — Read the programme out of the `<noscript>` block

| | |
| --- | --- |
| **Commit** | `fix(collect): parse the programme listing from its noscript fallback` |
| **Scope** | `pipelines/collect/virtual_site.py`, `config/sources.yaml`, `tests/test_virtual_site.py` |
| **Kind** | fix |

## What changed

The virtual-site collector added in [0009](0009-venue-programme-pages.md) now
parses only the page's `<noscript>` block, where the venue publishes the whole
programme as a plain `<ul>` of links. The speculative embedded-JSON path is
gone, venues can pin their own `virtual_years`, and the record's venue carries
the year.

0009 shipped with its markup assumptions unvalidated, because egress to the
venue hosts was blocked and still is. Its note said the fixtures were the first
thing to correct once a real page could be seen. A field report describing the
live pages arrived, and this is that correction.

## Why it is built this way

**The `<noscript>` block is the stable part, and reading only it is a
correctness fix rather than a tidiness one.** 0009 swept the whole document for
`/virtual/<year>/(poster|oral|…)/<id>` anchors, reasoning that the URL shape had
outlived several redesigns. It has — but the navigation bar's **login link
points at a poster path too**. That parser would have minted a paper titled
"Login" on every run, from every venue, and it would have looked like an
ordinary record. The fallback block exists to be read without a browser, which
is exactly why it is both the most stable region of the page and the one that
contains only papers.

**No fallback means no papers.** If the block is absent the collector returns
nothing rather than reverting to a looser scan. A page that is not the shape
this collector understands is a page it should decline to interpret; guessing at
the rest is how a scraper starts producing plausible rubbish. The existing
zero-result warning is what makes that visible.

**Entries are anchored on `<li>`**, so the "Enable Javascript in your browser"
sentence that shares the block cannot contribute an entry.

**Venues are not on the same cycle.** In the second half of a calendar year
ICML's current programme is that year's while NeurIPS's is still the previous
one, so a single shared sweep asks half the venues for a page that does not
exist. `virtual_years` pins the years that do; venues without it keep the
`years_back` sweep.

**The venue string now carries the year.** "ICML 2026" is the fact this
collector exists to record — that the paper cleared review at that edition.
Merged onto a preprint record by the title fingerprint, that string is the whole
of what the archive learns, and a bare "ICML" would not say which edition.

**The title fingerprint was already right and is worth restating.** Most of
these papers appeared as preprints first, so `canonical_paper_id(title=…)` makes
deduplication merge the listing onto a record the archive already holds. The
value is not more papers; it is that existing papers gain an acceptance. A
deployment should expect `data/papers/` records to change without new papers
appearing — that is the merge working, not a bug.

## Trade-offs and rejected alternatives

**Rejected: keep the whole-page scan as a fallback when `<noscript>` is
missing.** It reintroduces the login-link defect in exactly the situation where
nobody is watching — a page shape has just changed, so the operator is already
being told something is wrong.

**Rejected: the issue report's `proceedings.sites` config shape.** It lists
venue names a second time, separately from `conferences.venues`, where
`dblp_key` and `openreview_prefix` already live. Folding `virtual_host` and
`virtual_years` into the existing venue entry keeps one row per venue carrying
all of its identifiers. The per-venue years — the substantive part of that shape
— are adopted.

**Cost: still unvalidated against a live page.** Egress remains blocked, so this
is written against a field report rather than a fetched document. It is a large
improvement in confidence and not a substitute for one real fetch. The detail
page parser in particular is unchanged and still heuristic.

**Cost: `max_details_per_run` can bind.** A measured ICML programme listed 6,628
papers, of which 153 matched a three-topic deployment — more than the cap of 60.
What is dropped keeps its title and loses only its abstract, and the run logs the
count.

## What a reviewer should check

The login link is the specific regression this commit exists to prevent:

```bash
python3 -m unittest tests.test_virtual_site -v -k navbar
```

The fixture in `tests/test_virtual_site.py` now carries a navbar login link
pointing at `/virtual/2026/poster/00000`; if that test ever passes with a looser
parser, the parser is wrong. `test_a_page_without_the_fallback_block_yields_nothing`
is the other guard.

Then confirm the URLs match the venues' real cycles:

```bash
python3 -c "
from datetime import date
from pipelines.common import config as c
from pipelines.collect import virtual_site as vs
cfg = c.load(); b = cfg.sources['conferences']['virtual_site']
ys = vs._years(b, date.today(), date.today())
[print(u) for v in cfg.sources['conferences']['venues'] for _, u, _ in vs._listing_urls(v, ys)]"
```

## Downstream impact

A deployment already running 0009 gains correctness and loses nothing: the
whole-page scan produced a spurious "Login" paper per venue per run, which can
be found and deleted by searching `data/papers/` for `source: virtualsite` with
a one-word title.

`config/sources.yaml` gains `virtual_years` on the three shipped venues. A
deployment with its own venue list should add the key to any venue whose cycle
does not match the default sweep; without it, behaviour is unchanged.

Records from this collector now carry `venue: "<VENUE> <year>"` rather than
`"<VENUE>"`. Existing records are not rewritten until the paper is seen again.
