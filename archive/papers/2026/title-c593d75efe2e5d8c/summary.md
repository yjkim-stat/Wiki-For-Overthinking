<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011689>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Studies how quantization, distillation and pruning affect DeepSeek-R1's reasoning ability using mechanistic interpretation, finding weight count matters more for knowledge memorization than reasoning, and that protecting just 2% of over-compressed weights recovers 6.57 accuracy points.

## Problem

How compression techniques (quantization, distillation, pruning) specifically affect the reasoning capability of large reasoning models -- as opposed to general LLM capability -- and which model components are actually load-bearing for reasoning, was not well understood.

## Contributions

- a mechanistic-interpretation study isolating which model components matter for reasoning vs. memorization under compression
- a finding that weight count affects memorization more than reasoning, informing pruning/distillation risk
- a targeted-protection method (2% of weights) recovering 6.57 accuracy points, exceeding prior compression-mitigation methods

## Method

Applies quantization, distillation, and pruning to DeepSeek-R1 and evaluates across four reasoning benchmarks, using mechanistic interpretation methods to identify which model components are critical for reasoning versus for knowledge memorization.

## Results

Weight count has a greater impact on knowledge memorization than on reasoning, implying pruning and distillation carry particular reasoning risk; the MLP up-projection in the final layer is especially important in distilled models; current quantization methods over-compress the final-layer modules and MLP gate projections; protecting just 2% of the most excessively compressed weights increases average accuracy by 6.57%, exceeding existing mitigation methods.

## Limitations

Not stated in the fetched abstract beyond the four reasoning benchmarks and DeepSeek-R1 as the studied model.

## Why it matters here

- **overthinking**: Relevant as an efficiency-side result on the same class of models: it identifies which components of a reasoning model can be safely compressed without hurting reasoning, complementary to (but distinct from) reasoning-length-focused overthinking mitigations -- both aim at making reasoning-time compute cheaper, one via smaller/faster models and the other via shorter traces.

## Entities

- **Concepts**: mechanistic interpretation of compression effects, reasoning-critical weight identification, compression-induced reasoning degradation
- **Methods**: quantization, [distillation](../../../../wiki/methods/knowledge-distillation.md), pruning, mechanistic interpretability analysis
- **Datasets**: _none recorded_

Tags: `model-compression`, `large-reasoning-models`, `mechanistic-interpretability`, `quantization`

---

Record id: `title:c593d75efe2e5d8c`
