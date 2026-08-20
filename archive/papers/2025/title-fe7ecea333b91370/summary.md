<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Kinetics: Rethinking Test-Time Scaling Law

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115931>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Reworks test-time scaling laws to account for memory-access cost alongside compute, finding a 14B-parameter threshold below which test-time compute is less effective, and shows sparse attention substantially improves accuracy under a fixed test-time budget.

## Problem

Prior test-time scaling laws are grounded purely in compute-optimality and ignore memory access bottlenecks from strategies like Best-of-N and long chain-of-thought, leading to an overestimate of how effective smaller models are when given more test-time compute.

## Contributions

- Shows prior compute-optimal test-time scaling laws overestimate the effectiveness of smaller models by ignoring memory access costs from inference-time strategies like Best-of-N and long CoT
- Proposes the Kinetics Scaling Law, incorporating both computation and memory access costs, spanning models from 0.6B to 32B parameters
- Identifies attention (not parameter count) as the dominant cost factor in test-time scaling and proposes a sparse-attention scaling paradigm to lower per-token cost

## Method

Performs a holistic efficiency analysis of test-time scaling across model sizes (0.6B-32B) that accounts for both FLOPs and memory access costs from inference-time strategies such as Best-of-N sampling and long chain-of-thought generation. This yields the Kinetics Scaling Law, which shows test-time compute is more effective on models above roughly 14B parameters, since attention cost (not parameter count) dominates at test time. Based on this, proposes using sparse attention to reduce per-token cost, allowing longer generations and more parallel samples within the same compute budget.

## Results

Sparse attention models achieve over 60-point accuracy gains in low-cost regimes and over 5-point gains in high-cost regimes on AIME and LiveCodeBench compared to dense counterparts; the Kinetics Scaling Law shows test-time compute is more effective above a 14B-parameter threshold.

## Limitations

Analysis spans models from 0.6B to 32B parameters; abstract does not specify hardware assumptions in detail or discuss whether findings generalize beyond the tested model family/sizes.

## Why it matters here

- **overthinking**: Directly studies the accuracy/efficiency tradeoff of test-time compute scaling, including long chain-of-thought generation length and Best-of-N sampling, and shows that attention cost rather than parameter count governs the true cost of 'thinking longer,' which reshapes how much test-time compute (reasoning length or samples) is worth allocating to a given model.

## Entities

- **Concepts**: Kinetics Scaling Law, memory access bottleneck, sparse attention, compute-optimality vs practical efficiency
- **Methods**: Kinetics Scaling Law, sparse attention, Best-of-N sampling analysis
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `test-time-scaling`, `scaling-law`, `sparse-attention`, `memory-access-cost`, `best-of-n`, `chain-of-thought-length`

## Abstract

Abstract We rethink test-time scaling laws from a practical efficiency perspective, revealing that the effectiveness of smaller models is significantly overestimated. Prior work, grounded in compute-optimality, overlooks critical memory access bottlenecks introduced by inference-time strategies (e.g., Best-of-N, long CoTs). Our holistic analysis, spanning models from 0.6B to 32B parameters, reveals a new Kinetics Scaling Law that better guides resource allocation by incorporating both computation and memory access costs. The Kinetics Scaling Law suggests that test-time compute is more effective when used on models above a threshold (14B) than on smaller ones. A key reason is that in test-time scaling, attention—rather than parameter count—emerges as the dominant cost factor. Motivated by this, we propose a new scaling paradigm centered on sparse attention, which lowers per-token cost and enables longer generations and more parallel samples within the same resource budget. Empirically, we show that sparse attention models consistently outperform dense counterparts, achieving over 60-point gains in low-cost regimes and over 5-point gains in high-cost regimes for problem-solving accuracy on AIME and LiveCodeBench. These results suggest that sparse attention is essential for realizing the full potential of test-time scaling because, unlike training where parameter scaling saturates, test-time accuracy continues to improve through increased generation.

---

Record id: `title:fe7ecea333b91370`
