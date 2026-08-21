# AUC_OAA

<!-- auto:begin -->

A metric from OptimalThinkingBench for scoring overthinking: Overthinking-Adjusted Accuracy (OAA_t) counts a response correct only if it also stays under a thinking-token threshold t, and AUC_OAA is the area under the OAA_t curve as t sweeps up to 1000 tokens. A model that reaches the right answer but keeps generating unnecessary tokens scores lower on AUC_OAA than one that stops promptly, even at equal raw accuracy.

- **Kind**: concept
- **Also called**: OAA, Overthinking-Adjusted Accuracy
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [Overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [Test-Time Compute Scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
