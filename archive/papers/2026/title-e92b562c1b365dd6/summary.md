<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cache Coherent Resampling for Efficient Test Time Scaling in LLM Reasoning via Adaptive Sequential Monte Carlo

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64829>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Speeds up parallel test-time-scaled LLM reasoning by resampling candidate solution paths through in-place cache reorganization instead of recomputation.

## Problem

Chain-based sampling methods for scaling test-time compute in LLM reasoning are serial and high-latency; the paper addresses how to parallelize sampling of many candidate reasoning paths without paying a large recomputation cost each time paths are resampled.

## Contributions

- Adaptive Sequential Monte Carlo (ASMC) method for parallel test-time scaling of LLM reasoning, replacing purely serial chain-based sampling
- Cache coherent resampling: reorganizes the model's key-value cache in place when switching between candidate solution paths instead of recomputing it
- Reports 80.6% exact-match accuracy with p95 latency of 73.7s versus p95 = 1318s for a sequential alternative at comparable compute budget
- Uses a particle-degeneracy metric (ESS_min/N) to predict when the method may struggle, and shows robustness across different resampling strategies

## Method

ASMC runs many candidate reasoning paths (particles) in parallel using Sequential Monte Carlo instead of sampling reasoning chains one at a time. The key innovation, cache coherent resampling, reorganizes the model's internal key-value cache structures in place when the search resamples or switches between candidate paths, avoiding the cost of recomputing the cache from scratch. A particle-degeneracy metric, ESS_min/N (minimum effective sample size over particle count), is used to detect when the sampling is struggling.

## Results

80.6% exact-match accuracy with p95 latency of 73.7s on a mathematical reasoning benchmark, versus p95 = 1318s for a sequential chain-based alternative at a comparable computational budget.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Bears on the efficiency side of the topic's test-time compute scaling angle: it makes exploring many parallel reasoning paths at test time (a form of allocating more compute to reasoning) fast in wall-clock terms, directly affecting the accuracy-per-unit-latency tradeoff of scaling test-time compute for reasoning, though it addresses parallel sampling infrastructure rather than reasoning-length or stopping-point control per se.

## Entities

- **Concepts**: Sequential Monte Carlo for LLM reasoning, particle resampling, cache-coherent inference, particle degeneracy (ESS)
- **Methods**: Adaptive Sequential Monte Carlo (ASMC), cache coherent resampling
- **Datasets**: mathematical reasoning benchmark(s) (not individually named in the fetched material)

Tags: `test-time-scaling`, `sequential-monte-carlo`, `kv-cache`, `parallel-sampling`, `reasoning-efficiency`

---

Record id: `title:e92b562c1b365dd6`
