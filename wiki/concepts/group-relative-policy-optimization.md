# Group-Relative Policy Optimization

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Also called**: Group Relative Policy Optimization
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [Accuracy-Length Tradeoff](accuracy-length-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BIG-Bench Hard](../datasets/big-bench-hard.md), [CommonsenseQA](../datasets/commonsenseqa.md), [Dr. GRPO](../methods/dr-grpo.md), [GPQA](../datasets/gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [LASER](../methods/laser.md), [Length Penalty](length-penalty.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [StrategyQA](../datasets/strategyqa.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [SVAMP](../datasets/svamp.md), [Thinkless](../methods/thinkless.md), [ThinkPrune](../methods/thinkprune.md), [Token Budget](token-budget.md), [veRL](../methods/verl.md)

## Appears in

- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.
- [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](../../archive/papers/2026/title-39bbcb4cded34ec7/summary.md) — WS-GRPO trains a preference model from outcome-only correctness labels to score partial reasoning trajectories, turning terminal reward into prefix-level signal about whether continuing is worthwhile, and reports far shorter reasoning at some accuracy cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
