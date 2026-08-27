# scaling-law fitting

<!-- auto:begin -->

Deriving a mathematical relationship between a training-compute quantity and a resulting loss or optimal-configuration value from empirical measurements across scales. Sources apply this to two training-compute allocation questions: the optimal ratio of quantization-aware training to full-precision training as a function of total compute, and reconciling the Kaplan and Chinchilla compute-optimal scaling laws by correcting for confounds (last-layer compute cost, warmup duration, optimizer tuning) in how each was originally fit.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

## Appears in

- [Compute-Optimal Quantization-Aware Training](../../archive/papers/2026/title-19ebd4d7f589cbd8/summary.md) — Derives scaling laws for how to optimally split a fixed compute budget between full-precision training and quantization-aware training (QAT), finding the loss-optimal QAT fraction grows with total compute.
- [Resolving Discrepancies in Compute-Optimal Scaling of Language Models](../../archive/papers/2024/title-d494aac6d49ec910/summary.md) — Explains the discrepancy between the Kaplan and Chinchilla compute-optimal scaling laws by identifying and correcting three confounds (last-layer compute cost, warmup duration, scale-dependent optimizer tuning), after which the Kaplan-style reproduction matches the Chinchilla law.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
