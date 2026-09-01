<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SwiftPFN: Revisiting Row-Wise Attention–Only Tabular Foundation Models with Adaptive Early Exit

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61560>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

SwiftPFN is a streamlined tabular foundation model using a lightweight row-wise attention-only backbone (with gated attention stabilization and learnable register tokens) plus an adaptive layer-wise early-exit mechanism, matching TabPFN v2/TabICL accuracy on classification and regression while cutting inference compute.

## Problem

Tabular foundation models built on in-context learning (e.g. TabPFN) achieve strong accuracy but at high inference cost, and it is unclear how much of their architectural complexity is needed versus how much compute could be saved by adapting inference depth per sample.

## Contributions

- a lightweight row-wise-attention-only tabular foundation model matching more complex architectures (TabPFN v2, TabICL) at lower inference cost
- gated attention stabilization and learnable register tokens improving context and pretraining quality
- an adaptive per-sample early-exit mechanism enabling anytime inference

## Method

Builds a lightweight row-wise attention-only backbone (dropping column-wise attention used in prior TabPFN-style models) with two additions -- gated attention stabilization and learnable register tokens -- for improved context and pretraining quality; adds an adaptive layer-wise early-exit mechanism that dynamically adjusts inference depth per sample, letting shallow layers make reliable predictions on many samples.

## Results

SwiftPFN matches the performance of TabPFN v2 and TabICL on both classification and regression tasks while requiring fewer computational resources at inference; the adaptive early-exit mechanism reduces overall computation cost with minimal accuracy loss by allowing many samples to exit at shallow layers.

## Limitations

Not stated in the fetched abstract beyond the classification/regression task scope and the comparison models (TabPFN v2, TabICL).

## Why it matters here

- **overthinking**: Off-topic domain: this is an early-exit efficiency method for tabular in-context learning (classification/regression), unrelated to LLM reasoning-trace length or the accuracy/efficiency tradeoff of text-based reasoning; matched to the topic only via the shared term 'adaptive early exit'.

## Entities

- **Concepts**: row-wise attention-only backbone, gated attention stabilization, adaptive layer-wise early exit, anytime tabular in-context learning
- **Methods**: SwiftPFN, adaptive layer-wise early exit, gated attention stabilization
- **Datasets**: _none recorded_

Tags: `tabular-foundation-model`, `early-exit`, `in-context-learning`, `inference-efficiency`

---

Record id: `title:01b92aa66908c5e0`
