# compositionality

<!-- auto:begin -->

Whether a capability established for parts survives being combined, and both sources here find it is the harder case. The empirical source distinguishes two reasoning types learned by the same mechanism under extended training past overfitting: the circuit generalises out of distribution for comparison and fails for composition, so it is composition specifically that the learned structure does not carry. The theoretical source meets the same question about its own constructions rather than about a model's: two representations of one object, linked by a bijection its own construction realises, need separate chain-of-thought constructions with different token growth and head counts, and the authors leave open whether realisability is closed under bijective change of representation and hence under composition -- sketching that a VC bound showing linear aggregation over composed base classes would suffice. The reading the archive should carry is that composing two things that each work is a claim requiring its own evidence, at the level of a learned circuit and at the level of a proof alike.

- **Kind**: concept
- **Topics**: [reasoning-faithfulness](../topics/reasoning-faithfulness.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [causal analysis](../methods/causal-analysis.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit analysis](../methods/circuit-analysis.md), [circuit complexity](circuit-complexity.md), [Gemini-1.5-Pro](../models/gemini-1-5-pro.md), [hard attention](../methods/hard-attention.md), [identifiability](identifiability.md), [implicit reasoning](implicit-reasoning.md), [memorization](memorization.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [VC dimension](vc-dimension.md)

## Appears in

- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) — Constructs explicit two-layer hard-attention Transformer decoders that execute depth-first search and Dijkstra's algorithm step by step under chain of thought, then reuses those traversals as a substrate to compute two branching-complexity measures of a tree in a linear number of steps, without layer normalisation or positional encodings.
- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](../../archive/papers/2024/local-6252abed1b134f57/summary.md) — Shows that transformers can learn implicit multi-step reasoning over stored knowledge, but only through grokking — extended training far past overfitting — and that whether the resulting circuit generalizes out of distribution depends on the reasoning type, succeeding for comparison and failing for composition.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
