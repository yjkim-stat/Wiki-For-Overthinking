# feature consistency

<!-- auto:begin -->

Whether independently trained sparse autoencoders recover the same features from the same activations, proposed by one source as an evaluation axis that should be reported alongside reconstruction and sparsity rather than left implicit. That source supplies an assignment-based metric -- features are matched between runs before being compared, which is what makes it invariant to arbitrary feature ordering -- with theoretical grounding in an idealised TopK setting, synthetic validation against ground-truth recovery on a model organism, and the empirical result that consistency around 0.80 is achievable with the right architectural choices. The identifiability source reframes the same phenomenon: the run-to-run variability is structural rather than algorithmic, because the reconstruction-and-sparsity objective does not enforce the invariance that identifiability requires, so no amount of better training removes it. The two sit in tension worth recording. One shows consistency can be raised to 0.80 by architecture; the other shows that adding an explicit invariance penalty improves identifiability by 41 percent while cross-seed feature agreement moves the wrong way -- so consistency and identifiability are not the same quantity, and a method can improve one while degrading the other.

- **Kind**: concept
- **Also called**: run-to-run consistency
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](detection-versus-control.md), [feature absorption](feature-absorption.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](interpretability-illusion.md), [logit lens](../methods/logit-lens.md), [monosemanticity](monosemanticity.md), [PCA](../methods/pca.md), [pre-registration](../methods/pre-registration.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [reproducibility](reproducibility.md), [residual stream](residual-stream.md), [safety case](safety-case.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [superposition](superposition.md)

## Appears in

- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.
- [Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-99/summary.md) — Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
