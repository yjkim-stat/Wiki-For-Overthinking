# HellaSwag

<!-- auto:begin -->

HellaSwag serves in this archive as a short-output control - a benchmark whose answer is a few tokens - and both citing papers use it to show that costs which accumulate along a trace barely bite when there is no trace. C4 groups it with MMLU, ARC-Challenge, WinoGrande and PIQA as 'short-answer' at a 64-step budget, where its gates finish in 3.4-4.8 steps on LLaDA (92.5-94.7% of the budget saved, 14.3x-18.7x throughput) with accuracy equal to full decoding within 0.5 point; C4 measures 90%-answer-stabilisation at 0.04 of the budget on these tasks against 0.96 on long-reasoning ones. ParoQuant averages it with BoolQ, ARC-Challenge and ARC-Easy as its non-reasoning split, scoring 69.9 against FP16's 70.1 - a 0.2-point gap, against 0.9 points on MMLU-Pro, GPQA-Diamond and AIME - and attributes the difference explicitly to these benchmarks generating only a few tokens. It is therefore the archive's clearest example of the easy end of the tradeoff, where savings are near-total and accuracy is untouched.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [ARC-Challenge](arc-challenge.md), [C4](../methods/c4.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Early Exit](../methods/early-exit.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [SVAMP](svamp.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
