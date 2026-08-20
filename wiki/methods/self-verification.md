# self-verification

<!-- auto:begin -->

A model checking its own intermediate or final answers during reasoning, without an external verifier, to decide whether to continue, backtrack, or stop. GrAlgoBench identifies unproductive self-verification (excessive self-checking loops on graph-algorithm problems) as one driver of overthinking; LLaDA-S combines hierarchical search with self-verification to scale test-time compute for discrete diffusion language models.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [overthinking](../concepts/overthinking.md), [self-consistency](self-consistency.md)

## Appears in

- [Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems](../../archive/papers/2026/title-00481a9889909bb4/summary.md) — Introduces GrAlgoBench, a graph-algorithm-problem benchmark that exposes two weaknesses of large reasoning models: accuracy collapse on long-context inputs and unproductive overthinking via excessive self-verification.
- [Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models](../../archive/papers/2026/title-914a66aec4e7af2f/summary.md) — Introduces LLaDA-S, a hierarchical-search-and-self-verification test-time scaling framework for discrete diffusion language models that matches best-of-N accuracy with fewer function evaluations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
