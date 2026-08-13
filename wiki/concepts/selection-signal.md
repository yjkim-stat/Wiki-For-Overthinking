# selection signal

<!-- auto:begin -->

Whatever quantity decides which of several candidate answers is submitted, and in both sources the component whose contribution is deliberately held fixed so something else can be measured. One audits a perturbation-derived signal and finds it demonstrably dependent on the image — blanking its inputs collapses accuracy from 87.7 to 7.9 — yet no better at selection than a control that never sees the perturbations, which separates a signal that carries information from one that improves a decision. The other holds a self-certainty-and-Borda rule constant across its adaptive and full-budget arms, and separately shows what happens when the rule is weak: three samples score below one. Taken together the sources make the same point twice — the quality of this component bounds what any amount of extra sampling can buy.

- **Kind**: concept
- **Also called**: answer selection signal, selector
- **Topics**: [test-time-scaling](../topics/test-time-scaling.md)
- **Sources**: 2

**Related**: [adaptive compute allocation](adaptive-compute-allocation.md), [best-of-n](../methods/best-of-n.md), [Borda count](../methods/borda-count.md), [GSM8K](../datasets/gsm8k.md), [LLaVA-OneVision-7B](../models/llava-onevision-7b.md), [majority voting](../methods/majority-voting.md), [matched-budget comparison](matched-budget-comparison.md), [MATH](../datasets/math.md), [paired bootstrap confidence intervals](../methods/paired-bootstrap-confidence-intervals.md), [prompt difficulty](prompt-difficulty.md), [Qwen2.5-1.5B-Instruct](../models/qwen2-5-1-5b-instruct.md), [Qwen2.5-VL-7B-Instruct](../models/qwen2-5-vl-7b-instruct.md), [self-certainty](../methods/self-certainty.md), [self-consistency](../methods/self-consistency.md), [test-time scaling](../methods/test-time-scaling.md), [uncertainty quantification](uncertainty-quantification.md), [visual grounding](visual-grounding.md)

## What we have settled

- **Established** — Sampling more candidates is not monotone in accuracy: extra samples strengthen whatever the aggregation rule already does, including when it is wrong.
  - Two independent demonstrations with different aggregation rules. At inference, best-of-3 selection scores 0.093 against best-of-1's 0.153 on one model and dataset — three samples worse than one — which the authors attribute to a selector that does not exploit the candidate set, so extra samples add plausible wrong answers. In label-free RLVR training, where the reward is the consensus answer among rollouts, 64 rollouts reach 34.42 average accuracy against 34.66 at 16 and at 3.6x the wall clock, because more samples make a spurious consensus easier to form around an incorrect answer. The mechanism is shared even though one is a selector and the other a reward: the sample count amplifies the aggregation rule rather than averaging its errors away. The practical consequence is that a sample-count sweep is a required control, not an optional one, and that a scaling curve reported only at its endpoints can hide a reversal in between. A third instance is the cleanest of all, because it holds the candidate bank fixed and varies only the reducer: selecting by mean token log probability falls from 75.56% at one sample to 65.83% at eighty on the same banks where literal answer plurality rises to 78.33%, so nothing but the selection rule can explain the decline.

## Appears in

- [It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling](../../archive/papers/2026/arxiv-2608-01207/summary.md) — Shows that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language test-time scaling is a decoding-format effect, by adding a control that spends the same short-answer budget on the unperturbed image and finds it matches or beats the perturbation rule everywhere.
- [Interpretable Adaptive Sampling for LLM Test-Time Scaling](../../archive/papers/2026/arxiv-2608-03961/summary.md) — Allocates test-time samples per prompt with a fuzzy controller over human-readable difficulty and confidence signals, and — under a selector-matched protocol that isolates the budget policy from the answer selector — reports the result honestly as an accuracy-compute tradeoff rather than an accuracy gain.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
