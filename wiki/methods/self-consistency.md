# self-consistency

<!-- auto:begin -->

Sampling multiple reasoning traces and taking the most common final answer, the simplest form of parallel test-time compute. A theoretical paper derives that its sample complexity (Θ(1/Δ²)) is worse than best-of-n's (Θ(1/Δ)) for some tasks; CaTS uses a confidence signal to adaptively size how many samples to draw instead of a fixed count; 'Diversity Matters' finds it mostly fails to transfer to vision-language-model accuracy gains unless sampled outputs are genuinely diverse.

- **Kind**: method
- **Also called**: Self-Consistency, majority voting
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [Best-of-N](best-of-n.md), [best-of-N sampling](best-of-n-sampling.md), [confidence-based early stopping](confidence-based-early-stopping.md), [majority voting](majority-voting.md), [test-time compute](../concepts/test-time-compute.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [Sample Complexity and Representation Ability of Test-time Scaling Paradigms](../../archive/papers/2026/title-27bc5c2aff7ebdab/summary.md) — A theoretical paper deriving sample-complexity bounds for self-consistency versus best-of-n, and an expressiveness result showing self-correction lets a Transformer simulate online learning over multiple tasks at test time.
- [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](../../archive/papers/2026/title-3f7a94a14d75d893/summary.md) — An empirical study showing that test-time-compute methods effective for LLM reasoning mostly fail to transfer to vision-language models unless prediction diversity is present, and proposes an entropy-based selection method that works better in multi-model ensembles.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
