# contrastive activation addition

<!-- auto:begin -->

Adding a direction computed from the difference between activations on contrastive prompt pairs, at inference time, to shift a model's behaviour. Both sources treat it as the baseline whose limitation motivates them, and locate that limitation in the same place — a single aggregate direction applied at one site. One replaces the fixed single-layer intervention with sparse-feature-derived vectors applied at multiple points, on the grounds that one direction imposed across semantically diverse inputs has an effect that often fails to persist across layers. The other shows the failure is worse than insufficiency: a direction can be highly discriminative for a concept and aligned with its positive examples while steering reliably in the opposite direction, so the sign of the intervention cannot be read off the direction's discriminability at all.

- **Kind**: method
- **Also called**: CAA, Contrastive Activation Addition, contrastive activation steering
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [attention head](../concepts/attention-head.md), [causal intervention](../concepts/causal-intervention.md), [circuit discovery](circuit-discovery.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [monosemanticity](../concepts/monosemanticity.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [representation versus readout](../concepts/representation-versus-readout.md), [sparse autoencoder](sparse-autoencoder.md), [steering](../concepts/steering.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
