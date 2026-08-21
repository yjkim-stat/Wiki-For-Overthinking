# Token-Level Entropy

<!-- auto:begin -->

Token-level entropy is used as a per-token uncertainty signal computed during generation. LEMUR detects memorized private attributes from a token-level entropy signature and replaces the committed tokens with image-grounded sanitized embeddings, entirely at inference time; ARES instead uses sliding-window token entropy as the signal for when and how much exploration effort a multimodal reasoning model should spend, scaled to problem difficulty.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Ares](../methods/ares.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [MATH-500](../datasets/math-500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MMLU-PRO](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMStar](../datasets/mmstar.md), [overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](reasoning-trace-length.md), [Reinforcement Learning with Verifiable Rewards](reinforcement-learning-with-verifiable-rewards.md), [RLVR](rlvr.md), [WeMath](../datasets/wemath.md)

## Appears in

- [LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection](../../archive/papers/2026/arxiv-2608-11691/summary.md) — A training-free, inference-time unlearning method for RL-trained multimodal reasoning models that detects memorized private attributes from a token-level entropy signature and replaces the committed tokens with image-grounded sanitized embeddings.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
