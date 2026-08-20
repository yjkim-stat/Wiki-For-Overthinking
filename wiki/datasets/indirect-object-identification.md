# indirect object identification

<!-- auto:begin -->

A small synthetic task -- completing a sentence with the name that was not the subject -- and the archive's standard testbed for causal methods rather than a capability benchmark. All three sources use it that way: as the task where an ablation-interaction theorem is checked, as the setting where the methodological choices in activation patching are varied and shown to change the answer, and as one of the tasks where dictionary directions are compared against neurons for causal precision. Its value is that the correct circuit is known well enough that a method can be wrong in a visible way.

- **Kind**: dataset
- **Also called**: IOI, Indirect Object Identification (IOI)
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 4

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [causal intervention](../concepts/causal-intervention.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [feature absorption](../concepts/feature-absorption.md), [feature consistency](../concepts/feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [GPT-2 XL](../models/gpt-2-xl.md), [GPT-J 6B](../models/gpt-j-6b.md), [identifiability](../concepts/identifiability.md), [interpretability illusion](../concepts/interpretability-illusion.md), [localization](../concepts/localization.md), [logit lens](../methods/logit-lens.md), [low-rank weight ablation](../methods/low-rank-weight-ablation.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](../methods/pca.md), [polysemanticity](../concepts/polysemanticity.md), [pre-registration](../methods/pre-registration.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [residual stream](../concepts/residual-stream.md), [safety case](../concepts/safety-case.md), [self-repair](../concepts/self-repair.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [superposition](../concepts/superposition.md), [the Pile](the-pile.md), [weight-space ablation](../methods/weight-space-ablation.md)

## Appears in

- [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](../../archive/papers/2026/arxiv-2608-03629/summary.md) — Extends a single-block interaction theorem to ablated subsets spanning many layers, isolates the cross-layer remainder as an exact double integral rather than bounding it, supplies the one missing closed-form ingredient (a local attention Jacobian bound, verified without a violation on a real 1.5B model), and tests the whole picture on an emergent circuit nobody designed for it — reporting the mixed outcome as mixed.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.
- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
