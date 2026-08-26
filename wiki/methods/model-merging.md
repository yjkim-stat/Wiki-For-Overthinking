# Model Merging

<!-- auto:begin -->

Combining the parameters of two or more trained models into one, without further gradient-based training, to transfer a capability from one into the other. OptimalThinkingBench tests it as one of five overthinking mitigations, where -- like the other length-reduction methods -- it tends to trade OverthinkingBench gains against UnderthinkingBench accuracy; RAIN-Merging applies it gradient-free to merge an instruction-tuned model into a large reasoning model to improve instruction-following while preserving its thinking format.

- **Kind**: method
- **Also called**: model merging
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff of reasoning length](../concepts/accuracy-efficiency-tradeoff-of-reasoning-length.md), [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AdaptThink](adaptthink.md), [AIME 2025](../datasets/aime-2025.md), [AUC_OAA](../concepts/auc-oaa.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [difficulty-based routing between reasoning modes](../concepts/difficulty-based-routing-between-reasoning-modes.md), [F1^otb combined metric](../concepts/f1-otb-combined-metric.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [hybrid thinking/non-thinking models](../concepts/hybrid-thinking-non-thinking-models.md), [L1 length-controlled reinforcement learning](l1-length-controlled-reinforcement-learning.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Overthinking-Adjusted Accuracy (OAA)](../concepts/overthinking-adjusted-accuracy-oaa.md), [OverthinkingBench](../datasets/overthinkingbench.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [thinking-token budget](../concepts/thinking-token-budget.md), [trained difficulty-based router / oracle router](../concepts/trained-difficulty-based-router-oracle-router.md), [underthinking](../concepts/underthinking.md), [UnderthinkingBench](../datasets/underthinkingbench.md), [VeriThinker](verithinker.md)

## Appears in

- [OptimalThinkingBench: Evaluating Over and Underthinking in LLMs](../../archive/papers/2025/local-49199e3b0f694ee1/summary.md) — Introduces OptimalThinkingBench, a unified benchmark pairing OverthinkingBench (simple queries) and UnderthinkingBench (hard reasoning/math) with a shared F1 metric, showing that none of 33 evaluated LLMs balances accuracy and thinking-token efficiency.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
