# activation probing

<!-- auto:begin -->

Reading a property of a model's computation off its internal activations with a small auxiliary predictor, rather than from its output. The sources use it as a monitoring and verification tool: to detect hint-reliance when the reasoning trace is latent, to distinguish sound from flawed reasoning, and to predict answer correctness. They disagree on what to probe. Two argue that static single-layer activations invite the probe to latch onto surface lexical patterns, and read cross-layer displacement instead; a third restores restricted location information on the grounds that displacement alone discards too much; a fourth reduces the whole trace to one start-to-end delta and still beats single-layer baselines. All four report gains over single-layer probing, on different benchmarks and with no shared model.

- **Kind**: method
- **Also called**: activation probe, hidden-state probing, internal-state probing
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [answer stabilization](../concepts/answer-stabilization.md), [best-of-n](best-of-n.md), [calibration](calibration.md), [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [effective depth](../concepts/effective-depth.md), [error detection](../concepts/error-detection.md), [GPQA](../datasets/gpqa.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent chain of thought](latent-chain-of-thought.md), [latent reasoning](../concepts/latent-reasoning.md), [linear probe](linear-probe.md), [LLM-as-a-judge](llm-as-a-judge.md), [localization](../concepts/localization.md), [majority voting](majority-voting.md), [monitorability](../concepts/monitorability.md), [out-of-distribution generalization](../concepts/out-of-distribution-generalization.md), [pass@k](pass-k.md), [polysemanticity](../concepts/polysemanticity.md), [reasoning trajectory](../concepts/reasoning-trajectory.md), [residual stream](../concepts/residual-stream.md), [shortcut learning](../concepts/shortcut-learning.md), [superposition](../concepts/superposition.md), [verification](../concepts/verification.md)

## Appears in

- [Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?](../../archive/papers/2026/arxiv-2608-04928/summary.md) — Asks whether latent CoT destroys monitorability, and finds monitorability depends more on the task and on access to internals than on whether reasoning is explicit or latent.
- [Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs](../../archive/papers/2026/arxiv-2608-05660/summary.md) — Detects flawed reasoning from residual-stream trajectories by combining layerwise motion with a quantized region reader and a normalized direction reader, rather than probing full states.
- [Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2073/summary.md) — Reads reasoning validity from layer-to-layer displacement of hidden states rather than from the states themselves, on the grounds that static activations let probes latch onto lexical surface patterns.
- [Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-788/summary.md) — Verifies correctness without training by comparing a reasoning trace's start-to-end hidden-state delta against two class centroids built from labelled experience.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
