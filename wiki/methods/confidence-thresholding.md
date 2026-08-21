# Confidence Thresholding

<!-- auto:begin -->

Committing to a prediction as soon as a confidence score crosses a fixed cutoff, used in both sources as the exit rule of an early-exit network rather than as anything specific to LLM reasoning. UAT's premise is that the static threshold is the weak point: it replaces it with a multi-armed bandit that adapts the cutoff online and without supervision, reporting 1.70-2.10x speedup at under 2% performance drop. The second source attacks the signal instead of the cutoff, arguing that the calibrated confidence such thresholds read is the wrong quantity because it says nothing about whether later layers would have corrected the prediction. Neither source states how the static threshold is chosen in the first place, so the archive documents the two critiques of the technique better than the technique itself.

- **Kind**: method
- **Also called**: Confidence thresholding, confidence threshold, confidence thresholding, static confidence threshold
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Compute-optimal inference](../concepts/compute-optimal-inference.md), [Confidence Calibration](../concepts/confidence-calibration.md), [Conformal Prediction](conformal-prediction.md), [Early Exit](early-exit.md), [early-exit neural networks](../concepts/early-exit-neural-networks.md), [ImageNet-1k](../datasets/imagenet-1k.md), [Risk Control](../concepts/risk-control.md), [SST-2](../datasets/sst-2.md), [T5-Large](t5-large.md)

## Appears in

- [Rethinking Calibration for Early-Exit Neural Networks](../../archive/papers/2026/title-14e8a3607202d3e2/summary.md) — Argues that confidence calibration is the wrong objective for early-exit image classifiers and replaces it with Early-Exit Failure Prediction, a criterion that also accounts for whether later layers could fix the prediction.
- [Beyond Greedy Exits: Improved Early Exit Decisions for Risk Control and Reliability](../../archive/papers/2025/title-c65d4659ec08b51c/summary.md) — UAT replaces the static confidence threshold in early-exit deep networks with a multi-armed bandit that adapts the threshold online and unsupervised, reporting 1.70-2.10x speedup at under 2% performance drop.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
