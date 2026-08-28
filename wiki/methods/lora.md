# LoRA

<!-- auto:begin -->

LoRA (Low-Rank Adaptation) is used in these sources as the parameter-efficient fine-tuning mechanism behind adaptive-length reasoning adapters: AdaMix trains two separate LoRA adapters (a short adapter and a long adapter) and interpolates between them via task arithmetic, guided by a difficulty-aware router, to trade off reasoning length and accuracy.

- **Kind**: method
- **Also called**: Low-Rank Adaptation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [COCONUT](coconut.md), [CODI](codi.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [Latent reasoning](../concepts/latent-reasoning.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [Qwen3-4B](../models/qwen3-4b.md), [Recurrent Depth](../concepts/recurrent-depth.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [TLMRE (baseline)](tlmre-baseline.md)

## Appears in

- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](../../archive/papers/2026/arxiv-2607-25915/summary.md) — Penelope confines latent reasoning recurrence to a five-layer slice of a decoder-only Transformer, refining a fixed-size boundary memory K times instead of re-running the whole decoder or emitting a chain-of-thought trace.
- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
