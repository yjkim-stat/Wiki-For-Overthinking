# WeMath

<!-- auto:begin -->

Neither source describes WeMath directly; it appears as one of the multimodal reasoning benchmarks used to evaluate adaptive reasoning-mode methods. Mixture-of-Visual-Thoughts uses it as one of eight benchmarks on which a mode-relative-advantage RL method that picks between text-based and visually-grounded reasoning raises average accuracy by about 5 points; ARES uses it as an evaluation benchmark for its difficulty-aware, entropy-shaped exploration training for multimodal reasoning models.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [BBEH](bbeh.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [DynaMath](dynamath.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [MMStar](mmstar.md), [Overthinking](../concepts/overthinking.md), [POPE](pope.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [ViRL39k](virl39k.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
