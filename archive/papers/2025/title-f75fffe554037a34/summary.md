<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117966>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces a recurrent-depth architecture that scales test-time compute by iterating a latent reasoning block to arbitrary depth instead of generating more chain-of-thought tokens.

## Problem

Mainstream reasoning models scale test-time compute by producing more output tokens (chain-of-thought), which requires specialized training data and represents reasoning only in words; the paper asks whether test-time compute can instead be scaled through implicit latent-space computation.

## Contributions

- A language model architecture that scales test-time computation by iterating a recurrent block to unroll to arbitrary depth at test time, reasoning implicitly in latent space rather than by producing more tokens
- Trains a 3.5B-parameter proof-of-concept model from scratch on 800B tokens
- Shows the architecture naturally supports zero-shot per-token adaptive compute, KV-cache sharing, and speculative decoding

## Method

Instead of scaling test-time compute by generating more output tokens (as chain-of-thought reasoning models do), the model iterates a recurrent block at inference time, unrolling it to an arbitrary depth to perform reasoning implicitly in latent space. This requires no specialized chain-of-thought training data, works with small context windows, and can represent reasoning not easily expressed in words. The recurrent structure also enables zero-shot per-token adaptive compute, KV-cache sharing, and speculative decoding to reduce cost.

## Results

The 3.5B-parameter model trained on 800B tokens shows performance improving significantly with additional test-time compute, especially on math and coding reasoning tasks; no specific benchmark scores are given in the abstract.

## Limitations

Abstract does not report specific benchmark scores or comparisons to chain-of-thought baselines; described as a 'proof-of-concept' model, suggesting scale/maturity limits.

## Why it matters here

- **overthinking**: Offers an alternative mechanism for test-time compute scaling to token-based chain-of-thought: recurrent latent-space iteration with per-token adaptive compute, directly bearing on how much computation a model spends per problem and how that computation is allocated at test time, rather than how many tokens it verbalizes.

## Entities

- **Concepts**: latent reasoning, [recurrent depth](../../../../wiki/concepts/recurrent-depth.md), implicit test-time compute scaling, per-token adaptive compute
- **Methods**: recurrent-depth latent reasoning, per-token adaptive compute, KV-cache sharing, [speculative decoding](../../../../wiki/methods/speculative-decoding.md)
- **Datasets**: math and coding reasoning tasks (specific benchmarks not named in abstract)

Tags: `test-time-compute`, `latent-reasoning`, `recurrent-architecture`, `adaptive-compute`, `chain-of-thought-alternative`

## Abstract

Abstract We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space. Our model works by iterating a recurrent block, thereby unrolling to arbitrary depth at test-time. This stands in contrast to mainstream reasoning models that scale up compute by producing more tokens. Unlike approaches based on chain-of-thought, our approach does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words. We train a proof-of-concept model from scratch with 3.5 billion parameters and 800 billion tokens. We show that this model can effortlessly use varying levels of compute, significantly improving with additional compute especially on reasoning tasks, such as math and coding. Further, this architecture naturally reduces compute costs via zero-shot per-token adaptive compute, KV-cache sharing and speculative decoding.

---

Record id: `title:f75fffe554037a34`
