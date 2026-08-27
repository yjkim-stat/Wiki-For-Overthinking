<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011723>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

HiDrop reduces multimodal LLM inference cost by pruning ~90% of visual tokens through Late Injection, Concave Pyramid Pruning and an Early Exit mechanism, matching original performance while accelerating training by 1.72x.

## Problem

Processing visual tokens in multimodal large language models is computationally expensive, and existing pruning approaches for reducing visual token count carry efficiency overhead or do not adapt pruning rate to content.

## Contributions

- Late Injection, delaying visual-token introduction to the point of active fusion
- Concave Pyramid Pruning combined with an Early Exit mechanism for adaptive pruning rate
- ~90% visual-token compression matching original performance with 1.72x training acceleration

## Method

Introduces Late Injection, which strategically delays introducing visual tokens until the point where active cross-modal fusion begins, combined with Concave Pyramid Pruning and an Early Exit mechanism for adaptive pruning-rate adjustment across layers; uses an inter-layer similarity metric with a differentiable top-k operator, plus persistent positional encoding, FlashAttention-compatible token selection, and parallel decoupling of visual computation to remove overhead.

## Results

HiDrop compresses ~90% of visual tokens while matching original model performance and accelerating training by 1.72x, reported as state-of-the-art efficiency for both training and inference in multimodal systems.

## Limitations

Not stated in the fetched abstract beyond the described mechanisms and the 90%/1.72x headline figures.

## Why it matters here

- **overthinking**: Off-topic domain (visual-token efficiency in multimodal LLMs rather than text reasoning length), matched via 'early exit'; relevant only as a cross-modal parallel showing adaptive, content-dependent pruning of an input representation can preserve accuracy while cutting compute substantially.

## Entities

- **Concepts**: Late Injection, Concave Pyramid Pruning, adaptive visual-token early exit
- **Methods**: differentiable top-k token selection, FlashAttention-compatible token selection, early-exit visual token pruning
- **Datasets**: _none recorded_

Tags: `multimodal`, `token-pruning`, `early-exit`, `efficiency`, `MLLM`

---

Record id: `title:b2302bb0271de496`
