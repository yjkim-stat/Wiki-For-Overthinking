# diminishing returns

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [answer stabilization](answer-stabilization.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [budget forcing](../methods/budget-forcing.md), [generation-verification gap](generation-verification-gap.md), [greedy decoding](../methods/greedy-decoding.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [paired bootstrap](../methods/paired-bootstrap.md), [pool oracle](pool-oracle.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [reproducibility](reproducibility.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — Treats test-time scaling as routing rather than budgeting -- cheap evidence decides whether a decision is already settled, and expensive verification is spent only on candidates that can still change the answer -- and evaluates every baseline by replaying it over the same stored candidate pool so that only the allocation decision differs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
