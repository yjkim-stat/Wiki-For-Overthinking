# ModelMerging (baseline)

<!-- auto:begin -->

Model merging (combining separately-trained models' parameters, e.g. via task arithmetic) is used in these sources as a reasoning-efficiency baseline: AdaMix compares its LoRA-adapter-interpolation approach against a model-merging baseline (among ShorterBetter/TLMRE/CoT-Valve/SwitchCoT) on an accuracy-efficiency score, and ERRV reports its reasoning-vector approach transfers across base, distilled, and merged models, implying model merging is one of the model-preparation regimes its method is validated against.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LiveCodeBench-v6](../datasets/livecodebench-v6.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen3-4B](../models/qwen3-4b.md), [ShorterBetter (baseline)](shorterbetter-baseline.md), [TLMRE (baseline)](tlmre-baseline.md)

## Appears in

- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.
- [ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1425/summary.md) — ERRV defines a 'reasoning vector' -- the mean hidden-state difference between a question's shortest-correct and longest-incorrect sampled responses -- and instead of injecting it at inference (which limits autonomy and gives modest gains), steers RL rollouts with it during training via importance-sampling-corrected GRPO, letting the model internalize efficient reasoning so it needs no vector guidance at inference: ~30% length reduction with stable accuracy, and the vectors are shown to be stable across RL training (cosine similarity 0.83-0.83 pre/post-training) and to transfer across base, distilled, merged, and adaptive-reasoning models.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
