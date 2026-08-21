# StrategyQA

<!-- auto:begin -->

None of the four sources describe StrategyQA directly; it appears only as one of the evaluation benchmarks in their reasoning-efficiency experiments. ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task; ReBalance steers chain-of-thought length up or down at inference from token-confidence signals; DC-CoT isolates the effect of data augmentation, selection and mixing on CoT distillation; SuCo trains on a difficulty-adaptive 'Minimal Sufficient CoT' prefix via SFT plus a GRPO stage penalising both over- and under-thinking.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](../methods/activation-steering.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [BBH](bbh.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [CommonsenseQA](commonsenseqa.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [Manifold Steering](../methods/manifold-steering.md), [MATH](math.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU-STEM](mmlu-stem.md), [NoThinking](../methods/nothinking.md), [NOWAIT](../methods/nowait.md), [OlympiadBench](olympiadbench.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [s1K-1.1](s1k-1-1.md), [SEAL](../methods/seal.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [TrimR](../methods/trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
