# DAPO (baseline)

<!-- auto:begin -->

DAPO is cited here as an RL training baseline for large reasoning models that other methods compare against: MINER contrasts its own intrinsic-reward recovery mechanism against DAPO-style GRPO training under 'positive homogeneous' prompts, and DisCO reports average accuracy gains over DAPO (6%) alongside its gains over GRPO (7%) on six math-reasoning benchmarks with a 1.5B model.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink (baseline)](adaptthink-baseline.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [compression ratio](../concepts/compression-ratio.md), [DeepScaler (training)](deepscaler-training.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GRPO (baseline)](grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [LC-R1 (baseline)](lc-r1-baseline.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MedQA](../datasets/medqa.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [SFT (baseline)](sft-baseline.md)

## Appears in

- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.
- [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1520/summary.md) — SIGMA reframes token-efficient RL as a classical exploration-exploitation problem: a self-imitation exploitation module prioritizes training on prompts/rollouts with high compression potential via a dynamic priority table and a compression-ratio-weighted self-imitation loss, while a self-guidance exploration module directs otherwise-undirected long-response exploration via prompt-based token-budget regeneration or random truncation -- improving average accuracy by 7.9%/2.9% while cutting average reasoning length 43.4%/40.3% on 1.5B/7B DeepSeek-R1-Distill models across six benchmarks, beating eight RL-based efficient-reasoning baselines.
- [DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization](../../archive/papers/2025/title-ec9090a2d1f7fb05/summary.md) — DisCO replaces GRPO's group-relative advantage objective with a discriminative-learning objective (raising positive-answer scores, lowering negative-answer scores) using non-clipping surrogates and constrained KL optimization, eliminating GRPO's question-level difficulty bias and entropy instability, and beating GRPO/DAPO by 6-7% on math reasoning benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
