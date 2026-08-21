# ImageNet-1k

<!-- auto:begin -->

ImageNet-1K is in this wiki because two computer-vision papers matched the tracked topic on shared vocabulary, not because it plays any part in the overthinking literature. Rethinking Calibration matched on 'early exit' and evaluates intermediate classifiers in ResNet-34, ViT-Tiny/Small, EfficientNet-B2 and MSDNet over CIFAR-100, TinyImageNet and ImageNet-1k, reporting better cost-accuracy trade-offs than uncalibrated and temperature-calibrated baselines without per-dataset numbers; the archive records it as a keyword false positive and recommends it not be counted as evidence for any overthinking concept. KLAS matched on the generic phrase 'accuracy-efficiency tradeoff' and reports up to 1.21 percentage points higher ImageNet-1K top-1 at equal cost, or equal accuracy at 1.33x fewer FLOPs, from stitching pretrained vision backbones. Both adapt network depth or architecture for a single forward pass over an image; neither involves a chain of thought, a token budget, or a stop/continue decision over a trace.

- **Kind**: dataset
- **Also called**: ImageNet-1K, ImageNet-1k
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Confidence Calibration](../concepts/confidence-calibration.md), [Confidence Thresholding](../methods/confidence-thresholding.md), [early-exit neural networks](../concepts/early-exit-neural-networks.md), [GQA](gqa.md)

## Appears in

- Rethinking Calibration for Early-Exit Neural Networks — Argues that confidence calibration is the wrong objective for early-exit image classifiers and replaces it with Early-Exit Failure Prediction, a criterion that also accounts for whether later layers could fix the prediction.
- KLAS: Using Similarity to Stitch Neural Networks for Improved Accuracy-Efficiency Tradeoffs — KLAS selects which pretrained vision models to stitch together by comparing their intermediate representations with KL divergence, producing better accuracy-efficiency tradeoff curves than heuristic stitch selection.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
