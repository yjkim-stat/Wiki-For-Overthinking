# covariance of probability and advantage

<!-- auto:begin -->

The covariance, taken over the actions available at one decoding position, between the log-probability of an action and its probability-weighted advantage — the quantity both sources identify as governing how a policy-gradient step changes entropy. One derives it and reports that it tracks the measured entropy difference closely and never turns negative during training, which is its explanation for why entropy falls monotonically; the other re-derives the same identity inside a unified framework and uses it to argue that regularizing only the tokens where it is largest is asymptotically unbiased while a global entropy bonus is not. Both derivations assume a tabular softmax policy and are first-order in the update, so the identity describes the direction of a single step rather than a trajectory. A third archived source objects that the quantity depends on the advantage of tokens that were never sampled, which most reinforcement fine-tuning algorithms cannot estimate.

- **Kind**: concept
- **Also called**: covariance term
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage function](advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
