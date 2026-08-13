# weight-space ablation

<!-- auto:begin -->

Intervening on the parameters that generate every forward pass, as against on the activations realized in one. Both sources are one research programme, and their contribution is to make the difference from activation patching exact rather than cautionary: patching moves the readout by a component's donor-receiver contrast, this moves it by the component's absolute level at the receiver, and neither bounds the other. Two consequences are established. Inside an idealized additive model there is an if-and-only-if criterion for such an edit to collapse a conditional onto one branch, together with the polarity of the resulting error — and empirically two *nested* edited subsets collapse the same trained network onto opposite branches, which the idealized model forbids and which therefore locates a violated hypothesis. On a real pretrained model the gap against patching measures 0.224 to 0.852 across five instances of one circuit, never small.

- **Kind**: method
- **Also called**: parameter ablation, weight editing
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [causal tracing](causal-tracing.md), [circuit analysis](circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [low-rank weight ablation](low-rank-weight-ablation.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [residual stream](../concepts/residual-stream.md), [self-repair](../concepts/self-repair.md), [superposition](../concepts/superposition.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
