# DAPO-Math-17K

<!-- auto:begin -->

A math dataset used for reinforcement-learning training of reasoning models, and the training-data counterpart of the DAPO algorithm rather than the algorithm itself. TRAAC trains on it exclusively — which the archive records as a limitation, since the difficulty binning it drives is math-only with hand-set cutoffs — and Lightning OPD 2.0 uses it as the math half of its two-domain setup (150 steps, paired with KlearReasoner-CodeSub-15K for code). IAPO uses it on the evaluation side instead, alongside GSM8K and MATH-500. It also appears as 'DAPO-MATH' and, in at least one source, as a bare 'DAPO'; no archived source describes how it was built or what its problems look like.

- **Kind**: dataset
- **Also called**: DAPO-MATH, DAPO-Math, DAPO-Math-17k
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [BBH (Big Bench Hard)](bbh-big-bench-hard.md), [DAPO](../methods/dapo.md), [DeepScaleR](deepscaler.md), [GFPO](../methods/gfpo.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [GSM8K](gsm8k.md), [LC-R1](../methods/lc-r1.md), [LiveCodeBench v6](livecodebench-v6.md), [MATH500](math500.md), [on-policy distillation (OPD)](../methods/on-policy-distillation-opd.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-Instruct](../methods/qwen2-5-instruct.md), [S-GRPO](../methods/s-grpo.md), [SuperGPQA](supergpqa.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models](../../archive/papers/2026/arxiv-2607-28449/summary.md) — Lightning OPD 2.0 subtracts a cross-fitted estimate of recurring teacher-reference log-probability disagreement from the token-level on-policy-distillation signal, so an OPD teacher can differ from the model that generated the SFT demonstrations.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.
- [IAPO: Information-Aware Policy Optimization for Token-Efficient Reasoning](../../archive/papers/2026/title-4bd9ad89663d1e26/summary.md) — IAPO shapes token-level RL advantages by each reasoning token's conditional mutual information with the final answer, so uninformative exploration is suppressed rather than length being penalized in aggregate, reporting up to 36% shorter reasoning at equal or better accuracy on math benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
