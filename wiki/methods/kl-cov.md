# KL-Cov

<!-- auto:begin -->

The KL-penalty counterpart to Clip-Cov: apply a KL penalty to the tokens with the largest covariance between log-probability and advantage, rather than clipping them. Its originating source reports stabler entropy curves than Clip-Cov, preferable when precise entropy control matters, and sustains entropy over 10x higher than baseline at the point where the baseline plateaus. Two later sources include it as a strong baseline and beat it by 1.7-1.8 points, so it remains near the front without being the best method in the archive.

- **Kind**: method
- **Also called**: KL_Cov
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [calibration](calibration.md), [Clip-Cov](clip-cov.md), [clip-higher](clip-higher.md), [covariance of probability and advantage](../concepts/covariance-of-probability-and-advantage.md), [DAPO](dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [KodCode](../datasets/kodcode.md), [LiveCodeBench](../datasets/livecodebench.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [Mistral-7B](../models/mistral-7b.md), [OlympiadBench](../datasets/olympiadbench.md), [OMNI-MATH](../datasets/omni-math.md), [pass-k](pass-k.md), [performance ceiling](../concepts/performance-ceiling.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](policy-gradient.md), [PPO](ppo.md), [PRIME](prime.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [Qwen2.5-7B](../models/qwen2-5-7b.md), [Qwen2.5-Math-7B](../models/qwen2-5-math-7b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [REINFORCE++](reinforce.md), [RLOO](rloo.md), [RLVR](rlvr.md), [scaling laws](../concepts/scaling-laws.md), [softmax policy](../concepts/softmax-policy.md), [tabular softmax parameterization](../concepts/tabular-softmax-parameterization.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](verl.md)

## Appears in

- [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](../../archive/papers/2025/local-5175928072823010/summary.md) — Establishes that RL trades policy entropy for reward along a predictable exponential curve R = -a·exp(H) + b, derives that entropy change is driven by the covariance between action probability and advantage, and controls it by restricting updates to the highest-covariance tokens.
- [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](../../archive/papers/2026/local-8efebbee3585a141/summary.md) — Recasts entropy collapse as an imbalance of 'entropy flow' — tokens whose update lowers entropy persistently outweigh those that raise it — and rebalances the two sets with a closed-form coefficient computed from each batch, without reference policies or entropy bonuses.
- [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](../../archive/papers/2026/local-c70c8f6b2ab7db16/summary.md) — A systematic empirical study of entropy in RLVR that finds entropy correlates with response diversity but only weakly and inconsistently with accuracy, identifies clipping thresholds, off-policy updates and data diversity as its drivers, and argues positive-advantage tokens are what collapses it.
- [A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning for Reasoning Language Models](../../archive/papers/2026/local-ed740509686ff305/summary.md) — Proves that an entropy bonus permanently moves the stationary point of RL training while covariance-targeted control reaches the unregularized optimum once its coefficient is annealed, and that the bonus shrinks the stability margin where the targeted methods leave it intact.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
