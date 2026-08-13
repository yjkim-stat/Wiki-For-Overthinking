# GPT-5

<!-- auto:begin -->

An OpenAI frontier model, present in the archive as the ceiling that benchmarks are calibrated against — and beaten in both appearances. On a university-level multimodal math benchmark it is surpassed by Qwen3-VL given no image at all, which the source reads as evidence that visual input contributes little and can interfere. On a contamination-resistant inductive reasoning benchmark it stays below 5% on hard long-cascade instances even under expensive test-time scaling. Both results are used to argue that the benchmark is measuring something real rather than saturating, so GPT-5's presence here marks headroom rather than progress.

- **Kind**: model
- **Also called**: GPT5
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [adversarial robustness](../concepts/adversarial-robustness.md), [benchmark contamination](../concepts/benchmark-contamination.md), [calibration](../methods/calibration.md), [compositional generalization](../concepts/compositional-generalization.md), [construct validity](../concepts/construct-validity.md), [GPT-4o](gpt-4o.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [meta-evaluation](../concepts/meta-evaluation.md), [MMLU](../datasets/mmlu.md), [multimodal reasoning](../concepts/multimodal-reasoning.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [perception bottleneck](../concepts/perception-bottleneck.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3-VL](qwen3-vl.md), [routing](../concepts/routing.md), [sample complexity](../concepts/sample-complexity.md), [superposition](../concepts/superposition.md), [test-time compute](../concepts/test-time-compute.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2198/summary.md) — A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.
- [PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-432/summary.md) — An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
