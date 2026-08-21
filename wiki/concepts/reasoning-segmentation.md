# Reasoning Segmentation

<!-- auto:begin -->

A vision-language task in which a multimodal LLM is given an image and an indirect or complex query rather than a direct referring expression, reasons about it, and emits a segmentation mask. Both archived sources treat it mainly as a testbed for reasoning length: PixelThink conditions a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, reaching 60.17% gIoU at 47.66 average reasoning tokens on the ReasonSeg-Diff test set against Seg-Zero at 58.20% and 90.58 tokens; DR2Seg splits the task into a description stage and a referring-segmentation stage and rewards a shorter self-contained description that still yields the right mask, reaching gIoU 68.5 validation and 66.1 test on ReasonSeg at 7B against VisionReasoner's 65.4 and 62.3 with reasoning tokens of 26.9 against 85.3. What makes the task reasoning-heavy in their own accounts is the contrast with direct referring benchmarks, where the margin nearly vanishes (RefCOCO testA 79.3 for DR2Seg-7B against 78.8 for its baseline). Note that both papers' accuracy gains are small in absolute terms -- roughly 1 to 4 gIoU points -- so the case rests on the token reduction.

- **Kind**: concept
- **Also called**: reasoning segmentation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning length](adaptive-reasoning-length.md), [GRPO (Group Relative Policy Optimization)](../methods/grpo-group-relative-policy-optimization.md), [Length reward](length-reward.md), [overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [ReasonSeg](../datasets/reasonseg.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [task decomposition](task-decomposition.md)

## Appears in

- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [Don't Overthink with Pixels: Efficient Reasoning for Segmentation](../../archive/papers/2026/title-d94f940ea2e159b8/summary.md) — PixelThink regulates the length of a multimodal LLM's reasoning chain in reasoning segmentation by conditioning a GRPO reward on an externally estimated task difficulty and the model's own uncertainty, cutting reasoning tokens roughly in half while slightly improving mask accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
