<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ATTS: Asynchronous Test-Time Scaling via Conformal Prediction

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008898>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ATTS uses conformal prediction to asynchronously coordinate multi-dimensional test-time scaling, cutting synchronization overhead between draft and target models during LLM inference.

## Problem

Test-time scaling improves LLM accuracy but is hampered by high computational demands, in particular synchronization bottlenecks that appear when scaling is attempted along multiple processing dimensions (e.g., sequential and parallel) at the same time.

## Contributions

- ATTS, a framework for asynchronous test-time scaling that removes synchronization bottlenecks when scaling along multiple inference dimensions at once
- A statistically guaranteed adaptive scaling procedure based on conformal prediction / hypothesis testing with online calibration
- An ordinal classification algorithm supporting a three-stage rejection sampling pipeline usable in both sequential and parallel execution paths

## Method

ATTS treats test-time scaling as a hypothesis-testing / conformal-prediction problem: it uses online calibration to give statistical guarantees on when a draft model's output can be accepted, driving a three-stage rejection sampling pipeline that can run sequential and parallel decoding paths asynchronously instead of forcing them to synchronize.

## Results

Reports up to 56.7x speedup in test-time scaling and a 4.14x throughput improvement, with performance comparable to o3-mini (high) achieved using smaller draft/target model combinations, evaluated on MATH, AMC23, AIME24 and AIME25, while maintaining rejection-rate control without accuracy degradation.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly targets the compute cost of test-time scaling: it proposes a statistically grounded mechanism (conformal prediction with online calibration) to decide when extra test-time computation can be safely skipped or accepted, which is a stopping/scaling-control method for reasoning inference rather than a fixed reasoning budget.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), conformal prediction, asynchronous decoding, draft/target model speculation, rejection sampling
- **Methods**: ATTS, conformal prediction-based rejection sampling, ordinal classification
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [AMC23](../../../../wiki/datasets/amc23.md), AIME24, AIME25

Tags: `test-time-scaling`, `conformal-prediction`, `speculative-decoding`, `inference-efficiency`

---

Record id: `title:b601ad920fcc4d45`
