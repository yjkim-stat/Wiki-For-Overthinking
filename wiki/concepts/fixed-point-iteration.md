# fixed-point iteration

<!-- auto:begin -->

In these sources fixed-point iteration means running one block of weights repeatedly on its own output until the representation converges, so that compute is spent on depth of iteration rather than on more parameters; it is a third notion of variable computation, distinct from both exiting a reasoning trace and exiting a layer stack at an intermediate head. 'Expressive Power of Implicit Models' treats it as the defining construction of implicit models - an infinite-depth, weight-tied network trained with constant memory - and proves that for a broad class of such models expressive power grows with the number of test-time iterations, validated across imaging, scientific computing, operations research and LLM reasoning. MIND over Body applies the same idea per layer, iterating until the layer's activations converge, with a separate introspection model trained under an auxiliary loss to predict when the iteration can be skipped entirely, in both a CNN and a transformer. The archive's own record flags that this second, layer-level description comes from a third-party summary of the paper's talk and could not be confirmed against the paper, whose abstract states the mechanism only as adapting parameter count and computation time to task complexity.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Test-time scaling](test-time-scaling.md)

## Appears in

- [MIND over Body: Adaptive Thinking using Dynamic Computation](../../archive/papers/2025/title-3d49618364a0cc92/summary.md) — Adds a self-introspection module to CNN and transformer networks that decides, per input, how many parameters to reuse and how long to iterate, so computation scales with input complexity rather than input size.
- [Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling](../../archive/papers/2026/title-acc0cd457f5fd230/summary.md) — Provides a mathematical theory showing that implicit (weight-tied, fixed-point) models' expressive power grows with the number of test-time iterations, validated across imaging, scientific computing, operations research and LLM reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
