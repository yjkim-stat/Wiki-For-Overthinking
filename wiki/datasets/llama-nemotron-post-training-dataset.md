# Llama-Nemotron-Post-Training-Dataset

<!-- auto:begin -->

The Llama-Nemotron-Post-Training-Dataset is a long-CoT reasoning-distillation training dataset used in Distilling the Essence (section-wise supervision ablation for reasoning distillation) and SuCo (Sufficiency-guided Continuous Adaptive Reasoning, which trains on the Minimal Sufficient CoT prefix -- the shortest reasoning prefix at which confidence in the ground-truth answer crosses a difficulty-adaptive threshold).

- **Kind**: dataset
- **Also called**: Llama-Nemotron Post-Training Dataset, Llama-Nemotron-Post-Training-Dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [Bespoke-Stratos-17k](bespoke-stratos-17k.md), [CommonsenseQA](commonsenseqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench-v6](livecodebench-v6.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU STEM](mmlu-stem.md), [OpenCodeReasoning](opencodereasoning.md), [OpenR1-Math-220k](openr1-math-220k.md), [OpenThoughts-114k](openthoughts-114k.md), [Overthinking](../concepts/overthinking.md), [s1k-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-587/summary.md) — Systematically ablates which section (prompt, CoT, answer) of a reasoning-distillation training sequence carries the useful supervisory signal and how much of the CoT is needed, finding CoT-inclusive supervision is essential while training on only the first 50% of tokens retains ~91% of full-sequence accuracy at roughly half the training time, memory, and FLOPs.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
