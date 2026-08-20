# hybrid thinking/non-thinking models

<!-- auto:begin -->

Language models shipped with a switchable thinking mode (extended chain-of-thought) and a non-thinking mode (direct answer), so the same weights can behave as either. OptimalThinkingBench evaluates such models (e.g. the Qwen3 hybrid family) and finds their non-thinking mode underthinks hard problems (as low as 20% accuracy) while thinking mode overthinks simple ones -- motivating its difficulty-based routing experiments.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT 2025](../datasets/hmmt-2025.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
