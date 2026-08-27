# StrategyQA

<!-- auto:begin -->

None of the four sources describe StrategyQA directly; it appears only as one of the evaluation benchmarks in their reasoning-efficiency experiments. ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task; ReBalance steers chain-of-thought length up or down at inference from token-confidence signals; DC-CoT isolates the effect of data augmentation, selection and mixing on CoT distillation; SuCo trains on a difficulty-adaptive 'Minimal Sufficient CoT' prefix via SFT plus a GRPO stage penalising both over- and under-thinking.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [activation steering](../methods/activation-steering.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [BBH](bbh.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [CommonsenseQA](commonsenseqa.md), [DEER](../methods/deer.md), [Dynasor](../methods/dynasor.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LiveCodeBench](livecodebench.md), [LiveCodeBench-v6](livecodebench-v6.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Manifold Steering](../methods/manifold-steering.md), [MATH](math.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU-STEM](mmlu-stem.md), [NoThinking](../methods/nothinking.md), [NOWAIT](../methods/nowait.md), [OK-VQA](ok-vqa.md), [OlympiadBench](olympiadbench.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [s1K-1.1](s1k-1-1.md), [SEAL](../methods/seal.md), [self-consistency (majority voting)](../methods/self-consistency-majority-voting.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [TrimR](../methods/trimr.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [SoftCoT: Soft Chain-of-Thought for Efficient Reasoning with LLMs](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1137/summary.md) — SoftCoT keeps the backbone LLM frozen and instead uses a small auxiliary assistant model plus a trainable projection module to generate instance-specific continuous 'soft thought' tokens that prime the LLM's chain-of-thought, avoiding the catastrophic forgetting that full-model fine-tuning for continuous-space reasoning (e.g. Coconut) causes on modern instruction-tuned LLMs, and improving accuracy on five reasoning benchmarks with only ~6 soft tokens versus 24 hard tokens needed by a discrete-token assistant baseline.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
