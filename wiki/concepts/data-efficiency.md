# data efficiency

<!-- auto:begin -->

Achieving a training effect with few examples or few rollouts, used by the sources as evidence about what is being learned rather than only as a cost argument. One identifies rollouts wasted on prompts where every sample is already correct and the advantage is therefore zero, making efficiency a matter of which prompts are worth sampling. The other reports safety alignment from 1K supervised examples and treats that smallness as support for its claim that the target is a reusable reasoning structure rather than knowledge — if the fix needed knowledge it would need far more data. The inference from few examples to structure is the sources' argument, not a demonstrated mechanism.

- **Kind**: concept
- **Also called**: rollout efficiency, sample efficiency
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [advantage estimation](advantage-estimation.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [alignment tax](alignment-tax.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [exploration](exploration.md), [generalization](generalization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [on-policy self-distillation](../methods/on-policy-self-distillation.md), [policy entropy](policy-entropy.md), [post-hoc rationalization](post-hoc-rationalization.md), [post-training](../methods/post-training.md), [privileged information](privileged-information.md), [prompt difficulty](prompt-difficulty.md), [reward sparsity](reward-sparsity.md), [safety alignment](safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Self-Improving Large Language Models via Progressive Experience Evolution](../../archive/papers/2026/arxiv-2608-02139/summary.md) — Inserts a stage before RL in which the model extracts textual lessons from its own successful and failed rollouts, filters them by measured marginal utility on a held-out probe set, and distills the surviving pool into its own weights — so that GRPO starts from a policy that fails all-eight-samples less often.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
