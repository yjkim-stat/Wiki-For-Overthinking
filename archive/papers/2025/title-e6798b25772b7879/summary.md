<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/44939>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

LongVU is a spatiotemporal adaptive compression method for long video-language understanding that reduces video token count while preserving visual detail, identifying redundant frames via DINOv2 features, applying text-guided selective feature reduction, and performing temporal-relationship-based spatial token compression, achieving strong results on VideoMME and MLVU while remaining compatible with lightweight LLM backbones.

## Problem

Processing long videos within multimodal language models requires representing many frames as tokens, which quickly exceeds context budgets or computational limits, and naive uniform token reduction risks losing important visual details.

## Contributions

- LongVU, a spatiotemporal adaptive video-token compression method combining redundant-frame detection, text-guided feature reduction, and temporal-relationship-based spatial compression
- compatibility with lightweight LLM backbones for practical long-video deployment
- superior performance on VideoMME and MLVU with substantially reduced video token counts and little visual information loss

## Method

LongVU reduces video token count while preserving visual detail by leveraging cross-modal interactions and frame dependencies: it identifies redundant frames using DINOv2 feature similarity, applies text-guided selective feature reduction (using the query text to decide which visual features matter), and performs spatial token compression informed by temporal relationships between frames.

## Results

LongVU effectively processes a large number of video frames with little visual information loss, demonstrating superior performance on the VideoMME and MLVU long-video-understanding benchmarks, while remaining compatible with lightweight language model architectures for deployment.

## Limitations

Not stated in the fetched abstract beyond the VideoMME/MLVU benchmark results and lightweight-LLM compatibility claim.

## Why it matters here

- **overthinking**: Off-topic domain: this is a video-token compression method for long-video multimodal understanding, unrelated to LLM text-reasoning-trace length; matched to the topic only via the shared term 'adaptive compression'.

## Entities

- **Concepts**: spatiotemporal adaptive compression, DINOv2-based redundant-frame detection, text-guided selective feature reduction
- **Methods**: LongVU (spatiotemporal adaptive compression), DINOv2 (redundant-frame detection)
- **Datasets**: VideoMME, MLVU

Tags: `long-video-understanding`, `token-compression`, `multimodal`, `adaptive-compression`

---

Record id: `title:e6798b25772b7879`
