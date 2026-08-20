# hard attention

<!-- auto:begin -->

An idealisation of attention in which a head selects a single position rather than mixing over a softmax distribution. Both sources use it and one explains why: softmax hides a logistic activation, and sigmoidal activations are known to make VC dimension behave badly for feed-forward networks, so analysing hard attention is what makes a tight capacity bound obtainable at all. That source is explicit that the consequence is a result characterising a neighbouring architecture rather than the deployed one. The constructive source builds depth-first search and Dijkstra as unique hard-attention decoders of at most two layers and two heads, and computes tree branching measures by reusing them -- reaching NC1 without layer normalisation or positional encodings, which it argues shows such augmentations are not architecturally necessary. What the archive should carry is the shared caveat: results about hard attention bound what a closely related architecture can represent, not what a softmax transformer trained by gradient descent will do.

- **Kind**: method
- **Also called**: unique hard attention
- **Topics**: [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [chain of thought](chain-of-thought.md), [chain-of-thought prompting](chain-of-thought-prompting.md), [circuit complexity](../concepts/circuit-complexity.md), [compositionality](../concepts/compositionality.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [generalization](../concepts/generalization.md), [sample complexity](../concepts/sample-complexity.md), [teacher forcing](teacher-forcing.md), [VC dimension](../concepts/vc-dimension.md)

## Appears in

- [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](../../archive/papers/2026/arxiv-2608-11716/summary.md) — Constructs explicit two-layer hard-attention Transformer decoders that execute depth-first search and Dijkstra's algorithm step by step under chain of thought, then reuses those traversals as a substrate to compute two branching-complexity measures of a tree in a linear number of steps, without layer normalisation or positional encodings.
- [Tight Sample Complexity of Transformers](../../archive/papers/2026/local-209065fd89f43691/summary.md) — Pins down the VC dimension of transformers as depth times parameters times a logarithm, and shows chain-of-thought learning by teacher forcing costs only logarithmically more as the number of reasoning steps grows.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
