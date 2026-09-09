# DeepConf (baseline)

<!-- auto:begin -->

DeepConf (baseline) is named in this archive as a confidence-based test-time-scaling comparison point, but neither source describes its mechanism: Gambit's thought-level beam search and DTS's decision-token branching with shortest-trajectory selection are each presented as their own alternative to sampling and scoring full trajectories, without characterizing how DeepConf itself computes or applies its confidence signal.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [Decoding Tree Sketching (DTS)](decoding-tree-sketching-dts.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early termination](../concepts/early-termination.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [HMMT 2025](../datasets/hmmt-2025.md), [length-accuracy anti-correlation](../concepts/length-accuracy-anti-correlation.md), [parallel thinking](parallel-thinking.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Self-Consistency (baseline)](self-consistency-baseline.md), [Slim-SC (baseline)](slim-sc-baseline.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
