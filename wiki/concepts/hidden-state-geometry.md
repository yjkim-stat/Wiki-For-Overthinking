# hidden-state geometry

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [adversarial robustness](adversarial-robustness.md), [calibration](../methods/calibration.md), [DPO](../methods/dpo.md), [GPT-4o](../models/gpt-4o.md), [GPT-5](../models/gpt-5.md), [GSM8K](../datasets/gsm8k.md), [HumanEval+](../datasets/humaneval.md), [linear probe](../methods/linear-probe.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [MATH-500](../datasets/math-500.md), [MMLU](../datasets/mmlu.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [preference optimization](../methods/preference-optimization.md), [Qwen3-1.7B](../models/qwen3-1-7b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [reasoning trajectory](reasoning-trajectory.md), [routing](routing.md), [sample complexity](sample-complexity.md), [self-consistency](../methods/self-consistency.md), [superposition](superposition.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning](../../archive/papers/2026/arxiv-2608-01014/summary.md) — Scores unlabeled reasoning trajectories by how their mean-pooled hidden states connect to correct and incorrect reference point clouds built from a small labeled set, and uses that score to pick the concrete chosen and rejected responses inside answer clusters that self-consistency has already separated.
- [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](../../archive/papers/2026/arxiv-2608-02415/summary.md) — Compares two training-free intent classifiers built from summary statistics of prefill-time activations against trained heads on the same features, and finds the trade-off is not accuracy but where each fails — trained heads win fine-grained distinctions, statistical ones give better uncertainty on mixed prompts and survive adversarial rephrasing that collapses the trained heads to zero.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
