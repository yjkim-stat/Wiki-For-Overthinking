# log-linear policy

<!-- auto:begin -->

A policy whose log-density is linear in the parameters: an action's probability is proportional to the exponential of an inner product between the parameter vector and that action's feature vector, normalized over the action set. Both sources use it as the tractable class that contains the tabular softmax as the special case where the features are one-hot, and both work in the regime where there are fewer parameters than actions, so that not every policy is representable. One of them draws out the consequence that matters for proofs: because each weight moves the entire conditional log-density, the per-action decompositions the tabular arguments rely on are no longer available, and a different technique is needed.

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [importance sampling](../methods/importance-sampling.md), [KL divergence](../methods/kl-divergence.md), [linear function approximation](../methods/linear-function-approximation.md), [natural policy gradient](../methods/natural-policy-gradient.md), [policy gradient](policy-gradient.md), [PPO](../methods/ppo.md), [REINFORCE](../methods/reinforce.md), [softmax policy](softmax-policy.md), [tabular softmax parameterization](tabular-softmax-parameterization.md)

## Appears in

- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
