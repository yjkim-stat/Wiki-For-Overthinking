# DPO (baseline)

<!-- auto:begin -->

DPO (as a baseline) is cited in these sources as a preference-tuning technique other length-control methods are compared against or build on: LC-R1 studies 'invalid thinking' (redundant post-answer double-checking) as a form of overthinking with GRPO-based rewards, and AdaMix trains separate short/long LoRA adapters, with DPO-based approaches named among the accuracy-efficiency baselines these methods are benchmarked against. The sources do not detail the DPO baseline's own configuration.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepScaleR-1.5B-Preview](../models/deepscaler-1-5b-preview.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA](lora.md), [MATH (training)](../datasets/math-training.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B](../models/qwen3-4b.md), [QwQ-32B](../models/qwq-32b.md), [TLMRE (baseline)](tlmre-baseline.md)

## Appears in

- [Optimizing Length Compression in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-146/summary.md) — Names 'invalid thinking' -- redundant double-checking after a reasoning model has already derived the correct answer -- as a specific, measurable form of overthinking (Valid Thinking rate as low as 57.5-65.3% on four SOTA LRMs), and introduces LC-R1, a GRPO method with a dual Length Reward (global conciseness) and Compress Reward (targeted removal of the redundant tail), achieving ~46-52% length reduction for only 1.8-2.1% accuracy loss and 97%+ Valid Thinking rate.
- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
