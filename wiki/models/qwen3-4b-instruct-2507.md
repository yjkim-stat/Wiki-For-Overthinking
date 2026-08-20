# Qwen3-4B-Instruct-2507

<!-- auto:begin -->

A reasoning-oriented instruction-tuned checkpoint, used by both sources as the stronger model that tests whether a method's benefit survives a better starting point. One adds it specifically to ask whether hidden-state preference signals become more informative as reasoning capability improves, and finds the gain larger there than on weaker backbones. The other includes it among five backbones for test-time latent optimization. The two disagree in a way worth noting: one reports its method helping more as the base model strengthens, while several results elsewhere in this archive report the opposite, so which direction a method scales with base capability is not settled and is worth asking of each.

- **Kind**: model
- **Also called**: Qwen3-4B-Instruct
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [best-of-n](../methods/best-of-n.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [credit assignment](../concepts/credit-assignment.md), [DPO](../methods/dpo.md), [entropy collapse](../concepts/entropy-collapse.md), [entropy trajectory](../concepts/entropy-trajectory.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [latent reasoning](../concepts/latent-reasoning.md), [Llama-3.1-8B-Instruct](llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](llama-3-2-3b-instruct.md), [Llama-3-8B](llama-3-8b.md), [majority voting](../methods/majority-voting.md), [MATH](../datasets/math.md), [MATH500](../datasets/math500.md), [Mistral-7B-v0.3](mistral-7b-v0-3.md), [policy gradient](../methods/policy-gradient.md), [preference optimization](../methods/preference-optimization.md), [process supervision](../concepts/process-supervision.md), [Qwen2.5-14B-Instruct](qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-Math-7B](qwen2-5-math-7b.md), [Qwen3-8B](qwen3-8b.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [self-reflection](../methods/self-reflection.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md), [token-level entropy](../concepts/token-level-entropy.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](../../archive/papers/2026/arxiv-2608-02585/summary.md) — Inserts optimizable latent states at an intermediate Transformer layer rather than at the output, so self-attention makes every continuation token's log-probability differentiable with respect to every latent and reward-weighted gradients reach them from the whole continuation instead of only through their own decoded token.
- [EDIS: Diagnosing LLM Reasoning via Entropy Dynamics](../../archive/papers/2026/local-e64d3a8c4788daf7/summary.md) — Introduces EDIS, a trajectory-level score that measures how unstably token entropy evolves during generation, and uses it to select better reasoning rollouts at inference and to curate training samples in RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
