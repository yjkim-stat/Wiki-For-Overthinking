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

Studies compute-optimal scaling for online value-based deep RL along the model-capacity and update-to-data (UTD) ratio axes, identifying a 'TD-overfitting' phenomenon where larger batch sizes harm small models' Q-function accuracy but not large ones, enabling large-batch efficiency at scale.

## Problem

Compute-optimal scaling is well studied for language modeling but not for value-based deep reinforcement learning, which has two primary compute-allocation axes (model capacity and update-to-data ratio) whose optimal partitioning under a fixed budget was unclear.

## Contributions

- identification of TD-overfitting, where large batch sizes harm Q-function accuracy for small but not large models
- guidelines for partitioning compute between model capacity and UTD ratio in value-based deep RL
- a compute-optimal-scaling analysis for TD learning analogous to supervised-learning scaling studies

## Method

Investigates compute scaling for online value-based deep RL along the model-capacity and UTD-ratio axes, analyzing the interplay between model size, batch size, and UTD ratio under a fixed compute budget to determine how resources should be partitioned to maximize data efficiency.

## Results

Identifies 'TD-overfitting': increasing batch size quickly harms Q-function accuracy for small models, but this effect is absent in large models, which can therefore use large batch sizes effectively at scale; the paper provides a mental model for this phenomenon and guidelines for choosing batch size and UTD ratio to optimize compute usage, mirroring supervised-learning compute-optimal scaling but adapted to TD learning.

## Limitations

Not stated in the fetched abstract beyond the online, value-based deep RL setting studied.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is about training-compute allocation (model size vs. batch/UTD ratio) for value-based deep RL agents, unconnected to inference-time reasoning length or test-time compute for LLM reasoning.

## Entities

- **Concepts**: TD-overfitting, update-to-data (UTD) ratio, compute-optimal scaling for deep RL
- **Methods**: value-based deep reinforcement learning, compute-optimal scaling analysis
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `compute-optimal`, `scaling-laws`, `TD-learning`

## Abstract

Abstract As models grow larger and training them becomes expensive, it becomes increasingly important to scale training recipes not just to larger models and more data, but to do so in a compute-optimal manner that extracts maximal performance per unit of compute. While such scaling has been well studied for language modeling, reinforcement learning (RL) has received less attention in this regard. In this paper, we investigate compute scaling for online, value-based deep RL. These methods present two primary axes for compute allocation: model capacity and the update-to-data (UTD) ratio. Given a fixed compute budget, we ask: how should resources be partitioned across these axes to maximize data efficiency? Our analysis reveals a nuanced interplay between model size, batch size, and UTD. In particular, we identify a phenomenon we call TD-overfitting: increasing the batch quickly harms Q-function accuracy for small models, but this effect is absent in large models, enabling effective use of large batch size at scale. We provide a mental model for understanding this phenomenon and build guidelines for choosing batch size and UTD to optimize compute usage. Our findings provide a grounded starting point for compute-optimal scaling in deep RL, mirroring studies in supervised learning but adapted to TD learning. Project page: https://value-scaling.github.io/.

---

Record id: `title:d5d62f18a483fc4a`
