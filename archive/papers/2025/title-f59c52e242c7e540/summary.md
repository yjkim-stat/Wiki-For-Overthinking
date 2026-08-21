<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/31024>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Analyzes verifier-search and proposal-revision as the two primary mechanisms of test-time compute scaling and shows that allocating compute adaptively per prompt difficulty is more efficient than fixed strategies, and can be more effective than scaling model parameters.

## Problem

It was unclear how much an LLM's performance on a hard prompt can be improved by using a fixed additional amount of inference-time compute, how that should be weighed against scaling pretraining compute, and prior work had largely reported negative results for test-time scaling strategies.

## Contributions

- An analysis of two primary mechanisms for scaling test-time compute: searching against dense process-based verifier reward models, and adaptively updating the model's response distribution at test time given the prompt
- The finding that the effectiveness of test-time compute scaling strategies depends critically on prompt difficulty
- A compute-optimal strategy that adaptively allocates test-time compute per prompt, improving efficiency more than 4x over a best-of-N baseline
- A FLOPs-matched comparison showing test-time compute can let a smaller model outperform a 14x larger model on problems where the smaller model has non-trivial baseline success

## Method

The paper studies two mechanisms for scaling inference-time computation in LLMs: (1) searching against dense, process-based verifier reward models, and (2) adaptively revising the model's distribution over a response given the prompt at test time. Because the effectiveness of each mechanism varies with prompt difficulty, the authors propose a compute-optimal scaling strategy that allocates test-time compute adaptively per prompt based on estimated difficulty, rather than applying a fixed strategy uniformly.

## Results

The compute-optimal, difficulty-adaptive strategy improves test-time compute scaling efficiency by more than 4x compared to a best-of-N baseline. In a FLOPs-matched evaluation, on problems where a smaller base model attains non-trivial success rates, test-time compute lets it outperform a model 14x larger.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Foundational to the topic's test-time-compute side: establishes that test-time scaling strategies must be matched to prompt difficulty to be effective (a fixed amount of extra compute is not uniformly helpful), and quantifies the accuracy/compute tradeoff -- directly informing when a model should be given more or less inference-time compute rather than applying it uniformly.

## Entities

- **Concepts**: [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), [compute-optimal allocation](../../../../wiki/concepts/compute-optimal-allocation.md), process-based verification, difficulty-conditioned inference, inference-time vs pretraining compute tradeoff
- **Methods**: process-based verifier reward model search, adaptive proposal distribution revision, compute-optimal test-time scaling
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `compute-optimal`, `verifier-search`, `reasoning-efficiency`

---

Record id: `title:f59c52e242c7e540`
