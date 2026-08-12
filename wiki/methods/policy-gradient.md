# policy gradient

<!-- auto:begin -->

The gradient of expected return with respect to the parameters of a policy, and in all three sources an object of analysis rather than a tool. They converge on one difficulty: under a softmax parameterization the normalization makes the objective non-concave in the parameters, so convergence cannot be argued from convexity and has to be recovered from a gradient-dominance property instead. What they establish diverges with the setting. In stochastic bandits with unregularized reward the question is which feature representations admit convergence at all; in entropy-regularized Markov decision processes on continuous spaces it is the rate at which an idealized gradient flow converges and what keeps its constant from degenerating; in language-model fine-tuning it is which direction a single update moves the policy's entropy. Only the first two treat convergence; the third works one step at a time.

- **Kind**: method
- **Also called**: PG, softmax policy gradient
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [Clip-Cov](clip-cov.md), [clip-higher](clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [importance sampling](importance-sampling.md), [KL-Cov](kl-cov.md), [KodCode](../datasets/kodcode.md), [linear function approximation](linear-function-approximation.md), [log-linear policy](../concepts/log-linear-policy.md), [MATH500](../datasets/math500.md), [natural policy gradient](natural-policy-gradient.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [policy entropy](../concepts/policy-entropy.md), [PPO](ppo.md), [PRIME](prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE++](reinforce.md), [RLOO](rloo.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md)

## Appears in

- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
