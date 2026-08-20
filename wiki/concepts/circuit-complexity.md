# circuit complexity

<!-- auto:begin -->

The complexity-class characterisation of what a transformer can compute, and across 5 sources the formal backbone of the archive's chain-of-thought material. The established results: a single forward pass of a bounded-depth transformer sits in a low parallel class, generating intermediate tokens lifts that ceiling, and the number of steps maps onto classes -- a linear number of steps reaching NC1, with polynomially many steps reaching further. One source gives an exact fixed-step characterisation in terms of a rank measure of the function; another shows chain of thought lets transformers solve inherently serial problems; a third supplies a concrete witness by constructing graph traversal and a linear-step branching measure in two layers without layer normalisation. Two boundaries the archive should keep. These are representational results and say nothing about what gradient descent finds -- one source in the set proves a learning result instead, on how a transformer comes to learn a chain-of-thought procedure with length generalisation. And they are usually proved for hard attention, an idealisation adopted because softmax reintroduces difficulties known from sigmoidal networks.

- **Kind**: concept
- **Also called**: AC0, NC1, TC0, circuit classes, computational complexity of transformers
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 5

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [compositionality](compositionality.md), [effective depth](effective-depth.md), [expressivity](expressivity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [finite precision](finite-precision.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [hard attention](../methods/hard-attention.md), [latent reasoning](latent-reasoning.md), [length generalization](length-generalization.md), [process supervision](process-supervision.md), [self-training](self-training.md), [state tracking](state-tracking.md), [training dynamics](training-dynamics.md), [VC dimension](vc-dimension.md)

## Appears in

- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) — Constructs explicit two-layer hard-attention Transformer decoders that execute depth-first search and Dijkstra's algorithm step by step under chain of thought, then reuses those traversals as a substrate to compute two branching-complexity measures of a tree in a linear number of steps, without layer normalisation or positional encodings.
- [The Expressive Power of Transformers with Chain of Thought](../../archive/papers/2024/local-17f5eb14b12eda9b/summary.md) — Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.
- [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](../../archive/papers/2024/local-c4c2f126482f8e18/summary.md) — Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
