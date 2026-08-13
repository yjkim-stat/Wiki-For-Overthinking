# monosemanticity

<!-- auto:begin -->

The property of a direction in activation space responding to exactly one human-recognizable thing, as opposed to a polysemantic neuron firing across unrelated contexts. It is the target the archived sources optimize toward and the axis on which they claim success, but none measures it directly — the proxies are having a language model describe a feature and then predict its activations elsewhere, checking that a step's sparse code does not leak inherited context, and co-activation together with decoder-direction alignment used to select features for steering. Since several proxies are themselves judged by language models, a monosemanticity claim here should be read as 'a consistent description was found' rather than as an established property of the direction. Two entries complicate it from opposite sides: one shows run-to-run feature consistency is not guaranteed and argues it belongs alongside reconstruction and sparsity as a standard evaluation axis, and one finds sparse autoencoders can improve how recoverable a concept is while attenuating how much influence it actually exerts — so interpretability and causal relevance come apart.

- **Kind**: concept
- **Also called**: monosemantic features
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [causal mediation analysis](../methods/causal-mediation-analysis.md), [circuit discovery](../methods/circuit-discovery.md), [contrastive activation addition](../methods/contrastive-activation-addition.md), [GSM8K](../datasets/gsm8k.md), [Indirect Object Identification (IOI)](../datasets/indirect-object-identification-ioi.md), [information bottleneck](information-bottleneck.md), [linear probe](../methods/linear-probe.md), [linear probing](../methods/linear-probing.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [localization](localization.md), [MATH500](../datasets/math500.md), [OpenCodeInstruct](../datasets/opencodeinstruct.md), [polysemanticity](polysemanticity.md), [Pythia-410M](../models/pythia-410m.md), [Qwen2.5-0.5B](../models/qwen2-5-0-5b.md), [reproducibility](reproducibility.md), [residual stream](residual-stream.md), [self-consistency](../methods/self-consistency.md), [self-verification](self-verification.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [steering](steering.md), [superposition](superposition.md)

## Appears in

- [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](../../archive/papers/2026/arxiv-2608-05732/summary.md) — Builds multi-layer steering vectors from SAE features selected by co-activation and decoder-direction alignment, and intervenes at several points instead of one.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) — Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-99/summary.md) — Argues run-to-run feature consistency should be a standard SAE evaluation axis alongside reconstruction and sparsity, and gives a metric showing high consistency is achievable.
- [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](../../archive/papers/2026/local-d9699040f5220b4c/summary.md) — Trains a sparse autoencoder over whole reasoning steps rather than tokens, conditioning both encoder and decoder on the preceding trajectory so the sparse code carries only what the step adds, and shows that step correctness, logicality, length and first token are all linearly decodable from that code.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](../../archive/papers/2023/local-e33ecf791dfdfa8a/summary.md) — Trains sparse autoencoders on language model activations to recover an overcomplete dictionary of sparsely activating directions, and shows those directions are more interpretable and more precisely causal than neurons, PCA or ICA.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
