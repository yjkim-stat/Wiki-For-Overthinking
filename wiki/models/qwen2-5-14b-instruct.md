# Qwen2.5-14B-Instruct

<!-- auto:begin -->

A mid-scale instruction-tuned checkpoint, present in both sources as the larger member of a comparison rather than as a subject. One uses it among five backbones for test-time latent optimization, where it carries the highest clean chain-of-thought baseline of the set and the gains are correspondingly smaller. The other uses it in an analysis of entropy dynamics under reinforcement fine-tuning. Its role in the archive is as the point where a method's headroom starts to close — several results collected here separate clearly at 3B and much less at this size.

- **Kind**: model
- **Also called**: Qwen2.5-14B
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [clip-higher](../methods/clip-higher.md), [credit assignment](../concepts/credit-assignment.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [MATH-500](../datasets/math-500.md), [pass-k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient](../methods/policy-gradient.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-4B-Instruct-2507](qwen3-4b-instruct-2507.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../methods/test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md)

## Appears in

- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) — Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
