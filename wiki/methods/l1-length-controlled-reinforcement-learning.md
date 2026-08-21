# L1 length-controlled reinforcement learning

<!-- auto:begin -->

A reinforcement-learning method that adds a length-based reward term to directly control how many tokens a reasoning model generates. OptimalThinkingBench tests it as one of five overthinking mitigations: L1 (with AdaptThink) cuts OverthinkingBench token usage substantially but, like the other length-reduction methods tested, tends to degrade UnderthinkingBench accuracy.

- **Kind**: method
- **Also called**: L1
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [Model Merging](model-merging.md), [Overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
