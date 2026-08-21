# GSM-Hard

<!-- auto:begin -->

GSM-Hard appears in the archive as the hard end of the grade-school arithmetic family, and it sits on the losing side of the easy/hard split the group tracks. C4 groups it with GSM8K, MATH, SVAMP and ASDiv as 'long-reasoning' at a 256-step budget, where it scores 37.0 against a 35.0 full-decoding baseline; in that regime C4's global exit gate mostly declines to fire and no speedup exceeds 6.32x, against 13x or more on the short-answer sets and 8.69x on code. SLPO uses it as one of three held-out sets (with GSM8K-Test and MultiArith) for latent reasoners trained on GSM8K-Aug, and reports gains only at the level of the whole 12-cell table rather than per benchmark. So the archive's evidence on GSM-Hard is that the same stopping machinery that saves 92-95% of the budget on short-answer tasks saves comparatively little here.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [C4](../methods/c4.md), [COCONUT](../methods/coconut.md), [CODI](../methods/codi.md), [CoLaR](../methods/colar.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Early Exit](../methods/early-exit.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [HumanEval](humaneval.md), [Latent reasoning](../concepts/latent-reasoning.md), [MATH](math.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [RLOO](../methods/rloo.md), [SVAMP](svamp.md), [Test-time scaling](../concepts/test-time-scaling.md), [Thinking Budget](../concepts/thinking-budget.md)

## Appears in

- [SLPO: Scaling Latent Reasoning via a Surrogate Policy](../../archive/papers/2026/arxiv-2607-19691/summary.md) — SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.
- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
