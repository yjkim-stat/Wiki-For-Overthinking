# RefCOCOg

<!-- auto:begin -->

RefCOCOg is the companion referring-expression benchmark to RefCOCO. In this archive it is used identically to RefCOCO: as an evaluation set (scored by gIoU) for the reasoning-segmentation methods DR²Seg and PixelThink, with no further description of the benchmark itself in either source.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning length](../concepts/adaptive-reasoning-length.md), [GRPO](../methods/grpo.md), [Length reward](../concepts/length-reward.md), [LISA](lisa.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Segmentation](../concepts/reasoning-segmentation.md), [ReasonSeg](reasonseg.md), [RefCOCO](refcoco.md), [RLVR](../methods/rlvr.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Task Decomposition](../concepts/task-decomposition.md)

## Appears in

- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
