# UnderthinkingBench

<!-- auto:begin -->

The underthinking half of OptimalThinkingBench: 11 Reasoning Gym task types plus AIME'25/HMMT'25 math, keeping only tasks where a small thinking model (Qwen3-1.7B) outperforms a much larger non-thinking model (Qwen3-235B-A22B) by a margin, so the tasks genuinely require deliberate reasoning. Scored with programmatic verifiers and combined with OverthinkingBench into the F1^otb metric.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [AdaptThink](../methods/adaptthink.md), [AIME 2025](aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [HMMT 2025](hmmt-2025.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](../methods/l1-length-controlled-reinforcement-learning.md), [Model Merging](../methods/model-merging.md), [overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](overthinkingbench.md), [SuperGPQA](supergpqa.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [VeriThinker](../methods/verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2026/title-441c8494292f11c7/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
