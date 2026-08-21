# HumanEval

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AMC](amc.md), [AMC23](amc23.md), [ARC-Challenge](arc-challenge.md), [C4](c4.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [chain-of-thought prompting](../concepts/chain-of-thought-prompting.md), [confidence calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [DEER](../methods/deer.md), [Dynamic Early Exit](../concepts/dynamic-early-exit.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](gpqa-diamond.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH-500](math-500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [Still](still.md), [SVAMP](svamp.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.
- [Dynamic Early Exit in Reasoning Models](../../archive/papers/2026/title-f508a5b012a33fd1/summary.md) — DEER is a training-free decoding method that watches for the points where a reasoning model switches thought chains, prompts it for a trial answer there, and terminates the chain of thought when the trial answer's token confidence exceeds a threshold.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
