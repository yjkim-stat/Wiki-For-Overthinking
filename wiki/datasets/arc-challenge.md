# ARC-Challenge

<!-- auto:begin -->

The archive cannot define ARC-Challenge from its own sources: the two papers that mention it -- C4, which gates when a diffusion language model may stop and which token positions a step may commit, and DC-CoT, a benchmark isolating data augmentation, selection and mixing in chain-of-thought distillation -- use it as one evaluation set among several, and neither archived note describes its contents or task format. The archive also carries 'ARC' and 'ARC-C' as separate entries, which are the same benchmark family under different spellings rather than distinct datasets.

- **Kind**: dataset
- **Also called**: ARC-C
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [C4](../methods/c4.md), [chain-of-thought distillation](../methods/chain-of-thought-distillation.md), [CommonsenseQA](commonsenseqa.md), [confidence calibration](../concepts/confidence-calibration.md), [early exit](../methods/early-exit.md), [GPQA-Diamond](gpqa-diamond.md), [GSM-Hard](gsm-hard.md), [GSM8K](gsm8k.md), [HellaSwag](hellaswag.md), [HumanEval](humaneval.md), [MATH](math.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MMLU-PRO](mmlu-pro.md), [Out-of-Distribution Generalization](../concepts/out-of-distribution-generalization.md), [StrategyQA](strategyqa.md), [SVAMP](svamp.md)

## Appears in

- [Commit Locally, Exit Globally: Coordinating Adaptive Sampling and Early Exit in Diffusion Language Models](../../archive/papers/2026/arxiv-2607-28166/summary.md) — C4 accelerates diffusion language model decoding with two separate gates: one that decides when the whole sequence may stop, by checking that the extracted answer span is both confident and unchanged for several steps, and one that decides which token positions a step may commit, by committing only a boundary-anchored run and confirming deferred positions one step later.
- [The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation](../../archive/papers/2026/title-95b92d67054ad4f2/summary.md) — DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.
- [ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](../../archive/papers/2026/title-fe3c313c25254076/summary.md) — ParoQuant is a 4-bit weight-only post-training quantization method that applies a series of independent Givens (pairwise) rotations plus channel-wise scaling to weights before quantization, with a fused CUDA kernel, in order to keep accuracy on reasoning benchmarks where quantization error accumulates over long chains of thought.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
