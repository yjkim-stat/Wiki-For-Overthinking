# Omni-MATH

<!-- auto:begin -->

A competition-mathematics problem set that this archive sees in two distinct roles rather than one. As training data it is one of the four pools behind DeepScaleR-Preview (~40K problems from AIME, AMC, Omni-MATH and Still), which both DRPO and ShorterBetter fine-tune on, so there it shapes length-controlled models rather than testing them. As an evaluation set it appears in GFPO, where filtering rollouts cuts GRPO's excess length on Omni-MATH by 31.5% (Shortest-8/16), 82.6% (Token Efficiency) and 35.1% (Adaptive Difficulty) on Phi-4-reasoning - the last being the smallest cut of that variant's five benchmarks. 'Thinking Hard, Not Smart' instead uses Omni-MATH items of difficulty <=5 as the question pool for its shared-budget exams, and it is the only domain where that paper runs its full factorial design over exam length, question order and point values, with CRUXEval-O checked only for replication.

- **Kind**: dataset
- **Also called**: Omni-Math
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [BBH](bbh.md), [Chain-of-Thought Compression](../concepts/chain-of-thought-compression.md), [DAPO](../methods/dapo.md), [DeepScaleR](deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GFPO](../methods/gfpo.md), [GPQA](gpqa.md), [Group-Relative Advantage](../concepts/group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH500](math500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [Minerva](minerva.md), [MMLU](mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RLVR](../methods/rlvr.md), [Still](still.md)

## Appears in

- [Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](../../archive/papers/2026/arxiv-2608-07968/summary.md) — Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
