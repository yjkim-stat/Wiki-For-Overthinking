# softmax policy

<!-- auto:begin -->

A policy that turns real-valued logits into a distribution over actions by exponentiating and normalizing. All four archived sources adopt it as the setting for their analysis, and for the same two reasons: the normalization couples every action's probability to every logit, which is what makes the optimization objective non-concave in the parameters, and it makes the entropy of the resulting distribution differentiable in closed form, which is what allows entropy change to be written as a covariance or an inner product. Where the four differ is in what produces the logits — an independent parameter per state-action pair in two of them, a linear map from fixed features in the other two — and that difference is the substance of several of their results rather than a detail of presentation.

- **Kind**: concept
- **Also called**: softmax parameterization
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [advantage function](advantage-function.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [importance sampling](../methods/importance-sampling.md), [KL-Cov](../methods/kl-cov.md), [KL divergence](../methods/kl-divergence.md), [KodCode](../datasets/kodcode.md), [linear function approximation](../methods/linear-function-approximation.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [log-linear policy](log-linear-policy.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [natural policy gradient](../methods/natural-policy-gradient.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [policy gradient](policy-gradient.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [tabular softmax parameterization](tabular-softmax-parameterization.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Rethinking the Global Convergence of Softmax Policy Gradient with Linear Function Approximation](../../archive/papers/2025/local-8458ce24c9e6b3b5/summary.md) — Shows by two four-armed bandits with nearly identical approximation error, one of which converges and one of which does not, that approximation error cannot characterize whether softmax policy gradient reaches the optimum, and replaces it with a condition on whether the features preserve the ordering of the rewards.
- [Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs](../../archive/papers/2026/local-e7b4993440250612/summary.md) — Proves that entropy-regularized policy gradient converges to the regularized optimum at an exponential rate for log-linear softmax policies over continuous state and action spaces, by using the KL regularizer as a Lyapunov function to keep the Fisher information matrix from degenerating.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
