# finite precision

<!-- auto:begin -->

The bounded number of bits a deployed model actually computes with, which both sources treat as part of the theory rather than an implementation detail. One replaces the usual log-precision or infinite-precision assumption with constant-bit IEEE 754 floating point including correct rounding, and finds the no-CoT bound tightens from TC^0 to AC^0 — so the arithmetic is genuinely part of the limit. The other finds that restricting to fixed precision is what makes length-generalization bounds computable at all, where the unrestricted case is undecidable. Precision therefore cuts both ways: it narrows what a transformer can express and it makes what it will generalize to decidable.

- **Kind**: concept
- **Also called**: bounded precision, constant precision, log precision
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](chain-of-thought.md), [circuit complexity](circuit-complexity.md), [effective depth](effective-depth.md), [expressivity](expressivity.md), [generalization](generalization.md), [length generalization](length-generalization.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [scaling laws](scaling-laws.md)

## Appears in

- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.
- [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](../../archive/papers/2024/local-c4c2f126482f8e18/summary.md) — Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
