# MMMU-Pro

<!-- auto:begin -->

MMMU-Pro (a harder variant of the multimodal MMMU benchmark) is used in these sources to evaluate general-capability preservation and difficulty-aware exploration in multimodal reasoning models: RECAP reports MMMU-Pro scores among the benchmarks used to show reasoning-focused RLVR fine-tuning degrades general vision-language capability unless mitigated by replay, and ARES uses sliding-window token entropy to shape exploration effort proportional to difficulty on multimodal benchmarks including MMMU-Pro.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AI2D](ai2d.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [BBEH](bbeh.md), [ChartQA](chartqa.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [DynaMath](dynamath.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [LISA](lisa.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMStar](mmstar.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [SAT](sat.md), [ScienceQA](scienceqa.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [Uniform sampling baseline](../methods/uniform-sampling-baseline.md), [ViRL39k](virl39k.md), [VizWiz](vizwiz.md), [WeMath](wemath.md)

## Appears in

- [Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1717/summary.md) — RECAP mitigates the general-capability forgetting (perception, grounding, safety) that RLVR-based reasoning fine-tuning causes in vision-language models, by replaying general-domain data alongside the reasoning objective and dynamically reweighting each objective's loss based on its recent convergence rate and instability -- an entropy-regularized priority allocation that provably reduces to a closed-form softmax -- preserving or improving general capabilities while matching or exceeding reasoning-only fine-tuning's math/reasoning performance, and, as a side effect, producing shorter, more concise reasoning rationales without compromising reasoning ability.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
