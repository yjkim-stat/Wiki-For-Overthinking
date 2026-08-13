# policy gradient masking

<!-- auto:begin -->

Restricting a policy-gradient update to a chosen subset of tokens by zeroing the loss on the rest and renormalizing by the number of tokens kept. Both sources use it as the whole intervention and stress that nothing is added to the objective — the change is entirely in which tokens contribute a gradient — but they disagree on the selection rule. One keeps roughly the top 20 percent of tokens by entropy, arguing these act as decision forks; the other masks tokens whose entropy discriminator lies too far from the batch mean, having argued that entropy at a position is the wrong criterion because what governs the entropy change is a deviation from a policy-weighted baseline rather than a level. A third archived result complicates both: randomly masking a comparable set of positive-advantage tokens performed on par with a covariance-targeted rule.

- **Kind**: method
- **Also called**: gradient masking, token masking
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME 24](../datasets/aime-24.md), [AIME 25](../datasets/aime-25.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [clip-higher](clip-higher.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](grpo.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](pass-k.md), [policy entropy](../concepts/policy-entropy.md), [PPO](ppo.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-14B](../models/qwen3-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B](../models/qwen3-8b.md), [RLVR](rlvr.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](verl.md)

## Appears in

- [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](../../archive/papers/2025/local-7d5e3edea2d46b92/summary.md) — Shows that the roughly 20% of CoT tokens with the highest entropy act as decision forks, and that restricting RLVR policy-gradient updates to only those tokens matches or beats full-gradient training, with the advantage growing with model size.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
