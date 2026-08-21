# mechanistic interpretability

<!-- auto:begin -->

Both archived sources use 'mechanistic interpretability' loosely, as a label for reading and intervening on a model's internal representations rather than for circuit-level reverse engineering, and neither defines it. Manifold Steering works in that register: it finds a single activation-space direction correlated with overthinking, traces the plateau-then-harm behaviour of naive steering to that direction lying on a low-dimensional manifold, and projects the steering vector onto the manifold before applying it at inference, cutting output tokens by up to 71% on DeepSeek-R1 distilled models while maintaining or improving accuracy on mathematical benchmarks (the benchmarks are not named in the material the archive holds). The sparse-autoencoder paper attaches the term to the feature-dictionary line of work instead, and argues via compressed sensing that an SAE's linear-nonlinear encoder provably cannot recover the true sparse code even on solvable instances, so substituting a stronger sparse-inference procedure over the same learned dictionary recovers codes better for small extra compute -- the archive records no number for that gain, nor the interpretability metric claimed to improve. Between the two, the term covers both the analysis of internal representations and the interventions that analysis licenses.

- **Kind**: concept
- **Also called**: Mechanistic Interpretability, mechanistic interpretability
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [activation steering](../methods/activation-steering.md), [Manifold Steering](../methods/manifold-steering.md), [Overthinking](overthinking.md)

## Appears in

- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
