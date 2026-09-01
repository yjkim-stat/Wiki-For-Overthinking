<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BEEM: Boosting Performance of Early Exit DNNs using Multi-Exit Classifiers as Experts

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/30371>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

BEEM treats early-exit classifiers as an ensemble of experts, aggregating their confidence scores only when neighboring exits agree, and exits a sample once the aggregated confidence crosses a threshold set from intermediate-exit error rates, achieving 1.5-2.1x speedups over existing early-exit methods on image captioning (COCO) and language (GLUE) tasks with comparable or better accuracy.

## Problem

Early-exit deep neural networks reduce inference latency by allowing intermediate classifiers to make predictions once confident enough, but existing early-exit methods do not fully exploit the ensemble-like relationship between exit classifiers at different depths.

## Contributions

- BEEM, aggregating multi-exit classifier confidence as an ensemble of experts, gated by inter-exit prediction consistency
- an exit-threshold calibration procedure using intermediate exit error rates
- 1.5-2.1x speedup over existing early-exit methods with comparable-or-better accuracy on COCO captioning and GLUE

## Method

Treats each exit classifier as an 'expert' and combines their confidence scores into an ensemble prediction, but aggregates scores across neighboring exits only when their predictions are consistent (to avoid ensembling disagreeing/unreliable experts); a sample exits once the aggregated confidence surpasses a threshold, with the threshold determined from intermediate exit error rates so the method matches or exceeds standard (final-layer) DNN performance.

## Results

On COCO image captioning and GLUE language tasks, BEEM achieves speedups ranging from 1.5x to 2.1x over existing early-exit methods, reaching comparable accuracy to final-layer inference on harder tasks and improved performance on simpler ones.

## Limitations

Not stated in the fetched abstract beyond the two evaluated task types (image captioning, GLUE language tasks).

## Why it matters here

- **overthinking**: Off-topic domain: this is a layer-level early-exit method for vision/NLP classification and captioning tasks (not LLM reasoning-trace generation), matched to the topic only via the shared term 'early exit'; relevant only as a general pattern (treating multiple exit points as an ensemble rather than independent) that could in principle inform token-level early-exit design for reasoning traces.

## Entities

- **Concepts**: exit classifiers as experts, consistency-gated confidence aggregation, error-rate-calibrated exit threshold
- **Methods**: BEEM (multi-exit ensemble early exit)
- **Datasets**: COCO (image captioning), GLUE

Tags: `early-exit`, `ensemble-methods`, `inference-efficiency`, `image-captioning`

---

Record id: `title:033e4d34acb0410b`
