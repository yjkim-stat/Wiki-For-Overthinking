# gradient descent analysis

<!-- auto:begin -->

Proving what training actually converges to, rather than what an architecture could represent or how many samples would suffice. Both sources use a deliberately minimal setting to keep the dynamics tractable — a one-layer transformer block with softmax attention trained without positional encoding — and both study synthetic tasks whose structure is known exactly. This is what lets them make claims no expressivity result can: that gradient descent reaches NC^1-complete problems with chain of thought, and that a staged curriculum provably internalizes reasoning into hidden states. The cost of tractability is the setting: one layer, synthetic targets, and conclusions that are about the reachability of a solution rather than about a deployed model.

- **Kind**: method
- **Also called**: convergence analysis, optimization analysis, training dynamics analysis
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [attention analysis](attention-analysis.md), [chain of thought](chain-of-thought.md), [circuit complexity](../concepts/circuit-complexity.md), [curriculum learning](curriculum-learning.md), [effective depth](../concepts/effective-depth.md), [expressivity-learnability gap](../concepts/expressivity-learnability-gap.md), [implicit chain of thought](../concepts/implicit-chain-of-thought.md), [implicit reasoning](../concepts/implicit-reasoning.md), [latent reasoning](../concepts/latent-reasoning.md), [length generalization](../concepts/length-generalization.md), [parity](../datasets/parity.md), [sample complexity](../concepts/sample-complexity.md), [self-training](../concepts/self-training.md), [state tracking](../concepts/state-tracking.md), [test-time compute](../concepts/test-time-compute.md), [training dynamics](../concepts/training-dynamics.md)

## Appears in

- [Transformers Provably Learn to Internalize Chain-of-Thought](../../archive/papers/2026/local-ee30f023d9f2d8fb/summary.md) — Proves that reasoning can be moved from emitted tokens into hidden states without losing sample efficiency, using a curriculum that deletes thinking tokens in geometric chunks and so needs only logarithmically many training stages.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
