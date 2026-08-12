# 0016 — Turn off OpenReview: it now demands a bot challenge

| | |
| --- | --- |
| **Commit** | `config: disable the OpenReview collector` |
| **Scope** | `config/sources.yaml` |
| **Kind** | config |

## What changed

`conferences.openreview.enabled` becomes `false`, with a comment recording why
and what it would take to turn it back on.

The endpoint answers anonymous clients with:

```
HTTP 403  {"name":"ChallengeRequiredError",
           "message":"Challenge verification required",
           "details":{"challengeUrl":"https://openreview.net/challenge?..."}}
```

Setting the project's User-Agent makes no difference; the response is identical.
There is no header or query form that satisfies it, because the challenge is
meant to be completed in a browser.

## Why it is built this way

**A collector that cannot succeed should not be asked to try.** The pipeline is
deliberately fail-soft — an unreachable source is logged and skipped, and a run
that loses one is not a failed run. That is the right behaviour for an outage.
It is the wrong behaviour for a permanent condition, because every venue in
`conferences.venues` with an `openreview_prefix` costs the run a request plus its
retry budget on every firing, forever, to produce nothing. The daily log fills
with errors that carry no information.

**Coverage is not what is lost.** Semantic Scholar indexes the same venues, and
the venue list here keeps `dblp_key` entries alongside. What OpenReview provided
was *earliness* — review-bearing venues appear there before they reach
proceedings — so the cost of this change is that ICLR and COLM papers arrive in
the archive later, not that they are missed. For a group reading a literature
that also posts to arXiv, that lag is small.

**Disabled rather than deleted.** The block, its `api_url` and the
`openreview_prefix` fields on the venues all stay. If the endpoint reopens, or
this deployment gains credentials, the change is one boolean. Deleting the
configuration would make restoring it an archaeology exercise.

## Trade-offs and rejected alternatives

- *Implementing the challenge flow.* Rejected: it is a browser interaction by
  design, and automating around an anti-bot measure is both fragile and the
  wrong relationship to have with a service the group relies on.
- *Adding OpenReview credentials.* Not rejected on principle — an authenticated
  client may well work — but out of scope here, and it would put a secret in the
  run path of a pipeline that currently needs none.
- *Leaving it enabled and filtering the log.* Rejected: it hides the symptom and
  keeps paying the latency.
- *Dropping the COLM venue, which has no `dblp_key`.* Rejected: Semantic Scholar
  covers a venue with both index keys blank, which is the case the template's
  commented journal entry exists to document.

## What a reviewer should check

- The config still parses: `python3 -m unittest discover -s tests -t .` — 167
  tests, including `RealConfigTests`, which loads the shipped config as-is.
- That the venues keep their `openreview_prefix` values, so re-enabling is one
  boolean and not a rewrite.
- Whether the endpoint has reopened, before assuming this is still needed:
  `curl -sS "https://api2.openreview.net/notes?content.venueid=ICLR.cc/2026/Conference&limit=1"`
  should return notes rather than a `ChallengeRequiredError`.

## Downstream impact

A deployment that pulls this and relies on OpenReview for a venue Semantic
Scholar does not index will lose that venue. The check above says whether the
change is still warranted; flipping the boolean back restores the previous
behaviour exactly.

Nothing already in `data/` changes. Papers collected from OpenReview before this
stay, deduplicated against the same works arriving from other indexes as usual.
