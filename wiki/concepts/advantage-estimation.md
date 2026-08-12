# advantage estimation

<!-- auto:begin -->

Assigning each sampled rollout a learning signal relative to a baseline, which in the critic-free methods the sources use means comparing rollouts within a group. Both sources identify the same structural failure from opposite ends: when every rollout in a group receives the same reward the group-relative advantage is zero and the batch teaches nothing. One hits it on prompts where all rollouts are already correct, wasting the rollouts; the other on negative samples where no valid output exists, and forces a canonical 'None' rollout so the group regains variance. Together they show that group-relative methods depend on within-group disagreement, which makes example selection a requirement rather than an optimization.

- **Kind**: concept
- **Also called**: GRPO advantage, advantage estimate, group-relative advantage
- **Topics**: [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [abstention](abstention.md), [data efficiency](data-efficiency.md), [GRPO](../methods/grpo.md), [hallucination](hallucination.md), [prompt difficulty](prompt-difficulty.md), [reinforcement learning post-training](../methods/reinforcement-learning-post-training.md), [reward shaping](reward-shaping.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md)

## Appears in

- [Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO](../../archive/papers/2026/arxiv-2608-04698/summary.md) — A GRPO variant that teaches multimodal models to refuse when a referred object is absent, without losing localization accuracy on cases where it is present.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — Addresses wasted rollouts in critic-free RL on prompts where every sampled rollout is already correct and the advantage estimate is therefore zero.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
