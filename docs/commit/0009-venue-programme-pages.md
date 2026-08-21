# 0009 — Collect from the venues' own programme pages

| | |
| --- | --- |
| **Commit** | `feat(collect): read the accepted programme off the venue virtual sites` |
| **Scope** | `pipelines/collect/virtual_site.py`, `pipelines/collect/conferences.py`, `config/sources.yaml`, `pipelines/common/schema.py`, `tests/test_virtual_site.py`, `README.md` |
| **Kind** | feature |

## What changed

The conference collector gained a fourth index: the venue's own virtual site,
at `https://<host>/virtual/<year>/papers.html`. ICML, NeurIPS and ICLR ship
with a `virtual_host` set; a run sweeps the current programme year and the one
before it, and a year split across locations (NeurIPS 2025) lists each one.

This is the only index of the four that cannot be wrong about whether a paper
was accepted. The other three are second-hand: Semantic Scholar lags,
OpenReview's venue ids drift between cycles and are guessed at, DBLP arrives
with the proceedings. The programme page is the venue saying what it accepted,
on the day it says it.

## Why it is built this way

**Fetched per venue-year, not per topic.** The other three indexes are queries,
so they belong inside the per-topic loop. A programme page is not a query — it
is the same page whoever is asking. Running it inside that loop would refetch
the same six pages once per tracked topic. So it runs once, after the loop, over
the union of the venues the topics ask for, and scores each title against every
topic locally. Narrowing venues on one topic therefore cannot hide a venue from
another.

**A title is scored before an abstract is fetched.** The listing carries titles
only; abstracts and authors live on each paper's own page, and there are
thousands per venue. Scoring the title first and fetching only the matches
bounds the second round of requests to the papers somebody might actually read.
This is safe in one direction and not the other, which is worth stating
plainly: because adding text can only add keyword matches, a title-only score is
a *lower bound* on the final one, so nothing that would have cleared a threshold
is dropped by the gate. What the gate cannot see is a paper whose keywords
appear only in its abstract. That paper is left to the three indexes that do
search abstracts — which is why this is a fourth index and not a replacement.

**Parsed on the URL shape, not the markup.** `/virtual/<year>/poster/<id>` has
outlived several redesigns of the page around it; a CSS class has not. Detail
pages are read through Highwire `citation_*` meta tags first, because those are
emitted for Google Scholar and so are the one part of the page under outside
pressure to stay put.

**A shape change is loud, not silent.** A page that fetches but parses to zero
papers logs a warning rather than being reported as an empty programme. The
failure mode this guards against is the bad one for an archive: a scraper that
quietly returns nothing forever and looks like a quiet week.

**Records are stamped `<year>-01-01`.** Programme pages carry no per-paper
publication date. Nothing downstream filters on `published` — collection is
gated by score and by the dedup store — so the coarse stamp costs ordering
within a year and nothing else. The dedup store is also why refetching the same
programme every day does not re-queue the same reading task.

## Trade-offs and rejected alternatives

**Rejected: fetch every paper's detail page.** Complete, and thousands of
requests per venue per run. The title gate gives most of the benefit at a
bounded cost, with `max_details_per_run` as the hard ceiling.

**Rejected: titles only, and let dedup supply abstracts.** Zero extra requests,
and papers this index finds *first* — the ones that are the reason to have it —
would reach the reader with no abstract at all.

**Accepted cost: the abstract-only match is invisible here.** See above. It is a
real gap, mitigated by the other three indexes rather than closed.

**Accepted cost: the embedded-JSON path guesses a detail URL.** When a page
ships its programme as a JSON blob, the per-paper link is reconstructed rather
than read. A wrong guess 404s and the record keeps whatever the blob carried,
which is usually the abstract already.

## What a reviewer should check

**The markup assumptions are not validated against the live sites.** The
environment this was written in blocks egress to `icml.cc`, `neurips.cc` and
`iclr.cc` (and to the other collectors' endpoints), so the parsers were written
against the documented URL shape and tested against the fixtures in
`tests/test_virtual_site.py` — not against a real page. Those fixtures are the
first thing to correct once a real page can be fetched; `parse_listing` and
`parse_detail` are pure functions of page text precisely so that swapping in a
captured page is the whole job. Until then, treat a `virtual site ... returned
no papers` warning in the run log as the expected symptom of a wrong guess.

Verify the URLs match the venues' real ones:

```bash
python3 -c "
from datetime import date
from pipelines.common import config as c
from pipelines.collect import virtual_site as vs
cfg = c.load(); b = cfg.sources['conferences']['virtual_site']
ys = vs._years(b, date.today(), date.today())
[print(u) for v in cfg.sources['conferences']['venues'] for _, u, _ in vs._listing_urls(v, ys)]"
```

Then check that the title gate really is a lower bound (`_fill_details` is only
reached by entries with a non-empty `scores`), and that a venue with no
`virtual_host` is skipped rather than fetched from a guessed hostname.

## Downstream impact

A deployed copy keeps working untouched: `virtual_site` defaults to enabled,
but only venues carrying a `virtual_host` are fetched, and no existing venue
list has one. To turn it on, add `virtual_host: "<venue>.cc"` to the venues in
`config/sources.yaml` — the three shipped defaults show the shape, including
`virtual_locations` for a year split across sites. Papers from this index carry
`source: virtualsite`, which is a new value in that field for anything reading
the records directly.
