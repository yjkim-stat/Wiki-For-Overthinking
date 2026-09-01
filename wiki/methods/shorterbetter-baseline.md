# ShorterBetter (baseline)

<!-- auto:begin -->

ShorterBetter is an efficient-reasoning baseline method referenced in AdaMix (decoupling efficiency and accuracy into separately-trained short/long LoRA adapters routed by difficulty) and Step Pruner (which replaces token-count length penalties with a step-count reward), both comparing their approach against ShorterBetter as a prior length-reduction method.

- **Kind**: method
- **Also called**: ShorterBetter
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CoT-Valve (baseline)](cot-valve-baseline.md), [DeepSeek-R1-Distill-Llama-8B](../models/deepseek-r1-distill-llama-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [DPO (baseline)](dpo-baseline.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [LoRA](lora.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [ModelMerging (baseline)](modelmerging-baseline.md), [O1-Pruner (baseline)](o1-pruner-baseline.md), [Qwen3-4B](../models/qwen3-4b.md), [TLMRE (baseline)](tlmre-baseline.md)

## Appears in

- [AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1864/summary.md) — AdaMix decouples efficiency and accuracy into two separately-trained LoRA adapters (a short adapter and a long adapter), then uses a BERT-based difficulty-aware router to predict a per-problem complexity coefficient that linearly interpolates the two adapters via task arithmetic, cutting DeepSeek-R1-Distill-Qwen-7B's average response length 54.9% while improving accuracy up to 4.8% across five math benchmarks and outperforming ShorterBetter/TLMRE/CoT-Valve/model-merging/SwitchCoT baselines on an accuracy-efficiency score.
- [Beyond Token Length: Step Pruner for Efficient and Accurate Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-94/summary.md) — Step Pruner (SP) is an RL framework that replaces token-count length penalties with a step-count reward (paragraph-based segmentation as a proxy for reasoning steps), penalizing steps beyond the minimal number needed for a correct answer while masking rewards for incorrect responses, achieving state-of-the-art accuracy-efficiency trade-off and 44-70% token reduction across four benchmarks without the reward-hacking (degenerate step-merging) that token-based RL penalties are prone to.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
