<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116215>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SolverLLM is a training-free test-time-scaling framework that solves optimization problems by having an LLM generate mathematical formulations and translate them into solver-ready code, guided by a modified Monte Carlo Tree Search with dynamic expansion, prompt backpropagation, and uncertainty backpropagation.

## Problem

Existing LLM approaches to optimization problems either rely on prompt engineering, which generalizes poorly across problem types, or require costly supervised training on solver-formulation pairs.

## Contributions

- SolverLLM, a training-free framework generating solver-ready formulations rather than direct answers for optimization problems
- a modified MCTS with dynamic expansion, prompt backpropagation, and uncertainty backpropagation for guided search
- outperformance of both prompt-based and learning-based baselines on six benchmarks without additional training

## Method

SolverLLM generates a mathematical formulation of the problem and translates it into solver-ready code rather than solving directly, guided by a modified Monte Carlo Tree Search (MCTS) with three enhancements: dynamic expansion for adaptive formulation generation, prompt backpropagation to guide exploration via outcome-driven feedback, and uncertainty backpropagation to incorporate reward reliability into the search decisions.

## Results

Across six standard benchmark datasets, SolverLLM outperforms both prompt-based and learning-based baselines, achieving strong generalization across problem types without additional training.

## Limitations

Not stated in the fetched abstract beyond the six benchmark datasets tested; the training-free framing implies dependence on the underlying LLM's formulation quality, which is not discussed.

## Why it matters here

- **overthinking**: Indirectly relevant: an example of test-time scaling that spends inference compute on structured search (MCTS over formulations) rather than a single long chain-of-thought, illustrating an alternative use of test-time compute budget distinct from -- and potentially more efficient than -- simply generating a longer reasoning trace.

## Entities

- **Concepts**: formulate-then-solve via LLM-guided search, Monte Carlo Tree Search for test-time scaling, prompt/uncertainty backpropagation in search
- **Methods**: [Monte Carlo Tree Search (MCTS)](../../../../wiki/methods/monte-carlo-tree-search-mcts.md), LLM-guided search, test-time scaling
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `optimization`, `monte-carlo-tree-search`, `training-free`

## Abstract

Abstract Large Language Models (LLMs) offer promising capabilities for tackling complex reasoning tasks, including optimization problems. However, existing methods either rely on prompt engineering, which leads to poor generalization across problem types, or require costly supervised training. We introduce SolverLLM, a training-free framework that leverages test-time scaling to solve diverse optimization problems. Rather than solving directly, SolverLLM generates mathematical formulations and translates them into solver-ready code, guided by a novel Monte Carlo Tree Search (MCTS) strategy. To enhance the search process, we modify classical MCTS with (1) dynamic expansion for adaptive formulation generation, (2) prompt backpropagation to guide exploration via outcome-driven feedback, and (3) uncertainty backpropagation to incorporate reward reliability into decision-making. Experiments on six standard benchmark datasets demonstrate that SolverLLM outperforms both prompt-based and learning-based baselines, achieving strong generalization without additional training.

---

Record id: `title:e149fd58642147ea`
