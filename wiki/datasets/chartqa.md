# ChartQA

<!-- auto:begin -->

ChartQA (chart-based visual question answering) is used in these sources as a multimodal out-of-domain evaluation benchmark: ARM2 reports accuracy and token-efficiency results on it among its twelve in-/out-of-domain text and multimodal benchmarks, and RECAP includes it among the general-capability benchmarks used to test whether reasoning-focused RL fine-tuning causes forgetting in vision-language models.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning format selection](../methods/adaptive-reasoning-format-selection.md), [AI2D](ai2d.md), [AQuA-RAT](aqua-rat.md), [CommonsenseQA](commonsenseqa.md), [format collapse](../concepts/format-collapse.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO (baseline)](../methods/grpo-baseline.md), [GSM8K](gsm8k.md), [LISA](lisa.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [SAT](sat.md), [ScienceQA](scienceqa.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [VizWiz](vizwiz.md)

## Appears in

- [ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1365/summary.md) — ARM2 extends adaptive reasoning-format selection (Direct Answer, Short CoT, Code-Text, Code-Exec, Long CoT) to multimodal (vision) inputs and lets executable code substitute for lengthy chain-of-thought on tasks with verifiable computation, trained via GRPO-alp (a format-collapse-resistant, length-aware GRPO variant), reducing token usage over 70% versus standard GRPO while matching its accuracy across six in-domain and six out-of-domain text and multimodal benchmarks.
- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
