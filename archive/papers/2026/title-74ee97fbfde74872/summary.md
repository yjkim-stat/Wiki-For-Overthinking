<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Understanding the Role of Training Data in Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008915>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

A theoretical and empirical study of when test-time scaling helps versus hurts, showing it depends on whether the training data's tasks are diverse and hard enough to cover the skills a downstream problem requires.

## Problem

It is unclear what conditions in training data cause long chain-of-thought test-time scaling to emerge and actually improve performance, versus scaling test-time compute doing nothing or hurting.

## Contributions

- A theoretical analysis of test-time scaling for transformers trained on an in-context weight-prediction task for linear regression.
- Shows that, at fixed test error, more test-time compute can substitute for fewer in-context examples (shorter context length) at training time.
- Shows that test-time compute can harm performance when the skills required for a downstream task are not sufficiently represented in the training data.
- Characterizes task hardness via the smallest eigenvalue of the task's feature covariance matrix and shows diverse, relevant, hard training tasks give the best test-time scaling behavior.
- Confirms the theoretical findings with experiments on large, nonlinear transformer architectures.

## Method

The authors analyze transformers trained on an in-context weight-prediction task for linear regression, studying how test-time compute (more in-context reasoning/computation) interacts with the training data's task diversity and context length. They derive theoretical conditions under which increasing test-time compute helps or hurts, using the smallest eigenvalue of a task's feature covariance matrix as a measure of task hardness, and validate the theory with experiments on large nonlinear transformers.

## Results

At fixed test error, increasing test-time compute allows reducing the number of in-context training examples; when training-data skill coverage is insufficient for a downstream task, increasing test-time compute degrades performance; training on tasks with a smaller smallest-eigenvalue feature covariance (harder, diverse tasks) yields the best test-time scaling. These findings are confirmed experimentally on large nonlinear transformers, though no specific accuracy numbers are given in the abstract.

## Limitations

The abstract does not state which nonlinear transformer architectures or benchmark tasks were used to confirm the theory, nor does it report specific numeric results from those confirmatory experiments.

## Why it matters here

- **overthinking**: Gives a training-data-side theoretical account of why more test-time compute is not uniformly beneficial: it explains a condition (insufficient task diversity/hardness in training data) under which scaling test-time compute actively harms performance, directly bearing on when a model should or should not be pushed to think longer.

## Entities

- **Concepts**: in-context learning of linear regression, task hardness via smallest eigenvalue of feature covariance, test-time compute vs. training-data coverage tradeoff
- **Methods**: in-context weight prediction (linear regression), transformer architectures
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `theory`, `in-context-learning`, `training-data`, `task-hardness`

## Abstract

Abstract Test-time scaling improves the reasoning capabilities of large language models (LLMs) by allocating extra compute to generate longer Chains-of-Thoughts (CoTs). This enables models to tackle more complex problem by breaking them down into additional steps, backtracking, and correcting mistakes. Despite its strong performance--demonstrated by OpenAI's o1 and DeepSeek R1, the conditions in the training data under which long CoTs emerge, and when such long CoTs improve the performance, remain unclear. In this paper, we study the performance of test-time scaling for transformers trained on an in-context weight prediction task for linear regression. Our analysis provides a theoretical explanation for several intriguing observations: First, at any fixed test error, increasing test-time compute allows us to reduce the number of in-context examples (context length) in training prompts. Second, if the skills required to solve a downstream task are not sufficiently present in the training data, increasing test-time compute can harm performance. Finally, we characterize task hardness via the smallest eigenvalue of its feature covariance matrix and show that training on a diverse, relevant, and hard set of tasks results in best performance for test-time scaling. We confirm our findings with experiments on large, nonlinear transformer architectures.

---

Record id: `title:74ee97fbfde74872`
