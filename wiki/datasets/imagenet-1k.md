# ImageNet-1K

<!-- auto:begin -->

ImageNet-1K is in this wiki because two computer-vision papers matched the tracked topic on shared vocabulary, not because it plays any part in the overthinking literature. Rethinking Calibration matched on 'early exit' and evaluates intermediate classifiers in ResNet-34, ViT-Tiny/Small, EfficientNet-B2 and MSDNet over CIFAR-100, TinyImageNet and ImageNet-1k, reporting better cost-accuracy trade-offs than uncalibrated and temperature-calibrated baselines without per-dataset numbers; the archive records it as a keyword false positive and recommends it not be counted as evidence for any overthinking concept. KLAS matched on the generic phrase 'accuracy-efficiency tradeoff' and reports up to 1.21 percentage points higher ImageNet-1K top-1 at equal cost, or equal accuracy at 1.33x fewer FLOPs, from stitching pretrained vision backbones. Both adapt network depth or architecture for a single forward pass over an image; neither involves a chain of thought, a token budget, or a stop/continue decision over a trace.

- **Kind**: dataset
- **Also called**: ImageNet-1K, ImageNet-1k
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [GQA](gqa.md)

## Appears in

- [KLAS: Using Similarity to Stitch Neural Networks for Improved Accuracy-Efficiency Tradeoffs](../../archive/papers/2026/title-4eb373d18ecc04ff/summary.md) — KLAS stitches together pretrained neural networks by transforming intermediate activations from one model into another, using KL-divergence to automatically select the best stitching configuration and produce interpolated models across the accuracy-efficiency spectrum.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
