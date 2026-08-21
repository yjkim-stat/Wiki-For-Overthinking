# Reasoning Trace Length

<!-- auto:begin -->

The number of tokens a model spends on intermediate reasoning before answering, used by both sources as a quantity to be allocated by difficulty rather than minimised. ARES reports the allocation moving in both directions against its own cold-start model at 7B: 278.9 versus 358.8 tokens on GSM8K (about 22% shorter) but 22,618.8 versus 16,361.6 on AIME25 (about 38% longer), so the efficiency claim is a reallocation and not a net reduction. Dualformer treats length as a controllable mode of a single model, reaching 97.6% optimal rate on unseen 30x30 mazes at 854 average trace tokens against a complete-trace baseline's 93.3% at 1,538, and 96.6% at 617 tokens when the model picks the mode itself. Neither source treats length as a measure of reasoning quality, and Dualformer reports no trace-length figures at all for its transfer to language-model mathematics, where the gains are one to two points.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Ares](../methods/ares.md), [budget forcing](../methods/budget-forcing.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [RLVR](../methods/rlvr.md), [supervised fine-tuning](../methods/supervised-fine-tuning.md), [Token-Level Entropy](token-level-entropy.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.
- [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](../../archive/papers/2025/title-5478b4a8a7720be7/summary.md) — Dualformer trains a single Transformer on reasoning traces with parts randomly dropped, producing one model that can be run in a solution-only fast mode, a full-trace slow mode, or an auto mode that picks per problem.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
