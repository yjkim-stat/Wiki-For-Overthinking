# Omni-MATH

<!-- auto:begin -->

A competition-mathematics problem set that this archive sees in two distinct roles rather than one. As training data it is one of the four pools behind DeepScaleR-Preview (~40K problems from AIME, AMC, Omni-MATH and Still), which both DRPO and ShorterBetter fine-tune on, so there it shapes length-controlled models rather than testing them. As an evaluation set it appears in GFPO, where filtering rollouts cuts GRPO's excess length on Omni-MATH by 31.5% (Shortest-8/16), 82.6% (Token Efficiency) and 35.1% (Adaptive Difficulty) on Phi-4-reasoning - the last being the smallest cut of that variant's five benchmarks. 'Thinking Hard, Not Smart' instead uses Omni-MATH items of difficulty <=5 as the question pool for its shared-budget exams, and it is the only domain where that paper runs its full factorial design over exam length, question order and point values, with CRUXEval-O checked only for replication.

- **Kind**: dataset
- **Also called**: Omni-Math
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [BBEH](bbeh.md), [BBH](bbh.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [Claude-Opus-4.8](../models/claude-opus-4-8.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GFPO](../methods/gfpo.md), [GLM-5.2](../models/glm-5-2.md), [GPQA](gpqa.md), [GPT-5.5](../models/gpt-5-5.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [HLE](hle.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MuSiQue](musique.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Phi-4-Reasoning](../methods/phi-4-reasoning.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Resource-Rational Reasoning](../concepts/resource-rational-reasoning.md), [RLVR](../methods/rlvr.md), [Still](still.md), [SuperGPQA](supergpqa.md)

## Appears in

- [Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](../../archive/papers/2026/arxiv-2608-07968/summary.md) — Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.
- [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](../../archive/papers/unknown/arxiv-2608-16033/summary.md) — A benchmark that puts six problems of mixed difficulty under one shared computation budget and measures the gap between what a model solves problem-by-problem and what it solves when it must decide how to divide the budget.
- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
