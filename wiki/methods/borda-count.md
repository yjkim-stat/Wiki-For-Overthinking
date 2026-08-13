# Borda count

<!-- auto:begin -->

An aggregation rule that scores each candidate by its summed rank across voters rather than by first-place counts, so a broadly acceptable option can beat a narrowly preferred one. Both sources use it as a component of a selection pipeline rather than studying it. One includes it among the label-free selectors it races against a format-matched control, where it and confidence-weighted self-consistency track that control within noise while simpler confidence signals fall below it. The other combines it with self-certainty scoring as the fixed selector held constant across its adaptive and full-budget arms — which is what makes that comparison isolate the budget policy. The second use is the more instructive: this rule's value there is that it does not vary, so the experiment can attribute its result to something else.

- **Kind**: method
- **Also called**: Borda aggregation
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](../concepts/adaptive-compute-allocation.md), [best-of-n](best-of-n.md), [GSM8K](../datasets/gsm8k.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH](../datasets/math.md), [MathVision](../datasets/mathvision.md), [paired bootstrap confidence intervals](paired-bootstrap-confidence-intervals.md), [prompt difficulty](../concepts/prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [selection signal](../concepts/selection-signal.md), [self-certainty](self-certainty.md), [self-consistency](self-consistency.md), [test-time scaling](test-time-scaling.md), [uncertainty quantification](../concepts/uncertainty-quantification.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
