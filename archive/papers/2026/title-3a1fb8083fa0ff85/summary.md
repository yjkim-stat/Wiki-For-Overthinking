<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009980>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A KV-cache compression framework that labels segments of a reasoning trace by thought type and applies per-type quantization and progressive eviction, keeping accuracy near full-cache at under 5% of the cache.

## Problem

Large reasoning models emit long chains of thought, so the key-value cache grows with output length and exhausts GPU memory. Existing compression treats all cached tokens alike; quantization-only methods degrade reasoning accuracy, and eviction requires cache compaction that costs throughput.

## Contributions

- Observation that attention sparsity separates a chain of thought into distinct thought types (Reasoning, Execution, Transition) of unequal importance
- A hybrid quantization-plus-eviction policy that sets token precision by thought importance and progressively evicts tokens from less critical thoughts as the trajectory evolves
- A PagedAttention extension that reuses evicted tokens' memory slots, removing compaction overhead from eviction-based compression
- Measurement that quantization-only KV compression can inflate generated reasoning length by up to 5.1x, which the hybrid scheme reduces

## Method

ThinKV segments the chain of thought into three thought types identified from attention sparsity patterns: Reasoning (systematic thinking), Execution (calculation and code generation) and Transition (uncertainty and backtracking). It assigns each thought's tokens a precision by importance and progressively evicts tokens from less critical thoughts as the trajectory advances. Clustering is constrained to a single thought segment to limit RoPE-induced token drift. To make eviction cheap it extends PagedAttention with a kernel that reuses the memory slots of evicted tokens in place, removing the compaction step that makes eviction expensive in standard paged serving.

## Results

Evaluated on DeepSeek-R1-Distill-Llama 8B/70B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B, GPT-OSS 20B/120B, AceReason-Nemotron-14B and MobileLLM-R1-950M, over MATH-500, AIME, GSM8K and LiveCodeBench. Near-lossless accuracy with under 5% of the original KV cache; R1-Llama-8B on AIME loses under 4 points using about 1.3% of the cache. Main setting is a 1024-token budget, 2.51% of the full footprint against 5.48% for the R-KV baseline. Throughput up to 5.8x over R-KV with sequential gather (8,412 vs 1,450.5 tokens/sec on an A100) and up to 1.68x lower TPOT. Quantization baselines KIVI and PM-KVQ show substantially larger accuracy loss at comparable budgets. The paper also measures generated length and reports that quantization can inflate generation length by up to 5.1x across datasets and techniques, which the hybrid scheme reduces.

## Limitations

Complete eviction (minimum retention of zero) sharply degrades accuracy because the model loses track of trajectories it has already explored, so the method depends on a tuned retention floor. Accuracy falls as the refresh interval grows, since thought-type changes between refreshes are missed. RoPE-induced token drift is acknowledged and only mitigated, not solved, by confining clustering within a thought segment. The throughput figures are against a baseline using sequential gather, so the headline 5.8x is partly an artifact of the compaction cost ThinKV's kernel removes rather than of the compression policy itself. All results are on mathematics and code, where thought structure is comparatively regular.

## Why it matters here

- **overthinking**: Mostly tangential, on the same side as the other KV-cache work already in the archive (AsyncSpade, BeaconKV): it takes the length of the reasoning trace as given and reduces the memory and throughput cost of serving it, rather than deciding how long the model should think. Two details are closer to the topic than that summary suggests, and neither is the length decision. First, its premise is that a chain of thought divides into Reasoning, Execution and Transition segments of unequal importance, and that tokens from the less important ones can be evicted almost entirely with under 4 points of accuracy loss at ~1.3% cache -- an efficiency-side measurement consistent with long traces carrying low-value content, though evicting cache is not the same as not generating it. Second, the paper measures output length and reports that quantization-only compression can inflate generation by up to 5.1x, i.e. an efficiency intervention downstream of the length decision can make traces longer; that is a caution worth carrying for anyone combining cache compression with length control. The paper itself proposes no stopping criterion and does not shorten output.

## Entities

- **Concepts**: KV cache compression, thought types in chain of thought, attention sparsity, hybrid quantization-eviction, paged attention, generation length inflation under compression
- **Methods**: ThinKV, PagedAttention, KV cache quantization, [KV cache eviction](../../../../wiki/methods/kv-cache-eviction.md), KIVI, PM-KVQ, [R-KV](../../../../wiki/methods/r-kv.md)
- **Datasets**: [MATH-500](../../../../wiki/datasets/math500.md), [AIME](../../../../wiki/datasets/aime.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [LiveCodeBench](../../../../wiki/datasets/livecodebench.md)

Tags: `kv-cache`, `inference-efficiency`, `reasoning-models`, `quantization`, `cache-eviction`, `tangential`

---

Record id: `title:3a1fb8083fa0ff85`
