# MMMU

<!-- auto:begin -->

A multimodal benchmark used in this archive as one evaluation set among several in two test-time-scaling audits, neither of which describes how it was built. In the vision-language decoding-format audit it is one of four benchmarks on which a format-matched control matches the perturbation-based selector it was meant to beat (50.1 against 50.3), and it is also where the two diagnostics decouple: blanking the perturbation inputs collapses the selection score from 50.2 to 23.3, confirming the signal genuinely depends on the image, while its mean stability gap is only +0.071. In the test-time-augmentation study Claude 4.5 Haiku has a 66.1 percent chain-of-thought baseline on it, and paraphrase-based input diversity adds +2.01 against +1.01 for self-consistency at matched compute. Across both, it behaves as a mid-difficulty multimodal set where the headline effects are small enough that the control matters more than the method.

- **Kind**: dataset
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [answer aggregation](../methods/answer-aggregation.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [chain-of-thought prompting](../methods/chain-of-thought-prompting.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](../concepts/matched-budget-comparison.md), [MATH500](math500.md), [MathVision](mathvision.md), [MMLU](mmlu.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [prompt sensitivity](../concepts/prompt-sensitivity.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [selection signal](../concepts/selection-signal.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](../methods/test-time-scaling.md), [visual grounding](../concepts/visual-grounding.md)

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](../../archive/papers/2026/arxiv-2608-09351/summary.md) — Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
