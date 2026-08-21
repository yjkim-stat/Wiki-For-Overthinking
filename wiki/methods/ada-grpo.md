# Ada-GRPO

<!-- auto:begin -->

Ada-GRPO is the reinforcement-learning objective introduced with ARM: a GRPO variant whose advantage is computed so that the model learns to choose among several reasoning formats per task rather than always using the longest one. In ARM the four formats are Direct Answer, Short CoT, Code and Long CoT, and training with Ada-GRPO cuts average tokens by about 30% at roughly unchanged accuracy. The archive's second source, Mixture-of-Visual-Thoughts, uses the same construction under a different name -- a mode-relative advantage that makes a vision-language model select between text-based and visually-grounded reasoning per input, raising average accuracy over eight benchmarks by about 5 points -- so the sources agree on the mechanism (advantage normalised within a reasoning mode) while differing on what the mode selection is for: token saving in one, accuracy in the other.

- **Kind**: method
- **Also called**: AdaGRPO, Adaptive GRPO, mode-relative advantage
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2025](../datasets/aime-2025.md), [BIG-Bench Hard](../datasets/big-bench-hard.md), [CommonsenseQA](../datasets/commonsenseqa.md), [GPQA](../datasets/gpqa.md), [Group-Relative Policy Optimization](group-relative-policy-optimization.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MMStar](../datasets/mmstar.md), [overthinking](../concepts/overthinking.md), [POPE](../datasets/pope.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Token Budget](../concepts/token-budget.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
