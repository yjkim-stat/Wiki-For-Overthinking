# interpretability illusion

<!-- auto:begin -->

A finding that looks like a property of the model but is a property of the method that found it. Both sources here give it a formal footing rather than a cautionary anecdote. The ablation-theory work shows that patching and weight-space ablation measure two different quantities -- a carrier's donor-receiver contrast against its absolute level at the receiver -- which neither bounds, and constructs matched pairs on which every single-carrier patch flips the decision while no single-carrier ablation does, with no repair mechanism involved, so the disagreement is not the Hydra effect under another name. The identifiability work names the general condition: mechanistic interpretability has had no theorem asserting that a discovered structure is an invariant of the model, and the sparse-autoencoder evidence -- materially different features across seeds and widths, absorption, splitting, uncaptured components -- is what makes the question empirical rather than philosophical. Its answer is that non-identifiability is structural, and its dissociation theorem gives a stronger version of the same worry: in the non-normal regime these models occupy, the identifiable object and the human-legible object cannot be the same object, so a decomposition can be reliable or readable but not obviously both.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [causal intervention](causal-intervention.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](detection-versus-control.md), [feature absorption](feature-absorption.md), [feature consistency](feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [indirect object identification](../datasets/indirect-object-identification.md), [logit lens](../methods/logit-lens.md), [low-rank weight ablation](../methods/low-rank-weight-ablation.md), [PCA](../methods/pca.md), [permutation test](../methods/permutation-test.md), [pre-registration](../methods/pre-registration.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [residual stream](residual-stream.md), [safety case](safety-case.md), [self-repair](self-repair.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [superposition](superposition.md), [weight-space ablation](../methods/weight-space-ablation.md)

## Appears in

- [A Theory of Conditional Collapse under Low-Rank Weight-Space Ablations: I. The Single-Block Theory and Synthetic Validation](../../archive/papers/2026/arxiv-2608-03620/summary.md) — Proves that activation patching and weight-space ablation measure two different quantities — a carrier's donor-receiver contrast versus its absolute level at the receiver — which neither bounds, gives an exact if-and-only-if criterion for when ablating a subset collapses a conditional onto one branch, and then withdraws its own clean empirical separation when it fails out of sample.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
