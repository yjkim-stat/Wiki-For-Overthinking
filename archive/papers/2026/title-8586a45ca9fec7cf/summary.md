<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Causal Dependency-Aware Unsupervised Routing for Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64247>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes an unsupervised router that picks which large reasoning model should answer a query by separately estimating its reasoning quality and answer quality from the causal relationship between the two, without human preference labels.

## Problem

Supervised routing among LLMs/LRMs requires large amounts of expensive human-annotated preference data and degrades under distribution shift; routing among Large Reasoning Models specifically is complicated by their variable-length reasoning traces.

## Contributions

- ReasoningRouter, an unsupervised query router for Large Reasoning Models that avoids the need for expensive human-annotated preference data.
- A length-balanced embedding strategy intended to handle the variable-length reasoning traces produced by LRMs.
- A probabilistic model built on a 'Causal Triangulation Property' that gives label-free estimates of reasoning quality and answer quality separately.

## Method

The router embeds queries using a length-balanced embedding strategy so that routing decisions are not skewed by the varying length of LRM reasoning traces. It then fits a probabilistic model of the causal relationship between a model's thinking (reasoning trace) and its final answer, exploiting a 'Causal Triangulation Property' to estimate reasoning quality and answer quality separately without labeled preference data, and uses these estimates to route each query to the most suitable model.

## Results

No specific benchmark numbers were available in the retrieved material (no PDF or numeric results found on the paper's ICML page); the paper claims the method is computationally efficient and gives insight into model behavior through separate reasoning/answer quality estimates.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. This is a model-selection/routing method that happens to be built for Large Reasoning Models and touches the relationship between a model's thinking trace and its answer, but its goal is choosing which model handles a query, not deciding how long a given model should reason or trading off reasoning length against accuracy/efficiency.

## Entities

- **Concepts**: unsupervised model routing, causal triangulation property, length-balanced embeddings, reasoning vs. answer quality separation
- **Methods**: ReasoningRouter, causal triangulation, length-balanced embedding
- **Datasets**: _none recorded_

Tags: `routing`, `unsupervised`, `model-selection`, `causal-inference`

---

Record id: `title:8586a45ca9fec7cf`
