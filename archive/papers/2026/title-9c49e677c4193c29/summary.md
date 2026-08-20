<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ETS: Energy-Guided Test-Time Scaling for Training-Free RL Alignment

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61604>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ETS samples directly from an implicit RL-optimal policy at inference time via energy-guided decoding, aiming to reach RL-alignment quality without RL fine-tuning.

## Problem

RL post-training alignment for language models is effective but costly and unstable to train because of its complicated training process; the paper asks whether the same aligned behavior can be reached at inference time instead, without training an RL policy.

## Contributions

- Proposes sampling directly from an implicit RL-optimal policy at inference instead of running RL fine-tuning
- Combines a reference policy model with an energy term over masked language modeling, estimated via online Monte Carlo sampling with convergence guarantees
- Adds acceleration and importance-sampling techniques to keep inference latency practical
- Shows consistent generation-quality improvements across reasoning, coding, and science benchmarks compared to baselines

## Method

ETS pairs a reference policy model with an energy term applied via masked language modeling to approximate sampling from the optimal RL-aligned policy without training. The energy component is estimated online via Monte Carlo sampling with provable convergence guarantees, and acceleration plus importance-sampling techniques are used to make the resulting inference-time sampling procedure fast enough to be practical.

## Results

Consistent generation-quality improvements over baseline approaches across reasoning, coding, and science benchmarks; no specific numeric deltas were found in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: 'test-time scaling' here refers to inference-time energy-guided sampling that substitutes for RL fine-tuning to reach an aligned policy, not to allocating or trimming chain-of-thought length. It does not address overthinking, underthinking, or stopping criteria in reasoning.

## Entities

- **Concepts**: energy-based models, training-free alignment, online Monte Carlo estimation
- **Methods**: Energy-Guided Test-Time Scaling (ETS), energy-based sampling, online Monte Carlo estimation, importance sampling
- **Datasets**: _none recorded_

Tags: `alignment`, `training-free`, `energy-guided`, `test-time-scaling`

---

Record id: `title:9c49e677c4193c29`
