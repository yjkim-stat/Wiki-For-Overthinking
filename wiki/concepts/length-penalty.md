# Length Penalty

<!-- auto:begin -->

A negative reward term added during RL fine-tuning that charges a reasoning model for how much it produces, used to shorten chains of thought. The three archived sources agree on the mechanism but disagree on the unit charged: ARLCP penalises raw response length, scaled by estimated problem complexity and coupled to a second penalty on reflective steps through a shared budget (53.1% shorter with a 5.81% accuracy gain on DeepSeek-R1-Distill-Qwen-1.5B, 35.0% and 2.69% at 7B, trained with RLOO); CoSMo penalises deviation of the segment count from a per-problem reference, deliberately leaving intra-segment tokens free, so its 28.7% segment reduction is not a 28.7% token reduction; WS-GRPO penalises trajectories falling outside a hand-set range of 3 to 6 steps. All three treat a flat penalty on tokens as too blunt to use on its own, and WS-GRPO states outright that length-penalty calibration remains dataset-dependent, reporting 92.9% fewer tokens on ARC for 2.5 accuracy points and 52.5% on GSM8K for 7.3 on Qwen2.5-7B-Instruct. The archive uses 'length penalty' and 'length reward' for the same signal with the sign flipped; see that entry for the evidence that applying it naively costs accuracy.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DPO_Shortest](../methods/dpo-shortest.md), [Dr. GRPO](../methods/dr-grpo.md), [Group-Relative Policy Optimization](../methods/group-relative-policy-optimization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HotpotQA](../datasets/hotpotqa.md), [LASER](../methods/laser.md), [Length reward](length-reward.md), [MATH-500](../datasets/math-500.md), [NoThinking](../methods/nothinking.md), [O1-Pruner](../methods/o1-pruner.md), [overthinking](overthinking.md), [SFT_Shortest](../methods/sft-shortest.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [test-time compute scaling](test-time-compute-scaling.md), [Token Budget](token-budget.md)

## Appears in

- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
