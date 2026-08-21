# SuperGPQA

<!-- auto:begin -->

A large, broad-domain multiple-choice science-question dataset used as a source pool in the archive: TRAAC references it as part of its evaluation suite, and OptimalThinkingBench draws its 72-domain OverthinkingBench questions from SuperGPQA before filtering for unambiguous, easy items.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [BIG-Bench Hard](big-bench-hard.md), [CMIMC25](cmimc25.md), [DAPO-Math-17k](dapo-math-17k.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO (Group Relative Policy Optimization)](../methods/grpo-group-relative-policy-optimization.md), [HMMT 2025](hmmt-2025.md), [LC-R1](../methods/lc-r1.md), [MMLU-PRO](mmlu-pro.md), [OverthinkingBench](overthinkingbench.md), [Self-Certainty](../concepts/self-certainty.md), [test-time scaling](../concepts/test-time-scaling.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
