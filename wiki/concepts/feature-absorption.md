# feature absorption

<!-- auto:begin -->

The failure mode in which a sparse-autoencoder latent swallows a more specific feature into a more general one, so the specific concept no longer has its own direction and the dictionary's decomposition stops being the one it appears to be. Both sources here treat it as symptomatic of something deeper rather than as a bug to patch. The identifiability work lists it alongside feature splitting, run-to-run variability across seeds and widths, and residual-stream components no known variant captures, as the evidence that a decomposition may be a property of the procedure rather than of the model -- and then argues the non-identifiability behind all of them is structural, since the reconstruction-and-sparsity objective does not enforce the invariance identifiability requires. The set-level instability work supplies the sharpest measurement of the same family of problems: adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the reading of an active set as a bag of composable features. Neither source measures absorption directly; between them they place it as one symptom of dictionaries whose units are not stable under composition or re-training.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](detection-versus-control.md), [feature consistency](feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](interpretability-illusion.md), [Jaccard similarity](../methods/jaccard-similarity.md), [linear representation hypothesis](linear-representation-hypothesis.md), [logit lens](../methods/logit-lens.md), [monosemanticity](monosemanticity.md), [PCA](../methods/pca.md), [pre-registration](../methods/pre-registration.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [residual stream](residual-stream.md), [safety case](safety-case.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [superposition](superposition.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.
- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) — Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
