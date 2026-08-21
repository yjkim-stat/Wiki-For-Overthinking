# DAPO

<!-- auto:begin -->

No archived paper is about DAPO; it is named only in passing, and always as a GRPO-style clipped policy-optimization algorithm for RL with verifiable rewards. IAPO uses it as one baseline among GFPO, GTPO and S-GRPO, reporting the better Pass@k/Length@k ratio against it; other archived work borrows specific pieces of it, namely its clipped objective with asymmetric bounds and token-level aggregation, and its soft overlong penalty. QuRL uses the bare name loosely for training data rather than for the algorithm, which is the DAPO-Math-17k corpus, so the same string denotes both a method and a dataset in the archive and the two are kept as separate entries here. Nothing archived expands the acronym or describes the full method.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AMC23](../datasets/amc23.md), [DAPO-Math-17k](../datasets/dapo-math-17k.md), [DeepScaleR](../datasets/deepscaler.md), [GFPO](gfpo.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [Minerva Math](../datasets/minerva-math.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Reinforcement Learning with Verifiable Rewards](../concepts/reinforcement-learning-with-verifiable-rewards.md), [RLVR](../concepts/rlvr.md), [S-GRPO](s-grpo.md), [Still](../datasets/still.md)

## Appears in

- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
