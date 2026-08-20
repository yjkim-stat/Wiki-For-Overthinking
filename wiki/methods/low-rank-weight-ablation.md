# low-rank weight ablation

<!-- auto:begin -->

Editing a network's parameters by projecting a low-dimensional subspace out of them, as against altering activations inside one forward pass. Both sources are one research programme and treat it as an operator to be characterized rather than a tool to be used. The key identity is that this edit is *exactly* term deletion in the residual stream — projecting a unit direction out of a component's output projection removes one write-in term precisely, not approximately — which is what lets the analysis proceed in output space rather than in weight space. What is *not* an identity, and is the subject of both papers' hardest results, is the further assumption that deleting one component's term leaves every other component's term unchanged: it fails whenever an ablated head shares a block with its own MLP, and fails generically whenever the ablated set touches two or more layers at all.

- **Kind**: method
- **Also called**: low-rank ablation, weight projection
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [causal tracing](causal-tracing.md), [circuit analysis](circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](../concepts/interpretability-illusion.md), [permutation test](permutation-test.md), [pre-registration](pre-registration.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [residual stream](../concepts/residual-stream.md), [self-repair](../concepts/self-repair.md), [superposition](../concepts/superposition.md), [weight-space ablation](weight-space-ablation.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
