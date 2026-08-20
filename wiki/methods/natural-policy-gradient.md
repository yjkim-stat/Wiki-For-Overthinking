# natural policy gradient

<!-- auto:begin -->

The policy gradient preconditioned by the inverse of the Fisher information matrix; for log-linear policies both sources note it produces the same updates as mirror descent. Neither studies it directly — in both it is the comparison that locates what is hard about plain policy gradient. One observes that it keeps log densities bounded along the optimization automatically, so the Fisher matrix stays invertible for almost any feature basis, which is precisely the property its own analysis of vanilla policy gradient has to establish by other means. The other observes that its regression-based updates connect more directly to the notion of approximation error than the softmax policy gradient update does, which is part of why approximation error is the wrong metric for the latter.

- **Kind**: method
- **Also called**: NPG
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [importance sampling](importance-sampling.md), [KL divergence](kl-divergence.md), [linear function approximation](linear-function-approximation.md), [log-linear policy](../concepts/log-linear-policy.md), [policy gradient](../concepts/policy-gradient.md), [PPO](ppo.md), [REINFORCE](reinforce.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md)

## Appears in

- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
