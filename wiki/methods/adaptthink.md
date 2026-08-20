# AdaptThink

<!-- auto:begin -->

A length-based reward-shaping reinforcement-learning method for controlling reasoning length. OptimalThinkingBench tests it as one of five overthinking mitigations, where it cuts thinking tokens on math questions by up to 82% but only 37% on non-math questions, and is noted as the one tested method that improves both the over- and under-thinking sub-benchmarks together. TRAAC uses it as its strongest RL baseline (40.3% accuracy at 6.8k tokens on AIME/AMC/GPQA-D/BBEH, versus TRAAC's 48.2% at 4.8k tokens).

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [BBH (Big Bench Hard)](../datasets/bbh-big-bench-hard.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](l1-length-controlled-reinforcement-learning.md), [LC-R1](lc-r1.md), [Model Merging](model-merging.md), [overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [TokenSkip](tokenskip.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
