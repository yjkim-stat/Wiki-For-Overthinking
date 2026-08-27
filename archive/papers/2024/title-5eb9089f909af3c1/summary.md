<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/94731>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows that a constant-learning-rate-with-cooldown schedule scales as predictably and reliably as the standard cosine schedule for LLM pretraining, letting scaling-law experiments reuse partial training runs across durations and cut required compute.

## Problem

Scaling-law research has relied on the cosine learning-rate schedule, which requires committing to a fixed training length in advance and prevents reusing a single run to study multiple training durations for the same model size, adding needless complexity and compute cost.

## Contributions

- shows constant-LR-with-cooldown scaling matches cosine-schedule scaling reliability
- shows SWA improves performance along the training trajectory at no added cost, across scales
- a practical reduction in compute/GPU-hours needed for scaling-law research via reusable training runs

## Method

Investigates constant learning rate with cooldowns as a direct alternative to cosine scheduling, and separately evaluates stochastic weight averaging (SWA) along the training trajectory, across multiple model scales.

## Results

Constant-learning-rate-with-cooldowns scales predictably and reliably, similarly to cosine scheduling; stochastic weight averaging improves performance along the training trajectory at no additional training cost across scales; together these let scaling experiments reuse fewer, reusable training runs, reducing compute and GPU-hours needed.

## Limitations

Not stated in the fetched abstract beyond the pretraining-schedule scope; no discussion of downstream task types where the finding might not hold.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is about LLM pretraining schedule design and scaling-law methodology, unconnected to inference-time reasoning length or test-time compute.

## Entities

- **Concepts**: constant learning rate with cooldown, stochastic weight averaging (SWA), scaling-law experiment design
- **Methods**: constant learning rate with cooldown, cosine learning-rate schedule, stochastic weight averaging
- **Datasets**: _none recorded_

Tags: `scaling-laws`, `learning-rate-schedule`, `compute-efficiency`, `pretraining`

## Abstract

Abstract Scale has become a main ingredient in obtaining strong machine learning models. As a result, understanding a model's scaling properties is key to effectively designing both the right training setup as well as future generations of architectures. In this work, we argue that scale and training research has been needlessly complex due to reliance on the cosine schedule, which prevents training across different lengths for the same model size. We investigate the training behavior of a direct alternative --- constant learning rate and cooldowns --- and find that it scales predictably and reliably similar to cosine. Additionally, we show that stochastic weight averaging yields improved performance along the training trajectory, without additional training costs, across different scales. Importantly, with these findings we demonstrate that scaling experiments can be performed with significantly reduced compute and GPU hours by utilizing fewer but reusable training runs. Our code is available at https://github.com/epfml/schedules-and-scaling/.

---

Record id: `title:5eb9089f909af3c1`
