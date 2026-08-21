# veRL

<!-- auto:begin -->

Neither source describes veRL directly; it appears as a named point of reference alongside their own RL recipes. EvoThink cuts overthinking via Self-Pruning Training (removing reasoning steps whose local conclusion repeats the previous one) followed by Aha-Moment Preference Optimization (DPO on wrong-to-right preference pairs built from diverse failed attempts); QLPO over-generates rollouts per prompt and resamples the training group to favour short-correct and long-incorrect trajectories, shortening outputs 30-70% relative to GRPO at roughly unchanged accuracy.

- **Kind**: method
- **Also called**: VeRL
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Accuracy-Length Tradeoff](../concepts/accuracy-length-tradeoff.md), [aha moment](../concepts/aha-moment.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [GPQA](../datasets/gpqa.md), [Group-Relative Policy Optimization](group-relative-policy-optimization.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [LASER](laser.md), [MATH-500](../datasets/math-500.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](../concepts/overthinking.md), [preference optimization](preference-optimization.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Thinkless](thinkless.md), [ThinkPrune](thinkprune.md)

## Appears in

- [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](../../archive/papers/2026/arxiv-2607-19962/summary.md) — EvoThink cuts overthinking in two separable stages: Self-Pruning Training deletes reasoning steps whose local conclusion repeats the previous step's and self-trains on the shortened traces, while Aha-Moment Preference Optimization builds from-wrong-to-right preference pairs out of the model's most diverse failed attempts and applies DPO to them.
- [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](../../archive/papers/2026/arxiv-2607-21793/summary.md) — QLPO is a GRPO variant that leaves the reward, advantage estimator and update untouched and instead over-generates K=16 rollouts per prompt and resamples the M=8 training group to favour short-correct and long-incorrect trajectories, which shortens outputs by 30-70% relative to GRPO at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
