# parity

<!-- auto:begin -->

The k-parity task — whether an odd number of k relevant bits among n are set — used by both sources as the canonical testbed for what intermediate supervision buys, because the separation is sharp and proved rather than observed. Without intermediate supervision it is hard for finite-precision gradient methods; with explicit chain of thought even a one-layer transformer learns it efficiently. That makes it the cleanest available instrument for studying how CoT turns an expressible solution into a reachable one. In the archive it carries two results: that CoT changes the generalization bound from exponential to linear in reasoning length, and that internalizing the chain into hidden states preserves polynomial sample efficiency.

- **Kind**: dataset
- **Also called**: Parity, k-parity, parity learning
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](../methods/chain-of-thought.md), [curriculum learning](../concepts/curriculum-learning.md), [effective depth](../concepts/effective-depth.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [generalization](../concepts/generalization.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent reasoning](../concepts/latent-reasoning.md), [mechanistic interpretability](../concepts/mechanistic-interpretability.md), [sample complexity](../concepts/sample-complexity.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [A Sharper Picture of Generalization in Transformers](../../archive/papers/2026/local-03f1eff4f1d40725/summary.md) — Derives a non-vacuous PAC-Bayes generalization bound for transformers on boolean functions in terms of Fourier sparsity and degree, and uses it to show chain of thought turns an exponential dependence on reasoning length into a linear one for Parity.
- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
