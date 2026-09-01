# LISA

<!-- auto:begin -->

LISA (a reasoning-segmentation benchmark measuring generalized IoU for language-guided image segmentation) is used in these sources to evaluate general-capability preservation and reasoning-efficiency methods: RECAP reports LISA as achieving its highest segmentation score among compared methods in its hybrid RLVR+SFT setting (more than 2% above the base model), and DR2Seg reports its two-stage description-then-segmentation approach cuts reasoning length while raising gIoU on reasoning-segmentation tasks including LISA.

- **Kind**: dataset
- **Also called**: LISA++
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AI2D](ai2d.md), [ChartQA](chartqa.md), [Length reward](../concepts/length-reward.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Reasoning Segmentation](../concepts/reasoning-segmentation.md), [ReasonSeg](reasonseg.md), [RefCOCO](refcoco.md), [RefCOCOg](refcocog.md), [RLVR](../methods/rlvr.md), [SAT](sat.md), [ScienceQA](scienceqa.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Task Decomposition](../concepts/task-decomposition.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [VizWiz](vizwiz.md)

## Appears in

- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.
- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
