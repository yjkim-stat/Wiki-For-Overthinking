# Qwen2.5-7B-Instruct

<!-- auto:begin -->

An instruction-tuned checkpoint used in both sources as the base policy a method is applied to rather than as something being characterized. One reinforcement-fine-tunes it and reports a GRPO baseline of 16.88 Avg@32 and 50.00 Pass@32 on AIME24, against 19.69 and 56.67 for its own variant — numbers low enough that the benchmark is near its floor for this model. The other uses it as one of the models whose hidden-state trajectories are scored for progress and stability. Its presence marks the scale most of this archive's reinforcement-learning work is actually done at.

- **Kind**: model
- **Also called**: Qwen2.5-7B-Instruct
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [advantage function](../concepts/advantage-function.md), [AIME24](../datasets/aime24.md), [AIME25](../datasets/aime25.md), [clip-higher](../methods/clip-higher.md), [DAPO](../methods/dapo.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy regularization](../methods/entropy-regularization.md), [exploration-exploitation trade-off](../concepts/exploration-exploitation-trade-off.md), [GPQA](../datasets/gpqa.md), [GPT-4o](gpt-4o.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [linear probe](../methods/linear-probe.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [LoRA](../methods/lora.md), [MATH](../datasets/math.md), [pass-k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [policy gradient masking](../methods/policy-gradient-masking.md), [PPO](../methods/ppo.md), [Qwen2.5-0.5B](qwen2-5-0-5b.md), [Qwen2.5-1.5B](qwen2-5-1-5b.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [token-level entropy](../concepts/token-level-entropy.md)

## Appears in

- [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](../../archive/papers/2026/local-837612b527cb427c/summary.md) — Reduces the question of whether an update raises or lowers entropy to the sign of one scalar per token, shows that under GRPO what matters is that scalar's deviation from a policy-weighted baseline rather than its own value, and proves the deviation averages to zero over a batch.
- [Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability](../../archive/papers/2026/local-85a70e78b4a93190/summary.md) — TRACED scores a reasoning chain by the geometry of its hidden-state trajectory -- net displacement as progress and curvature as stability -- and uses the two as features for a Gaussian classifier that separates correct from incorrect chains without reading the text.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
