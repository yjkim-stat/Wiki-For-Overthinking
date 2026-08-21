# Reinforcement Learning with Verifiable Rewards

<!-- auto:begin -->

Reinforcement Learning with Verifiable Rewards (RLVR) is RL training whose reward is computed by a programmatic checker (e.g. a correctness checker on a math answer) rather than a learned reward model. The archive's sources treat it as the standard rollout-then-update loop that efficiency work modifies rather than replaces: ARES reshapes exploration effort using token-level entropy, DR²Seg splits the rollout into separate description and segmentation stages, QuRL runs the rollout phase with a quantized actor for speed, GFPO trains only on a filtered subset of a larger sampled rollout group, and ShorterBetter rewards matching the shortest correct rollout's length.

- **Kind**: concept
- **Also called**: RLVR, Reinforcement learning with verifiable rewards
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME](../datasets/aime.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [Ares](../methods/ares.md), [chain-of-thought compression](chain-of-thought-compression.md), [DAPO](../methods/dapo.md), [DeepScaleR](../datasets/deepscaler.md), [DeepSeek-R1-Distill-Qwen-1.5B](../methods/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../methods/deepseek-r1-distill-qwen-7b.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [GFPO](../methods/gfpo.md), [GPQA](../datasets/gpqa.md), [group relative advantage](group-relative-advantage.md), [GRPO](../methods/grpo.md), [GSM8K](../datasets/gsm8k.md), [HumanEval](../datasets/humaneval.md), [Length reward](length-reward.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [MathQA](../datasets/mathqa.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MBPP](../datasets/mbpp.md), [Minerva Math](../datasets/minerva-math.md), [MMLU](../datasets/mmlu.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [O1-Pruner](../methods/o1-pruner.md), [OlympiadBench](../datasets/olympiadbench.md), [Omni-MATH](../datasets/omni-math.md), [overthinking](overthinking.md), [Phi-4-reasoning](../methods/phi-4-reasoning.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Segmentation](reasoning-segmentation.md), [Reasoning Trace Length](reasoning-trace-length.md), [ReasonSeg](../datasets/reasonseg.md), [Redundant Self-Verification](redundant-self-verification.md), [RefCOCO](../datasets/refcoco.md), [RefCOCOg](../datasets/refcocog.md), [RLVR](rlvr.md), [Seg-Zero (baseline)](../methods/seg-zero-baseline.md), [Still](../datasets/still.md), [task decomposition](task-decomposition.md), [Token-Level Entropy](token-level-entropy.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models](../../archive/papers/2026/title-56bdffcf992c5e91/summary.md) — DR2Seg splits reasoning segmentation into a description stage and a referring-segmentation stage and rewards the model when a shorter self-contained description still yields the right mask, cutting reasoning length while raising gIoU.
- [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](../../archive/papers/2026/title-9b034ca49bd46f6f/summary.md) — QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.
- [Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning](../../archive/papers/2026/title-d02c8db6721c4d3c/summary.md) — GFPO samples a larger group of rollouts per problem during RL training and updates only on the top-k by length or by reward-per-token, converting extra training-time compute into shorter responses at inference.
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](../../archive/papers/2025/title-d40396527f776f1d/summary.md) — ShorterBetter takes the length of the shortest correct response in a sampled group as a per-problem target and rewards the model for matching it, cutting output length by 50%-80% on DeepSeek-Distill-Qwen-1.5B/7B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
