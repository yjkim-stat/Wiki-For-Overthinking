# parallel thinking

<!-- auto:begin -->

Parallel thinking denotes sampling several independent reasoning traces for the same problem and aggregating them by majority vote, instead of extending a single trace further. 'Does Thinking More Always Help?' frames it as the more effective use of a fixed compute budget once a single trace's accuracy peaks and then declines from overthinking. DTS treats full independent parallel sampling as the alternative it is built to avoid, instead branching one generation into a small tree only at high-uncertainty tokens and returning the shortest completed trajectory -- both papers measure it against a matched compute or trajectory budget rather than in isolation, since its cost scales with the number of traces sampled.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Best-of-N sampling](best-of-n-sampling.md), [Decoding Tree Sketching (DTS)](decoding-tree-sketching-dts.md), [DeepConf (baseline)](deepconf-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early termination](../concepts/early-termination.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [length-accuracy anti-correlation](../concepts/length-accuracy-anti-correlation.md), [majority voting](majority-voting.md), [Overthinking](../concepts/overthinking.md), [pass@n](../concepts/pass-n.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Self-Consistency](self-consistency.md), [Self-Consistency (baseline)](self-consistency-baseline.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
