# difference-of-means probe

<!-- auto:begin -->

Classifying by the sign of a projection onto the difference of class means -- the simplest probe in the archive and the one most steering work reuses as its direction. Across 3 sources its recurring result is that its classification accuracy and its usefulness for intervention are different things: one study reports it as slightly the weakest of four classifiers on the same data and explicitly declines to select its intervention by classification accuracy, and another finds directions of this family that discriminate well and steer backwards. The corpus's practical note is that where this probe is used both to detect and to steer, the two roles must be validated separately, and the archive's inverted-vector material is what makes that non-optional.

- **Kind**: method
- **Also called**: MM difference direction, diff-in-means probe, mean-difference probe
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation steering](activation-steering.md), [attention head](../concepts/attention-head.md), [causal intervention](causal-intervention.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [construct validity](../concepts/construct-validity.md), [contrastive activation addition](contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [detection versus control](../concepts/detection-versus-control.md), [difference-in-means direction](difference-in-means-direction.md), [Gemma-3-12B](../models/gemma-3-12b.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [LLM-as-a-judge](llm-as-a-judge.md), [logistic regression](logistic-regression.md), [MMLU](../datasets/mmlu.md), [monitorability](../concepts/monitorability.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [randomized control](../concepts/randomized-control.md), [representation versus readout](../concepts/representation-versus-readout.md), [safety alignment](../concepts/safety-alignment.md), [self-repair](../concepts/self-repair.md), [steering vector](steering-vector.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Tampers with a model's own reasoning trace in two directions — toward an equivalent safe option and toward an unsafe one — and finds the models that follow their traces most faithfully are the ones that follow them into harm, with the two behaviours carried by two distinct, anti-correlated residual-stream directions that can be steered apart.
- [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](../../archive/papers/2026/arxiv-2608-03892/summary.md) — Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
