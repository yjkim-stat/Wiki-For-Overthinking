<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# What If We Allocate Test-Time Compute Adaptively?

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/60797>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Replaces uniform test-time compute allocation with a process-reward-model-guided framework that adaptively prunes, expands and selects reasoning trajectories per problem.

## Problem

Standard test-time compute scaling spends inference computation uniformly, uses fixed sampling strategies, and only applies verification at the reranking stage, which wastes compute on low-utility reasoning paths.

## Contributions

- A verifier-guided adaptive framework that treats reasoning as iterative trajectory generation and selection, replacing uniform test-time compute allocation and fixed sampling strategies.
- Use of a process reward model (PRM) both within an iteration (step-level scores guide pruning and expansion during generation) and across iterations (aggregated trajectory rewards select the final response).
- A compute intensity metric, alongside theoretical FLOPs, that penalizes wasted generation and tool overhead to characterize efficiency.

## Method

For each problem the agent runs multiple inference iterations; in each iteration it optionally produces a high-level plan, selects a set of reasoning tools and a compute strategy with an exploration parameter, and generates a candidate reasoning trajectory. A process reward model scores steps within an iteration to guide pruning/expansion of the generation, and aggregated trajectory-level rewards across iterations are used to select the final response, so compute is allocated adaptively toward high-utility reasoning paths instead of uniformly.

## Results

The dynamic, PRM-guided approach consistently outperforms direct (uniform) test-time scaling, with large gains on MATH-500 and several-fold improvements on harder benchmarks such as AIME24 and AMO-Bench. Efficiency is measured via theoretical FLOPs and a compute intensity metric that penalizes wasted generation and tool overhead, showing computation is concentrated on high-utility reasoning paths (arXiv:2602.01070).

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly on-topic: the paper's whole premise is that uniform test-time compute allocation is wasteful, and it proposes a PRM-guided adaptive mechanism to concentrate compute on high-utility reasoning paths and prune unproductive ones, which is precisely the accuracy/efficiency tradeoff and 'when to keep going vs. stop' question the topic tracks.

## Entities

- **Concepts**: verifier-guided adaptive compute allocation, process reward model as control signal, compute intensity metric, iterative trajectory generation and selection
- **Methods**: process reward model (PRM), verifier-guided adaptive test-time compute allocation
- **Datasets**: [MATH-500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), AMO-Bench

Tags: `test-time-compute`, `process-reward-model`, `adaptive-allocation`, `efficient-reasoning`

---

Record id: `title:892443a8a7093b83`
