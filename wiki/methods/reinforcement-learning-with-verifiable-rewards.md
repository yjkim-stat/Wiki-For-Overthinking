# Reinforcement Learning with Verifiable Rewards

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: Reinforcement learning with verifiable rewards
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Ares](ares.md), [chain-of-thought compression](../concepts/chain-of-thought-compression.md), [DAPO](dapo.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GFPO](gfpo.md), [GPQA](../datasets/gpqa.md), [group relative advantage](../concepts/group-relative-advantage.md), [GRPO](grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [Length reward](../concepts/length-reward.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MBPP](../datasets/mbpp.md), [Minerva Math](../datasets/minerva-math.md), [MMLU](../datasets/mmlu.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [O1-Pruner](o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](../concepts/overthinking.md), [Phi-4-reasoning](phi-4-reasoning.md), [Qwen2.5-Instruct](qwen2-5-instruct.md), [Qwen2.5-VL](qwen2-5-vl.md), [Reasoning Segmentation](../concepts/reasoning-segmentation.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [ReasonSeg](../datasets/reasonseg.md), [Redundant Self-Verification](../concepts/redundant-self-verification.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [RLVR](rlvr.md), [Seg-Zero (baseline)](seg-zero-baseline.md), [Still](../datasets/still.md), [task decomposition](../concepts/task-decomposition.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
