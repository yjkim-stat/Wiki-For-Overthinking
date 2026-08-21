# Group-Relative Policy Optimization

<!-- auto:begin -->

The spelled-out name for GRPO, used here in papers that build directly on it: QLPO leaves its reward, advantage estimator and update untouched and only resamples which rollouts form the training group (K=16 over-generated, M=8 kept), shortening outputs 30-70% at roughly unchanged accuracy; ARM replaces it with Ada-GRPO to pick among four reasoning formats, cutting tokens about 30%; WS-GRPO keeps the group-relative update but replaces a global length penalty with prefix-level rewards from a preference model trained on outcome-only labels. What the three share is the assumption that the group-relative update is sound and that the leverage is elsewhere — in the reward, the group composition or the format choice. Note: the archive tracks this under three unmerged entries — GRPO, Group-Relative Policy Optimization and GRPO (Group Relative Policy Optimization) — which are the same algorithm.

- **Kind**: method
- **Also called**: Group Relative Policy Optimization
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [Ada-GRPO](ada-grpo.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BIG-Bench Hard](../datasets/big-bench-hard.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Dr. GRPO](dr-grpo.md), [GPQA](../datasets/gpqa.md), [group relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GRPO (Group Relative Policy Optimization)](grpo-group-relative-policy-optimization.md), [GSM8K](../datasets/gsm8k.md), [LASER](laser.md), [Length Penalty](../concepts/length-penalty.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Thinkless](thinkless.md), [ThinkPrune](thinkprune.md), [Token Budget](../concepts/token-budget.md), [veRL](verl.md)

## Appears in

- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
