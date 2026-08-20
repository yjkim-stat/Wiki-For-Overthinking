<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# R-Horizon: How Far Can Your Large Reasoning Model Really Go in Breadth and Depth?

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007149>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces R-HORIZON, a query-composition benchmark for long, multi-step reasoning, finds current reasoning models degrade sharply and misallocate compute across sub-problems, and uses the same data to improve models via RL.

## Problem

Existing evaluations of large reasoning models mostly use single, isolated problems, so it is unclear how well these models sustain reasoning breadth and depth across long, interdependent multi-step tasks.

## Contributions

- Proposes R-HORIZON, a query-composition method for constructing complex multi-step reasoning tasks with interdependent problems that span long reasoning horizons, to evaluate reasoning models beyond single-step benchmarks.
- Identifies that current large reasoning models show significant performance degradation on these composed long-horizon tasks and have a limited effective reasoning length.
- Shows models struggle to properly distribute computational resources (reasoning effort) across multiple interdependent problems within one task.
- Uses R-HORIZON-generated data for reinforcement learning with verified rewards, improving both multi-step task performance and standard benchmarks, including +7.5 on AIME2024.

## Method

R-HORIZON composes multiple interdependent problems into single queries to create reasoning tasks with long horizons, testing whether a model's reasoning breaks down as the number of chained sub-problems grows. The resulting data is then used to train models via reinforcement learning with verified rewards, aiming to improve both long-horizon composed-task performance and standard single-step benchmarks.

## Results

Reports significant performance degradation of advanced reasoning models on R-HORIZON's composed long-horizon tasks, and a +7.5 point improvement on AIME2024 after RL training with verified rewards on R-HORIZON data. No other specific benchmark numbers were available from this source.

## Limitations

Only a third-party-extracted summary of the abstract was available (no PDF attachment); exact numeric results beyond the +7.5 AIME2024 figure, model names tested, and the precise definition of 'effective reasoning length' are not available from this source.

## Why it matters here

- **overthinking**: Directly addresses the reasoning-length side of the topic: it shows that reasoning models have a limited 'effective reasoning length' and fail to properly distribute computational effort across multiple sub-problems, i.e. a form of misallocated (rather than merely excessive or insufficient) test-time compute. The RL fix that improves long-horizon performance and AIME2024 by +7.5 is a concrete method for improving how models spend reasoning budget.

## Entities

- **Concepts**: query composition, multi-step reasoning horizon, effective reasoning length, compute allocation across sub-problems, reinforcement learning with verified rewards
- **Methods**: R-HORIZON query composition, reinforcement learning with verified rewards
- **Datasets**: R-HORIZON (composed multi-step reasoning benchmark), AIME2024

Tags: `long-horizon-reasoning`, `test-time-compute`, `reasoning-length`, `compute-allocation`, `reinforcement-learning`, `benchmark`

---

Record id: `title:2976f6142ca2d636`
