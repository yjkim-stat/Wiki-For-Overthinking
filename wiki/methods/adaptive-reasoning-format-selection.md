# adaptive reasoning format selection

<!-- auto:begin -->

Adaptive reasoning-format selection is a family of methods that train a model to choose, per task, among qualitatively different reasoning formats (e.g. Direct Answer, Short CoT, Code, Long CoT) rather than only adapting the length within one format. ARM trains this choice via Ada-GRPO across four formats, cutting average tokens ~30% at roughly unchanged accuracy; ARM2 extends the same idea to multimodal (vision) inputs and adds Code-Exec (executed, not just written, code) as a fifth format, via a format-collapse-resistant GRPO-alp variant, cutting token usage over 70% versus standard GRPO with matched accuracy.

- **Kind**: method
- **Also called**: Adaptive Reasoning Format Selection
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](ada-grpo.md), [AIME 2025](../datasets/aime-2025.md), [AQuA-RAT](../datasets/aqua-rat.md), [BBH](../datasets/bbh.md), [ChartQA](../datasets/chartqa.md), [CommonsenseQA](../datasets/commonsenseqa.md), [format collapse](../concepts/format-collapse.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](grpo.md), [GRPO (baseline)](grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [MMMU](../datasets/mmmu.md), [OpenBookQA](../datasets/openbookqa.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
