# diminishing returns

<!-- auto:begin -->

Each additional unit of inference compute buying less than the one before, and in both sources here the shape that motivates routing rather than uniform spending. The compute-balanced routing work observes it directly in its ablation: the first few candidates escalated to strong verification buy a large accuracy gain while later ones cost more per point, which it reads as exactly what a compute-allocation view predicts -- verification is useful and its value depends on which candidate receives it. The refinement work exploits the same curvature by spending the budget on iteratively improving each sampled rollout rather than drawing more of them, on the premise that the marginal value of an additional independent sample falls faster than the marginal value of another refinement pass over an existing one. Neither source measures a scaling law; between them they establish the practical consequence, which is that a uniform budget spends its most expensive units where they are worth least, and that the presence of diminishing returns is what makes an allocation policy worth having at all.

- **Kind**: concept
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [answer stabilization](answer-stabilization.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [budget forcing](../methods/budget-forcing.md), [generation-verification gap](generation-verification-gap.md), [greedy decoding](../methods/greedy-decoding.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../methods/matched-budget-comparison.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [paired bootstrap](../methods/paired-bootstrap.md), [pool oracle](pool-oracle.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [reproducibility](reproducibility.md), [selection signal](selection-signal.md), [self-consistency](../methods/self-consistency.md), [self-correction](self-correction.md), [test-time compute](test-time-compute.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](../../archive/papers/2026/arxiv-2608-07424/summary.md) — Treats test-time scaling as routing rather than budgeting -- cheap evidence decides whether a decision is already settled, and expensive verification is spent only on candidates that can still change the answer -- and evaluates every baseline by replaying it over the same stored candidate pool so that only the allocation decision differs.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
