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

KLAS selects which pretrained vision models to stitch together by comparing their intermediate representations with KL divergence, producing better accuracy-efficiency tradeoff curves than heuristic stitch selection.

## Problem

Combining pretrained models via activation stitching can interpolate the accuracy-efficiency tradeoff for deployment, but existing stitch-selection methods rely on heuristics and produce suboptimal, non-generalizable tradeoffs.

## Contributions

- Introduces KLAS, a stitch-selection framework that automates and generalizes the choice of which pretrained models to stitch, across model families.
- Uses KL divergence between intermediate representations of pretrained models to identify promising binary stitches out of O(k^2 n^2) possibilities for k models of depth n.
- Demonstrates improved accuracy-efficiency curves versus heuristic stitch-selection baselines at the same finetuning cost.

## Method

Model stitching combines intermediate activations from one pretrained model into another to produce an interpolated network positioned between them on the accuracy-efficiency spectrum. Prior stitching methods pick which model pair/layer to stitch heuristically. KLAS instead measures the KL divergence between intermediate representations of candidate pretrained models and uses this similarity measure to select the most promising stitch configurations out of the full O(k^2 n^2) search space for k pretrained models of depth n.

## Results

Up to 1.21 percentage points higher ImageNet-1K top-1 accuracy at the same computational cost as baseline stitching methods, or the same accuracy with a 1.33x reduction in FLOPs.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. This is about selecting which layers of separate pretrained vision models to splice together to interpolate an accuracy/compute tradeoff across a pool of static architectures; it does not involve reasoning models, reasoning chains, or inference-time control of how much a model computes on a given input. It matched the topic only on the generic phrase 'accuracy-efficiency tradeoff'.

## Entities

- **Concepts**: model stitching, accuracy-efficiency tradeoff curve, representation similarity (KL divergence)
- **Methods**: KLAS, neural network stitching, KL-divergence-based stitch selection
- **Datasets**: ImageNet-1K

Tags: `model-stitching`, `accuracy-efficiency-tradeoff`, `vision`, `model-selection`

## Abstract

Abstract Given the wide range of deployment targets, flexible model selection is essential for optimizing performance within a given compute budget. Recent work demonstrates that stitching pretrained models within a model family enables cost-effective interpolation of the accuracy-efficiency tradeoff space. Stitching transforms intermediate activations from one pretrained model into another, producing a new interpolated stitched network. Such networks provide a pool of deployment options along the accuracy-efficiency spectrum. However, existing stitching approaches often yield suboptimal tradeoffs and lack generalizability, as they primarily rely on heuristics to select stitch configurations. We argue that constructing improved accuracy-efficiency tradeoffs requires explicitly capturing and leveraging the similarity between pretrained models being stitched. To this end, we introduce KLAS, a novel stitch selection framework that automates and generalizes stitch selection across model families by leveraging KL divergence between intermediate representations. KLAS identifies the most promising binary stitches from the $\mathcal{O}(k^2n^2)$ possibilities for $k$ pretrained models of depth $n$. Through comprehensive experiments, we demonstrate that KLAS improves the accuracy-efficiency curve of stitched models at the same finetuning cost as baselines. KLAS achieves up to $1.21\%$ higher ImageNet-1K top-1 accuracy at the same computational cost, or maintains accuracy with a $1.33\times$ reduction in FLOPs.

---

Record id: `title:4eb373d18ecc04ff`
