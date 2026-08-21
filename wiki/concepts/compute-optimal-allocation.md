# compute-optimal allocation

<!-- auto:begin -->

The two archived sources use this phrase for two unrelated problems, and the entry should not be read as one idea. Compute-Optimal Quantization-Aware Training means it in the pretraining sense: how to split a fixed pretraining compute budget between a full-precision phase and a quantization-aware phase, fitted as a loss scaling law that predicts the optimal QAT fraction. The test-time compute paper means it in the inference sense: how much decoding compute to spend per prompt, via verifier search or proposal revision, where allocating adaptively by prompt difficulty beats a fixed strategy and can beat spending the same compute on more parameters. Nothing in the archive connects the two, and only the second bears on the group's overthinking topic.

- **Kind**: concept
- **Also called**: Compute-optimal allocation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Compute-optimal inference](compute-optimal-inference.md), [compute-optimal scaling](compute-optimal-scaling.md), [test-time compute scaling](test-time-compute-scaling.md)

## Appears in

- [Compute-Optimal Quantization-Aware Training](../../archive/papers/2026/title-19ebd4d7f589cbd8/summary.md) — An empirical scaling study of how to split a fixed pretraining compute budget between a full-precision phase and a quantization-aware training phase, yielding a loss scaling law that predicts the optimal QAT fraction.
- [Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](../../archive/papers/2025/title-f59c52e242c7e540/summary.md) — Analyzes verifier-search and proposal-revision as the two primary mechanisms of test-time compute scaling and shows that allocating compute adaptively per prompt difficulty is more efficient than fixed strategies, and can be more effective than scaling model parameters.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
