# trained difficulty-based router / oracle router

<!-- auto:begin -->

Two variants of a router that decides per query whether a hybrid model should think or answer directly: a 'trained' router learned from data, and an 'oracle' router with perfect foresight of which mode would have been correct, used as an upper-bound comparison. OptimalThinkingBench finds a trained router improves its combined F1^otb metric 20.4% on average over the best single mode, but still trails the oracle router by roughly 15 points -- showing real routers leave most of the achievable gain on the table.

- **Kind**: concept
- **Also called**: difficulty-based routing between reasoning modes
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [test-time compute scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
