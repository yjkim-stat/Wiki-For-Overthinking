# Pythia-410M

<!-- auto:begin -->

A 410M model from the Pythia suite, chosen in these sources for its open training checkpoints and small size. It is the model in which sparse dictionary features are shown to localize indirect object identification more tightly than PCA components, and it recurs in circuit-level arithmetic analysis. Its size is the standing caveat: interpretability results established here are a long way from the reasoning models the rest of this archive studies.

- **Kind**: model
- **Also called**: Pythia-410M
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [benchmark contamination](../concepts/benchmark-contamination.md), [causal analysis](../methods/causal-analysis.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [circuit analysis](../methods/circuit-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [generalization](../concepts/generalization.md), [GPT-J 6B](gpt-j-6b.md), [indirect object identification](../datasets/indirect-object-identification.md), [Llama-3.1-8B](llama-3-1-8b.md), [localization](../concepts/localization.md), [membership inference](../methods/membership-inference.md), [memorization](../concepts/memorization.md), [modularity](../concepts/modularity.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](../methods/pca.md), [permutation test](../methods/permutation-test.md), [polysemanticity](../concepts/polysemanticity.md), [residual stream](../concepts/residual-stream.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md)

## Appears in

- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics](../../archive/papers/2025/local-26fdb25b9d157d04/summary.md) — Reverse-engineers the arithmetic circuit down to individual neurons and finds it is neither a learned algorithm nor memorization, but an unordered collection of sparse heuristic neurons that each fire on a numerical input pattern and vote for corresponding answers.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
