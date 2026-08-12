# performance ceiling

<!-- auto:begin -->

The upper limit a training method can reach regardless of how long it is run, which both sources treat as a property to be raised rather than approached. One reports that aligning meta-abilities first raises the ceiling that subsequent domain-specific RL can reach, so the alignment stage changes what later training can achieve rather than substituting for it. The other locates the ceiling in policy entropy, giving a mechanism: as entropy collapses the policy stops exploring and performance saturates, which makes the ceiling a consequence of the optimization dynamics rather than of model capacity.

- **Kind**: concept
- **Also called**: ceiling, saturation point, upper bound
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [aha moment](aha-moment.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](covariance-of-probability-and-advantage.md), [emergent behaviour](emergent-behaviour.md), [entropy bonus](entropy-bonus.md), [entropy collapse](entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [KodCode](../datasets/kodcode.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [model merging](../methods/model-merging.md), [OlympiadBench](../datasets/olympiadbench.md), [OMNI-MATH](../datasets/omni-math.md), [policy entropy](policy-entropy.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE++](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](scaling-laws.md), [self-verification](self-verification.md), [softmax policy](softmax-policy.md), [token-level entropy](token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [Beyond &apos;Aha!&apos;: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1981/summary.md) — Replaces reliance on unpredictable emergent 'aha moments' by explicitly aligning models to deduction, induction and abduction on self-verifiable tasks before domain RL.
- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
