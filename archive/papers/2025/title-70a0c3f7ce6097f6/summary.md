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

Introduces the Gated Memory Unit, a mechanism for sharing memory readout states across layers, and uses it to build SambaY, a decoder-hybrid-decoder architecture whose 3.8B instance (Phi4-mini-Flash-Reasoning) matches or beats Phi4-mini-Reasoning on math and science benchmarks while decoding up to 10x faster on 32K-token generations.

## Problem

Hybrid SSM/attention architectures such as Samba and the decoder-decoder YOCO improve on Transformers, but prior work had not exploited representation sharing between SSM layers. The cost that matters here is the per-token cost of decoding a long generation: reasoning workloads emit tens of thousands of tokens, and attention-based cross-decoders make that expensive. The paper's question is architectural -- how to keep long-context quality and linear pre-filling while cutting decoding cost -- not when a model should stop reasoning.

## Contributions

- The Gated Memory Unit (GMU), a gating mechanism for sharing memory readout states across layers.
- SambaY, a decoder-hybrid-decoder architecture placing GMUs in the cross-decoder to consume memory from a Samba-based self-decoder, with linear pre-filling and no explicit positional encoding.
- Scaling experiments showing lower irreducible loss than a YOCO baseline.
- Phi4-mini-Flash-Reasoning (3.8B): higher accuracy than Phi4-mini-Reasoning on AIME24/25, Math500 and GPQA Diamond without RL, at up to 10x decoding throughput on 32K generations under vLLM.
- Released training codebase on open-source data (microsoft/ArchScale).

## Method

The Gated Memory Unit (GMU) computes y_l = (m_l' * sigma(W1 x_l)) W2: a memory representation from an earlier layer is gated elementwise by a projection of the current layer's input, then projected out. SambaY applies this in a decoder-hybrid-decoder layout: a Samba-based self-decoder (Mamba SSM layers plus one full-attention layer) produces memory readout states, and the cross-decoder replaces half of its cross-attention layers with GMUs that read those states from the last SSM layers of the self-decoder. This preserves linear pre-filling time complexity, removes the need for explicit positional encoding, and cuts per-token decoding work. The largest model adds Differential Attention and is released as Phi4-mini-Flash-Reasoning (3.8B), trained without reinforcement learning.

## Results

Phi4-mini-Flash-Reasoning (3.8B) vs Phi4-mini-Reasoning: AIME24 52.29% vs 48.13%, AIME25 33.59% vs 31.77%, Math500 92.45% vs 91.20%, GPQA Diamond 45.08% vs 44.51%. Efficiency: up to 10x higher decoding throughput on 2K-length prompts with 32K generation length under vLLM, and 4.9x speedup in long-context processing. Scaling experiments report a lower irreducible loss than a YOCO baseline. Evaluation uses a maximum generation length of 32K. The paper reports no measurement of accuracy as a function of reasoning-chain length, and no token-count comparison between the two models -- the efficiency axis throughout is throughput and latency, not tokens emitted.

## Limitations

Stated: the Differential Attention implementation uses a naive four-pass of the FlashAttention operator for vLLM compatibility rather than an optimized custom kernel, leaving speed on the table. A reader should also notice: (1) the accuracy margins over Phi4-mini-Reasoning are small and, on AIME24/25 (30 problems each), within the range a handful of problems can move -- +4.16 points on AIME24 is at most a couple of items; (2) 'efficient reasoning' here means faster tokens, not fewer: no reasoning-length statistic, token-budget sweep or overthinking analysis appears anywhere in the paper; (3) the 10x figure is measured at one operating point (2K prompt, 32K generation, vLLM) and does not generalize as a blanket speedup; (4) results are at a single 3.8B scale for the reasoning model, with scaling evidence coming from loss curves rather than downstream accuracy.

## Why it matters here

- **overthinking**: Tangential, and the record should say so plainly. This is an architecture paper: its efficiency claim is decoding throughput (up to 10x at 2K prompt / 32K generation under vLLM) and long-context processing speed (4.9x), and it measures accuracy on Math500, AIME24/25 and GPQA Diamond separately from that. It never measures a reasoning-length/accuracy tradeoff, never varies a token budget, and never uses the word overthinking; the matched keyword was 'efficient reasoning' in the throughput sense, not the length sense. It is worth keeping only as a boundary marker for the topic: it shows that the cost of long reasoning can be attacked at the serving layer instead of the trace-length layer, so a throughput result and a token-reduction result are not comparable quantities and should not be pooled when the group compares efficiency numbers across the archive. If the group wants an architectural counterpart to the compression and early-exit literature, this is that; it is not evidence about when a model should stop.

## Entities

- **Concepts**: State Space Models, Hybrid Attention-SSM Architecture, Cross-Layer Memory Sharing, Decoding Throughput, Linear Pre-filling Complexity, Long Generation, Irreducible Loss Scaling
- **Methods**: Gated Memory Unit (GMU), SambaY, Samba, YOCO, Mamba / State Space Models, Differential Attention, Phi4-mini-Flash-Reasoning, [vLLM](../../../../wiki/methods/vllm.md)
- **Datasets**: [Math500](../../../../wiki/datasets/math500.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `architecture`, `state space models`, `decoding throughput`, `long generation`, `hybrid model`, `gated memory unit`, `inference efficiency`

## Abstract

Abstract Recent advances in language modeling have demonstrated the effectiveness of State Space Models (SSMs) for efficient sequence modeling. While hybrid architectures such as Samba and the decoder-decoder architecture, YOCO, have shown promising performance gains over Transformers, prior works have not investigated the efficiency potential of representation sharing between SSM layers. In this paper, we introduce the Gated Memory Unit (GMU), a simple yet effective mechanism for efficient memory sharing across layers. We apply it to create SambaY, a decoder-hybrid-decoder architecture that incorporates GMUs in the cross-decoder to share memory readout states from a Samba-based self-decoder. SambaY significantly enhances decoding efficiency, preserves linear pre-filling time complexity, and boosts long-context performance, all while eliminating the need for explicit positional encoding. Through extensive scaling experiments, we demonstrate that our model exhibits a significantly lower irreducible loss compared to a strong YOCO baseline, indicating superior performance scalability under large-scale compute regimes. Our largest model enhanced with Differential Attention, Phi4-mini-Flash-Reasoning, achieves significantly better performance than Phi4-mini-Reasoning on reasoning tasks such as Math500, AIME24/25, and GPQA Diamond without any reinforcement learning, while delivering up to 10× higher decoding throughput on 2K-length prompts with 32K generation length under the vLLM inference framework. We release our training codebase on open-source data at https://github.com/microsoft/ArchScale.

---

Record id: `title:70a0c3f7ce6097f6`
