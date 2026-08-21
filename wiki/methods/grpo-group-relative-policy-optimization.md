# GRPO (Group Relative Policy Optimization)

<!-- auto:begin -->

Under this spelling the archive holds only two multimodal/adaptive-compression papers, and both use GRPO as an unmodified training loop whose reward they reshape by difficulty: TRAAC prunes a chain of thought using attention from the </think> token and calibrates how aggressively it prunes to estimated problem difficulty, and PixelThink conditions the GRPO reward on an externally estimated task difficulty plus the model's own uncertainty, halving reasoning tokens in reasoning segmentation while slightly improving mask accuracy. Neither source defines the algorithm; both treat it as the given online-RL substrate onto which a difficulty-aware length signal is attached. Note: the archive tracks this under three unmerged entries — GRPO, Group-Relative Policy Optimization and GRPO (Group Relative Policy Optimization) — which are the same algorithm.

- **Kind**: method
- **Also called**: GRPO (group-relative policy optimization)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning length](../concepts/adaptive-reasoning-length.md), [AdaptThink](adaptthink.md), [BBH (Big Bench Hard)](../datasets/bbh-big-bench-hard.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [group relative advantage](../concepts/group-relative-advantage.md), [Group-Relative Policy Optimization](group-relative-policy-optimization.md), [GRPO](grpo.md), [LC-R1](lc-r1.md), [overthinking](../concepts/overthinking.md), [Reasoning Segmentation](../concepts/reasoning-segmentation.md), [ReasonSeg](../datasets/reasonseg.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [Seg-Zero (baseline)](seg-zero-baseline.md), [SuperGPQA](../datasets/supergpqa.md), [TokenSkip](tokenskip.md)

## Appears in

- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
