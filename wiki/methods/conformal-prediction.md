# Conformal Prediction

<!-- auto:begin -->

In this archive conformal prediction is used not to produce prediction sets but as a wrapper that turns a learned score into a stopping threshold carrying a distribution-free, finite-sample guarantee. The mixed-integer optimization paper is the clearest case: a network estimates the solver's true optimality gap from its internal state, and conformal calibration converts that estimate into a termination threshold with a distribution-free probabilistic guarantee on the quality of the returned solution. ATTS applies the same machinery inside LLM inference, using it to coordinate multi-dimensional test-time scaling asynchronously and cut synchronization overhead between draft and target models. The statistical early-stopping paper is adjacent rather than conformal — it bounds the probability of halting too early on a well-posed query from uncertainty-keyword arrivals — so the archive's three sources share the guarantee's shape more than they share the technique.

- **Kind**: method
- **Also called**: Conformal Prediction, conformal prediction
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [abstention](../concepts/abstention.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Confidence Thresholding](confidence-thresholding.md), [early stopping](../concepts/early-stopping.md), [GPQA](../datasets/gpqa.md), [GSM-MC](../datasets/gsm-mc.md), [GSM8K](../datasets/gsm8k.md), [HLE](../datasets/hle.md), [MATH](../datasets/math.md), [MMLU](../datasets/mmlu.md), [Overthinking](../concepts/overthinking.md), [rejection sampling](rejection-sampling.md), [Test-Time Compute](../concepts/test-time-compute.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [UMWP](../datasets/umwp.md), [Uncertainty Quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [ATTS: Asynchronous Test-Time Scaling via Conformal Prediction](../../archive/papers/2026/title-b601ad920fcc4d45/summary.md) — ATTS uses conformal prediction to asynchronously coordinate multi-dimensional test-time scaling, cutting synchronization overhead between draft and target models during LLM inference.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
