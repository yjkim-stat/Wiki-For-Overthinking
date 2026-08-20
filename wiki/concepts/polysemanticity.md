# polysemanticity

<!-- auto:begin -->

A single neuron or direction responding to several unrelated features, which both sources treat as the obstacle that makes raw activations hard to read. One uses it as the reason to distrust static-activation probing: because activations are saturated with polysemantic features, a linear probe learns surface lexical patterns rather than reasoning structure, so the analysis moves to cross-layer displacement instead. The other treats it as the problem a sparse autoencoder is meant to undo, decomposing activations into more numerous, more monosemantic features. The two therefore respond to the same fact in opposite ways — avoid the activations, or factor them.

- **Kind**: concept
- **Also called**: polysemantic neurons
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [activation probing](../methods/activation-probing.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [effective depth](effective-depth.md), [indirect object identification](../datasets/indirect-object-identification.md), [linear probe](../methods/linear-probe.md), [localization](localization.md), [monosemanticity](monosemanticity.md), [PCA](../methods/pca.md), [Pythia-410M](../models/pythia-410m.md), [reasoning trajectory](reasoning-trajectory.md), [residual stream](residual-stream.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](sparse-dictionary-learning.md), [superposition](superposition.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2073/summary.md) — Reads reasoning validity from layer-to-layer displacement of hidden states rather than from the states themselves, on the grounds that static activations let probes latch onto lexical surface patterns.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
