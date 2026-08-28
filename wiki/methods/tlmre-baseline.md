# TLMRE (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepScaleR-preview (training)](../datasets/deepscaler-preview-training.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-4B](../models/qwen3-4b.md)

## Appears in

- [AttnPO: Attention-Guided Process Supervision for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1845/summary.md) — Discovers Key-Focus Heads (KFHs) -- a small subset of attention heads that, during final-answer generation, naturally attend more to essential reasoning steps than redundant ones -- and builds ATTNPO, an RL framework that rescales GRPO's outcome-level advantage per reasoning step using KFH attention scores, cutting reasoning length 55-61% while improving accuracy +2.9 to +7.3 points on DeepSeek-R1-Distill-Qwen-1.5B/7B.
- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
