# circuit complexity

<!-- auto:begin -->

The classification of problems by the size and depth of boolean circuits that solve them, and the archive's main tool for saying what a transformer can and cannot compute. The sources agree a step-free transformer is confined to a small class and disagree on which, because the answer depends on the precision model: log-precision gives TC^0, while constant-bit floating point tightens it to AC^0, a proper subset. They agree on the consequence — problems complete for larger classes, such as automaton simulation (NC^1-complete), graph connectivity (NL-complete) and linear equalities (P-complete), are out of reach without intermediate steps. All separations are conditional on the standard conjecture that AC^0, TC^0, NC^1 and P do not collapse.

- **Kind**: concept
- **Also called**: AC0, NC1, TC0, circuit classes
- **Topics**: [reasoning-interpretability](../topics/reasoning-interpretability.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 4

**Related**: [attention analysis](../methods/attention-analysis.md), [chain of thought](../methods/chain-of-thought.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [effective depth](effective-depth.md), [expressivity](expressivity.md), [expressivity-learnability gap](expressivity-learnability-gap.md), [finite precision](finite-precision.md), [gradient descent analysis](../methods/gradient-descent-analysis.md), [latent reasoning](latent-reasoning.md), [length generalization](length-generalization.md), [process supervision](process-supervision.md), [self-training](self-training.md), [state tracking](state-tracking.md), [training dynamics](training-dynamics.md)

## Appears in

- [The Expressive Power of Transformers with Chain of Thought](../../archive/papers/2024/local-17f5eb14b12eda9b/summary.md) — Characterizes exactly how much computational power a chain of thought buys as a function of its length, sandwiching the class of languages a decoder recognizes with t(n) decoding steps between two standard complexity classes.
- [Chain of Thought Empowers Transformers to Solve Inherently Serial Problems](../../archive/papers/2024/local-c4c2f126482f8e18/summary.md) — Proves a tighter no-CoT upper bound of AC^0 for constant-precision transformers, and shows T steps of chain of thought let a constant-depth model compute anything a size-T boolean circuit can.
- [Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective](../../archive/papers/2023/local-f3c308f76ff7a114/summary.md) — Proves via circuit complexity that bounded-depth Transformers cannot directly solve basic arithmetic, linear equations or general dynamic programming unless their size grows super-polynomially, while constant-size autoregressive Transformers can solve all of them by generating chain-of-thought derivations.
- [Transformers Provably Learn Chain-of-Thought Reasoning with Length Generalization](../../archive/papers/2025/local-fe69869b0e362891/summary.md) — Gives the first optimization guarantee that gradient descent trains constant-depth transformers to solve NC1-complete problems with chain of thought, and shows the algebraic structure of the task decides how far the learned reasoning extrapolates.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
