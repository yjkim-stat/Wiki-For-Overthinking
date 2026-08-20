# length generalization

<!-- auto:begin -->

Whether a model trained on short instances handles longer ones, and across 3 sources the property the archive's theoretical chain-of-thought results are stated in terms of. One source proves transformers provably learn chain-of-thought reasoning with length generalisation, which is a learning result rather than an expressivity one and therefore the closest thing here to an account of why the training works. Another gives bounds specifically for it. And the expressivity work supplies the reason it is the right axis: chain of thought converts sequence length into effective depth, so the step count is the resource, and what generalises is a procedure over steps rather than a function of a fixed input size.

- **Kind**: concept
- **Also called**: extrapolation to longer inputs, length extrapolation
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 3

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [circuit complexity](circuit-complexity.md), [compositional generalization](compositional-generalization.md), [effective depth](effective-depth.md), [expressivity](expressivity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [finite precision](finite-precision.md), [generalization](generalization.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [out-of-distribution generalization](out-of-distribution-generalization.md), [process supervision](process-supervision.md), [scaling laws](scaling-laws.md), [self-training](self-training.md), [state tracking](state-tracking.md), [training dynamics](training-dynamics.md)

## Appears in

- [Length Generalization Bounds for Transformers](../../archive/papers/2026/local-bd58c1406f4a1ef5/summary.md) — Proves that no computable length-generalization bound exists for transformers of depth two or beyond, and gives a matching exponential bound for the positive fragment that corresponds to fixed-precision transformers.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
