# ablation

<!-- auto:begin -->

Removing a component -- a direction, a latent, a weight subset -- and reading the change in behaviour as evidence of what that component did. Both sources use it as the causal step that follows an identification step, and both find the step is not automatic. One shows a dictionary's directions are more precisely causal than individual neurons under ablation, which is the case for the method; the other is the case against relying on a named direction, since ablating the standard refusal direction from a steering vector recovers almost none of the safety it lost, and the direction that must be removed has to be learned against the intervention's own objective instead. Elsewhere in this archive the same instrument is contrasted with patching, which measures a contrast between two runs rather than the absolute level ablation reports.

- **Kind**: method
- **Also called**: weight-space ablation, zero ablation
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 3

**Related**: [activation patching](activation-patching.md), [activation steering](activation-steering.md), [causal intervention](../concepts/causal-intervention.md), [causal mediation analysis](causal-mediation-analysis.md), [contrastive activation addition](contrastive-activation-addition.md), [detection versus control](../concepts/detection-versus-control.md), [indirect object identification](../datasets/indirect-object-identification.md), [jailbreak](../concepts/jailbreak.md), [KL divergence](../concepts/kl-divergence.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [LLM-as-a-judge](llm-as-a-judge.md), [logit lens](logit-lens.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](pca.md), [polysemanticity](../concepts/polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-14B-Instruct](../models/qwen2-5-14b-instruct.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [representation versus readout](../concepts/representation-versus-readout.md), [residual stream](../concepts/residual-stream.md), [ridge regression](ridge-regression.md), [sparse autoencoder](sparse-autoencoder.md), [steering vector](steering-vector.md), [superposition](../concepts/superposition.md), [the Pile](../datasets/the-pile.md), [XSTest](../datasets/xstest.md)

## Appears in

- [Finding Usable Weight Mechanisms with Tiled SVD](../../archive/papers/2026/arxiv-2608-06969/summary.md) — Extracts interpretable units directly from a transformer's weight matrices by column-tiled SVD, so a unit's identity is the weight rule itself rather than an atom of a separately trained dictionary, and judges them with a pre-registered suite whose central move is refusing a metric that a trivial baseline would win.
- [Safety Cost of Steering Vectors Is Separable and Reducible](../../archive/papers/2026/arxiv-2608-08383/summary.md) — Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
