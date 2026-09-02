# Qwen2.5-VL-7B

<!-- auto:begin -->

Qwen2.5-VL-7B is a vision-language model used across multiple studies of reasoning-training side effects: ARM2 extends adaptive reasoning-format selection to multimodal inputs on it, RECAP evaluates it to mitigate general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes, and GPRO diagnoses that visual perception failures (not reasoning errors) dominate its incorrect predictions.

- **Kind**: model
- **Also called**: Qwen2.5VL-7B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [adaptive reasoning format selection](../methods/adaptive-reasoning-format-selection.md), [AI2D](../datasets/ai2d.md), [AQuA-RAT](../datasets/aqua-rat.md), [ChartQA](../datasets/chartqa.md), [CommonsenseQA](../datasets/commonsenseqa.md), [DynaMath](../datasets/dynamath.md), [format collapse](../concepts/format-collapse.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](../datasets/gsm8k.md), [LISA](../datasets/lisa.md), [MATH500](../datasets/math500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MM-Vet](../datasets/mm-vet.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL-3B](qwen2-5-vl-3b.md), [SAT](../datasets/sat.md), [ScienceQA](../datasets/scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [ViRL39k](../datasets/virl39k.md), [VizWiz](../datasets/vizwiz.md)

## Appears in

- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — GPRO diagnoses that visual perception failures (not reasoning errors) cause over twice as many incorrect predictions across model scales in vision-language models, then routes each generated token through one of three paths -- a fast FFN, a slow cross-attention perception path for re-examining the image, or a slow self-reflection reasoning path -- via a lightweight meta-reasoning controller trained with PPO on a multi-objective reward (task accuracy, path-cost penalty, and an uncertainty-calibration term derived from ~790K GPT-4-labeled perception-vs-reasoning failure attributions); GPRO-7B matches/beats far larger closed models and long-CoT distillation baselines while cutting response length up to 51.5%, activating slow paths sparsely (73% Fast/17% Perception/10% Reasoning) and correctly, targeting perception re-examination at high-frequency visual tokens and reasoning refinement at logical connectives.
- [VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception](../../archive/papers/2025/title-4888764f9c757f11/summary.md) — Visual Test-Time Scaling (VTTS) lets a multimodal LLM iteratively refine its perception of high-confidence spatio-temporal regions during inference, guided by its own updated textual predictions, and the resulting VideoChat-R1.5 model improves over strong baselines by 5%+ on 15+ video benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
