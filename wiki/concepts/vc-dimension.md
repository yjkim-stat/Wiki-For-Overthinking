# VC dimension

<!-- auto:begin -->

The largest number of points a hypothesis class can label in every possible way, which tightly characterises the sample complexity of PAC learning. One source computes it for transformers: depth-L models with W parameters have VC dimension O(LW log(TW)) with a nearly matching lower bound, so both the LW log W dependence and the multiplicative log T factor in sequence length are tight -- and the practical corollary is that chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows. The analysis is parametric rather than norm-based and uses hard attention deliberately, because softmax hides a logistic activation and sigmoidal activations make VC dimension behave badly. The other source reaches it as the route to an open question: chain-of-thought learnability reduces to finiteness of the VC dimension of the base classes, so a bound showing linear aggregation over composed classes would establish closure under composition. What the archive should carry is that these are statements about how many samples suffice in principle, not about what gradient descent finds.

- **Kind**: concept
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit complexity](circuit-complexity.md), [compositionality](compositionality.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [generalization](generalization.md), [hard attention](../methods/hard-attention.md), [identifiability](identifiability.md), [sample complexity](sample-complexity.md), [teacher forcing](../methods/teacher-forcing.md)

## Appears in

- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) — Constructs explicit two-layer hard-attention Transformer decoders that execute depth-first search and Dijkstra's algorithm step by step under chain of thought, then reuses those traversals as a substrate to compute two branching-complexity measures of a tree in a linear number of steps, without layer normalisation or positional encodings.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
