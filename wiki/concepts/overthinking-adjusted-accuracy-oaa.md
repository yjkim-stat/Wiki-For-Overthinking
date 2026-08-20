# Overthinking-Adjusted Accuracy (OAA)

<!-- auto:begin -->

OptimalThinkingBench's per-threshold overthinking metric: OAA_t counts a response correct only if it also stays under a thinking-token threshold t, so a model that reaches the right answer but keeps generating unnecessary tokens scores lower than one that stops promptly. AUC_OAA (area under the OAA_t curve to t_max=1000) is the summary version. Note: same metric as the archive's separately-tracked 'AUC_OAA' entry -- not merged.

- **Kind**: concept
- **Also called**: AUC_OAA, OAA
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [overthinking](overthinking.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](test-time-compute-scaling.md), [thinking-token budget](thinking-token-budget.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
