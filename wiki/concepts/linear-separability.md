# linear separability

<!-- auto:begin -->

The precondition that makes a concept readable by a linear probe or a concept vector: that the activations carrying the concept can be split from those that do not by a hyperplane. Both sources here treat it as a property of the representation as presented to the probe rather than a fixed fact about the model, and both engineer it rather than merely measuring it -- the L2 speaking assessment paper notes that Concept Activation Vectors assume linear separability, which is less likely in complex neural embeddings, and responds by learning CAVs in a sparse autoencoder latent space and mapping them back to activation space; the hallucination-detection paper trains a LoRA adapter that restructures a low-dimensional grounding signal into a shift-stable linear geometry, verified by transfer and by cross-trajectory patching. On what improving it buys, the two sources point opposite ways: the SAE route improves linear recoverability while attenuating activation-space sensitivity, especially in low-dimensional layers, whereas the adapter's restructuring is what makes the detector able to act. Read together they say separability and causal influence are distinct axes, and that a method can raise one while lowering the other.

- **Kind**: concept
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md)
- **Sources**: 4

**Related**: [activation patching](../methods/activation-patching.md), [activation steering](../methods/activation-steering.md), [calibration](../methods/calibration.md), [detection versus control](detection-versus-control.md), [difference-in-means direction](../methods/difference-in-means-direction.md), [Gemma-4-31B-it](../models/gemma-4-31b-it.md), [hallucination](hallucination.md), [linear probe](../methods/linear-probe.md), [linear representation hypothesis](linear-representation-hypothesis.md), [Llama-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [localization](localization.md), [logistic regression](../methods/logistic-regression.md), [logit lens](../methods/logit-lens.md), [LoRA](../methods/lora.md), [monosemanticity](monosemanticity.md), [PCA](../methods/pca.md), [predictive entropy](predictive-entropy.md), [Qwen3-4B](../models/qwen3-4b.md), [ReAct](../methods/react.md), [residual stream](residual-stream.md), [ridge regression](../methods/ridge-regression.md), [selectivity control](../methods/selectivity-control.md), [semantic entropy](../methods/semantic-entropy.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [superposition](superposition.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [TF-IDF](../methods/tf-idf.md), [tuned lens](../methods/tuned-lens.md), [uncertainty quantification](uncertainty-quantification.md)

## Appears in

- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) — Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering](../../archive/papers/2026/arxiv-2608-06638/summary.md) — Applies linear probing, the logit and tuned lenses, activation patching and difference-in-means steering to two public text-to-MIDI models, and shows that the architecture of the conditioning pathway determines which steering strategy stays stable.
- [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](../../archive/papers/2026/arxiv-2608-07208/summary.md) — Compares linear probes against RFM-derived concept vectors for reading how much a sentence concerns a concept out of a frozen LLM's activations, on a human-annotated ESG benchmark, and finds the simpler probe consistently stronger.
- [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](../../archive/papers/2026/arxiv-2608-10430/summary.md) — Detects the class of hallucination where a model confidently fabricates a parameter the user never gave, by running a LoRA adapter alongside the frozen model that restructures the residual stream and then names the offending parameter in words the agent can act on.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
