# Still

<!-- auto:begin -->

Neither source describes Still directly; it appears as a named point of reference alongside their own contributions. QuRL instead runs RLVR's rollout phase with an INT8/FP8 quantized actor for 20-80% faster rollout; ShorterBetter rewards matching the shortest correct response length in a sampled group, cutting output length 50-80% on DeepSeek-Distill-Qwen-1.5B/7B.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](aime.md), [AIME 2024](aime-2024.md), [AMC](amc.md), [AMC23](amc23.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [DAPO](../methods/dapo.md), [DeepScaleR](deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [LiveCodeBench](livecodebench.md), [MATH](math.md), [MATH-500](math-500.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [Minerva Math](minerva-math.md), [MMLU](mmlu.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](olympiadbench.md), [Omni-MATH](omni-math.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [RLVR](../concepts/rlvr.md)

## Appears in

- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
