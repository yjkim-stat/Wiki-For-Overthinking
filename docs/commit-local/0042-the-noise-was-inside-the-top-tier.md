# 0042 — The noise was inside the top tier

| | |
| --- | --- |
| **Commit** | `archive: discard 90 readings that no overthinking claim rests on` |
| **Scope** | `data/papers/`, `data/summaries/papers/`, `data/index/`, `archive/`, `wiki/`, `outputs/`; `docs/commit-local/0042-the-noise-was-inside-the-top-tier.md` |
| **Kind** | chore · editorial · breaking |

## What changed

Ninety of 282 readings were discarded through `scripts/discard.py --id`, one
id at a time, after every reading in the archive was reviewed against a single
question: *if this record were gone, would any claim the archive makes lose
support?*

```
data/papers/          282 -> 192
data/summaries/       282 -> 192
wiki entities       3,166 -> 2,280
```

`archive/`, `wiki/` and `outputs/` were then regenerated from what remains.

## Why it is built this way

**The request that started this was to keep only top-tier venues, and the
numbers said that filter would have done the opposite of what was wanted.**
208 of the 282 readings already carried an ICLR, ICML or NeurIPS venue. The 71
with no venue were, almost entirely, arXiv preprints from the preceding six
weeks — the frontier, which has not had time to be accepted anywhere. Every
paper this archive's own fixed-point and allocation analyses rest on sits in
that group. Filtering by venue would have deleted the newest work and kept the
noise.

**Because the noise was inside the top tier.** Of the ninety discarded, 72
carry ICLR, ICML or NeurIPS. Venue is a statement about a paper's quality; it
says nothing about whether the paper is about this topic. The archive's
problem was never quality.

**What it was, instead, was a keyword rule firing on other fields.** The
discards fall into six kinds, and each is a different way for `test-time`,
`early exit`, `compute-optimal`, `adaptive reasoning` or `overthinking` to be
the right words about the wrong subject:

| Kind | n | What matched |
| --- | --- | --- |
| Another modality entirely | 31 | early exit in image classifiers, speech separation, TinyML, deep RL; test-time scaling of diffusion images, protein design, TSP, robot control |
| `compute-optimal` as a pretraining term | 8 | Chinchilla reconciliation, QAT budget splits, scaling-law phases — training-time compute, not test-time |
| Inference efficiency with no length claim | 5 | 4-bit quantization kernels, low-precision RL rollout, edge RAG compression |
| Test-time scaling applied to another task | 22 | GUI agents, CAD, text-to-SQL, time series, table re-ranking, VLA robots, RTL optimisation |
| Safety and security, no length claim | 6 | jailbreak robustness, geolocation leakage, and one paper titled *Overthinking* that is about weight-space secret extraction |
| Reasoning, but not how long it reasons | 18 | hallucination, sycophancy, prompt optimisation, GRPO variants measured on accuracy alone |

**Discard was the right instrument and it is deliberately hard to use.**
`scripts/discard.py` exists for exactly this — records a scoring mistake let
in — and it refuses `--rescore` on hand-filed PDFs, so removing one requires
naming its id. All ninety were named individually. The alternative,
hand-editing `data/`, is forbidden and would leave no record of the judgement.

**Every id was reviewed by reading its summary, not its score.** Scores were
no help: the discarded run 0.40 to 0.73 and the survivors run the same range.
A protein-design paper and *Think Shallow, Solve Deep* both score 0.50.

## Trade-offs and rejected alternatives

**This is close to irreversible, by design.** `discard.py` does not touch
`data/index/seen.sqlite`, so a discarded paper will not be collected again. A
discarded record should stay discarded — but it means a mistake in this review
costs a re-collection by hand, and there are ninety chances to have made one.
The list as applied is recoverable from this commit's diff.

**Rejected: raising `score.default_min_score` instead.** It would have cut
across the same range from both sides. The discarded and the kept score alike;
threshold is not the axis the mistake lives on.

**Rejected: restricting `semantic_scholar.restrict_to_venues` to the venue
list.** The config already warns why: a preprint's venue is recorded as
`arXiv.org`, so the filter drops every preprint — which here is the frontier.

**Deferred: 18 borderline records.** KV-cache compression for long reasoning,
layer-level early exit, reasoning-trace extraction, and papers that report a
token saving as a side effect of something else. They concern reasoning models
without being about how long a model reasons. They were listed and left in
place; a second pass is a separate decision.

**Not done, and this is the live risk: nothing stops the same papers arriving
again.** The topic's keywords and `min_score` are unchanged, and a dry run
taken just before this change reported 211 papers that would be archived on
the next collection. The rule that admitted these ninety is still the rule.
Until the keywords are narrowed, this is a sweep and not a fix.

## What a reviewer should check

- `ls data/papers/*.json | wc -l` → 192, and the same for
  `data/summaries/papers/`.
- No wiki note was orphaned: every concept record carrying a definition still
  has at least one piece of evidence. **43 are now at one**, below
  `wiki.promote_after_mentions: 2`, and survive because the carry-over rule
  never destroys authored text. Several are relics of the discarded domains —
  `gqa`, `pope`, `hellaswag`, `sst-2`, `libero-long`, `t5-large`,
  `contextual-bandits`. Retiring one destroys its definition, so none were.
- `python3 -m pipelines.render` on the reduced archive — `wiki.removed: 0`,
  `stale.analysis: 0`, and the run changes no record.
- The 11 records the `fixed-point-iteration` analysis cites are all present.

## Downstream impact

For this deployment only; the code is untouched. Note one gap this exposes,
which is a question for the code repository rather than a change here:

**A definition can now describe papers the archive no longer holds, and
nothing reports it.** `render`'s staleness check fires when a definition's
evidence *grows* past a multiple of what it was written against. It has no
counterpart for evidence that shrinks. A definition written against five
sources, three of which were discarded here, still reads as settled while
describing work that is gone — the same failure mode `refresh_definition_at`
was built for, in the other direction. The stale count fell from 25 to 16
through this change, which is the counter moving for the wrong reason.
