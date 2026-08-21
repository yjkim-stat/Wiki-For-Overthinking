<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61200>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Identifies which tokens in a large reasoning model's chain-of-thought actually steer the final answer and evicts the Key-Value cache for the rest, cutting memory and latency without hurting accuracy.

## Problem

Large reasoning models generate long reasoning traces to solve hard problems, but the resulting Key-Value cache and compute overhead bottleneck inference efficiency; not all of that generated reasoning is functionally necessary.

## Contributions

- An attention-map analysis showing that only a small subset of tokens in a reasoning trace are decision-critical for the final answer, while most tokens contribute negligibly.
- DynTS, a method that identifies decision-critical tokens and retains only their Key-Value cache entries, evicting the rest during inference.
- Empirical results showing DynTS surpasses prior KV-cache compression methods on Pass@1 at matched cache budget, while cutting inference latency and peak KV-cache memory.

## Method

DynTS analyzes attention maps over a generated reasoning trace to identify decision-critical tokens (the ones that steer the model toward its final answer) versus tokens that contribute little. It then keeps only the Key-Value cache states associated with the decision-critical tokens and evicts the remaining, redundant KV entries during inference, reducing memory and compute without regenerating the trace.

## Results

DynTS improves Pass@1 by 2.6% over state-of-the-art KV-cache compression methods at the same cache budget, reduces inference latency by 1.84-2.62x, and reduces peak KV-cache memory footprint by 3.32-5.73x compared to vanilla Transformer inference, without compromising reasoning performance (arXiv:2601.18383).

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly addresses the efficiency side of the overthinking tradeoff: it shows most tokens in a reasoning trace are redundant for the final answer and proposes a way to prune the corresponding computation/memory (KV cache) while preserving accuracy, i.e. making long reasoning traces cheaper without shortening or truncating the reasoning itself.

## Entities

- **Concepts**: decision-critical tokens, KV-cache redundancy in reasoning traces, attention-guided token selection
- **Methods**: DynTS, [KV-cache eviction](../../../../wiki/methods/kv-cache-eviction.md)
- **Datasets**: _none recorded_

Tags: `efficient-reasoning`, `kv-cache`, `token-pruning`, `inference-efficiency`

## Abstract

Abstract Large Reasoning Models (LRMs) excel at solving complex problems by explicitly generating a reasoning trace before deriving the final answer. However, these extended generations incur substantial memory footprint and computational overhead, bottlenecking LRMs' efficiency. This work uses attention maps to analyze the influence of reasoning traces and uncover an interesting phenomenon: *only some decision-critical tokens in a reasoning trace steer the model toward the final answer, while the remaining tokens contribute negligibly.* Building on this observation, we propose **Dyn**amic **T**hinking-Token **S**election (**DynTS**). This method identifies decision-critical tokens and retains only their associated Key-Value (KV) cache states during inference, evicting the remaining redundant entries to optimize efficiency. Across six benchmarks, **DynTS** surpasses the state-of-the-art KV cache compression methods, improving Pass@1 by $2.6\\%$ under the same budget. Compared to vanilla Transformers, it reduces inference latency by $1.84–2.62\times$ and peak KV-cache memory footprint by $3.32–5.73\times$ without compromising LRMs' reasoning performance.

---

Record id: `title:84172089e3270d37`
