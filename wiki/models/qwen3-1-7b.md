# Qwen3-1.7B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [adversarial robustness](../concepts/adversarial-robustness.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [BBH](../datasets/bbh.md), [calibration](../methods/calibration.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-R1-Distill-Llama-8B](deepseek-r1-distill-llama-8b.md), [GPQA](../datasets/gpqa.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](../concepts/hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [MMLU-Pro](../datasets/mmlu-pro.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [overthinking](../concepts/overthinking.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [routing](../concepts/routing.md), [sample complexity](../concepts/sample-complexity.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](../concepts/superposition.md), [uncertainty quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [The Tell-Tale Norm: L2 Magnitude as a Signal for Reasoning Dynamics in Large Language Models](../../archive/papers/2026/local-f92e5f936a3c7422/summary.md) — Argues that the L2 norm of a hidden state is a training-free proxy for how hard a model is reasoning at that layer and token, proves it bounds the activation of SAE-identified reasoning features, and uses norm peaks to decide where to recurse a layer, where to steer, and which sampled response to keep.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
