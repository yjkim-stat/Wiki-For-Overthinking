<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62942>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A training-free KV-cache compression method for long reasoning-model inference that preserves the distant context tokens later reasoning steps revisit, using clustered 'beacon queries'.

## Problem

KV cache memory for large reasoning models grows with the long sequences their extended thought processes produce, and existing compression methods assume recent queries predict future attention, which breaks down when reasoning revisits distant earlier context.

## Contributions

- Identifies 'Thought Revisiting Tokens': decoding steps in long reasoning traces that attend back to distant early context such as the initial problem framing
- Shows these queries cluster into similarity groups in embedding space
- Introduces BeaconKV, which retains representative 'beacon queries' per cluster to anticipate needed prior KV entries without retraining
- Reports up to 5.8x KV cache memory reduction and over 4.3x throughput improvement while nearly preserving full-cache accuracy

## Method

BeaconKV observes that standard KV cache compression assumes recent queries predict future attention, which fails for long reasoning chains that later revisit distant early tokens (e.g. the original problem statement). It identifies such 'Thought Revisiting' decoding steps, clusters their queries by similarity in embedding space, and keeps a representative 'beacon query' per cluster so the cache-eviction policy can anticipate which earlier context will be needed again, without retraining the model.

## Results

Up to 5.8x KV cache memory reduction while nearly preserving full-cache accuracy, and over 4.3x throughput improvement, reported across multiple reasoning models and benchmarks; specific benchmark names and per-model numbers are not given in the available abstract.

## Limitations

Not stated in the available material (abstract only; no PDF attached). The method's premise is specific to reasoning traces long enough to contain revisits to distant early context.

## Why it matters here

- **overthinking**: Addresses the memory and throughput cost of serving long reasoning traces, not why or when a model should reason longer or shorter. It takes the length of the reasoning trace as given and optimizes cache efficiency for it, rather than addressing the accuracy/efficiency tradeoff of reasoning length or stopping criteria that the topic tracks. Matches the topic only via the generic 'large reasoning model' keyword; tangential.

## Entities

- **Concepts**: [KV cache compression](../../../../wiki/concepts/kv-cache-compression.md), Thought Revisiting Tokens, beacon queries, attention pattern clustering
- **Methods**: BeaconKV
- **Datasets**: _none recorded_

Tags: `kv-cache`, `inference-efficiency`, `reasoning-models`, `memory-compression`, `tangential`

---

Record id: `title:3663586d2c722911`
