# DAPO

<!-- auto:begin -->

No archived paper is about DAPO; it is named only in passing, and always as a GRPO-style clipped policy-optimization algorithm for RL with verifiable rewards. IAPO uses it as one baseline among GFPO, GTPO and S-GRPO, reporting the better Pass@k/Length@k ratio against it; other archived work borrows specific pieces of it, namely its clipped objective with asymmetric bounds and token-level aggregation, and its soft overlong penalty. QuRL uses the bare name loosely for training data rather than for the algorithm, which is the DAPO-Math-17k corpus, so the same string denotes both a method and a dataset in the archive and the two are kept as separate entries here. Nothing archived expands the acronym or describes the full method.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink](adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AutoThink](autothink.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [Dr. GRPO](dr-grpo.md), [GFPO](gfpo.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [RLVR](rlvr.md), [routing collapse](../concepts/routing-collapse.md), [S-GRPO](s-grpo.md), [Thinkless](thinkless.md)

## Appears in

- [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](../../archive/papers/2026/arxiv-2608-20256/summary.md) — Trains a 1.5B reasoning model to emit one of three mode tokens (NoThink, Short, Long) as the very first token of its response and to reason under that mode's budget, learned end-to-end inside GRPO with no separate router.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
