# SuperGPQA

<!-- auto:begin -->

A large, broad-domain multiple-choice science-question dataset used as a source pool in the archive: TRAAC references it as part of its evaluation suite, and OptimalThinkingBench draws its 72-domain OverthinkingBench questions from SuperGPQA before filtering for unambiguous, easy items.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [AUC_OAA](../concepts/auc-oaa.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [BIG-Bench Hard](big-bench-hard.md), [CMIMC25](cmimc25.md), [DAPO-Math-17k](dapo-math-17k.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO (Group Relative Policy Optimization)](../methods/grpo-group-relative-policy-optimization.md), [HMMT 2025](hmmt-2025.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [LC-R1](../methods/lc-r1.md), [MMLU-PRO](mmlu-pro.md), [Model Merging](../methods/model-merging.md), [overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](overthinkingbench.md), [Self-Certainty](../methods/self-certainty.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [TokenSkip](../methods/tokenskip.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
