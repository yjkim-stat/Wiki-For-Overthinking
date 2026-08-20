<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64598>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proves standard best-of-n sampling is suboptimal for test-time compute under a mixture-of-reference-policy model and proposes reward-filtered sequential inference as a stronger alternative.

## Problem

Test-time compute methods such as best-of-n sampling and sequential revision are widely used to improve LLM performance, but their fundamental limits and optimality were unclear before this work.

## Contributions

- Proof, under a mixture-of-reference-policy model, that standard best-of-n (BoN) sampling is inherently suboptimal for test-time compute
- Reward-filtered sequential inference: a procedure that selectively incorporates only high-reward generations into the context
- Theoretical guarantees showing reward-filtered sequential inference is strictly stronger than standard test-time-compute paradigms
- Empirical evaluation across diverse benchmarks showing consistent improvements over widely used test-time-compute approaches

## Method

Models test-time compute using a mixture-of-reference-policy formulation and proves that standard best-of-n sampling is suboptimal within it. Proposes reward-filtered sequential inference, which selectively incorporates only high-reward generations into the context, concentrating computation on stronger candidates and suppressing weaker ones, and derives theoretical guarantees comparing it to standard test-time-compute methods.

## Results

Theoretically shown to yield strictly stronger guarantees than standard test-time-compute paradigms (BoN, sequential revision); empirically evaluated across diverse benchmarks with consistent improvements over widely used approaches. Exact numeric results were not available in the fetched material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly studies test-time compute scaling: it proves a fundamental suboptimality of standard best-of-n sampling and proposes reward-filtered sequential inference to concentrate compute on higher-reward generations instead of simply sampling more, i.e. how to allocate a fixed test-time compute budget more effectively.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), best-of-n sampling, sequential revision, mixture-of-reference-policy model
- **Methods**: [best-of-n (BoN) sampling](../../../../wiki/methods/best-of-n-bon-sampling.md), reward-filtered sequential inference
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `best-of-n`, `sequential-inference`, `reward-filtering`

---

Record id: `title:cd5c62ac6be53cbc`
