# advantage function

<!-- auto:begin -->

How much better an action is than the policy's average at that state, and in both sources the quantity that scales the update applied to a token's logit. They obtain it in different ways: one takes it from the policy gradient theorem as the state-action value minus the state value, with the property that its expectation under the policy is zero, while the other never estimates a value function at all and instead standardizes the rewards within a group of sampled responses. What the two share is its role rather than its construction — the sign of the advantage sets the direction of the logit update, and that direction combined with the token's probability is what decides whether the update raises or lowers entropy.

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [pass-k](../methods/pass-k.md), [policy entropy](policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [RLOO](../methods/rloo.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md)

## Appears in

- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
