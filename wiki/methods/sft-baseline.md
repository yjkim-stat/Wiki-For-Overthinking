# SFT (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [compression ratio](../concepts/compression-ratio.md), [DAPO (baseline)](dapo-baseline.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LC-R1 (baseline)](lc-r1-baseline.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-32B](../models/qwen3-32b.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1520/summary.md) — SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
