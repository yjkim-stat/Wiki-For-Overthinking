# self-repair

<!-- auto:begin -->

A network compensating downstream for a component that has been removed, so an ablation-based importance score is measured on a network that has already partly repaired the damage. Both sources invoke it as the standing reason ablation and patching are expected to disagree — and then establish that the disagreement does not need it. Their construction produces matched pairs on which every single-carrier patch flips the decision while no single-carrier ablation does, with no repair mechanism present at all: the two interventions measure a carrier's contrast and its absolute level respectively, and those come apart in a redundantly coded network by arithmetic. So this phenomenon is one route to the mismatch rather than its explanation, which matters because a result attributed to it may instead be the identity, and the two call for different remedies.

- **Kind**: concept
- **Also called**: Hydra effect, self-healing
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 3

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [causal intervention](causal-intervention.md), [causal tracing](../methods/causal-tracing.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [circuit analysis](../methods/circuit-analysis.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [DeepSeek-R1-Distill-Llama-70B](../models/deepseek-r1-distill-llama-70b.md), [detection versus control](detection-versus-control.md), [difference-of-means probe](../methods/difference-of-means-probe.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](interpretability-illusion.md), [linear probe](../methods/linear-probe.md), [low-rank weight ablation](../methods/low-rank-weight-ablation.md), [MMLU](../datasets/mmlu.md), [monitorability](monitorability.md), [permutation test](../methods/permutation-test.md), [pre-registration](../methods/pre-registration.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen3-32B](../models/qwen3-32b.md), [Qwen3-8B](../models/qwen3-8b.md), [QwQ-32B](../models/qwq-32b.md), [residual stream](residual-stream.md), [safety alignment](safety-alignment.md), [steering vector](../methods/steering-vector.md), [superposition](superposition.md), [weight-space ablation](../methods/weight-space-ablation.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.
- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Tampers with a model's own reasoning trace in two directions — toward an equivalent safe option and toward an unsafe one — and finds the models that follow their traces most faithfully are the ones that follow them into harm, with the two behaviours carried by two distinct, anti-correlated residual-stream directions that can be steered apart.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
