# AMC

<!-- auto:begin -->

A competition mathematics benchmark, used by both sources purely as an evaluation set reported alongside AIME and MATH500. Neither describes its contents, size or construction, so nothing about the benchmark itself can be stated from the archived material. Note that the archive separately holds AMC23; the sources here name the benchmark without a year, and whether they mean the same collection is not established.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](aime24.md), [AIME25](aime25.md), [answer stabilization](../concepts/answer-stabilization.md), [beam search](../methods/beam-search.md), [best-of-n](../methods/best-of-n.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [greedy decoding](../methods/greedy-decoding.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [KodCode](kodcode.md), [majority voting](../methods/majority-voting.md), [MATH500](math500.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PRIME](../methods/prime.md), [Qwen2.5-1.5B](../models/qwen2-5-1-5b.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [RLOO](../methods/rloo.md), [self-consistency](../methods/self-consistency.md), [self-correction](../concepts/self-correction.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md)

## Appears in

- [Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning](../../archive/papers/2026/arxiv-2608-05643/summary.md) — Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
