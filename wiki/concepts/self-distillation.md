# Self-Distillation

<!-- auto:begin -->

Self-distillation here means using a model's own outputs, produced under some favorable condition, as training data for itself under the ordinary condition. ConPress harvests the shorter reasoning traces a model naturally produces when several questions share one prompt, and fine-tunes on them for the single-question setting; D-CORE instead self-distills before a diversity-aware RL stage, to correct 'Lazy Reasoning' (inadequate task decomposition) in complex tool-use settings.

- **Kind**: concept
- **Also called**: Self-Distillation, self-distillation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](accuracy-efficiency-tradeoff.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MMLU STEM](../datasets/mmlu-stem.md), [OlympiadBench](../datasets/olympiadbench.md), [Overthinking](overthinking.md), [Task Decomposition](task-decomposition.md)

## Appears in

- [ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure](../../archive/papers/2026/title-11f96b3e58a44cf5/summary.md) — ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.
- [D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use](../../archive/papers/2026/title-6c0fc879a2cc7d5b/summary.md) — Trains large reasoning models with self-distillation followed by diversity-aware RL to overcome 'Lazy Reasoning' -- inadequate task decomposition -- in complex tool-use settings.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
