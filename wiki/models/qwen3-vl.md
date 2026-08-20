# Qwen3-VL

<!-- auto:begin -->

The Qwen3 vision-language line, used across 3 sources as the newer multimodal backbone. Its archived appearances: the backbone for a self-checking video agent whose supervised stage installs tool-invocation format (99.8 percent compliance against 50.6 without it) before reinforcement learning adds region-switching judgement; one of four checkpoints supported by an open vision-language interpretability library; and a subject in a university-level mathematics benchmark where a model given no image beats its own multimodal variants.

- **Kind**: model
- **Also called**: Qwen3-VL, Qwen3-VL-Instruct, Qwen3VL
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [advantage estimation](../concepts/advantage-estimation.md), [attention pattern](../concepts/attention-pattern.md), [component ablation](../methods/component-ablation.md), [construct validity](../concepts/construct-validity.md), [credit assignment](../concepts/credit-assignment.md), [error compounding](../concepts/error-compounding.md), [exploration](../concepts/exploration.md), [format compliance](../concepts/format-compliance.md), [Gemini-1.5-Pro](gemini-1-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GRPO](../methods/grpo.md), [LLaVA-1.5](llava-1-5.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [meta-evaluation](../concepts/meta-evaluation.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [outcome reward](../concepts/outcome-reward.md), [perception bottleneck](../concepts/perception-bottleneck.md), [premature convergence](../concepts/premature-convergence.md), [process reward](../concepts/process-reward.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen2.5-VL](qwen2-5-vl.md), [Qwen3-8B](qwen3-8b.md), [reproducibility](../concepts/reproducibility.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [tool learning](../concepts/tool-learning.md), [tool orchestration](../concepts/tool-orchestration.md), [Video-MME](../datasets/video-mme.md)

## Appears in

- [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](../../archive/papers/2026/arxiv-2608-07959/summary.md) — Replaces the monotonic zoom-in that tool-using video agents follow once they pick a region with a policy that self-checks each tool observation and can switch regions, and trains it with turn-level credit applied multiplicatively -- reweighting the trajectory advantage's magnitude while preserving its sign -- rather than additively.
- [Spectra: A Mechanistic Interpretability Library for Vision-Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-demo-78/summary.md) — An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.
- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) — A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
