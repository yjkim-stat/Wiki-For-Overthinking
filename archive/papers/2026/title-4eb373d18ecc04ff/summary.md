<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# KLAS: Using Similarity to Stitch Neural Networks for Improved Accuracy-Efficiency Tradeoffs

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007961>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

KLAS stitches together pretrained neural networks by transforming intermediate activations from one model into another, using KL-divergence to automatically select the best stitching configuration and produce interpolated models across the accuracy-efficiency spectrum.

## Problem

Model selection under compute constraints is usually limited to choosing among existing pretrained models; combining pretrained models to reach intermediate points on the accuracy-efficiency spectrum is underexplored, and prior stitching approaches rely on heuristics to pick stitching configurations.

## Contributions

- KLAS, a framework for combining pretrained models via activation stitching to reach new accuracy-efficiency tradeoff points
- a KL-divergence-based method for automatically selecting stitching configurations instead of heuristics
- up to 1.21% accuracy improvement at equal cost or 1.33x FLOPs reduction at equal accuracy on ImageNet-1K

## Method

Transforms intermediate activations from a source model into a target model's representation space ('stitching'), and uses KL-divergence measurements between stitched and original outputs to automatically select the best stitching configuration among the ~k^2n^2 possible pairings for k pretrained models of depth n.

## Results

Stitched models reach up to 1.21% higher ImageNet-1K top-1 accuracy at the same computational cost, or maintain accuracy with a 1.33x reduction in FLOPs, versus the constituent pretrained models.

## Limitations

Not stated in the fetched abstract; evaluated on ImageNet-1K image classification, so generality to other modalities or tasks is untested.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'accuracy-efficiency tradeoff': this is about combining pretrained vision classifiers via activation stitching, unconnected to LLM reasoning length or test-time compute for reasoning.

## Entities

- **Concepts**: neural network stitching, KL-divergence-guided model selection, accuracy-efficiency interpolation
- **Methods**: neural network stitching, KL-divergence-based configuration selection
- **Datasets**: [ImageNet-1K](../../../../wiki/datasets/imagenet-1k.md)

Tags: `model-merging`, `accuracy-efficiency-tradeoff`, `vision-models`, `compute-efficiency`

---

Record id: `title:4eb373d18ecc04ff`
