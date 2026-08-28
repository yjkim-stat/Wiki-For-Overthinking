# GPT-5.5

<!-- auto:begin -->

GPT-5.5 is a proprietary model that appears in the archive only as an instrument or a subject of evaluation, never described. ParallelWorld uses it as the verifier agent that scores and prunes candidate exploration branches, paired with GPT-5.4 as the answer agent; because both are closed, the paper's gains cannot be separated from backbone capability and cannot be reproduced without API access. R3-Bench evaluates it under a shared computation budget across six problems of mixed difficulty. Neither source reports its architecture, size, training or release details, so the archive holds no description of the model itself -- only records of what it was used for.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [Claude-Opus-4.5](claude-opus-4-5.md), [Claude-Opus-4.8](claude-opus-4-8.md), [Confidence-Based Stopping](../methods/confidence-based-stopping.md), [critical-path latency](../concepts/critical-path-latency.md), [DeepSeek-R1](deepseek-r1.md), [deepseek-v4-pro](deepseek-v4-pro.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-5.2](glm-5-2.md), [Information Gain](../concepts/information-gain.md), [MATH500](../datasets/math500.md), [Omni-MATH](../datasets/omni-math.md), [OpenMathReasoning](../datasets/openmathreasoning.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Resource-Rational Reasoning](../concepts/resource-rational-reasoning.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](../../archive/papers/unknown/arxiv-2608-16033/summary.md) — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.
- [ParallelWorld: Test-Time Scaling for Embodied Reasoning](../../archive/papers/2026/arxiv-2608-22971/summary.md) — ParallelWorld is a verifier-guided tree search over simulated future observations for embodied reasoning: from a restorable simulator state it expands several candidate camera and physical actions in parallel, prunes branches with a verifier agent under a branch-width schedule, and answers from the top-ranked root-to-leaf route.
- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
