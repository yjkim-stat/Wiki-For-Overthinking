<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute-Optimal Scaling for Value-Based Deep RL

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119555>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An empirical study of how to split a fixed training-compute budget between model capacity and update-to-data ratio in online value-based deep RL, identifying a TD-overfitting effect that makes the best batch size depend on model size.

## Problem

Compute-optimal scaling recipes are well studied for language model pretraining but not for online value-based RL, which has two distinct allocation axes: model capacity and the update-to-data (UTD) ratio. Given a fixed compute budget, how those should be partitioned to maximise data efficiency was open.

## Contributions

- Identification and naming of TD-overfitting: increasing batch size harms Q-function accuracy for small models but not for large ones
- A fitted predictive law for the best batch size as a function of UTD ratio and model size
- A fitted data-efficiency law giving samples-to-performance as a function of UTD ratio and model size, yielding power-law rules for allocating a compute budget between UTD and capacity
- An empirical sweep over 17 control tasks with BRO and SimbaV2 supporting the above

## Method

The authors sweep model size, batch size and UTD ratio for SAC-style value-based agents (BRO, SimbaV2) on simulated control tasks and fit predictive relationships to the sweep. Two fitted forms are reported: a best-batch-size law B(sigma, N) as a function of UTD ratio sigma and model size N, and a data-efficiency law D_J(sigma, N) for the samples needed to reach a target return J, from which optimal UTD and model size are read off as power laws in the compute budget. The central empirical mechanism is TD-overfitting: raising the batch size quickly degrades Q-function accuracy for small models but not for large ones, because low-capacity networks produce poor-quality TD targets that generalise badly. The practical consequence is that batch size should grow with model size and shrink as the UTD ratio rises.

## Results

Evaluated on 17 simulated continuous-control tasks: 13 from the DeepMind Control Suite (split into 7 medium and 6 hard) and 4 from HumanoidBench, using BRO and SimbaV2. The paper reports fitted scaling forms rather than a single headline benchmark number; no accuracy or reward figure is quoted in the supplied material.

## Limitations

The authors state they were limited in how many variables they could study because each additional variable requires a higher-dimensional grid search, and that the study covers only simulated robotic control tasks, with visual and language domains left to future work. A reader should also note that the fitted laws are extrapolated from a sweep over two SAC-derived architectures, so their transfer to other value-based algorithms is untested here.

## Why it matters here

- **overthinking**: Tangential: this matched only on the keyword 'compute-optimal'. The compute being scaled is training compute for an online value-based RL agent (model capacity vs update-to-data ratio), not test-time reasoning compute in a language model, and nothing here concerns reasoning length, when a model should stop generating, or the accuracy/efficiency tradeoff of a chain of thought. The only loose conceptual echo is that both literatures fit budget-allocation laws; the paper offers no evidence bearing on overthinking and should not be cited for it.

## Entities

- **Concepts**: [compute-optimal scaling](../../../../wiki/concepts/compute-optimal-scaling.md), TD-overfitting, update-to-data ratio, batch size / model size interaction, data efficiency scaling law
- **Methods**: BRO, SimbaV2, Soft Actor-Critic (SAC), TD learning, update-to-data (UTD) ratio sweeps
- **Datasets**: DeepMind Control Suite (13 tasks), HumanoidBench (4 tasks)

Tags: `reinforcement-learning`, `scaling-laws`, `compute-optimal`, `td-learning`, `batch-size`, `continuous-control`

## Abstract

Abstract As models grow larger and training them becomes expensive, it becomes increasingly important to scale training recipes not just to larger models and more data, but to do so in a compute-optimal manner that extracts maximal performance per unit of compute. While such scaling has been well studied for language modeling, reinforcement learning (RL) has received less attention in this regard. In this paper, we investigate compute scaling for online, value-based deep RL. These methods present two primary axes for compute allocation: model capacity and the update-to-data (UTD) ratio. Given a fixed compute budget, we ask: how should resources be partitioned across these axes to maximize data efficiency? Our analysis reveals a nuanced interplay between model size, batch size, and UTD. In particular, we identify a phenomenon we call TD-overfitting: increasing the batch quickly harms Q-function accuracy for small models, but this effect is absent in large models, enabling effective use of large batch size at scale. We provide a mental model for understanding this phenomenon and build guidelines for choosing batch size and UTD to optimize compute usage. Our findings provide a grounded starting point for compute-optimal scaling in deep RL, mirroring studies in supervised learning but adapted to TD learning. Project page: https://value-scaling.github.io/.

---

Record id: `title:d5d62f18a483fc4a`
