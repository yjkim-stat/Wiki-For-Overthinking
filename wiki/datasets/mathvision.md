# MathVision

<!-- auto:begin -->

A vision-language mathematics benchmark that reaches this archive through two multimodal papers rather than through the reasoning-length literature. ARES, which the archive files as directly on topic, reports its largest single gain here - ARES-7B at 51.9 pass@1 against 31.3 for the Vision-G1 baseline - but gives no token counts for MathVision itself; its length numbers are reported for GSM8K (about -22%), MathVista (about -19%) and AIME25 (about +38% longer). Mixture-of-Visual-Thoughts (AdaVaR) evaluates on it as one of eight benchmarks and is filed as only partly relevant, because it selects between text and visually-grounded reasoning modes rather than between more and less reasoning, and reports no token counts, latency or cost at all. MathVision therefore entered the wiki through papers sharing the topic's vocabulary - adaptive reasoning, mode selection - rather than its subject, and the archive holds no accuracy/length tradeoff evidence measured on it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Ares](../methods/ares.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [MATH-500](math-500.md), [MathVerse](mathverse.md), [MathVista](mathvista.md), [MMLU-PRO](mmlu-pro.md), [MMMU](mmmu.md), [MMStar](mmstar.md), [overthinking](../concepts/overthinking.md), [POPE](pope.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [Reinforcement Learning with Verifiable Rewards](../methods/reinforcement-learning-with-verifiable-rewards.md), [RLVR](../methods/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
