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

Reduces the number of video tokens fed to a multimodal LLM for long videos via redundant-frame removal, text-guided feature reduction, and temporal-relationship-based spatial compression.

## Problem

Multimodal language models struggle to process long videos because the number of video tokens grows with length; the paper addresses how to compress that token count without losing the visual detail needed for understanding.

## Contributions

- Adaptive spatiotemporal compression mechanism that reduces the number of video tokens fed to a multimodal LLM while preserving visual detail for long videos
- Removes redundant frames via similarity detection
- Applies text-guided (query-aware) selective feature reduction
- Performs spatial compression based on temporal relationships between frames
- Shows the approach also works when scaled down to smaller language models

## Method

LongVU uses cross-modal interactions and temporal dependencies to cut the number of video tokens given to a multimodal language model while keeping visual detail. It combines three steps: (1) removing redundant frames using similarity detection, (2) applying text-guided selective feature reduction, and (3) performing spatial compression based on temporal relationships between frames.

## Results

The fetched material reports consistent improvements across video understanding benchmarks, particularly for extended videos, and states the approach remains effective when scaled to smaller language models; no specific numeric scores were available in the fetched material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. This is a video-language model paper about compressing video tokens (frame redundancy removal, text-guided feature reduction, spatial compression) for long video understanding. It shares only the generic phrase 'adaptive compression' with the tracked topic and says nothing about reasoning length, test-time compute scaling for reasoning, or the accuracy/efficiency tradeoff of how long a reasoning model thinks.

## Entities

- **Concepts**: video token compression, cross-modal query-aware selection, temporal redundancy removal
- **Methods**: LongVU
- **Datasets**: long video understanding benchmarks (not individually named in the fetched material)

Tags: `video-language-model`, `token-compression`, `long-video`, `tangential`

---

Record id: `title:e6798b25772b7879`
