# ViRL39k

<!-- auto:begin -->

ViRL39K is a vision-language RL training dataset used in GPRO (Gated Perception-Reasoning Optimization, which diagnoses that visual perception failures rather than reasoning errors cause over twice as many incorrect predictions across model scales) and ARES (training multimodal reasoning models to spend exploration effort proportional to problem difficulty via sliding-window token entropy).

- **Kind**: dataset
- **Also called**: ViRL39K
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [BBEH](bbeh.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [DynaMath](dynamath.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MM-Vet](mm-vet.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [MMStar](mmstar.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Qwen2.5-VL-3B](../models/qwen2-5-vl-3b.md), [Qwen2.5-VL-7B](../models/qwen2-5-vl-7b.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-215/summary.md) — GPRO diagnoses that visual perception failures (not reasoning errors) cause over twice as many incorrect predictions across model scales in vision-language models, then routes each generated token through one of three paths -- a fast FFN, a slow cross-attention perception path for re-examining the image, or a slow self-reflection reasoning path -- via a lightweight meta-reasoning controller trained with PPO on a multi-objective reward (task accuracy, path-cost penalty, and an uncertainty-calibration term derived from ~790K GPT-4-labeled perception-vs-reasoning failure attributions); GPRO-7B matches/beats far larger closed models and long-CoT distillation baselines while cutting response length up to 51.5%, activating slow paths sparsely (73% Fast/17% Perception/10% Reasoning) and correctly, targeting perception re-examination at high-frequency visual tokens and reasoning refinement at logical connectives.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
