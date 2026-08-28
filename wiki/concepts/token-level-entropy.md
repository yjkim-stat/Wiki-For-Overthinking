# Token-Level Entropy

<!-- auto:begin -->

Token-level entropy is used as a per-token uncertainty signal computed during generation. LEMUR detects memorized private attributes from a token-level entropy signature and replaces the committed tokens with image-grounded sanitized embeddings, entirely at inference time; ARES instead uses sliding-window token entropy as the signal for when and how much exploration effort a multimodal reasoning model should spend, scaled to problem difficulty.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [adaptive reasoning](adaptive-reasoning.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ARES](../methods/ares.md), [BBEH](../datasets/bbeh.md), [Difficulty-aware compute allocation](difficulty-aware-compute-allocation.md), [GPQA](../datasets/gpqa.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [MathVerse](../datasets/mathverse.md), [MathVision](../datasets/mathvision.md), [MathVista](../datasets/mathvista.md), [MMLU-Pro](../datasets/mmlu-pro.md), [MMMU](../datasets/mmmu.md), [MMMU-Pro](../datasets/mmmu-pro.md), [MMStar](../datasets/mmstar.md), [Overthinking](overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [WeMath](../datasets/wemath.md)

## Appears in

- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
