# KodCode

<!-- auto:begin -->

A code dataset used as one of the two code-generation sources in the reinforcement learning experiments both papers draw on, alongside Eurus-2-RL-Code. It is selected for the same reason as the mathematics data — its rewards are verifiable, here as a pass rate — which the sources say is what removes reward-model misspecification from the measurement. Neither source describes how the dataset was built or how large it is.

- **Kind**: dataset
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [MATH500](math500.md), [Minerva](minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [PPO](../methods/ppo.md), [PRIME](../methods/prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [REINFORCE](../methods/reinforce.md), [RLOO](../methods/rloo.md), [RLVR](../methods/rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
