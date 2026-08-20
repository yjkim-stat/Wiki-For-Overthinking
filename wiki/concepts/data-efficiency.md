# data efficiency

<!-- auto:begin -->

Reaching a given level of performance from less training data or fewer rollouts, and across 4 sources approached from the same direction: identify before training which prompts will teach something. The archive's instances. Task learnability is separated from current pass rate, shown reproducible across independent runs, and shown to predict downstream value at matched current performance -- estimated from a short probe run before training begins, which is what makes it a prior rather than a diagnosis. Prompts on which every sampled rollout already succeeds are identified and removed, since their advantage estimate is zero and the rollouts are pure waste. And a stage inserted before reinforcement learning, in which the model extracts textual lessons from its own rollouts and distils the surviving ones into its weights, produces a policy that fails all-eight-samples less often -- reported as matched performance at roughly 28 percent fewer trajectories and steps, a 1.39-fold speedup. A fourth instance is about supervised data rather than rollouts: 1,000 examples suffice to change a model's reasoning structure enough for safety alignment with no reinforcement learning at all.

- **Kind**: concept
- **Also called**: rollout efficiency, sample efficiency, sample efficiency of training
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [alignment tax](alignment-tax.md), [AMC23](../datasets/amc23.md), [ARC-AGI](../datasets/arc-agi.md), [curriculum learning](../methods/curriculum-learning.md), [DAPO-Math-17K](../datasets/dapo-math-17k.md), [exploration](exploration.md), [generalization](generalization.md), [group-relative advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-3B](../models/llama-3-2-3b.md), [MATH500](../datasets/math500.md), [Minerva](../datasets/minerva.md), [OlympiadBench](../datasets/olympiadbench.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [policy entropy](policy-entropy.md), [post-hoc rationalization](post-hoc-rationalization.md), [post-training](../methods/post-training.md), [privileged information](privileged-information.md), [prompt difficulty](prompt-difficulty.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-1.7B-Base](../models/qwen3-1-7b-base.md), [Qwen3-4B](../models/qwen3-4b.md), [Qwen3-4B-Base](../models/qwen3-4b-base.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reward sparsity](reward-sparsity.md), [safety alignment](safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [training dynamics](training-dynamics.md), [zero-advantage group](zero-advantage-group.md)

## Appears in

- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training](../../archive/papers/2026/arxiv-2608-09217/summary.md) — Separates how well a policy currently does on a task from how positively that task responds to further training, shows the second is reproducible across independent runs and predicts downstream value at matched current pass rate, and estimates it from a short probe run before RL begins.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
