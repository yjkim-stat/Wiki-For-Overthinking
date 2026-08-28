# format collapse

<!-- auto:begin -->

Format collapse is the failure mode, in adaptive-reasoning-format training, where a model trained via standard GRPO to choose among multiple reasoning formats disproportionately favors whichever format earns the highest reward during training and stops exploring the others. ARM2 addresses it directly with a format-encouragement reward term (in GRPO-alp) that scales reward inversely by how often a format already appears within its response group, and ARM's Ada-GRPO is cited as a related format-adaptive training approach facing the same risk.

- **Kind**: concept
- **Also called**: Format Collapse
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning format selection](../methods/adaptive-reasoning-format-selection.md), [AIME 2025](../datasets/aime-2025.md), [AQuA-RAT](../datasets/aqua-rat.md), [BBH](../datasets/bbh.md), [ChartQA](../datasets/chartqa.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMMU](../datasets/mmmu.md), [OpenBookQA](../datasets/openbookqa.md), [Overthinking](overthinking.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Token Budget](token-budget.md)

## Appears in

- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
