# HellaSwag

<!-- auto:begin -->

HellaSwag serves in this archive as a short-output control - a benchmark whose answer is a few tokens - and both citing papers use it to show that costs which accumulate along a trace barely bite when there is no trace. C4 groups it with MMLU, ARC-Challenge, WinoGrande and PIQA as 'short-answer' at a 64-step budget, where its gates finish in 3.4-4.8 steps on LLaDA (92.5-94.7% of the budget saved, 14.3x-18.7x throughput) with accuracy equal to full decoding within 0.5 point; C4 measures 90%-answer-stabilisation at 0.04 of the budget on these tasks against 0.96 on long-reasoning ones. ParoQuant averages it with BoolQ, ARC-Challenge and ARC-Easy as its non-reasoning split, scoring 69.9 against FP16's 70.1 - a 0.2-point gap, against 0.9 points on MMLU-Pro, GPQA-Diamond and AIME - and attributes the difference explicitly to these benchmarks generating only a few tokens. It is therefore the archive's clearest example of the easy end of the tradeoff, where savings are near-total and accuracy is untouched.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [ARC-Challenge](arc-challenge.md), [ASDiv](asdiv.md), [C4](../methods/c4.md), [Confidence Calibration](../concepts/confidence-calibration.md), [DeepSeek-R1-Distill-Qwen-32B](../models/deepseek-r1-distill-qwen-32b.md), [Early Exit](../methods/early-exit.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GSM-Hard](gsm-hard.md), [GSM-MC](gsm-mc.md), [GSM8K](gsm8k.md), [HumanEval](humaneval.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Phi-4](../models/phi-4.md), [Qwen2.5-32B](../models/qwen2-5-32b.md), [SVAMP](svamp.md), [UMWP](umwp.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-608/summary.md) — TRACE INVERSION reframes abstention as query misalignment -- a hallucinating model answered a different (reconstructed) question than the one the user actually posed -- and detects this by reconstructing the implied query from a model's own reasoning trace and comparing it to the original via an ensemble of embedding-similarity, LLM-judged, and groundedness-detection metrics, beating five baselines in 33/36 settings across four LLMs and nine abstention datasets, while separately showing that CoT/reasoning-trace prompting itself degrades abstention accuracy by an average 2.6% versus non-reasoning prompting.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
