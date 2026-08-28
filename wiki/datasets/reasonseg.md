# ReasonSeg

<!-- auto:begin -->

The benchmark both archived sources evaluate reasoning segmentation on. Neither describes how it was built, so what the archive holds is only how it is used: PixelThink-7B reports 63.8% gIoU / 62.7% cIoU on it against Seg-Zero-7B at 62.6% / 62.0%, and DR2Seg at 7B with SAM2 reports gIoU 68.5 on validation and 66.1 on test against VisionReasoner at 65.4 and 62.3, with reasoning tokens falling from 85.3 to 26.9. PixelThink additionally builds ReasonSeg-Diff, an extension annotated with reasoning references and per-sample difficulty scores, where it reaches 60.17% gIoU at 47.66 average reasoning tokens against Seg-Zero's 58.20% at 90.58. Both papers position its queries as reasoning-heavy by contrast with RefCOCO, on which their margins over the same baselines shrink to roughly half a point.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning length](../concepts/adaptive-reasoning-length.md), [GRPO](../methods/grpo.md), [Length reward](../concepts/length-reward.md), [LISA](lisa.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Segmentation](../concepts/reasoning-segmentation.md), [RefCOCO](refcoco.md), [RefCOCOg](refcocog.md), [RLVR](../methods/rlvr.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Task Decomposition](../concepts/task-decomposition.md)

## Appears in

- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
