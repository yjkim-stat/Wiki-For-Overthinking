# 0100 — A source that answers 403 to everything

| | |
| --- | --- |
| **Commit** | `chore(sources): stop asking OpenReview, which refuses every request` |
| **Scope** | `config/sources.yaml` |
| **Kind** | chore |

## What changed

`conferences.openreview.enabled` is now `false`. Nothing else moves: the
`api_url` stays, and every venue keeps its `openreview_prefix`, so re-enabling
is one word.

## Why it is built this way

`api2.openreview.net` answered HTTP 403 to every lookup on 2026-08-21, from
this machine and from the scheduled cloud environment alike. Two hosts with
different network policies failing identically is what separates "the source is
refusing us" from "this box cannot reach it", and only the first is worth
acting on in config.

A source that fails on every attempt is not free. It costs three requests and
their retries per run, and it puts a line in every digest's "Run problems" —
which is the actual damage, because a standing failure is how a genuinely new
one gets lost. The run-level `give_up_after_failures` already bounds the cost
within a single run; it cannot stop the run after next from paying it again.

What this loses is early sight of a venue between decisions and proceedings.
It does not lose the venues: Semantic Scholar and the programme pages
(`virtual_site`) both cover NeurIPS, ICLR and ICML, and DBLP backs them.

The flag is turned off rather than the block deleted, and the reason is written
where the flag is, because the next person to wonder why OpenReview is missing
will look at `sources.yaml` and not at this note.

## Trade-offs and rejected alternatives

Turning it off means nothing will notice when OpenReview starts answering
again. That is the real cost, and it is accepted: the alternative — leaving it
enabled and reading past its failures every night — is how the digest's problem
list stops being read at all.

Rejected: raising `retries` or lowering `give_up_after_failures` for this source
only. Neither addresses a source that is refusing rather than flaking, and both
add a knob whose correct value is unknowable from here.

Rejected: removing the venues' `openreview_prefix` entries. They cost nothing
while the collector is off and they are exactly what a re-enable needs.

## What a reviewer should check

- `python3 -m pipelines.run_daily --dry-run` — no OpenReview request is made and
  no OpenReview line appears under run problems.
- The next digest under `archive/daily/` should have a shorter "Run problems"
  section, not an empty one: `export.arxiv.org` rate limiting and any transient
  DBLP failure are still reported, which is the point.

## Downstream impact

For a deployment that reads review-bearing venues before proceedings: it will
stop seeing them early. Set `enabled: true` to restore, and nothing else has to
change.

## Note on the number

This note is 0100 rather than 0075. `origin/main` here stops at 0074, so the
rule in `CLAUDE.md` — pick against a fetched `origin/main` — points at 0075.
The template repository this deployment tracks (the `src` remote) already holds
0075 through 0099, so following that rule to the letter would file twenty-five
collisions against the next merge, which is the exact harm the rule exists to
prevent. The number is picked above upstream's head instead. See
`0074-taking-the-template-back-in.md` for the first collision and how it was
resolved; upstream pushed first then, and will again.
