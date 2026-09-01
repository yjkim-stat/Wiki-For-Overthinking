<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# QUTE: Quantifying Uncertainty in TinyML models with Early-exit-assisted ensembles for model-monitoring

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/45956>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

QUTE is a resource-efficient early-exit-assisted ensemble architecture for uncertainty quantification on tinyML devices, distilling early-exit knowledge into lightweight output blocks at the final exit, achieving comparable UQ quality to larger prior methods with 59% smaller model size and 31% lower on-device latency.

## Problem

On-device uncertainty quantification (UQ) for monitoring tinyML models deployed without access to true labels needs to be resource-efficient, but existing UQ methods -- including prior early-exit ensembles that quantify uncertainty in a single forward pass -- still impose prohibitive memory and compute costs for ultra-low-power, KB-sized tinyML devices.

## Contributions

- QUTE, a resource-efficient early-exit-assisted ensemble for uncertainty quantification optimized for tinyML devices
- distillation of early-exit knowledge into lightweight final-exit output blocks forming a diverse ensemble
- 59% smaller model size and 31% lower microcontroller latency than the closest prior work, with superior accuracy-drop detection

## Method

QUTE introduces additional output blocks at the final exit of the base network and distills early-exit knowledge into these blocks, forming a diverse yet lightweight ensemble for uncertainty quantification, optimized specifically for tinyML deployment constraints.

## Results

QUTE delivers superior uncertainty quality on tiny models and achieves comparable performance to the closest prior work on larger models while being 59% smaller; deployed on a microcontroller, it demonstrates a 31% average latency reduction and outperforms all prior methods at detecting accuracy-drop events.

## Limitations

Not stated in the fetched abstract beyond the tinyML/microcontroller deployment scope.

## Why it matters here

- **overthinking**: Off-topic domain: this is an early-exit ensemble method for uncertainty quantification on tinyML/microcontroller devices, unrelated to LLM reasoning-trace length; matched to the topic only via the shared term 'early exit'.

## Entities

- **Concepts**: early-exit knowledge distillation for uncertainty quantification, resource-efficient ensemble architecture, on-device model-monitoring
- **Methods**: QUTE (early-exit-assisted ensemble)
- **Datasets**: _none recorded_

Tags: `early-exit`, `uncertainty-quantification`, `tinyml`, `edge-devices`

---

Record id: `title:53c7cfefc569f403`
