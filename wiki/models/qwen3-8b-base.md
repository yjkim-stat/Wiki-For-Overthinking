# Qwen3-8B-Base

<!-- auto:begin -->

An open base checkpoint, and in both sources the model on which a controlled post-training comparison is built — which is the point, since vendors release neither matched pre- and post-training pairs nor the data that would let an effect be attributed. One distils and then RLVR-trains it themselves to isolate what reinforcement learning changes, reporting maze exploration entropy falling from 2.3380 to 1.8138 and dead-end backtracking probability rising from 0.0068 to 0.1537. The other uses it among three base sizes for an experience-distillation stage inserted before RL. Its recurrence marks a methodological preference this archive should note: a base checkpoint whose post-training you performed yourself is worth more than a stronger one whose history you cannot see.

- **Kind**: model
- **Also called**: Qwen3-8B Base
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](../concepts/advantage-estimation.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [backtracking](../concepts/backtracking.md), [DAPO](../methods/dapo.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [data efficiency](../concepts/data-efficiency.md), [entropy collapse](../concepts/entropy-collapse.md), [exploration](../concepts/exploration.md), [gpt-oss-120b](gpt-oss-120b.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](../methods/knowledge-distillation.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [long chain-of-thought distillation](../methods/long-chain-of-thought-distillation.md), [MATH500](../datasets/math500.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [pass@k](../methods/pass-k.md), [policy entropy](../concepts/policy-entropy.md), [post-hoc rationalization](../concepts/post-hoc-rationalization.md), [privileged information](../concepts/privileged-information.md), [Qwen3-1.7B-Base](qwen3-1-7b-base.md), [Qwen3-4B-Base](qwen3-4b-base.md), [reasoning boundary](../concepts/reasoning-boundary.md), [reward sparsity](../concepts/reward-sparsity.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [trajectory diversity](../concepts/trajectory-diversity.md)

## Appears in

- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [BODHI: Do LLMs Branch Out and Discover Heterogeneous Inferences?](../../archive/papers/2026/arxiv-2608-02867/summary.md) — Builds prefix trees of semantically equivalent reasoning statements and measures how RLVR changes a model's preference between branches, finding the entropy collapse is not stylistic — the collapse is stronger for semantically distinct continuations than for syntactic variants of the same statement.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
