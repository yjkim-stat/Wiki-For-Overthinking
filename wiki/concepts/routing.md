# routing

<!-- auto:begin -->

Deciding per input which of several processing paths to take, rather than applying one procedure uniformly. One source routes on a text-only regex detector of restrictive cues, activating a two-stage constraint-extraction protocol only where constraints exist to exploit and falling back to direct chain-of-thought otherwise. The other routes at every generation step among a fast path, a slow perception path and a slow reasoning path, with the router trained by multi-objective RL on roughly 790k samples of teacher-attributed perception-versus-reasoning failures. The pair spans the design range: a hand-written detector applied once per problem, and a learned controller applied at each step.

- **Kind**: concept
- **Also called**: dispatch, gating, path selection
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-training](../topics/reasoning-training.md), [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [AIME](../datasets/aime.md), [chain of thought](../methods/chain-of-thought.md), [meta-reasoning](../methods/meta-reasoning.md), [OlympiadBench](../datasets/olympiadbench.md), [overthinking](overthinking.md), [perception bottleneck](perception-bottleneck.md), [self-correction](self-correction.md), [self-verification](self-verification.md), [test-time compute](test-time-compute.md), [verification](verification.md)

## Appears in

- [Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving](../../archive/papers/2026/arxiv-2608-05254/summary.md) — A training-free two-stage prompting protocol that extracts a problem's answer-space constraints first and then checks its own intermediate and final results against them, routed on by a regex detector.
- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — Routes each generation step among a fast path, a perception re-examination path and a self-reflection path, trained on 790k samples of teacher-attributed perception-versus-reasoning failures.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
