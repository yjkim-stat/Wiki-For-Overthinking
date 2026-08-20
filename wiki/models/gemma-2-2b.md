# Gemma-2-2B

<!-- auto:begin -->

A 2-billion-parameter Gemma model used in both sources as a mid-sized interpretability test-bed. In the tiled-SVD work it is the only model, the setting in which interpretable units are extracted directly from weight matrices and judged by a pre-registered suite -- including the depth curve on which agreement between what an unembedding lens predicts and what steering does runs from about zero in the earliest layers to roughly 0.91 at the final one. In the Koopman identifiability work it is the middle of three models, where the spectrum converges but does not attain the predicted rate (-0.329 against a predicted -0.5, with the largest model reaching -0.506), and where the sparse-autoencoder invariance gap sits at 3.1 times the spectral residual. Neither source describes the model; both chose it as small enough to instrument exhaustively and large enough not to be a toy.

- **Kind**: model
- **Also called**: Gemma-2-2B
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [feature absorption](../concepts/feature-absorption.md), [feature consistency](../concepts/feature-consistency.md), [GPT-2 small](gpt-2-small.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](../concepts/interpretability-illusion.md), [logit lens](../methods/logit-lens.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](../methods/pca.md), [pre-registration](../methods/pre-registration.md), [Qwen3-8B-Base](qwen3-8b-base.md), [residual stream](../concepts/residual-stream.md), [ridge regression](../methods/ridge-regression.md), [safety case](../concepts/safety-case.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [WikiText-2](../datasets/wikitext-2.md)

## Appears in

- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
