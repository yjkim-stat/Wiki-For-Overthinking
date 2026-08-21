# Accuracy-Length Tradeoff

<!-- auto:begin -->

The narrowest of the archive's tradeoff entries: here the cost axis is explicitly the number of tokens in the chain of thought, and the three sources treat the tradeoff as something to be steered rather than accepted. QLPO leaves GRPO's reward, advantage estimator and update untouched and only resamples the training group -- over-generating K=16 rollouts and keeping M=8 that favour short-correct and long-incorrect trajectories -- reporting 30-70% shorter outputs at roughly unchanged accuracy; ARLCP adds coupled penalties on reflective steps and on length scaled by estimated problem complexity. ReBalance is the one source that treats the tradeoff as two-sided, reading token confidence at inference to detect underthinking as well as overthinking and steering hidden states to extend or shorten the trace accordingly. Note: the archive tracks this under several near-duplicate entries that were never merged -- 'Accuracy-Efficiency Tradeoff', 'Accuracy-Efficiency Pareto Frontier', 'Accuracy-token Pareto frontier' and 'accuracy-efficiency tradeoff of reasoning length' -- describing substantially the same idea with a different cost axis named.

- **Kind**: concept
- **Also called**: Accuracy/Length Tradeoff, accuracy-length trade-off, length-accuracy tradeoff
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Accuracy-Efficiency Tradeoff](accuracy-efficiency-tradeoff.md), [accuracy-efficiency tradeoff of reasoning length](accuracy-efficiency-tradeoff-of-reasoning-length.md), [Accuracy-token Pareto frontier](accuracy-token-pareto-frontier.md), [activation steering](../methods/activation-steering.md), [AdaptThink](../methods/adaptthink.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DEER](../methods/deer.md), [DPO_Shortest](../methods/dpo-shortest.md), [GPQA](../datasets/gpqa.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Group-Relative Policy Optimization](../methods/group-relative-policy-optimization.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [LASER](../methods/laser.md), [Length Penalty](length-penalty.md), [LiveCodeBench](../datasets/livecodebench.md), [Manifold Steering](../methods/manifold-steering.md), [MATH-500](../datasets/math-500.md), [NoThinking](../methods/nothinking.md), [NOWAIT](../methods/nowait.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [SEAL](../methods/seal.md), [SFT_Shortest](../methods/sft-shortest.md), [StrategyQA](../datasets/strategyqa.md), [test-time compute scaling](test-time-compute-scaling.md), [Thinkless](../methods/thinkless.md), [ThinkPrune](../methods/thinkprune.md), [TrimR](../methods/trimr.md), [underthinking](underthinking.md), [veRL](../methods/verl.md)

## Appears in

- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.
- [Efficient Reasoning with Balanced Thinking](../../archive/papers/2026/title-7a3e08192f168bcb/summary.md) — ReBalance is a training-free inference-time steering method that reads a reasoning model's token confidence to detect overthinking or underthinking and applies a hidden-state steering vector to shorten or extend the chain of thought accordingly.
- [Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty](../../archive/papers/2026/title-833de99e9b3ea69d/summary.md) — ARLCP is a reinforcement-learning fine-tuning recipe that adds two coupled reward penalties -- one on reflective steps, one on response length scaled by estimated problem complexity -- to shorten chains of thought in distilled reasoning models without losing accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
