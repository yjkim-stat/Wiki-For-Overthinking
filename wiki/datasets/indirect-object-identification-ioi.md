# Indirect Object Identification (IOI)

<!-- auto:begin -->

A synthetic task in which a model must complete a sentence such as 'When John and Mary went to the office, John gave a book to ___' with the indirect object, chosen because it isolates a simple, previously mapped behaviour implemented by an identified set of attention heads. Both sources use it as a testbed rather than a target: one measures whether learned sparse dictionary features localize the behaviour more precisely than PCA components, and the other uses it to show that different corruption methods and evaluation metrics recover different subsets of the known circuit. The second source reports that even under its recommended settings the recovered circuit is far from complete, with critical misses such as the Name Mover heads.

- **Kind**: dataset
- **Also called**: IOI, indirect object identification
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 2

**Related**: [activation patching](../methods/activation-patching.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [causal tracing](../methods/causal-tracing.md), [circuit analysis](../methods/circuit-analysis.md), [GPT-J 6B](../models/gpt-j-6b.md), [localization](../concepts/localization.md), [monosemanticity](../concepts/monosemanticity.md), [polysemanticity](../concepts/polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [residual stream](../concepts/residual-stream.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](../concepts/superposition.md)

## Appears in

- [Towards Best Practices of Activation Patching in Language Models: Metrics and Methods](../../archive/papers/2024/local-956614b275995bc4/summary.md) — Systematically varies the methodological choices in activation patching — how prompts are corrupted, which metric scores the patching effect, and whether layers are patched singly or in sliding windows — and shows each choice can change which model components a study concludes are important.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
