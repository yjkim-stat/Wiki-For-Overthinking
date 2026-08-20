# expressivity

<!-- auto:begin -->

What a model can represent in principle, independent of whether training finds it. The archived sources use it to establish that chain of thought changes a transformer's computational class rather than merely helping it, and they converge on the same regime boundaries from different directions: a logarithmic number of intermediate steps buys essentially nothing, a linear number buys the ability to simulate recurrence and recognize all regular languages, and a polynomial number reaches P exactly. Two of the sources reach these conclusions independently under different precision assumptions. The sources are also explicit about the limit of the notion: one names in its own limitations that it explains why CoT increases expressivity and not why scaling improves it, nor whether anything expressible is learnable.

- **Kind**: concept
- **Also called**: expressive power, representational capacity
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [chain of thought](chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit complexity](circuit-complexity.md), [effective depth](effective-depth.md), [finite precision](finite-precision.md), [generalization](generalization.md), [latent reasoning](latent-reasoning.md), [length generalization](length-generalization.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [process supervision](process-supervision.md), [scaling laws](scaling-laws.md)

## Appears in

- [The Expressive Power of Transformers with Chain of Thought](../../archive/papers/2024/local-17f5eb14b12eda9b/summary.md) — Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.
- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.
- [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](../../archive/papers/2024/local-c4c2f126482f8e18/summary.md) — Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
