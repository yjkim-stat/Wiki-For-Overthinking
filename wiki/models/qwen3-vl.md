# Qwen3-VL

<!-- auto:begin -->

A Qwen vision-language model, and the subject of the archive's sharpest modality-ablation result: on a university-level multimodal math benchmark it scores higher with no image input than either of its own multimodal variants or GPT-5. It is also one of four checkpoints supported by an open mechanistic-interpretability library for VLMs. The pairing is useful — one source shows the visual pathway contributing little or interfering on a reasoning benchmark, the other supplies the activation-patching and attention tooling that could say why, and no source in the archive has yet done that.

- **Kind**: model
- **Also called**: Qwen3-VL-Instruct, Qwen3VL
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [advantage estimation](../concepts/advantage-estimation.md), [attention pattern](../concepts/attention-pattern.md), [component ablation](../methods/component-ablation.md), [construct validity](../concepts/construct-validity.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [exploration](../concepts/exploration.md), [format compliance](../concepts/format-compliance.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GRPO](../methods/grpo.md), [LLaVA-1.5](llava-1-5.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [meta-evaluation](../concepts/meta-evaluation.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [outcome reward](../concepts/outcome-reward.md), [perception bottleneck](../concepts/perception-bottleneck.md), [premature convergence](../concepts/premature-convergence.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-VL](qwen2-5-vl.md), [reproducibility](../concepts/reproducibility.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md), [Video-MME](../datasets/video-mme.md)

## Appears in

- [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](../../archive/papers/2026/arxiv-2608-07959/summary.md) — Replaces the monotonic zoom-in that tool-using video agents follow once they pick a region with a policy that self-checks each tool observation and can switch regions, and trains it with turn-level credit applied multiplicatively -- reweighting the trajectory advantage's magnitude while preserving its sign -- rather than additively.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) — A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
