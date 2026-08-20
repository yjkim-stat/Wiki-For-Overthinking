# Shapley value

<!-- auto:begin -->

The game-theoretic allocation of a joint outcome across the parts that produced it, averaged over all orderings in which those parts could be added. Both sources use it to reason about whether a set of components combine additively, and both find the answer matters more than the exact attribution. In per-instance activation steering it underwrites the structural account of why a greedy top-K-by-single-layer-effect rule reaches the exhaustive joint optimum over layer subsets: the mid-band steering vectors are near-collinear, synergy between layers is negligible, and the remainder is padding -- so the joint value decomposes and greedy selection loses nothing. In the uncertainty work it is the attribution machinery itself, assigning conformal-prediction coverage to specific training examples and to specific reasoning steps. Neither source computes exact Shapley values at scale; between them they establish the property the archive should check first, which is whether the parts interact at all, since a near-additive system makes cheap greedy attribution correct and a strongly interacting one makes it wrong.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 2

**Related**: [activation steering](../methods/activation-steering.md), [Aya-expanse-8B](../models/aya-expanse-8b.md), [beam search](../methods/beam-search.md), [calibration](../methods/calibration.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [detection versus control](detection-versus-control.md), [GPT-2](../models/gpt-2.md), [layer selection](../methods/layer-selection.md), [Llama-3-8B-Instruct](../models/llama-3-8b-instruct.md), [logistic regression](../methods/logistic-regression.md), [PCA](../methods/pca.md), [steering vector](../methods/steering-vector.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](../../archive/papers/2026/arxiv-2608-08829/summary.md) — Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.
- [Quantifying and Understanding Uncertainty in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1511/summary.md) — Applies conformal prediction to the joint reasoning-answer structure of reasoning models, then attributes coverage to specific training examples and reasoning steps with Shapley values.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
