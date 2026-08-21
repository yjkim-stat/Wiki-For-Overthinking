# 0027 — A reference for every external request the pipeline makes

| | |
| --- | --- |
| **Commit** | `docs: describe every external source the pipeline collects from` |
| **Scope** | `docs/API.html`, `README.md` |
| **Kind** | docs |

## What changed

`docs/API.html` — a standalone page describing each source this repository
fetches from: the endpoint, the request it builds, what comes back, what that
source is authoritative about, what it cannot tell you, and how it fails.

It also documents the layers around the sources that are easy to miss when
reading one collector at a time: the shared HTTP client, scoring,
deduplication, and the coverage ledger.

## Why it is built this way

**Organised by question answered, not by module.** The first thing the page
establishes is that the sources fall into three kinds — *search* (a query goes
out, a filtered set comes back), *browse* (everything comes back, filtering is
local) and *hand* (a person decided). That distinction explains most of the
design decisions further down: why the venue programme pages can be checked for
completeness and Semantic Scholar cannot, why the arXiv listing has worse recall
than the arXiv API, why the inbox bypasses scoring. A module-by-module tour
would have listed the same facts and explained none of them.

**Each source says what it cannot tell you.** A reference that only lists
capabilities invites the reader to assume the gaps are covered. OpenReview knows
about acceptance and is often unreachable; DBLP has no abstracts; the arXiv
listing cannot search them. Those are the facts that decide which source to
trust for what.

**The failure modes are documented as prominently as the endpoints**, because in
this system they are the interesting part. The page states the rule directly —
the dangerous failure is not the loud one but the wrong subset that looks like a
complete one — and every warning it describes exists because that happened:
a venue filter that excluded every preprint, a keyword that missed its own
plural, a parser that read a login link as a paper.

**Standalone HTML, no build step and no external requests.** The CSS is inline
and there are no fonts, scripts or images to fetch, so the file opens correctly
from a clone, from a file:// URL, or from a viewer with no network. That matches
how the rest of the repository is deployed — by copying.

**It admits it can go stale.** The footer says plainly that where the page and
`pipelines/collect/` disagree, the code is right and the page has a bug. A
document that claims to be authoritative over code it does not generate from is
lying about its own reliability.

## Trade-offs and rejected alternatives

**Rejected: generate it from docstrings.** The collectors' docstrings are
already good, and a generated page would reproduce them without the
cross-cutting material — the three-kinds distinction, the failure table, the
config index — which is most of the value here.

**Rejected: Markdown in `docs/`.** Reasonable, and the request was specifically
for HTML. The tables comparing request shapes across eight sources also read
better with real column control.

**Cost: it is hand-maintained and will drift.** A new collector, a changed
default or a renamed config key will not update it. Mitigated only by the
footer's admission and by the fact that `docs/commit/` remains the authoritative
record of *why* each behaviour exists.

## What a reviewer should check

The facts, against the code — the page makes specific claims that are cheap to
verify and embarrassing to get wrong:

- Request parameters against `pipelines/collect/arxiv.py`,
  `conferences.py`, `arxiv_listing.py` and `youtube.py`.
- Per-host intervals: 3 s for the arXiv API, 5 s for the listing pages and PDF
  fetching, 1 s for the conference indexes and YouTube.
- Defaults in the configuration index against `config/settings.yaml` and
  `config/sources.yaml`.

- The storage claim in §05 against `.gitignore`: `data/abstracts/` is ignored
  and `data/index/coverage.jsonl` is not. The first draft of this page said the
  opposite, which is exactly the drift the footer warns about — it was written
  before [0026](0026-abstracts-are-not-committed.md) settled the question.

Anchors and tag balance were checked mechanically; content accuracy was not, and
is what review is for.

## Downstream impact

None to the pipeline. A deployment that has changed its sources or intervals
should expect this page to describe the template's defaults rather than its own.
