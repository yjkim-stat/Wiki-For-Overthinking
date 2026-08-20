# the Pile

<!-- auto:begin -->

A large general-purpose text corpus used across these four sources as the substrate a method is fitted or measured on rather than as an object of study. It supplies the activations sparse autoencoders are trained on -- dictionaries in the foundational paper come from the first 10,000 elements, about 7 million activations -- and the same role recurs in the set-level instability work that takes the set of active latents as its unit and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active. It is also one of the corpora over which dense trained lenses are fitted at every layer and hookpoint. Its fourth appearance is different in kind: in the contamination-detectability work it figures in an analysis casting benchmark contamination auditing as sparse-mixture detection, where what matters about a pretraining corpus is its size relative to the contaminated fraction. No source here describes its composition.

- **Kind**: dataset
- **Also called**: Pile
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 4

**Related**: [2WikiMultiHopQA](2wikimultihopqa.md), [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [ARC-Easy](arc-easy.md), [benchmark contamination](../concepts/benchmark-contamination.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](../concepts/detection-versus-control.md), [feature absorption](../concepts/feature-absorption.md), [GPT-2](../models/gpt-2.md), [GPT-2 XL](../models/gpt-2-xl.md), [importance sampling](../methods/importance-sampling.md), [indirect object identification](indirect-object-identification.md), [Jaccard similarity](../methods/jaccard-similarity.md), [KL divergence](../methods/kl-divergence.md), [knowledge distillation](../methods/knowledge-distillation.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](../concepts/linear-representation-hypothesis.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [Llama-3.3-70B](../models/llama-3-3-70b.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [low-rank approximation](../methods/low-rank-approximation.md), [membership inference](../concepts/membership-inference.md), [monosemanticity](../concepts/monosemanticity.md), [PCA](../methods/pca.md), [permutation test](../methods/permutation-test.md), [polysemanticity](../concepts/polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [residual stream](../concepts/residual-stream.md), [SciQ](sciq.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md), [superposition](../concepts/superposition.md), [tuned lens](../methods/tuned-lens.md), [WikiText-2](wikitext-2.md)

## Appears in

- [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](../../archive/papers/2026/arxiv-2608-07914/summary.md) — Casts benchmark contamination auditing as sparse-mixture detection, proves that detectability is governed by the single quantity alpha*rho*sqrt(m), and shows empirically that the resulting power predictions transport while the sample-size budgets derived from them do not.
- [Interpreting Language Model Hidden States at Scale](../../archive/papers/2026/arxiv-2608-10260/summary.md) — Makes trained lenses cheap enough to attach densely across a whole model — every layer, and residual, attention and MLP alike — and then uses that coverage to show that where a behaviour is most visible is not where intervening on it works best.
- [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](../../archive/papers/2026/arxiv-2608-11197/summary.md) — Takes the set of active sparse-autoencoder latents as the unit of analysis and finds that adding a semantically compatible adjective to a noun deactivates 20 to 60 percent of the latents the noun alone had active, which contradicts the bag-of-features reading those sets are usually given.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
