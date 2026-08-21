# MMLU-STEM

<!-- auto:begin -->

The science-and-mathematics subset of MMLU, which appears in the archive only as one component of averaged evaluation suites, never on its own. SuCo averages it with GSM8K, MATH-500, AMC23, AIME25, MBPP, LiveCodeBench-v6 and GPQA-Diamond to report 53.1% accuracy at 1,483 mean response tokens for a 1.5B model, against DeepSeek-R1-Distill-Qwen at 45.2% / 5,736 tokens and LHRMs at 50.5% / 2,055 tokens; ConPress lists it among its evaluation sets. Neither source reports a per-benchmark MMLU-STEM accuracy or length figure, so the archive states no accuracy/length tradeoff for this set specifically — only that it is part of a mix on which one method cut tokens roughly fourfold while raising accuracy.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [CommonsenseQA](commonsenseqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench-v6](livecodebench-v6.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MMLU-Pro](mmlu-pro.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [s1K-1.1](s1k-1-1.md), [Self-Distillation](../concepts/self-distillation.md), [StrategyQA](strategyqa.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure](../../archive/papers/2026/title-11f96b3e58a44cf5/summary.md) — ConPress observes that a reasoning model shortens its traces when several independent questions share one prompt, and harvests those shortened traces as self-supervised fine-tuning data for the single-question setting.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
