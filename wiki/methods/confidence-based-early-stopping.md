# confidence-based early stopping

<!-- auto:begin -->

Stopping a model's sampling or reasoning process once its own confidence signal (e.g. self-distilled calibration, or cross-agent consensus) indicates further compute is unlikely to change the answer, rather than running a fixed budget. CaTS uses a self-distilled confidence signal to adaptively size the sampling budget per query; TUMIX's multi-agent tool-use ensemble stops iterating once its agents' answers converge.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Best-of-N](best-of-n.md), [self-consistency](self-consistency.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning](../../archive/papers/2026/title-03232c54fde9b57f/summary.md) — Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.
- [TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture](../../archive/papers/2026/title-545becf86760af05/summary.md) — An ensemble of parallel agents using different tool-use strategies that iteratively refine and share answers, with a confidence-based rule to stop early and cut inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
