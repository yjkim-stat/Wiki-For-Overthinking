# KL divergence

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [credit assignment](credit-assignment.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [linear function approximation](../methods/linear-function-approximation.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [log-linear policy](log-linear-policy.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [natural policy gradient](../methods/natural-policy-gradient.md), [outcome reward](outcome-reward.md), [policy gradient](../methods/policy-gradient.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [reward hacking](reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md)

## Appears in

- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
