<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Every Rollout Counts: Optimal Resource Allocation for Efficient Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115239>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Formulates test-time search as a resource-allocation problem and introduces DORA, which allocates a fixed rollout budget across reasoning directions rather than individual solutions to avoid wasting compute on over-represented directions.

## Problem

How to allocate a fixed rollout budget most effectively during test-time search is underexplored, and existing solution-level allocation strategies favor reasoning directions with more candidate solutions, leading to theoretically suboptimal and inefficient use of test-time compute.

## Contributions

- Formulates test-time search under a fixed rollout budget as a resource-allocation problem and derives the allocation that maximizes probability of a correct solution
- Identifies that existing solution-level allocation is biased toward reasoning directions with more candidates, making it theoretically suboptimal
- Proposes Direction-Oriented Resource Allocation (DORA), which decouples direction quality from candidate count and allocates resources at the direction level

## Method

The paper models test-time search (allocating a fixed number of rollouts across candidate reasoning paths) as a resource-allocation problem and derives the theoretically optimal allocation strategy. It shows existing solution-level allocation methods are biased toward reasoning directions that happen to spawn more candidate solutions, wasting compute. DORA instead allocates the rollout budget at the level of reasoning directions rather than individual solutions, decoupling a direction's estimated quality from how many candidates it produced.

## Results

DORA consistently outperforms strong baselines at comparable computational cost on MATH500, AIME2024 and AIME2025, achieving state-of-the-art accuracy among methods tested under the same rollout budget.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly tackles the accuracy/efficiency tradeoff of test-time compute scaling: it derives the provably optimal way to spend a fixed rollout budget across reasoning paths, showing that naive allocation wastes compute on directions with more candidates rather than higher quality.

## Entities

- **Concepts**: test-time search as resource allocation, direction-level vs. solution-level allocation, rollout budget
- **Methods**: Direction-Oriented Resource Allocation (DORA)
- **Datasets**: MATH500, AIME2024, AIME2025

Tags: `test-time-scaling`, `resource-allocation`, `rollout-budget`, `search`

## Abstract

Abstract Test-Time Scaling (TTS) improves the performance of Large Language Models (LLMs) by using additional inference-time computation to explore multiple reasoning paths through search. Yet how to allocate a fixed rollout budget most effectively during search remains underexplored, often resulting in inefficient use of compute at test time. To bridge this gap, we formulate test-time search as a resource allocation problem and derive the optimal allocation strategy that maximizes the probability of obtaining a correct solution under a fixed rollout budget. Within this formulation, we reveal a core limitation of existing search methods: solution-level allocation tends to favor reasoning directions with more candidates, leading to theoretically suboptimal and inefficient use of compute. To address this, we propose Direction-Oriented Resource Allocation (DORA), a provably optimal method that mitigates this bias by decoupling direction quality from candidate count and allocating resources at the direction level. To demonstrate DORA’s effectiveness, we conduct extensive experiments on challenging mathematical reasoning benchmarks including MATH500, AIME2024, and AIME2025. The empirical results show that DORA consistently outperforms strong baselines with comparable computational cost, achieving state-of-the-art accuracy. We hope our findings contribute to a broader understanding of optimal TTS for LLMs.

---

Record id: `title:69246b2008f8e22d`
