# Gemma-2-9B

<!-- auto:begin -->

A 9-billion-parameter Gemma model appearing in the same two studies as its larger sibling and useful mainly for the comparison between them. In the cross-family steering audit it records a held-out steering effect of +21.0, close to the 27B model's +22.9 despite three times fewer parameters -- one of the data points behind that paper's finding that steerability shows no detectable scaling trend once interventions are made residual-norm-comparable and the operating point is selected on held-out concepts. It also appears in the propositional-logic circuit analysis spanning models up to 27B. Neither source describes the model; its role here is as a rung on a within-family ladder.

- **Kind**: model
- **Also called**: Gemma-2-9B
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [bootstrap confidence intervals](../methods/bootstrap-confidence-intervals.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemma-2-27B](gemma-2-27b.md), [implicit reasoning](../concepts/implicit-reasoning.md), [interpretability illusion](../concepts/interpretability-illusion.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-70B](llama-3-1-70b.md), [Llama-3.1-8B](llama-3-1-8b.md), [Llama-3.2-1B](llama-3-2-1b.md), [Llama-3.2-3B](llama-3-2-3b.md), [localization](../concepts/localization.md), [measurement invariance](../concepts/measurement-invariance.md), [Mistral-7B](mistral-7b.md), [modularity](../concepts/modularity.md), [operating point](../concepts/operating-point.md), [Phi-4](phi-4.md), [Qwen2.5-72B](qwen2-5-72b.md), [Qwen3-0.6B](qwen3-0-6b.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [residual stream](../concepts/residual-stream.md), [selection bias](../concepts/selection-bias.md), [selectivity control](../methods/selectivity-control.md), [steering vector](../methods/steering-vector.md)

## Appears in

- [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](../../archive/papers/2026/arxiv-2608-08159/summary.md) — Audits four neuroscience-inspired claims about language models across 17 checkpoints from five families and 0.6B to 72B, and shows that an apparent emergence of concept steerability with scale is produced entirely by uncalibrated measurement -- raw intervention units, the readout metric, and a fixed operating point -- with correcting any one of the three removing the trend.
- [A Implies B: Circuit Analysis in LLMs for Propositional Logical Reasoning](../../archive/papers/2025/local-99a25b62fd9ad86c/summary.md) — Uses causal mediation analysis on a minimal propositional logic task to recover a sparse reasoning circuit in Mistral-7B and Gemma-2 up to 27B, and decomposes it into four families of attention heads that execute rule locating, rule moving, fact processing and decision making as sequential steps.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
