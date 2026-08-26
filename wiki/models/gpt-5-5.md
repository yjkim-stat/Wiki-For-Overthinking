# GPT-5.5

<!-- auto:begin -->

GPT-5.5 is a proprietary model that appears in the archive only as an instrument or a subject of evaluation, never described. ParallelWorld uses it as the verifier agent that scores and prunes candidate exploration branches, paired with GPT-5.4 as the answer agent; because both are closed, the paper's gains cannot be separated from backbone capability and cannot be reproduced without API access. R3-Bench evaluates it under a shared computation budget across six problems of mixed difficulty. Neither source reports its architecture, size, training or release details, so the archive holds no description of the model itself -- only records of what it was used for.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Claude-Opus-4.8](claude-opus-4-8.md), [Confidence-Based Stopping](../methods/confidence-based-stopping.md), [deepseek-v4-pro](deepseek-v4-pro.md), [GLM-5.2](glm-5-2.md), [Information Gain](../concepts/information-gain.md), [Omni-MATH](../datasets/omni-math.md), [Resource-Rational Reasoning](../concepts/resource-rational-reasoning.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](../../archive/papers/unknown/arxiv-2608-16033/summary.md) — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.
- [ParallelWorld: Test-Time Scaling for Embodied Reasoning](../../archive/papers/2026/arxiv-2608-22971/summary.md) — ParallelWorld is a verifier-guided tree search over simulated future observations for embodied reasoning: from a restorable simulator state it expands several candidate camera and physical actions in parallel, prunes branches with a verifier agent under a branch-width schedule, and answers from the top-ranked root-to-leaf route.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
