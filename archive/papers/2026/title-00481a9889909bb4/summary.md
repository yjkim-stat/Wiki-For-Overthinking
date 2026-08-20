<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010419>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces GrAlgoBench, a graph-algorithm-problem benchmark that exposes two weaknesses of large reasoning models: accuracy collapse on long-context inputs and unproductive overthinking via excessive self-verification.

## Problem

Whether existing evaluations adequately probe the reasoning robustness of large reasoning models on tasks with controllable difficulty and long-context demands, and what specifically causes them to fail as problems scale up.

## Contributions

- Introduces GrAlgoBench, a benchmark of graph algorithm problems for evaluating large reasoning models with tunable difficulty and programmatic (automatic) scoring
- Shows accuracy falls below 50% once input graphs exceed 120 nodes
- Identifies an overthinking phenomenon: models perform extensive self-verification that expands reasoning traces without improving accuracy

## Method

Uses graph algorithm problems as an evaluation testbed because they allow long-context reasoning, fine-grained control of difficulty (e.g. graph size), and standardized programmatic (automatic, non-LLM-judged) evaluation. Large reasoning models are run on these graph problems across a range of sizes and the resulting traces and accuracy are analyzed.

## Results

Accuracy falls below 50% once graphs exceed 120 nodes; degradation is attributed to execution errors, inadequate memory retention, and unnecessary reasoning loops (overthinking via ineffective self-verification).

## Limitations

Only summarized from the poster/abstract page, not the full paper, so details on model list, exact benchmark construction and statistical significance are not available here.

## Why it matters here

- **overthinking**: Directly documents the overthinking phenomenon in large reasoning models: as graphs grow, models expand their self-verification effort without any corresponding gain in accuracy, which is a direct empirical instance of reasoning-length/accuracy decoupling that the topic tracks.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), self-verification, long-context reasoning, controllable-difficulty benchmarking
- **Methods**: GrAlgoBench
- **Datasets**: GrAlgoBench

Tags: `overthinking`, `benchmark`, `graph-algorithms`, `large-reasoning-models`, `self-verification`

---

Record id: `title:00481a9889909bb4`
