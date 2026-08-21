# MathVerse

<!-- auto:begin -->

A vision-language mathematics benchmark that appears in this archive only through multimodal papers. ARES reports a comparatively small gain on it - ARES-7B at 56.5 pass@1 on MathVerse-V against 50.0 for the Vision-G1 baseline, next to 51.9 against 31.3 on MathVision - and no token counts for it; the only lengths that paper reports are for GSM8K, MathVista and AIME25. In vStream it is not an accuracy benchmark at all but one of three maths-category sets (with MathVista and OlympiadBench) over which visual-attribution faithfulness is measured, and the archive files that paper as tangential: its 0.024 s per 10 tokens is the cost of explaining a trace, not of producing one. Mixture-of-Visual-Thoughts uses it as one of eight benchmarks and reports no cost figures either, so MathVerse entered the wiki through papers sharing the topic's vocabulary rather than its subject, and no accuracy/length tradeoff result held here is measured on it.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Ada-GRPO](../methods/ada-grpo.md), [adaptive reasoning](../concepts/adaptive-reasoning.md), [AI2D](ai2d.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [Ares](../methods/ares.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GQA](gqa.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [MATH500](math500.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMStar](mmstar.md), [OlympiadBench](olympiadbench.md), [Overthinking](../concepts/overthinking.md), [POPE](pope.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Mixture-of-Visual-Thoughts: Exploring Context-Adaptive Reasoning Mode Selection for General Visual Reasoning](../../archive/papers/2026/title-4321f3ae06d02a2e/summary.md) — Unifies text-based and visually-grounded reasoning in one vision-language model and uses RL with a mode-relative advantage to make the model pick which mode to use per input, raising average accuracy over eight benchmarks by about 5 points.
- [Real-Time Visual Attribution Streaming in Thinking Model](../../archive/papers/2026/title-503ded235751878b/summary.md) — vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
