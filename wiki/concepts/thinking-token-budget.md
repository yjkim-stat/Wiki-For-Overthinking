# thinking-token budget

<!-- auto:begin -->

A cap or target on how many tokens a reasoning model may spend thinking before answering, used both as a measurement device (OAA_t scores accuracy only under a given token threshold t) and as a control target for training methods that calibrate output length to problem difficulty (as in the archive's overthinking-mitigation literature more broadly).

- **Kind**: concept
- **Also called**: token budget
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](auc-oaa.md), [difficulty-based routing between reasoning modes](difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](f1-otb-combined-metric.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [overthinking](overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](test-time-compute-scaling.md), [trained difficulty-based router / oracle router](trained-difficulty-based-router-oracle-router.md), [underthinking](underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
