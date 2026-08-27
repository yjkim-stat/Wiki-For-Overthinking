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

Introduces Test-Time Augmentation (TTAug) and Test-Time Adaptation (TTAdapt), two test-time scaling methods designed for small vision-language models, giving consistent gains across nine benchmarks without additional tuning.

## Problem

Small vision-language models are computationally efficient but generalize more weakly than larger ones, and prior test-time-scaling methods are typically not designed for resource-constrained small-VLM settings.

## Contributions

- TTAug, token-level aggregation over multiple augmented inputs with no parameter updates
- TTAdapt, inference-time parameter adaptation via consensus-based pseudolabels
- consistent gains across nine benchmarks and multiple small VLMs without additional tuning

## Method

TTAug generates multiple augmented inputs and aggregates outputs at the token level without any parameter updates; TTAdapt adapts model parameters during inference using consensus-based pseudolabels derived from the model's own outputs.

## Results

Across nine benchmarks and multiple VLMs of different scales, both methods yield consistent performance gains while maintaining computational efficiency, generalizing without requiring additional tuning.

## Limitations

Not stated in the fetched abstract; no discussion of the added inference-time cost of augmentation/adaptation relative to the baseline small-VLM cost.

## Why it matters here

- **overthinking**: Relevant as a resource-constrained variant of test-time scaling: it targets small VLMs rather than reasoning-length-heavy LRMs, but demonstrates that test-time compute methods can be made efficient enough for small models -- a useful data point for where the accuracy/efficiency tradeoff sits when the base model itself is already cheap.

## Entities

- **Concepts**: Test-Time Augmentation (TTAug), Test-Time Adaptation (TTAdapt), consensus-based pseudolabeling
- **Methods**: Test-Time Augmentation, Test-Time Adaptation, consensus pseudolabeling
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `vision-language-models`, `small-models`, `test-time-adaptation`

---

Record id: `title:9fd38a270d13bf45`
