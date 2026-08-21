# MMMU

<!-- auto:begin -->

A multimodal knowledge and reasoning benchmark that reaches this archive through two papers on multimodal models rather than through the reasoning-length literature proper. Its one substantive appearance is in Amplified Does Not Mean Predictive, where MMMU is one of the places the thinking-model advantage disappears: post-failure recovery rates are 32.9% for thinking models against 33.8% for instruct models, comparable rather than the 2-3x gap seen on VisualPuzzles, MATH-500 and MMLU-Pro — evidence that visible deliberation does not pay off uniformly across task types. ARES lists it among ten multimodal benchmarks and reports its largest gains on the harder MMMU-Pro (54.8 versus 41.2 for the Vision-G1 baseline) rather than on MMMU itself. Neither source reports token counts on MMMU — in the first, reasoning length is only a nuisance control — so the archive holds no accuracy/length tradeoff for it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMStar](mmstar.md), [Overthinking](../concepts/overthinking.md), [Process Supervision](../concepts/process-supervision.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](../../archive/papers/2026/arxiv-2608-13760/summary.md) — Annotates 15,282 reasoning traces from 15 models on 6 benchmarks with a nine-behavior taxonomy and shows that the behaviors reasoning-oriented training amplifies most (self-correction, hypothesis testing, uncertainty acknowledgment) are not the behaviors most associated with getting the answer right (confidence calibration, knowledge alignment, self-awareness).
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
