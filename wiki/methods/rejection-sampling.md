# rejection sampling

<!-- auto:begin -->

A test-time-compute strategy that samples candidates and discards (rejects) ones that fail a check, resampling as needed, distinct from Best-of-N's fixed-N-then-select approach. ROC-n-reroll proves that verifier ROC-curve geometry determines its accuracy under a fixed compute budget, and shows it beats Best-of-N at fixed budget, with both converging at infinite compute; ATTS uses conformal prediction to coordinate it asynchronously with other test-time-scaling dimensions.

- **Kind**: method
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [best-of-N sampling](best-of-n-sampling.md), [GSM8K](../datasets/gsm8k.md), [MATH](../datasets/math.md), [MATH-500](../datasets/math-500.md), [test-time compute scaling](../concepts/test-time-compute-scaling.md), [test-time scaling](../concepts/test-time-scaling.md)

## Appears in

- [ROC-n-reroll: How verifier imperfection affects test-time scaling](../../archive/papers/2026/title-6b3727a0a0ac9a23/summary.md) — Proves that verifier ROC-curve geometry determines the accuracy of Best-of-N and Rejection Sampling under a fixed compute budget, and shows RS beats BoN at fixed compute while both converge in the infinite-compute limit.
- [ATTS: Asynchronous Test-Time Scaling via Conformal Prediction](../../archive/papers/2026/title-b601ad920fcc4d45/summary.md) — ATTS uses conformal prediction to asynchronously coordinate multi-dimensional test-time scaling, cutting synchronization overhead between draft and target models during LLM inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
