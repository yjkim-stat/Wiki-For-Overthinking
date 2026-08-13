# tabular softmax parameterization

<!-- auto:begin -->

The special case of a softmax policy in which every state-action pair carries its own free parameter, so nothing is shared between states and there is no function approximation. All three sources name it as the setting existing convergence theory is confined to. Two treat escaping it as the problem and report what breaks on the way out: once parameters are shared, the per-action decompositions the tabular proofs depend on are unavailable, and one of the substitute devices — radial unboundedness of the KL term — cannot arise in the tabular case at all, so that result is described as complementing the tabular theory rather than extending it. The third instead adopts the assumption deliberately, to analyse language-model training, which is the reading a user of these results should weigh: a transformer shares parameters across states by construction, so an analysis that assumes independent per-state parameters has removed the thing it is being applied to.

- **Kind**: concept
- **Also called**: tabular setting, tabular softmax
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage function](advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [importance sampling](../methods/importance-sampling.md), [KL-Cov](../methods/kl-cov.md), [KL divergence](kl-divergence.md), [KodCode](../datasets/kodcode.md), [linear function approximation](../methods/linear-function-approximation.md), [log-linear policy](log-linear-policy.md), [MATH500](../datasets/math500.md), [natural policy gradient](../methods/natural-policy-gradient.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [policy entropy](policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [softmax policy](softmax-policy.md)

## Appears in

- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
