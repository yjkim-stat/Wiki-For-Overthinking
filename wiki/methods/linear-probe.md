# linear probe

<!-- auto:begin -->

A linear classifier trained on activations to test whether some property is linearly readable from them, and the archive's most common interpretability instrument at five sources. The sources agree it works and disagree about what it measures. Two argue that probing static single-layer activations lets the probe learn surface lexical patterns rather than reasoning structure, and use cross-layer displacement instead; one restores restricted location information because displacement discards the originating state. One detects sycophantic commitment at 74-85% balanced accuracy, beating text-only baselines only at high commitment. One separates recoverability from influence — a concept can be linearly recoverable without affecting the output — and finds sparse autoencoders improve the first while attenuating the second.

- **Kind**: method
- **Also called**: linear probing, probe, probing classifier
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 5

**Related**: [activation probing](activation-probing.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [commitment boundary](../concepts/commitment-boundary.md), [effective depth](../concepts/effective-depth.md), [error detection](../concepts/error-detection.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](../concepts/latent-reasoning.md), [localization](../concepts/localization.md), [monitorability](../concepts/monitorability.md), [monosemanticity](../concepts/monosemanticity.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [polysemanticity](../concepts/polysemanticity.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [sparse autoencoder](sparse-autoencoder.md), [superposition](../concepts/superposition.md), [sycophancy](../concepts/sycophancy.md)

## Appears in

- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) — Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors](../../archive/papers/2026/arxiv-2608-06300/summary.md) — Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.
- [Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2073/summary.md) — Reads reasoning validity from layer-to-layer displacement of hidden states rather than from the states themselves, on the grounds that static activations let probes latch onto lexical surface patterns.
- [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-20/summary.md) — Locates the sentences in a reasoning trace that commit a model to agreeing with an incorrect user suggestion, using counterfactual rollouts and linear probes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
