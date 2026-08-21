<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Test-Time Scaling for Small Vision-Language Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007164>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes TTAug and TTAdapt, two lightweight test-time scaling strategies for small vision-language models that use input augmentation and consensus pseudolabels instead of external supervision.

## Problem

Small vision-language models are computationally efficient but generalize and perform worse than larger models; existing test-time scaling methods that could close this gap are themselves computationally demanding, which contradicts the resource-efficient design goal of using a small model in the first place.

## Contributions

- Proposes TTAug, which aggregates outputs at the token level from multiple augmented inputs without updating model parameters
- Proposes TTAdapt, which adapts model parameters at inference using consensus-based pseudolabels derived from TTAug
- Demonstrates consistent performance improvements across nine benchmarks while keeping computational cost suitable for resource-constrained settings
- Shows generality across model scales and across different VLMs without additional tuning

## Method

TTAug generates multiple augmented versions of each input at inference and aggregates the model's outputs at the token level, without any parameter updates. TTAdapt builds on this by using consensus among TTAug's aggregated outputs as pseudolabels, then adapting the model's parameters at inference time against those pseudolabels. Both rely on model-internal features rather than external supervision or additional training.

## Results

Consistent performance improvements across nine benchmarks while maintaining computational efficiency; generality demonstrated across models of different scales and across different VLMs without additional tuning; no specific numeric deltas were found in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: 'test-time scaling' here means input augmentation and lightweight parameter adaptation at inference to boost accuracy of small vision-language models under a fixed compute budget, not chain-of-thought reasoning length or when a large reasoning model should stop reasoning. There is no discussion of reasoning chains or stopping criteria in the material.

## Entities

- **Concepts**: test-time augmentation, [test-time adaptation](../../../../wiki/concepts/test-time-adaptation.md), consensus pseudolabeling
- **Methods**: Test-Time Augmentation (TTAug), Test-Time Adaptation (TTAdapt)
- **Datasets**: _none recorded_

Tags: `vlm`, `test-time-scaling`, `efficiency`, `small-models`, `test-time-adaptation`

## Abstract

Abstract Small Vision-Language Models (VLMs) provide a computationally efficient alternative to larger models, at the cost of weaker generalization abilities and downstream task performance. These shortcomings could be addressed by test-time scaling techniques, but existing methods are typically computationally demanding, contradicting the resource-efficient design goals of small models. To address these limitations, we propose two novel and efficient test-time scaling strategies that leverage the model-internal features rather than external supervision: (i) Test-Time Augmentation (TTAug), which generates multiple augmented inputs and aggregates outputs at the token level without parameter updates, and (ii) Test-Time Adaptation (TTAdapt), which adapts model parameters during inference using consensus-based pseudolabels from TTAug. Through extensive experiments across nine benchmarks, we demonstrate consistent performance improvements while maintaining computational efficiency suitable for resource-constrained environments. The generality of our approach is demonstrated both within models at different scales and across different VLMs without additional tuning.

---

Record id: `title:9fd38a270d13bf45`
