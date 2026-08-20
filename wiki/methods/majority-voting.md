# majority voting

<!-- auto:begin -->

Sampling multiple independent answers and taking the most common one, a simple parallel test-time-compute strategy that needs no verifier or reward model. 'Diversity Matters' finds it mostly fails to improve vision-language-model accuracy unless the sampled outputs are actually diverse; 'Does Thinking More Always Help?' proposes 'parallel thinking' (multiple short chains plus majority vote) as an alternative to extending a single chain, beating extended thinking by up to 20%.

- **Kind**: method
- **Also called**: self-consistency
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [best-of-N sampling](best-of-n-sampling.md), [overthinking](../concepts/overthinking.md), [self-consistency](self-consistency.md), [test-time compute](../concepts/test-time-compute.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.
- [Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models](../../archive/papers/2025/title-5d66fe9a10241ce8/summary.md) — Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
