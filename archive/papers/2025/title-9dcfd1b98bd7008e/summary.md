<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119365>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ST-BoN cuts the cost of Best-of-N test-time scaling by using early sampling consistency in internal states to truncate unpromising candidates before they finish generating, without a reward model.

## Problem

Best-of-N sampling broadens the search space at inference time to find better solutions, but its cost-performance trade-off is underexplored: generating N full samples consumes substantial GPU memory, and reward models used to select among them add memory, latency and training-data cost.

## Contributions

- Self-Truncation Best-of-N (ST-BoN): a decoding method that avoids fully generating all N Best-of-N samples
- Removes the need for a reward model by using early sampling consistency in internal states to identify the most promising path
- Reduces dynamic GPU memory usage by over 80% and inference latency by 50% versus Full-BoN
- Matches Full-BoN accuracy at 70-80% lower compute cost, or improves accuracy by 3-4 points at equal cost

## Method

ST-BoN generates N candidate continuations but does not let all of them run to completion. It monitors early sampling consistency in the model's internal states during decoding across the N partial samples, uses this signal to identify the most promising candidate path, and truncates the generation of the other, less promising candidates early. This removes the need for a separate reward model to score full completions.

## Results

ST-BoN reduces dynamic GPU memory usage by over 80% and inference latency by 50% versus Full-BoN; matches Full-BoN performance while cutting computational cost by 70-80%; at equal cost it improves accuracy by 3-4 points.

## Limitations

Abstract does not name the specific benchmarks or models used in the experiments, nor does it report failure modes of the early-truncation heuristic.

## Why it matters here

- **overthinking**: Directly addresses the test-time-compute cost/accuracy tradeoff for LLMs: it is a decoding-time method that stops generating unpromising Best-of-N samples early rather than letting all N run to completion, trading unnecessary parallel compute for controlled accuracy loss (or gain at fixed cost).

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), Best-of-N sampling, early truncation, sampling consistency in internal states
- **Methods**: Self-Truncation Best-of-N (ST-BoN), [Best-of-N (BoN) sampling](../../../../wiki/methods/best-of-n-bon-sampling.md)
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `best-of-n`, `decoding`, `efficiency`, `reward-model-free`

## Abstract

Abstract Test-time scaling enhances large language model performance by allocating additional compute resources during decoding. Best-of-$N$ (BoN) sampling serves as a common sampling-based scaling technique, broadening the search space in parallel to find better solutions from the model distribution. However, its cost–performance trade-off is still underexplored. Two main challenges limit the efficiency of BoN sampling: (1) Generating $N$ full samples consumes substantial GPU memory, reducing inference capacity under limited resources. (2) Reward models add extra memory and latency overhead, and training strong reward models introduces potential training data costs. Although some studies have explored efficiency improvements, none have addressed both challenges at once. To address this gap, we propose **Self-Truncation Best-of-$N$ (ST-BoN)**, a decoding method that avoids fully generating all $N$ samples and eliminates the need for reward models. It leverages early sampling consistency in the model’s internal states to identify the most promising path and truncate suboptimal ones. In terms of cost, ST-BoN reduces dynamic GPU memory usage by over 80% and inference latency by 50%. In terms of cost–performance trade-off, ST-BoN achieves the same performance as Full-BoN while saving computational cost by 70%–80%, and under the same cost, it can improve accuracy by 3–4 points.

---

Record id: `title:9dcfd1b98bd7008e`
