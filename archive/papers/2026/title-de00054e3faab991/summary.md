<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Strategic Scaling of Test-Time Compute: A Bandit Learning Approach

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011899>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Formulates test-time compute allocation across queries as a bandit learning problem so that harder queries get more compute and easier ones get less.

## Problem

Allocating test-time compute uniformly across all queries is wasteful: easy queries receive more compute than they need and very hard (possibly unsolvable) queries can consume large amounts of compute without a proportional accuracy gain.

## Contributions

- Formulates test-time compute allocation across queries as a bandit learning problem
- Adaptive algorithm that estimates query difficulty online and allocates more compute to harder queries while preserving accuracy on easier ones
- Identifies solvable-but-hard instances to avoid wasting compute on effectively unsolvable queries
- Theoretical guarantees of improved efficiency over uniform compute allocation

## Method

Casts the problem of distributing a test-time compute budget across a stream of queries as a bandit learning problem. The algorithm adaptively estimates each query's difficulty as it goes and allocates more compute (more reasoning/sampling effort) to harder queries and less to easier ones, while also trying to detect instances that are difficult but effectively unsolvable so compute is not wasted on them.

## Results

Roughly 11 percentage points (about 15% relative) improvement on MATH-500, about 10.8 points (14.4% relative) on AIME25, and about 11.2 points (15.3% relative) on LiveCodeBench, compared to uniform compute allocation.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly targets the accuracy/efficiency tradeoff at the center of the topic by adaptively deciding, per query, how much test-time compute to spend based on estimated difficulty, rather than a fixed budget applied to every query regardless of need.

## Entities

- **Concepts**: test-time compute allocation, bandit learning, query difficulty estimation
- **Methods**: bandit learning algorithm for compute allocation
- **Datasets**: [MATH-500](../../../../wiki/datasets/math-500.md), AIME25, [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `test-time-compute`, `bandit-learning`, `adaptive-allocation`, `reasoning-efficiency`

---

Record id: `title:de00054e3faab991`
