# Self-Consistency (baseline)

<!-- auto:begin -->

Self-Consistency (sampling multiple reasoning traces and majority-voting) is used as a comparison baseline in Gambit (thought-level beam search that periodically prunes weak reasoning traces and branches new ones) and BrowseConf (confidence-guided test-time scaling for web agents, showing web-search agents' verbalized confidence systematically exceeds actual accuracy despite being informative for guiding search).

- **Kind**: method
- **Also called**: Self-Consistency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AIME 2026](../datasets/aime-2026.md), [BrowseComp](../datasets/browsecomp.md), [Confidence-Informed Self-Consistency (CISC, baseline)](confidence-informed-self-consistency-cisc-baseline.md), [Decoding Tree Sketching (DTS)](decoding-tree-sketching-dts.md), [DeepConf (baseline)](deepconf-baseline.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [early termination](../concepts/early-termination.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [HMMT 2025](../datasets/hmmt-2025.md), [length-accuracy anti-correlation](../concepts/length-accuracy-anti-correlation.md), [parallel thinking](parallel-thinking.md), [Qwen3-0.6B](../models/qwen3-0-6b.md), [Slim-SC (baseline)](slim-sc-baseline.md)

## Appears in

- [Thought-Level Beam Search for Reasoning](../../archive/papers/2026/arxiv-2608-08020/summary.md) — Introduces Gambit, an inference algorithm that formulates test-time reasoning as thought-level beam search, periodically pruning weak reasoning traces and branching new ones from high-quality prefixes to concentrate a fixed hardware budget on the most promising partial reasoning.
- [BrowseConf: Confidence-Guided Test-Time Scaling for Web Agents](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-21/summary.md) — BrowseConf shows that despite web-search agents being poorly calibrated in absolute terms (verbalized confidence systematically exceeds actual accuracy), their confidence is strongly rank-correlated with correctness -- near-zero accuracy below 70% confidence, more than double the average accuracy above 95% -- and exploits this by triggering additional search attempts only when confidence falls below a calibrated threshold rather than always sampling a fixed number, matching or beating fixed-budget Self-Consistency/CISC on BrowseComp while cutting average attempts from a fixed 10 down to 2.06-5.72.
- [DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching](../../archive/papers/2026/local-6ea04c0fef8fdbd9/summary.md) — A training-free decoding framework that selectively branches a reasoning model's generation into a small tree only at high-uncertainty 'decision tokens', then exploits an observed length-accuracy anti-correlation by terminating on and returning the shortest completed trajectory instead of sampling many full independent trajectories.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
