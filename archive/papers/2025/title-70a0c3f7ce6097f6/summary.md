<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115542>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SambaY is a decoder-hybrid-decoder architecture that shares memory states across State Space Model layers via a Gated Memory Unit, and its largest variant (Phi4-mini-Flash-Reasoning) matches or beats a same-size reasoning model on Math500/AIME24-25/GPQA without RL while delivering up to 10x higher decoding throughput on long-generation prompts.

## Problem

Hybrid SSM-Transformer architectures (e.g. Samba, YOCO) improve on plain Transformers but have not exploited representation sharing between SSM layers, leaving decoding efficiency for long generations (as needed for long reasoning traces) on the table.

## Contributions

- the Gated Memory Unit (GMU) for cross-layer memory sharing in SSM-based architectures
- SambaY, a decoder-hybrid-decoder architecture with linear pre-filling and no explicit positional encoding
- Phi4-mini-Flash-Reasoning, matching/exceeding a same-size reasoning model's accuracy with up to 10x higher decoding throughput on long generations

## Method

Introduces the Gated Memory Unit (GMU), a mechanism for sharing memory-readout states across layers, and applies it in a cross-decoder to build SambaY, a decoder-hybrid-decoder architecture that shares memory from a Samba-based self-decoder, preserves linear pre-filling time complexity, and needs no explicit positional encoding.

## Results

SambaY shows significantly lower irreducible loss than a strong YOCO baseline at scale; the largest variant, Phi4-mini-Flash-Reasoning (with added Differential Attention), significantly outperforms Phi4-mini-Reasoning on Math500, AIME24/25, and GPQA Diamond without any reinforcement learning, while delivering up to 10x higher decoding throughput on 2K-prompt/32K-generation workloads under vLLM.

## Limitations

Not stated in the fetched abstract beyond the architectures and benchmarks tested.

## Why it matters here

- **overthinking**: Directly relevant as an architectural (rather than prompting/training) mitigation: it targets exactly the cost of long reasoning generations by making the underlying decoder architecture faster per token (up to 10x throughput) rather than shortening the trace, and shows this can match reasoning accuracy without needing RL -- a different lever than the length-penalty or early-stopping approaches common in the overthinking literature.

## Entities

- **Concepts**: Gated Memory Unit (GMU), decoder-hybrid-decoder architecture, memory-state sharing across SSM layers
- **Methods**: State Space Models (SSM), Gated Memory Unit, Differential Attention
- **Datasets**: [Math500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `architecture`, `efficient-reasoning`, `decoding-throughput`, `state-space-models`, `long-generation`

## Abstract

Abstract Recent advances in language modeling have demonstrated the effectiveness of State Space Models (SSMs) for efficient sequence modeling. While hybrid architectures such as Samba and the decoder-decoder architecture, YOCO, have shown promising performance gains over Transformers, prior works have not investigated the efficiency potential of representation sharing between SSM layers. In this paper, we introduce the Gated Memory Unit (GMU), a simple yet effective mechanism for efficient memory sharing across layers. We apply it to create SambaY, a decoder-hybrid-decoder architecture that incorporates GMUs in the cross-decoder to share memory readout states from a Samba-based self-decoder. SambaY significantly enhances decoding efficiency, preserves linear pre-filling time complexity, and boosts long-context performance, all while eliminating the need for explicit positional encoding. Through extensive scaling experiments, we demonstrate that our model exhibits a significantly lower irreducible loss compared to a strong YOCO baseline, indicating superior performance scalability under large-scale compute regimes. Our largest model enhanced with Differential Attention, Phi4-mini-Flash-Reasoning, achieves significantly better performance than Phi4-mini-Reasoning on reasoning tasks such as Math500, AIME24/25, and GPQA Diamond without any reinforcement learning, while delivering up to 10× higher decoding throughput on 2K-length prompts with 32K generation length under the vLLM inference framework. We release our training codebase on open-source data at https://github.com/microsoft/ArchScale.

---

Record id: `title:70a0c3f7ce6097f6`
