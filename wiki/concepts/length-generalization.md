# length generalization

<!-- auto:begin -->

Making correct predictions on inputs longer than any seen in training, which both sources treat as the property long-context and long-chain reasoning actually need. They divide sharply. One proves no computable bound exists on how long the training inputs must be, already at depth two, so the required lengths grow faster than any computable function; restricting to fixed precision restores computability at exponential cost. The other proves a positive result in a narrower setting, that a one-layer transformer trained by gradient descent does length-generalize on state-tracking — but only when the task's group action is simply transitive, and only partly for symmetry group actions. Read together: extrapolation is decided by the structure of the specific task, and no general procedure can tell you in advance.

- **Kind**: concept
- **Also called**: extrapolation to longer inputs, length extrapolation
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit complexity](circuit-complexity.md), [effective depth](effective-depth.md), [expressivity](expressivity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [finite precision](finite-precision.md), [generalization](generalization.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [process supervision](process-supervision.md), [scaling laws](scaling-laws.md), [self-training](self-training.md), [state tracking](state-tracking.md), [training dynamics](training-dynamics.md)

## Appears in

- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
