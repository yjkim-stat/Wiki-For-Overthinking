# RLVR

<!-- auto:begin -->

RLVR is the standard abbreviation for Reinforcement Learning with Verifiable Rewards, RL training whose reward is computed by a programmatic checker rather than a learned model. Its two sources here use it as the training loop being made more efficient: ARES reshapes per-problem exploration effort via sliding-window token entropy, and QuRL runs the RLVR rollout phase with an INT8/FP8 quantized actor for 20-80% faster rollout.

- **Kind**: concept
- **Also called**: Reinforcement Learning with Verifiable Rewards
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Ares](../methods/ares.md), [DAPO](../methods/dapo.md), [DeepScaleR](../datasets/deepscaler.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [Minerva Math](../datasets/minerva-math.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](reasoning-trace-length.md), [Reinforcement Learning with Verifiable Rewards](reinforcement-learning-with-verifiable-rewards.md), [Still](../datasets/still.md), [Token-Level Entropy](token-level-entropy.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
