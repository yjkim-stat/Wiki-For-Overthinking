<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# 4+3 Phases of Compute-Optimal Neural Scaling Laws

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/94549>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Analyzes a solvable three-parameter neural scaling model (data complexity, target complexity, model-parameter-count) to derive the compute-optimal model size in the compute-limited, infinite-data regime, identifying 4 phases (+3 subphases) with proven scaling-law exponents in each.

## Problem

A rigorous, provable characterization of compute-optimal model-parameter-count as a function of compute budget, across different regimes of data and target complexity, was lacking for neural scaling laws.

## Contributions

- a solvable three-parameter neural scaling model with a loss-curve representation valid across all iteration counts
- identification and proof of 4 phases (+3 subphases) governing compute-optimal scaling behavior
- derived, proven scaling-law exponents and optimal model-parameter-count as a function of compute budget in each phase

## Method

Uses a solvable neural scaling model parameterized by data complexity, target complexity, and model-parameter-count, trained via one-pass stochastic gradient descent on mean-squared loss, deriving a representation of the loss curve valid across all iteration counts that improves in accuracy as parameter count grows; analyzes the compute-optimal model-parameter-count across the data-complexity/target-complexity phase plane.

## Results

Identifies 4 phases (plus 3 subphases) in the data-complexity/target-complexity phase plane, with boundaries determined by the relative importance of model capacity, optimizer noise, and feature embedding; derives, with mathematical proof and extensive numerical evidence, the scaling-law exponents in every phase, including the optimal model-parameter-count as a function of floating-point-operation budget; provides a companion notebook reproducing key results.

## Limitations

Not stated in the fetched abstract beyond the solvable model's assumptions (one-pass SGD, mean-squared loss); applicability to real large-scale training dynamics beyond this idealized model is not discussed in the excerpt retrieved.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is a theoretical analysis of pretraining-compute-vs-model-size scaling laws, unconnected to inference-time reasoning length or test-time compute for LLM reasoning.

## Entities

- **Concepts**: compute-optimal model-parameter-count, neural scaling-law phase diagram, data/target-complexity parameterization
- **Methods**: solvable neural scaling model, one-pass stochastic gradient descent theory
- **Datasets**: _none recorded_

Tags: `scaling-laws`, `compute-optimal`, `theory`, `neural-scaling`

## Abstract

Abstract We consider the solvable neural scaling model with three parameters: data complexity, target complexity, and model-parameter-count. We use this neural scaling model to derive new predictions about the compute-limited, infinite-data scaling law regime. To train the neural scaling model, we run one-pass stochastic gradient descent on a mean-squared loss. We derive a representation of the loss curves which holds over all iteration counts and improves in accuracy as the model parameter count grows. We then analyze the compute-optimal model-parameter-count, and identify 4 phases (+3 subphases) in the data-complexity/target-complexity phase-plane. The phase boundaries are determined by the relative importance of model capacity, optimizer noise, and embedding of the features. We furthermore derive, with mathematical proof and extensive numerical evidence, the scaling-law exponents in all of these phases, in particular computing the optimal model-parameter-count as a function of floating point operation budget. We include a colab notebook https://tinyurl.com/2saj6bkj, nanoChinchilla, that reproduces some key results of the paper.

---

Record id: `title:fde0b046e948bb47`
