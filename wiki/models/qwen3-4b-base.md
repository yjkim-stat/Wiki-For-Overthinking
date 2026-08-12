# Qwen3-4B-Base

<!-- auto:begin -->

A 4B-parameter base checkpoint from the Qwen3 family, used by both sources as a starting point for reinforcement learning with verifiable rewards on mathematics. In one it is the second of two base models for the entropy-flow experiments, trained on DAPO-17K; in the other it appears in an appendix extension checking that the entropy-discriminator clipping methods hold across model families rather than only on the Qwen2.5-Instruct models of the main study. Neither source describes the model itself.

- **Kind**: model
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [AMC23](../datasets/amc23.md), [Clip-Cov](../methods/clip-cov.md), [clip-higher](../methods/clip-higher.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [entropy bonus](../concepts/entropy-bonus.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GRPO](../methods/grpo.md), [KL-Cov](../methods/kl-cov.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [pass-k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [RLVR](../methods/rlvr.md), [token-level entropy](../concepts/token-level-entropy.md), [VeRL](../methods/verl.md)

## Appears in

- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](../../archive/papers/2026/local-8efebbee3585a141/summary.md) — Recasts entropy collapse as an imbalance of 'entropy flow' — tokens whose update lowers entropy persistently outweigh those that raise it — and rebalances the two sets with a closed-form coefficient computed from each batch, without reference policies or entropy bonuses.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
