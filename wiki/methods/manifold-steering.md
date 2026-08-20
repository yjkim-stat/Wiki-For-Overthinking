# Manifold Steering

<!-- auto:begin -->

An overthinking-mitigation technique that identifies overthinking as movement along a low-dimensional manifold in a reasoning model's activation space, then steers activations along that manifold at inference time to shorten reasoning. Its source paper reports cutting output tokens up to 71% while maintaining or improving accuracy; the 'Don't Overthink It' survey categorizes it under 'Representation Engineering', alongside similar steering-vector methods (SEAL, Pre-allocated Direction Vectors, Thinking Progress Vector).

- **Kind**: method
- **Also called**: activation steering, representation engineering
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [activation steering](activation-steering.md), [early exit](early-exit.md), [LC-R1](lc-r1.md), [overthinking](../concepts/overthinking.md), [PLAN-AND-BUDGET](plan-and-budget.md), [TokenSkip](tokenskip.md), [VeriThinker](verithinker.md)

## Appears in

- [Don't Overthink It: A Survey of Efficient R1-style Large Reasoning Models](../../archive/papers/2025/local-6c80b6fd388d671e/summary.md) — A survey that organizes methods for making R1-style large reasoning models reason efficiently (i.e., avoid overthinking) into two axes: single-model optimization and multi-model collaboration.
- [Mitigating Overthinking in Large Reasoning Models via Manifold Steering](../../archive/papers/2025/title-b4ba27743c499d8d/summary.md) — Identifies that overthinking in large reasoning models corresponds to a low-dimensional manifold in activation space and proposes projecting steering interventions onto that manifold to cut output tokens by up to 71% without hurting accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
