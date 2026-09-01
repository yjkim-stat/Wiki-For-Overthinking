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

ETS enables training-free sampling from an optimal RL-aligned policy by combining a reference model with an energy term over Masked Language Modeling, estimating the energy via online Monte Carlo with a provable convergence rate, and using acceleration frameworks plus importance sampling to substantially reduce inference latency while provably preserving sampling quality on both autoregressive and diffusion language models.

## Problem

Sampling from the policy that would result from RL alignment normally requires actually performing the RL training, which is costly; a training-free way to sample from (or approximate) that optimal policy, applicable across both autoregressive and diffusion language models, was not established with provable guarantees.

## Contributions

- a training-free method (ETS) for sampling from an optimal RL-aligned policy by combining a reference model with an energy term over Masked Language Modeling
- an online Monte Carlo energy estimator with a provable convergence rate
- acceleration and importance-sampling techniques provably preserving sampling quality while substantially reducing inference latency, validated across reasoning, coding and science benchmarks on both autoregressive and diffusion LMs

## Method

Combines a fixed reference policy model with an energy term applied via Masked Language Modeling to define an implicit target distribution corresponding to the optimal RL-aligned policy; estimates the energy component using online Monte Carlo estimation with a provable convergence rate; incorporates modern acceleration frameworks and importance sampling estimators to reduce the inference latency of sampling from this implicit distribution while provably preserving sampling quality.

## Results

Testing across reasoning, coding, and science benchmarks shows consistent generation-quality improvements for both autoregressive and diffusion language models, substantially reducing inference latency versus a naive implementation while provably preserving sampling quality.

## Limitations

Not stated in the fetched abstract beyond the reasoning/coding/science benchmark scope and the autoregressive/diffusion model classes tested.

## Why it matters here

- **overthinking**: Indirectly relevant: a test-time-scaling method for training-free RL alignment (approximating an aligned policy's sampling distribution without actually running RL) rather than a reasoning-length control method, but it is evaluated on reasoning benchmarks and offers an alternative, provably-quality-preserving lever for improving generation quality at inference time without the cost of RL training.

## Entities

- **Concepts**: energy-guided training-free RL alignment, online Monte Carlo energy estimation, importance-sampling acceleration for policy sampling
- **Methods**: ETS (Energy-Guided Test-time Scaling), online Monte Carlo estimation, importance sampling
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `training-free-alignment`, `energy-based-models`, `diffusion-language-models`

---

Record id: `title:9c49e677c4193c29`
