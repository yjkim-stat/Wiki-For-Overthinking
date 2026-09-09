# Decoding Tree Sketching (DTS)

<!-- auto:begin -->

Decoding Tree Sketching (DTS) is a training-free decoding framework that replaces sampling many independent full reasoning trajectories with a single compact 'sketch' tree: it branches, up to a branch factor of 3 and capped at 48 simultaneous branches, only at high-uncertainty 'decision tokens' identified by entropy and varentropy thresholds, leaving low-uncertainty spans unbranched. It exploits an empirically and theoretically established length-accuracy anti-correlation -- shorter trajectories tend to be more often correct -- through an early-termination selection rule (DTS-Greedy / DTS-Stable) that returns the first, shortest completed trajectory rather than checking correctness. Across four models and four benchmarks it improves accuracy by 14% and reduces repetitive generation by 8% on average, letting smaller models match or beat models ten times their size at matched compute; because the anti-correlation it exploits is only a population-level statistical trend, DTS-Greedy's no-correctness-check rule can systematically prefer a quick-but-wrong trajectory when the correlation is weak or reversed for a specific problem.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [DeepConf (baseline)](deepconf-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early termination](../concepts/early-termination.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [length-accuracy anti-correlation](../concepts/length-accuracy-anti-correlation.md), [Overthinking](../concepts/overthinking.md), [parallel thinking](parallel-thinking.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Self-Consistency (baseline)](self-consistency-baseline.md)

## Appears in

- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.
- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/title-c614f5d4c1a5c21d/summary.md) — A decoding-time framework that sketches a reasoning tree via selective branching and terminates long, low-accuracy reasoning trajectories early, using an observed length-accuracy anti-correlation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
