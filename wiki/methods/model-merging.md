# Model Merging

<!-- auto:begin -->

Combining the parameters of two or more trained models into one, without further gradient-based training, to transfer a capability from one into the other. OptimalThinkingBench tests it as one of five overthinking mitigations, where -- like the other length-reduction methods -- it tends to trade OverthinkingBench gains against UnderthinkingBench accuracy; RAIN-Merging applies it gradient-free to merge an instruction-tuned model into a large reasoning model to improve instruction-following while preserving its thinking format.

- **Kind**: method
- **Also called**: model merging
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [HMMT 2025](../datasets/hmmt-2025.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](l1-length-controlled-reinforcement-learning.md), [overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [SuperGPQA](../datasets/supergpqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format](../../archive/papers/2026/title-6efe3d418b4ef980/summary.md) — A gradient-free model-merging method that integrates an instruction-tuned model into a large reasoning model to improve instruction following while preserving the reasoning model's thinking format and quality.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
