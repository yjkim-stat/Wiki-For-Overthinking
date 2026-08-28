# SVAMP

<!-- auto:begin -->

Neither source describes SVAMP directly; it appears as one of the math-word-problem benchmarks used to evaluate their methods. C4 accelerates diffusion language model decoding with a sequence-level stopping gate and a token-commit gate; ARM trains a model to choose among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per problem, cutting average tokens about 30% at roughly unchanged accuracy.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [Ada-GRPO](../methods/ada-grpo.md), [AIME 2025](aime-2025.md), [ARC-Challenge](arc-challenge.md), [ASDiv](asdiv.md), [BBH](bbh.md), [C4](../methods/c4.md), [CommonsenseQA](commonsenseqa.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Early Exit](../methods/early-exit.md), [GPQA](gpqa.md), [GRPO](../methods/grpo.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [HumanEval](humaneval.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [OpenBookQA](openbookqa.md), [Overthinking](../concepts/overthinking.md), [StrategyQA](strategyqa.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [Token Budget](../concepts/token-budget.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [ARM: Adaptive Reasoning Model](../../archive/papers/2025/title-21d562149c3adad6/summary.md) — ARM trains a model to pick among four reasoning formats (Direct Answer, Short CoT, Code, Long CoT) per task using Ada-GRPO, cutting average tokens by about 30% at roughly unchanged accuracy.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
