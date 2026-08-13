# representation versus readout

<!-- auto:begin -->

The distinction between what a model's internal state contains and what its output does with it — the archive's name for a gap both sources measure directly rather than infer. One finds cultural identity linearly readable from the residual stream at 0.79 while generation emits it at 0.09, with the decoding-suppressed cell the largest in all 18 models tested and activation patching locating the failure in the last quarter of layers. The other pushes the distinction further than encoding: a direction can detect a concept nearly perfectly and, when steered along, produce the opposite behaviour, so readout can invert rather than merely drop what representation holds. Together they establish that detection, decoding and control are three separate questions and an experiment answering one answers neither of the others.

- **Kind**: concept
- **Also called**: detection versus control, encoding versus decoding
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [attention head](attention-head.md), [causal intervention](causal-intervention.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [Gemma-4-26B-A4B-it](../models/gemma-4-26b-a4b-it.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](linear-representation-hypothesis.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-3B-Instruct](../models/llama-3-2-3b-instruct.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [logit lens](../methods/logit-lens.md), [Phi-4](../models/phi-4.md), [principal component analysis](../methods/principal-component-analysis.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3.6-35B-A3B](../models/qwen3-6-35b-a3b.md), [residual stream](residual-stream.md), [scaling laws](scaling-laws.md), [steering vector](../methods/steering-vector.md), [TruthfulQA](../datasets/truthfulqa.md)

## What we have settled

- **Established** — How well a direction or signal detects a property licenses no claim about what intervening on it does — not the size of the effect, and not even its sign.
  - Three independent demonstrations, at three levels. Directions with near-perfect discriminability for a concept (AUC up to 0.97, aligned with its positive examples) reliably steer the model the *opposite* way, consistently across inputs rather than on a minority subset; 45 such vectors are mined across 15 model-concept pairs, and correcting their sign improves a standard steering pipeline in 27 of 30 experiments by up to 138%, with one uncorrected case steering a concept below its unsteered baseline. In an 18-model sweep a linear probe reads an entity's culture from the residual stream at 0.79 while generation emits it at 0.09, and only activation patching establishes where the pathway actually runs. And a perturbation score that provably depends on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — is matched or beaten at selection by a format-matched control that never sees the perturbations. Detection, decoding and control are three separate questions, and an experiment answering one answers neither of the others.

## Appears in

- [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](../../archive/papers/2026/arxiv-2608-02486/summary.md) — Builds a parallel entity grid of 27 folk-narrative motifs across 10 cultures and instruments 18 models with probing, logit lens, activation patching and generation, finding that the residual stream separates cultures cleanly in every model while the readout collapses onto Greco-Roman defaults — so the failure is at the decoder, not the encoder.
- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
