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

A training-free framework that uses MCTS-guided test-time search to turn optimization problems into solver-ready code instead of solving them directly.

## Problem

Existing LLM approaches to optimization problems either rely on prompt engineering, which generalizes poorly across problem types, or require costly supervised training; the paper wants a training-free method that generalizes across optimization problem types.

## Contributions

- Training-free framework (SolverLLM) that uses test-time scaling to solve diverse optimization problems without supervised training
- Generates mathematical formulations and translates them into solver-ready code rather than solving directly
- Modifies classical MCTS with dynamic expansion for adaptive formulation generation, prompt backpropagation for outcome-driven exploration, and uncertainty backpropagation that incorporates reward reliability
- Outperforms prompt-based and learning-based baselines on six standard benchmark datasets

## Method

SolverLLM does not solve an optimization problem directly; it generates a mathematical formulation of the problem and translates that formulation into solver-ready code, guided by a modified Monte Carlo Tree Search. The MCTS variant adds three components: dynamic expansion (adapts formulation generation during search), prompt backpropagation (propagates outcome-driven feedback to guide exploration), and uncertainty backpropagation (folds reward reliability into the search decisions).

## Results

The abstract states SolverLLM outperforms both prompt-based and learning-based baselines on six standard benchmark datasets and achieves strong generalization without additional training; no specific accuracy numbers are given in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Shares only the generic phrase 'test-time scaling' with the tracked topic. The paper uses MCTS-guided search at inference time to generate and refine solver code for combinatorial/mathematical optimization problems; it does not address reasoning-length overthinking or underthinking, stopping criteria, or the accuracy/efficiency tradeoff of an LLM's chain-of-thought length. The connection is tangential.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), Monte Carlo Tree Search for LLM search, solver-guided code generation
- **Methods**: Monte Carlo Tree Search (MCTS), SolverLLM
- **Datasets**: six standard optimization benchmark datasets (not individually named in the abstract)

Tags: `test-time-scaling`, `mcts`, `optimization`, `code-generation`, `tangential`

## Abstract

Abstract Large Language Models (LLMs) offer promising capabilities for tackling complex reasoning tasks, including optimization problems. However, existing methods either rely on prompt engineering, which leads to poor generalization across problem types, or require costly supervised training. We introduce SolverLLM, a training-free framework that leverages test-time scaling to solve diverse optimization problems. Rather than solving directly, SolverLLM generates mathematical formulations and translates them into solver-ready code, guided by a novel Monte Carlo Tree Search (MCTS) strategy. To enhance the search process, we modify classical MCTS with (1) dynamic expansion for adaptive formulation generation, (2) prompt backpropagation to guide exploration via outcome-driven feedback, and (3) uncertainty backpropagation to incorporate reward reliability into decision-making. Experiments on six standard benchmark datasets demonstrate that SolverLLM outperforms both prompt-based and learning-based baselines, achieving strong generalization without additional training.

---

Record id: `title:e149fd58642147ea`
