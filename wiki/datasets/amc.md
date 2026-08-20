# AMC

<!-- auto:begin -->

The American Mathematics Competitions set, referred to generically across 3 sources as the mid-difficulty rung between grade-school and invitational problems. Its use in these sources is as one column in test-time-scaling and entropy-control suites; the specific 2023 edition, which the archive treats separately, carries the measured results. Its size means single-item movements, and the archive's related caution about small competition sets applies.

- **Kind**: dataset
- **Also called**: AMC
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [advantage function](../concepts/advantage-function.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC23](amc23.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [credit assignment](../concepts/credit-assignment.md), [diminishing returns](../concepts/diminishing-returns.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [greedy decoding](../methods/greedy-decoding.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [IFEval](ifeval.md), [KL-Cov](../methods/kl-cov.md), [KL divergence](../methods/kl-divergence.md), [KodCode](kodcode.md), [LiveCodeBench](livecodebench.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [majority voting](../methods/majority-voting.md), [MATH](math.md), [MATH500](math500.md), [MMLU-Pro](mmlu-pro.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [outcome reward](../concepts/outcome-reward.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PRIME](../methods/prime.md), [process reward model](../concepts/process-reward-model.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [reward hacking](../concepts/reward-hacking.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR](../../archive/papers/2026/arxiv-2608-03119/summary.md) — Diagnoses label-free RLVR's collapse as a shortcut in which the same answer-level consensus signal both estimates the reward and receives the gradient, and fixes it by masking the answer span from updates entirely — so a reward can only be raised by improving the reasoning that produces the answer.
- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
