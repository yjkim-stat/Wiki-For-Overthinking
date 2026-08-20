# safety case

<!-- auto:begin -->

An argument that a system is safe to deploy, which for mechanistic interpretability means naming a mechanism responsible for a behaviour and then defending that attribution. The identifiability work states what such a programme has been missing and supplies part of it: a certificate that the named mechanism is a property of the model rather than of the procedure that found it. It is equally explicit about what that certificate does not cover -- behavioural coverage, distribution shift, adversarial robustness -- and about the consequence of its own dissociation theorem, that since the identifiable object and the legible object cannot coincide in the non-normal regime, a safety case needing both will need two tools and should say which one it is using where. The monitoring source attacks the same programme empirically from the deployment side, showing that chain-of-thought detection falls 41 to 46 points when the prompt never instructs the model to conceal anything -- so a case built on monitoring evidence gathered under explicit-influence benchmarks overstates what monitoring will deliver. Neither source builds a safety case; together they mark the two ways one fails, by resting on a mechanism that is an artifact of its finder, and by resting on a monitor validated under conditions kinder than deployment.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [ablation](../methods/ablation.md), [activation patching](../methods/activation-patching.md), [chain of thought faithfulness](chain-of-thought-faithfulness.md), [circuit analysis](../methods/circuit-analysis.md), [detection versus control](detection-versus-control.md), [feature absorption](feature-absorption.md), [feature consistency](feature-consistency.md), [Gemma-2-2B](../models/gemma-2-2b.md), [GPT-2 small](../models/gpt-2-small.md), [indirect object identification](../datasets/indirect-object-identification.md), [interpretability illusion](interpretability-illusion.md), [logit lens](../methods/logit-lens.md), [monitorability](monitorability.md), [PCA](../methods/pca.md), [post-hoc rationalization](post-hoc-rationalization.md), [pre-registration](../methods/pre-registration.md), [Qwen3-8B-Base](../models/qwen3-8b-base.md), [residual stream](residual-stream.md), [sparse autoencoder](../methods/sparse-autoencoder.md), [sparse dictionary learning](../methods/sparse-dictionary-learning.md)

## Appears in

- [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](../../archive/papers/2026/arxiv-2608-04735/summary.md) — The first benchmark comparing CoT monitorability under explicit versus implicit influence, finding detection falls 41-46 points when the prompt never instructs the model to hide anything.
- [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](../../archive/papers/2026/arxiv-2608-10172/summary.md) — Treats a transformer forward pass as a controlled dynamical system with depth as time, lifts it with the Koopman operator to get a finite linear realisation whose spectrum is coordinate-free, proves that spectrum is recoverable from finite calibration data at the parametric rate, and then proves that the identifiable object and the human-legible object cannot be the same object.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
