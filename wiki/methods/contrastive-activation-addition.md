# contrastive activation addition

<!-- auto:begin -->

Adding a direction computed from the difference between activations on contrastive prompt pairs, at inference time, to shift a model's behaviour. Both sources treat it as the baseline whose limitation motivates them, and locate that limitation in the same place — a single aggregate direction applied at one site. One replaces the fixed single-layer intervention with sparse-feature-derived vectors applied at multiple points, on the grounds that one direction imposed across semantically diverse inputs has an effect that often fails to persist across layers. The other shows the failure is worse than insufficiency: a direction can be highly discriminative for a concept and aligned with its positive examples while steering reliably in the opposite direction, so the sign of the intervention cannot be read off the direction's discriminability at all.

- **Kind**: method
- **Also called**: CAA, Contrastive Activation Addition, contrastive activation steering
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [activation steering](activation-steering.md), [attention head](../concepts/attention-head.md), [causal intervention](../concepts/causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [circuit discovery](circuit-discovery.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-of-means probe](difference-of-means-probe.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Inference Time Intervention](../concepts/inference-time-intervention.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [logistic regression](logistic-regression.md), [MMLU](../datasets/mmlu.md), [monitorability](../concepts/monitorability.md), [monosemanticity](../concepts/monosemanticity.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [randomized control](../concepts/randomized-control.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-repair](../concepts/self-repair.md), [sparse autoencoder](sparse-autoencoder.md), [steering](../concepts/steering.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Tampers with a model's own reasoning trace in two directions — toward an equivalent safe option and toward an unsafe one — and finds the models that follow their traces most faithfully are the ones that follow them into harm, with the two behaviours carried by two distinct, anti-correlated residual-stream directions that can be steered apart.
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) — Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.
- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
