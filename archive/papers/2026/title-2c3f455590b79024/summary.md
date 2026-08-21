<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AsyncSpade: Efficient Test-Time Scaling with Asynchronous Sparse Decoding

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63012>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

AsyncSpade speeds up decoding of long chain-of-thought generations by predicting query states from recent patterns and running sparse KV-cache selection asynchronously alongside decoding, cutting per-token latency without hurting accuracy.

## Problem

Long chain-of-thought generation causes the KV cache to grow linearly, worsening the memory-bound bottleneck of LLM decoding and slowing inference, but existing sparse-attention methods still require the KV selection step to happen sequentially before each decoding step.

## Contributions

- Identifies that linear KV-cache growth during long chain-of-thought generation amplifies the memory-bound bottleneck of LLM decoding.
- Shows that per-token query states can be approximated from recent query patterns via a lightweight temporal-regressive module, removing the sequential dependency of KV selection on the current step's query.
- Introduces AsyncSpade, an asynchronous framework that decouples KV cache selection from the decoding step so the two can run in parallel.
- Reports over 20% TPOT (time-per-output-token) reduction versus the SoTA sparse baseline Quest, and at least 50% TPOT reduction versus full attention on Qwen3-8B and Qwen3-32B, while maintaining accuracy.

## Method

AsyncSpade predicts the query state of the token currently being decoded from recent query patterns using a lightweight temporal-regressive module, instead of waiting for that token's actual query. This breaks the sequential dependency between KV cache selection (choosing which cached keys/values to attend to, i.e. sparse decoding) and the decoding step itself, allowing the KV selection to run asynchronously and in parallel with decoding, reducing the memory-bound bottleneck caused by linear KV-cache growth over long chains of thought.

## Results

Over 20% TPOT reduction compared to the SoTA sparse-decoding baseline Quest, and at least 50% TPOT reduction compared to full attention, on Qwen3-8B and Qwen3-32B, while maintaining accuracy on AIME-24/25, GPQA-Diamond and MATH-500.

## Limitations

Only a third-party-extracted summary of the abstract was available (no PDF attachment); details on accuracy deltas, hardware setup, and any stated limitations of the temporal-regressive approximation (e.g. failure cases where recent query patterns diverge from the true query) are not available from this source.

## Why it matters here

- **overthinking**: This is a systems/inference-efficiency paper about serving already-long chains of thought faster (via asynchronous sparse KV-cache decoding), not about deciding how long a model should reason or about the accuracy/length tradeoff itself. It shares only the general 'test-time scaling' and long-chain-of-thought context with the topic; it does not address overthinking, underthinking, or stopping criteria, so its connection to the topic is tangential rather than substantive.

## Entities

- **Concepts**: KV-cache memory-bound decoding bottleneck, query state approximation from temporal patterns, asynchronous KV cache selection, sparse attention decoding
- **Methods**: AsyncSpade, temporal-regressive query prediction, asynchronous sparse KV cache selection
- **Datasets**: [AIME-24](../../../../wiki/datasets/aime-2024.md), [AIME-25](../../../../wiki/datasets/aime-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [MATH-500](../../../../wiki/datasets/math500.md)

Tags: `kv-cache`, `sparse-attention`, `inference-efficiency`, `asynchronous-decoding`, `long-context`, `tangential`

---

Record id: `title:2c3f455590b79024`
