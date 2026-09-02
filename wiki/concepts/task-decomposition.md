# Task Decomposition

<!-- auto:begin -->

Task decomposition here means splitting a single reasoning problem into ordered sub-stages rather than solving it in one pass. DR²Seg splits reasoning segmentation into a description stage and a referring-segmentation stage, rewarding shorter descriptions that still yield the correct mask; D-CORE instead names inadequate task decomposition 'Lazy Reasoning', a failure mode in complex tool-use settings that its self-distillation-then-diversity-aware-RL recipe is designed to correct.

- **Kind**: concept
- **Also called**: Task Decomposition, task decomposition
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BFCL v3](../datasets/bfcl-v3.md), [Length reward](length-reward.md), [LISA](../datasets/lisa.md), [Overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Segmentation](reasoning-segmentation.md), [ReasonSeg](../datasets/reasonseg.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [RLVR](../methods/rlvr.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Self-Distillation](self-distillation.md)

## Appears in

- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use](../../archive/papers/2026/title-6c0fc879a2cc7d5b/summary.md) — Trains large reasoning models with self-distillation followed by diversity-aware RL to overcome 'Lazy Reasoning' -- inadequate task decomposition -- in complex tool-use settings.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
