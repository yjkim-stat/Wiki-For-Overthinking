# Resource-Rational Reasoning

<!-- auto:begin -->

The idea, taken from resource-rational analysis in cognitive science, that an agent should allocate limited computation to maximise expected value -- so the question is not only how to solve a problem but whether further computation is worth its cost. In this archive it is the framing that turns reasoning length into an allocation problem with an opportunity cost: one source builds a benchmark around it by putting six problems under one shared budget and measuring the gap between what a model demonstrably solves in isolation and what it realises when spending is zero-sum, and another uses it to motivate difficulty-adaptive distillation. The first source's finding is that the framing exposes a real deficit: the gap is present in 71 of 72 cells and is not predicted by a general-capability composite over fifty-plus benchmarks.

- **Kind**: concept
- **Also called**: Resource-Rational Reasoning, resource-rational reasoning
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Claude-Opus-4.8](../models/claude-opus-4-8.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GLM-5.2](../models/glm-5-2.md), [GPT-5.5](../models/gpt-5-5.md), [GRPO](../methods/grpo.md), [Omni-MATH](../datasets/omni-math.md), [Overthinking](overthinking.md), [Reasoning Collapse](reasoning-collapse.md), [Reward Hacking](reward-hacking.md)

## Appears in

- [Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation](../../archive/papers/2026/arxiv-2607-29287/summary.md) — TwT trains a translation model to spend reasoning tokens in proportion to input difficulty, by cold-starting on 7K difficulty-rewritten CoT traces and then running GRPO with a BLEU+COMET quality reward and an n-gram repetition penalty.
- [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](../../archive/papers/unknown/arxiv-2608-16033/summary.md) — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
