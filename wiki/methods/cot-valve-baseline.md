# CoT-Valve (baseline)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Ada-R1](ada-r1.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [MMLU](../datasets/mmlu.md), [Model Merging](model-merging.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Olympiad](../datasets/olympiad.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-4B](../models/qwen3-4b.md), [TLMRE (baseline)](tlmre-baseline.md), [TokenSkip (baseline)](tokenskip-baseline.md)

## Appears in

- [Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1766/summary.md) — TH2T (Think-How-to-Think) is a two-stage fine-tuning method that first injects an explicit 'difficulty hypnosis' cue into a model's output prefix (prospective, global strategy selection) and then a 'redundancy hypnosis' cue into in-progress reasoning to truncate reflection loops (retrospective, local correction), cutting inference cost over 70% on easy tasks and 40% on hard tasks with minimal accuracy loss and no external difficulty labels at inference time.
- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.
- [Ada-R1: Hybrid-CoT via Bi-Level Adaptive Reasoning Optimization](../../archive/papers/2025/title-a6dab00057eab5aa/summary.md) — Ada-R1 merges a long-CoT and a short-CoT model into one hybrid, then applies two levels of preference training so the model first picks a reasoning style per problem and then prefers the shorter correct trace within that style, cutting average reasoning length by about 51% on five maths datasets.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
