# Slim-SC (baseline)

<!-- auto:begin -->

A self-consistency-style baseline used for comparison by test-time-scaling papers in the archive, evaluated against by both Gambit's thought-level beam search and Funnel of Thoughts' early-voting rollout pruning as one of the parallel-sampling methods their own approaches aim to beat on cost or accuracy.

- **Kind**: method
- **Also called**: Slim-SC
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [AMC23](../datasets/amc23.md), [Best-of-N sampling](best-of-n-sampling.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [MATH500](../datasets/math500.md), [Self-Consistency](self-consistency.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](../../archive/papers/2026/arxiv-2608-15065/summary.md) — Funnel of Thoughts detects and discards the subset of parallel reasoning rollouts that are spiraling into unproductive self-correction (flagged by a rising density of hesitation words like 'Wait' and 'perhaps'), matching self-consistency's accuracy while cutting attention FLOPs by up to 56% and wall time by 37.6%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
