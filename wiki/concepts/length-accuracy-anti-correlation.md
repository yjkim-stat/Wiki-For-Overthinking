# length-accuracy anti-correlation

<!-- auto:begin -->

An observed negative relationship between how long a reasoning trajectory runs and how likely it is to be correct: among completed trajectories on the same problem, the shorter ones tend to be the accurate ones. It is read by Decoding Tree Sketching (DTS), a training-free decoding framework that branches generation into a small tree only at high-uncertainty 'decision tokens' and then exploits this anti-correlation by terminating on and returning the shortest completed trajectory, rather than sampling many full independent trajectories.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Decoding Tree Sketching (DTS)](../methods/decoding-tree-sketching-dts.md), [DeepConf (baseline)](../methods/deepconf-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early termination](early-termination.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Overthinking](overthinking.md), [parallel thinking](../methods/parallel-thinking.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Self-Consistency (baseline)](../methods/self-consistency-baseline.md)

## Appears in

- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
