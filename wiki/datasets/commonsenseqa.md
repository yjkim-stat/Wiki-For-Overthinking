# CommonsenseQA

<!-- auto:begin -->

A multiple-choice commonsense question-answering set, used across the archive as the easy, non-mathematical end of the benchmark suite - the place where adaptive-length methods show their largest token savings and where math-trained models are checked for out-of-domain transfer. ARM uses it both as RL training data (with GSM8K and MATH, 19.8K items combined) and as the benchmark where format selection saves about 73% of tokens, against a +7.9% accuracy gain on AIME'25 - the pair the paper reads as evidence the model is judging difficulty roughly correctly. SuCo uses it as one of three out-of-domain checks for a math-trained model, scoring 49.3 against R1-Distill's 45.0, while WS-GRPO finds commonsense sets degrade less than mathematical ones under trajectory-level preference training and that behaviour on this set varies across Qwen variants; DC-CoT includes it among the reasoning domains over which it isolates distillation data effects. No source treats it as a target in its own right.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [BBH](bbh.md), [Chain-of-Thought Distillation](../methods/chain-of-thought-distillation.md), [Dr. GRPO](../methods/dr-grpo.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [Length Penalty](../concepts/length-penalty.md), [LiveCodeBench v6](livecodebench-v6.md), [MATH](math.md), [MATH500](math500.md), [MBPP](mbpp.md), [MMLU-STEM](mmlu-stem.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [Overthinking](../concepts/overthinking.md), [s1K-1.1](s1k-1-1.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](svamp.md), [Test-Time Compute Scaling](../concepts/test-time-compute-scaling.md), [Token Budget](../concepts/token-budget.md), [underthinking](../concepts/underthinking.md)

## Appears in

- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [SuCo: Sufficiency-guided Continuous Adaptive Reasoning](../../archive/papers/2026/title-b37859867120f044/summary.md) — Defines the Minimal Sufficient CoT — the shortest reasoning prefix at which the model's confidence in the ground-truth answer crosses a difficulty-adaptive threshold — and trains on it via supervised fine-tuning plus a GRPO stage whose reward penalises both over- and under-thinking, so reasoning length is calibrated continuously rather than by discrete modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
