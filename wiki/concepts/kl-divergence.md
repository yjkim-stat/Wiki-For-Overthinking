# KL divergence

<!-- auto:begin -->

A measure of how far one distribution sits from another, and in these two sources a constraint and a proof device respectively. One uses it as the penalty anchoring a policy to its reference during reinforcement learning, and — more usefully — decomposes it by token position as a diagnostic: under a voting-based label-free objective, divergence on answer tokens rises sharply while divergence on reasoning tokens barely moves, which localizes a collapse that a trajectory-wide scalar would register only as a symptom. The other makes the entropy regularizer, which is a divergence from the uniform policy, do the work of a Lyapunov function: it keeps the Fisher information matrix from degenerating and thereby yields exponential convergence for a non-convex problem over continuous state and action spaces. The transferable idea from the pair is that this quantity is more informative when it is resolved — by position in one case, as a potential function in the other — than when reported as a single number.

- **Kind**: concept
- **Also called**: KL, Kullback-Leibler divergence
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [credit assignment](credit-assignment.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [IFEval](../datasets/ifeval.md), [KL regularization](../methods/kl-regularization.md), [linear function approximation](../methods/linear-function-approximation.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [log-linear policy](log-linear-policy.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [natural policy gradient](../methods/natural-policy-gradient.md), [outcome reward](outcome-reward.md), [policy gradient](../methods/policy-gradient.md), [process reward model](../methods/process-reward-model.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [reward hacking](reward-hacking.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md)

## Appears in

- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
