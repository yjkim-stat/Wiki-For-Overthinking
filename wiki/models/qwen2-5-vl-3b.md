# Qwen2.5-VL-3B

<!-- auto:begin -->

Qwen2.5-VL-3B is a smaller vision-language model evaluated alongside Qwen2.5-VL-7B in RECAP (mitigating general-capability forgetting caused by RLVR-based reasoning fine-tuning in VLMs) and GPRO (diagnosing that visual perception failures, not reasoning errors, dominate incorrect predictions across model scales).

- **Kind**: model
- **Also called**: Qwen2.5VL-3B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AI2D](../datasets/ai2d.md), [ChartQA](../datasets/chartqa.md), [DynaMath](../datasets/dynamath.md), [LISA](../datasets/lisa.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MM-Vet](../datasets/mm-vet.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [Qwen2.5-VL-7B](qwen2-5-vl-7b.md), [SAT](../datasets/sat.md), [ScienceQA](../datasets/scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [ViRL39k](../datasets/virl39k.md), [VizWiz](../datasets/vizwiz.md)

## Appears in

- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — GPRO diagnoses that visual perception failures (not reasoning errors) cause over twice as many incorrect predictions across model scales in vision-language models, then routes each generated token through one of three paths -- a fast FFN, a slow cross-attention perception path for re-examining the image, or a slow self-reflection reasoning path -- via a lightweight meta-reasoning controller trained with PPO on a multi-objective reward (task accuracy, path-cost penalty, and an uncertainty-calibration term derived from ~790K GPT-4-labeled perception-vs-reasoning failure attributions); GPRO-7B matches/beats far larger closed models and long-CoT distillation baselines while cutting response length up to 51.5%, activating slow paths sparsely (73% Fast/17% Perception/10% Reasoning) and correctly, targeting perception re-examination at high-frequency visual tokens and reasoning refinement at logical connectives.
- [VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception](../../archive/papers/2025/title-4888764f9c757f11/summary.md) — Visual Test-Time Scaling (VTTS) lets a multimodal LLM iteratively refine its perception of high-confidence spatio-temporal regions during inference, guided by its own updated textual predictions, and the resulting VideoChat-R1.5 model improves over strong baselines by 5%+ on 15+ video benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
