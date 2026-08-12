# linear function approximation

<!-- auto:begin -->

Representing the policy through a fixed set of basis functions combined by a weight vector, instead of giving every state-action pair its own parameter. Both sources adopt it as the first step past the tabular setting that keeps a convergence analysis tractable, and both report that the step is not free — in each case the guarantee comes to depend on a property of the basis rather than on how well it approximates anything. One shows the conventional measure, approximation error, cannot characterize convergence at all, exhibiting two instances with the same error and opposite outcomes, and replaces it with a condition on whether the features preserve the ordering of rewards. The other finds convergence hinges on the smallest eigenvalue of a Fisher information or uncentered feature covariance matrix staying away from zero, and gives a standard one-dimensional finite-element basis for which its condition fails. Neither reaches non-linear approximation.

- **Kind**: method
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [importance sampling](importance-sampling.md), [log-linear policy](../concepts/log-linear-policy.md), [natural policy gradient](natural-policy-gradient.md), [policy gradient](policy-gradient.md), [PPO](ppo.md), [REINFORCE++](reinforce.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md)

## Appears in

- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
