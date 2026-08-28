# MATH (training)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](../methods/dpo-baseline.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [LLaMA 3.2 3B Instruct](../models/llama-3-2-3b-instruct.md), [MATH500](math500.md), [O1-Pruner (baseline)](../methods/o1-pruner-baseline.md), [OlympiadBench](olympiadbench.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [QwQ-32B](../models/qwq-32b.md)

## Appears in

- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [Reinforced Efficient Reasoning via Semantically Diverse Exploration](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2216/summary.md) — ROSE improves MCTS-based RLVR by branching reasoning rollouts at semantic-entropy positions (generation entropy weighted by embedding-space token dispersion, not raw token-probability entropy, which conflates functionally-equivalent tokens like 'can'/'need' as diverse) plus an epsilon-exploration mechanism, combined with a length-aware segment-level advantage estimator that penalizes unnecessarily long correct branches, outperforming GRPO variants and MCTS baselines (TreePO, FR3E) on AIME/MATH500/AMC23 while producing measurably shorter, less overthought reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
