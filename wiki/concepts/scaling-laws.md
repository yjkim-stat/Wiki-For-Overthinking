# scaling laws

<!-- auto:begin -->

Predictable relationships between resources spent and performance obtained, which the archived sources invoke mostly to mark where the familiar ones stop applying. One derives a law inside RL training rather than pretraining: reward trades against policy entropy as R = -a*exp(H) + b, fitted across model families and predictive enough that coefficients from the first 36 steps extrapolate 200 steps ahead at under 1% RMSE, with the ceiling at zero entropy. The other observes that length generalization is often wholly independent of conventional scaling laws — models from 50M to 3B failed to extend 15-digit addition to 20 digits, and data past a threshold did not help. Both are cautions against reading a compute-loss curve as a capability curve.

- **Kind**: concept
- **Also called**: compute-performance scaling, scaling law
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [expressivity](expressivity.md), [finite precision](finite-precision.md), [generalization](generalization.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [length generalization](length-generalization.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [performance ceiling](performance-ceiling.md), [policy entropy](policy-entropy.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [softmax policy](softmax-policy.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
