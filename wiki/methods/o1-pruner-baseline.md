# O1-Pruner (baseline)

<!-- auto:begin -->

O1-Pruner (baseline) is a PPO-like offline fine-tuning method for compressing chain-of-thought length, used in this archive as a comparison baseline by LC-R1 (which achieves a more favorable efficacy-efficiency trade-off, e.g. 46-52% length reduction vs. O1-Pruner's ~34-36% at greater accuracy cost) and by Ada-R1's hybrid-CoT merging method.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Model Merging](model-merging.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-32B](../models/qwen3-32b.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
