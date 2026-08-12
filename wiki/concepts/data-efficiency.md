# data efficiency

<!-- auto:begin -->

Achieving a training effect with few examples or few rollouts, used by the sources as evidence about what is being learned rather than only as a cost argument. One identifies rollouts wasted on prompts where every sample is already correct and the advantage is therefore zero, making efficiency a matter of which prompts are worth sampling. The other reports safety alignment from 1K supervised examples and treats that smallness as support for its claim that the target is a reusable reasoning structure rather than knowledge — if the fix needed knowledge it would need far more data. The inference from few examples to structure is the sources' argument, not a demonstrated mechanism.

- **Kind**: concept
- **Also called**: rollout efficiency, sample efficiency
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [advantage estimation](advantage-estimation.md), [alignment tax](alignment-tax.md), [generalization](generalization.md), [GRPO](../methods/grpo.md), [post-training](../methods/post-training.md), [prompt difficulty](prompt-difficulty.md), [safety alignment](safety-alignment.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.
- [Reasoning Structure Matters for Safety Alignment of Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-240/summary.md) — Argues reasoning models' safety failures come from the reasoning structure itself, and achieves safety alignment by altering that structure with 1K supervised examples and no RL.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
