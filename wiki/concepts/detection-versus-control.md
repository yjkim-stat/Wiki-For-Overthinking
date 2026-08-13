# detection versus control

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [attention head](attention-head.md), [causal intervention](causal-intervention.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [GPT-4.1-mini](../models/gpt-4-1-mini.md), [Inference Time Intervention](inference-time-intervention.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](linear-representation-hypothesis.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [low-rank weight ablation](../methods/low-rank-weight-ablation.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-14B](../models/qwen2-5-14b.md), [representation versus readout](representation-versus-readout.md), [residual stream](residual-stream.md), [self-repair](self-repair.md), [steering vector](../methods/steering-vector.md), [superposition](superposition.md), [TruthfulQA](../datasets/truthfulqa.md), [weight-space ablation](weight-space-ablation.md)

## What we have settled

- **Established** — How well a direction or signal detects a property licenses no claim about what intervening on it does — not the size of the effect, and not even its sign.
  - Three independent demonstrations, at three levels. Directions with near-perfect discriminability for a concept (AUC up to 0.97, aligned with its positive examples) reliably steer the model the *opposite* way, consistently across inputs rather than on a minority subset; 45 such vectors are mined across 15 model-concept pairs, and correcting their sign improves a standard steering pipeline in 27 of 30 experiments by up to 138%, with one uncorrected case steering a concept below its unsteered baseline. In an 18-model sweep a linear probe reads an entity's culture from the residual stream at 0.79 while generation emits it at 0.09, and only activation patching establishes where the pathway actually runs. And a perturbation score that provably depends on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — is matched or beaten at selection by a format-matched control that never sees the perturbations. Detection, decoding and control are three separate questions, and an experiment answering one answers neither of the others.

## Appears in

- [Inverted Detection and Control in Steering Vectors](../../archive/papers/2026/arxiv-2608-02957/summary.md) — Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.
- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
