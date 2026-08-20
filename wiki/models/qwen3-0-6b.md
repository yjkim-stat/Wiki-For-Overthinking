# Qwen3-0.6B

<!-- auto:begin -->

A 0.6-billion-parameter Qwen model, the smallest in two of this archive's cross-scale studies and useful mainly for what it does not show. In the steering audit it is the bottom rung of a dense ladder from 0.6B to 14B, and its held-out steering effect of +9.4 with a pass rate of 0.71 is comfortably above chance -- one of the observations behind that paper's finding that no significant scaling trend survives residual-norm normalisation and held-out operating-point selection. On the theory-of-mind benchmark it sits near the bottom of a 28-model field at 58.33 average accuracy, in a study whose class means run 84.1 for proprietary models against 66.5 for open non-reasoning ones. Neither source describes the model.

- **Kind**: model
- **Also called**: Qwen3-0.6B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation steering](../methods/activation-steering.md), [benchmark design](../concepts/benchmark-design.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [class imbalance](../concepts/class-imbalance.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [cross-validation](../methods/cross-validation.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [Gemini-2.5-pro](gemini-2-5-pro.md), [Gemma-2-27B](gemma-2-27b.md), [Gemma-2-9B](gemma-2-9b.md), [GPT-5](gpt-5.md), [interpretability illusion](../concepts/interpretability-illusion.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-70B](llama-3-1-70b.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3.2-3B](llama-3-2-3b.md), [measurement invariance](../concepts/measurement-invariance.md), [operating point](../concepts/operating-point.md), [permutation test](../methods/permutation-test.md), [Phi-4](phi-4.md), [Qwen2.5-72B](qwen2-5-72b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-4B-Thinking-2507](qwen3-4b-thinking-2507.md), [Qwen3.5-2B](qwen3-5-2b.md), [Qwen3-8B](qwen3-8b.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [selection bias](../concepts/selection-bias.md), [selectivity control](../methods/selectivity-control.md), [steering vector](../methods/steering-vector.md), [test-time scaling](../concepts/test-time-scaling.md), [theory of mind](../concepts/theory-of-mind.md), [zero-shot prompting](../methods/zero-shot-prompting.md)

## Appears in

- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) — Audits four neuroscience-inspired claims about language models across 17 checkpoints from five families and 0.6B to 72B, and shows that an apparent emergence of concept steerability with scale is produced entirely by uncalibrated measurement -- raw intervention units, the readout metric, and a fixed operating point -- with correcting any one of the three removing the trend.
- [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](../../archive/papers/2026/arxiv-2608-09638/summary.md) — Turns the hidden-role game Avalon into a diagnostic instrument rather than an arena, decomposing theory of mind into a 2x2 taxonomy of perspective-constrained binary statements, and shows by probing, ground-truth injection and steering that models represent the right answer internally while failing to say it.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
