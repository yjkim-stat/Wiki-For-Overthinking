# 0046 — Fifteen keywords that buy three papers

| | |
| --- | --- |
| **Commit** | `config(topics): add intervention vocabulary, and measure what it buys` |
| **Scope** | `config/topics/overthinking.yaml`; `docs/commit-local/` |
| **Kind** | config |

## What changed

Fifteen phrases naming inference-time intervention — `activation steering`,
`steering vector`, `representation engineering`, `sparse autoencoder`,
`logit bias`, `linear probe` and nine more — are added to the topic's `any`
list. Nothing else moves. `min_score` stays at 0.6.

The addition serves a survey of how a reasoning model is guided or controlled
mid-generation rather than retrained. The keyword list had no vocabulary for
that at all: papers on activation steering, logit-level control and
probe-driven exit reached this archive only when they also happened to say
"efficient reasoning" or "reasoning length".

## Why it is built this way

The widening was measured before it was made, because the interesting result
is how little it does. Four dry runs over the same 30-day window:

| keywords | `min_score` | would archive |
| --- | --- | --- |
| baseline | 0.6 | 62 |
| **+15 terms** | **0.6** | **65** |
| baseline | 0.35 | 438 |
| +15 terms | 0.35 | 613 |

Three papers. The reason is the interaction between the two levers rather
than either alone: work using this vocabulary mentions the overthinking terms
once in passing, so it scores around 0.25 and dies at a 0.6 bar no matter what
the `any` list contains. The band where this literature actually sits is
0.35–0.6, and the last row shows it is populated — adding the terms at the
lower bar is worth 175 papers, against 3 at the higher one.

So the honest reading is that vocabulary is not the binding constraint here,
and the change is kept anyway only because three papers a month is cheap and
an unmatched phrase costs nothing. The comment in the file carries these
numbers, so the next person to look at this list does not have to re-derive
why it is longer than it needed to be.

## Trade-offs and rejected alternatives

**Lowering `min_score` to 0.35 was rejected.** It is the change that would
actually reach this literature, and it multiplies the archive's intake by
seven. The bar was raised from 0.35 to 0.6 on 2026-09-01 against a calibration
of 1,347 already-scored items; reversing that for one survey trades a
permanent property of the archive for a temporary need.

**The route taken instead is `inbox/`.** Four papers that scored 0.25 and were
rejected — including *Controllable LLM Reasoning via Sparse Autoencoder-Based
Steering* and *Less is More: Improving LLM Reasoning with Minimal Test-Time
Intervention* — are filed by hand in the same session. That path exists for
exactly this case: filing a PDF is the editorial decision scoring tries to
approximate, so it skips scoring, and it reaches the four papers that matter
without moving a threshold that governs everything else.

## What a reviewer should check

- `python3 -m pipelines.run_daily --dry-run --days 30` should report a count
  near 65, not near 438. If it reports the larger number, `min_score` moved
  and this note's premise no longer holds.
- The four hand-filed PDFs should appear as queued reading tasks after the
  next `--source local` run, and their records should carry `bibliography`
  answers rather than keyword scores.

## Downstream impact

A deployment that pulls this file gets a slightly wider `any` list and the
same bar. Nothing already archived changes; nothing is re-scored. A deployment
that does not care about intervention methods can drop the block without
touching anything else, since the terms are additive and independent.
