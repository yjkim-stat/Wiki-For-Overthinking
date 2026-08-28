# GSM8K (appendix)

<!-- auto:begin -->

GSM8K (appendix) refers to the grade-school-math benchmark as reported in the appendix of the two papers citing it here -- REDE's attention-based hallucination-detection denoising method and ASTRO's spatial/temporal redundancy optimization framework, which reports up to 11.3x composite efficiency gains while retaining 80-99% of original accuracy. Sources do not explain why results appear in an appendix rather than the main text.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AMC23](amc23.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [MATH500](math500.md), [Qwen3-8B](../models/qwen3-8b.md), [SPIRIT](../methods/spirit.md), [TruthfulQA](truthfulqa.md)

## Appears in

- [Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](../../archive/papers/2026/arxiv-2607-22098/summary.md) — REDE uses the attention that the final answer token pays to each reasoning step as annotation-free supervision for a lightweight projection, in whose shaped embedding space irrelevant and repetitive steps become kNN outliers that can be dropped before a hallucination detector reads the trace.
- [Adaptive Spatial and Temporal Redundancy Optimization for Efficient Reasoning in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1130/summary.md) — ASTRO is a training-free framework that jointly exploits temporal redundancy (unnecessary reasoning steps once confidence stabilizes) and spatial redundancy (reasoning phases that tolerate lower numerical precision), segmenting a trace into five Dewey-inspired cognitive phases and coordinating phase-aware progressive quantization with confidence-based early termination, achieving up to 11.3x composite efficiency gains and 2.3-4.7x measured latency speedups while retaining 80-99% of original accuracy across two models and four reasoning benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
