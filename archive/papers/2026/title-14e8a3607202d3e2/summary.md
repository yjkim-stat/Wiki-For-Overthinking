<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rethinking Calibration for Early-Exit Neural Networks

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62138>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Argues that confidence calibration is the wrong objective for early-exit image classifiers and replaces it with Early-Exit Failure Prediction, a criterion that also accounts for whether later layers could fix the prediction.

## Problem

Early-exit neural networks attach intermediate classifiers to a backbone and stop computation once a prediction is confident enough. Because the exit rule is a confidence threshold, the field assumes that better-calibrated intermediate classifiers give better cost-accuracy trade-offs. The paper challenges that assumption: calibration is a property of a classifier in isolation and says nothing about the sequential structure of the network or the cost of continuing, so a well-calibrated exit can still waste computation on a sample no later exit will get right.

## Contributions

- Shows that improving calibration of intermediate classifiers does not by itself improve early-exit performance, and that calibration metrics such as ECE misrank early-exit models
- Defines Early-Exit Failure Prediction, an exit criterion accounting for both whether the current prediction is correct and whether any later exit could correct it
- Provides a lightweight procedure that replaces the calibration step in an existing early-exit network, with better cost-accuracy trade-offs on CIFAR-100, TinyImageNet and ImageNet-1k across five architectures

## Method

The authors show two failure modes of calibration as a proxy: a well-calibrated classifier can still push samples through the whole network unnecessarily, and common calibration methods do not preserve the ranking of samples within a classifier, which is what a threshold rule actually depends on. In its place they define Early-Exit Failure Prediction (EEFP), which scores an exit decision by whether the current prediction is correct or, failing that, whether every remaining exit would also fail - in the second case further computation is futile and the sample should leave immediately. This joins prediction correctness with the cost of continuing rather than treating confidence in isolation. They then give a lightweight EEFP-motivated procedure that adjusts the intermediate classifiers and can be substituted for a calibration step in an existing early-exit network, and they use EEFP as an evaluation metric for comparing early-exit models.

## Results

Across ResNet-34, ViT-Tiny, ViT-Small, EfficientNet-B2 and MSDNet on CIFAR-100, TinyImageNet and ImageNet-1k, the EEFP-corrected networks give better cost-accuracy trade-offs than uncalibrated and temperature-calibrated baselines. As a metric, EEFP ranks models consistently with their end-to-end early-exit performance whereas calibration error (ECE) does not. The material available does not give per-dataset accuracy or FLOP numbers.

## Limitations

The paper notes it offers no method for enforcing the required ordering across exits, and that its grouping functions stay abstract and are not measurable in high dimensions. A reader should add the scope limit: every experiment is image classification with convolutional and vision-transformer backbones, and while the authors mention that the idea might carry to language model reasoning, no such experiment is presented.

## Why it matters here

- **overthinking**: This is a keyword false positive. The paper matched on 'early exit', which is standard vocabulary in efficient deep learning, but it is about intermediate classifiers in image-classification backbones - ResNet, ViT, EfficientNet, MSDNet on CIFAR-100, TinyImageNet and ImageNet-1k - and has nothing to do with large reasoning models, chain-of-thought length or test-time compute scaling. The authors mention in passing that the idea might apply to language model reasoning, but present no experiment in that direction. The only transferable thing is an analogy the group should treat as an analogy and not as evidence: the paper's core argument is that a confidence signal is the wrong stopping criterion because it ignores whether continuing would actually help, and the correct criterion is 'stop when the answer is right, or when more computation cannot make it right'. That framing is suggestive for confidence-based stopping in reasoning chains, but nothing here tests it. Recommend keeping the record and not counting it as evidence for any overthinking concept.

## Entities

- **Concepts**: Early-Exit Neural Network, [Confidence Calibration](../../../../wiki/concepts/confidence-calibration.md), Failure Prediction, Adaptive Computation, Cost-Accuracy Tradeoff, Confidence Thresholding
- **Methods**: Early-Exit Failure Prediction (EEFP), [early-exit neural networks](../../../../wiki/methods/early-exit-neural-networks.md), temperature scaling (baseline), [confidence thresholding](../../../../wiki/methods/confidence-thresholding.md), MSDNet, ResNet-34, ViT-Tiny, ViT-Small, EfficientNet-B2
- **Datasets**: CIFAR-100, TinyImageNet, [ImageNet-1k](../../../../wiki/datasets/imagenet-1k.md)

Tags: `early-exit`, `calibration`, `failure-prediction`, `adaptive-computation`, `image-classification`, `computer-vision`, `keyword-false-positive`

---

Record id: `title:14e8a3607202d3e2`
