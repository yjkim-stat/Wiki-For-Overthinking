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

An analytically solvable three-parameter neural scaling model is used to derive the loss curve of one-pass SGD on a mean-squared objective and to partition the data-complexity/target-complexity plane into 4 phases (plus 3 subphases), each with its own scaling-law exponent for the compute-optimal parameter count.

## Problem

Compute-optimal scaling laws of the Chinchilla kind are fitted empirically: the optimal model-parameter-count as a function of the FLOP budget is read off from training runs rather than derived. The paper addresses the compute-limited, infinite-data regime and asks what the optimal parameter count is as a function of compute when the answer can be proved rather than fitted, and what determines whether one regime or another holds.

## Contributions

- A representation of the one-pass-SGD loss curve for the solvable scaling model that holds at all iteration counts and improves with parameter count.
- Identification of 4 phases and 3 subphases in the data-complexity/target-complexity plane, with boundaries determined by model capacity, optimizer noise and feature embedding.
- Scaling-law exponents in every phase, with proof and numerical evidence, including the compute-optimal parameter count as a function of FLOP budget.
- nanoChinchilla, a colab notebook reproducing some key results.

## Method

The authors take a solvable neural scaling model parameterised by data complexity, target complexity and model-parameter-count, and train it with one-pass (single-epoch) stochastic gradient descent on a mean-squared loss. They derive a representation of the loss curve that is valid at all iteration counts and becomes more accurate as the parameter count grows. From that representation they analyse the compute-optimal parameter count and show that the data-complexity/target-complexity phase plane splits into 4 phases with 3 further subphases, with boundaries set by the relative importance of three effects: model capacity, optimizer noise, and the embedding of the features. Scaling-law exponents in each phase, including the optimal parameter count as a function of the FLOP budget, are established with mathematical proof and numerical evidence. A colab notebook, nanoChinchilla, reproduces some of the results.

## Results

_not recorded_

## Limitations

The result is derived inside one solvable model trained by one-pass SGD on a mean-squared loss; the abstract does not claim the phase structure has been checked against a transformer or any real training run, and the loss-curve representation is stated to be accurate only in the limit of growing parameter count. The abstract reports no benchmark numbers.

## Why it matters here

- **overthinking**: Not relevant - this is a false positive. The task was queued on the keyword 'compute-optimal', which in this paper means the training-time allocation between model-parameter-count and FLOP budget in the Chinchilla sense, under one-pass SGD on infinite data. This topic is about test-time compute: how long a reasoning trace should be for a given problem and when a model should stop. The two share only the phrase. The paper contains no language model, no reasoning trace, no inference-time budget and no accuracy/length tradeoff; its phases are regions of a data-complexity/target-complexity plane for pretraining, not regimes of reasoning effort. Nothing here should be cited in the topic's notes, and the concept vocabulary it introduces (data complexity, target complexity, optimizer noise) does not transfer to the test-time setting.

## Entities

- **Concepts**: Compute-optimal scaling law, Data complexity, Target complexity, Optimizer noise, Phase diagram of scaling exponents, Infinite-data regime
- **Methods**: solvable neural scaling model, one-pass stochastic gradient descent, nanoChinchilla
- **Datasets**: _none recorded_

Tags: `scaling-laws`, `compute-optimal`, `pretraining`, `sgd`, `theory`, `phase-diagram`, `false-positive`, `neurips2024`

## Abstract

Abstract We consider the solvable neural scaling model with three parameters: data complexity, target complexity, and model-parameter-count. We use this neural scaling model to derive new predictions about the compute-limited, infinite-data scaling law regime. To train the neural scaling model, we run one-pass stochastic gradient descent on a mean-squared loss. We derive a representation of the loss curves which holds over all iteration counts and improves in accuracy as the model parameter count grows. We then analyze the compute-optimal model-parameter-count, and identify 4 phases (+3 subphases) in the data-complexity/target-complexity phase-plane. The phase boundaries are determined by the relative importance of model capacity, optimizer noise, and embedding of the features. We furthermore derive, with mathematical proof and extensive numerical evidence, the scaling-law exponents in all of these phases, in particular computing the optimal model-parameter-count as a function of floating point operation budget. We include a colab notebook https://tinyurl.com/2saj6bkj, nanoChinchilla, that reproduces some key results of the paper.

---

Record id: `title:fde0b046e948bb47`
