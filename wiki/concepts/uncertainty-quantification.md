# uncertainty quantification

<!-- auto:begin -->

Attaching a defensible measure of confidence to a model's output, which the two sources approach with opposite priorities. One demands statistical guarantees, applying conformal prediction to the joint reasoning-answer structure rather than to the answer alone on the grounds that existing methods ignore the logical connection between trace and answer, and then attributes coverage back to specific training examples and reasoning steps using Shapley values. The other shows a confidence signal can be worthless as a probability and excellent as a ranking: a diffusion language model reaches 31.2% expected calibration error on mathematical reasoning while achieving 0.826 AUROC against 0.611 for comparable single-pass autoregressive baselines. The pair separates two properties commonly conflated — calibrated magnitude and correct ordering — which matters because threshold-gated methods need the first and selection methods need only the second.

- **Kind**: concept
- **Also called**: UQ, confidence estimation, uncertainty estimation
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [adversarial robustness](adversarial-robustness.md), [answer stabilization](answer-stabilization.md), [calibration](../methods/calibration.md), [cosine similarity](../methods/cosine-similarity.md), [expected calibration error](expected-calibration-error.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [hidden-state geometry](hidden-state-geometry.md), [HumanEval+](../datasets/humaneval.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [routing](routing.md), [sample complexity](sample-complexity.md), [superposition](superposition.md)

## Appears in

- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.
- [Quantifying and Understanding Uncertainty in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1511/summary.md) — Applies conformal prediction to the joint reasoning-answer structure of reasoning models, then attributes coverage to specific training examples and reasoning steps with Shapley values.
- [The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-2142/summary.md) — Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
