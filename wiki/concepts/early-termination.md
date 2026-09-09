# early termination

<!-- auto:begin -->

In this source, early termination is the selection rule applied at the end of Decoding Tree Sketching's branching process: rather than sampling many independent full trajectories and checking their correctness, the DTS-Greedy and DTS-Stable variants return whichever branch of the sketch tree finishes generating first -- the shortest completed trajectory -- with no correctness check. This exploits an empirically and theoretically established length-accuracy anti-correlation in large reasoning models, where shorter trajectories are more often correct on average. Because that anti-correlation is only a population-level statistical trend, the rule can systematically prefer a quick-but-wrong trajectory over a slower-but-correct one on problems where the correlation is weak or reversed for that specific instance.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Decoding Tree Sketching (DTS)](../methods/decoding-tree-sketching-dts.md), [DeepConf (baseline)](../methods/deepconf-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [length-accuracy anti-correlation](length-accuracy-anti-correlation.md), [Overthinking](overthinking.md), [parallel thinking](../methods/parallel-thinking.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Self-Consistency (baseline)](../methods/self-consistency-baseline.md)

## Appears in

- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.
- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/title-c614f5d4c1a5c21d/summary.md) — A decoding-time framework that sketches a reasoning tree via selective branching and terminates long, low-accuracy reasoning trajectories early, using an observed length-accuracy anti-correlation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
