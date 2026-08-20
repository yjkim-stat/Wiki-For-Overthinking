<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TTS-VAR: A Test-Time Scaling Framework for Visual Auto-Regressive Generation

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115886>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes a test-time scaling framework for visual auto-regressive image generation that searches over coarse-to-fine generation paths, improving GenEval score on Infinity2B from 0.69 to 0.75.

## Problem

Scaling visual generation models via additional training is computationally expensive; the paper asks whether test-time scaling -- generating and selecting among multiple candidate paths at inference -- can improve visual auto-regressive generation quality without further training.

## Contributions

- First general test-time scaling framework for visual auto-regressive (VAR) models, framing generation as a path-searching problem
- Clustering-based diversity search at coarse scales to preserve structural variety before later selection
- Resampling-based potential selection at fine scales using reward functions built from multi-scale generation history
- Adaptive descending batch-size schedule to balance compute against exploration during causal generation

## Method

TTS-VAR models the visual auto-regressive generation process as a path-searching problem across VAR's coarse-to-fine multi-scale token generation. At coarse scales, where generated tokens are hard to evaluate reliably, clustering-based diversity search preserves structurally varied candidates via semantic feature clustering rather than risking erroneous accept/reject decisions. At fine scales, resampling-based potential selection ranks candidates using reward functions that incorporate the multi-scale generation history. An adaptive descending batch-size schedule reduces the candidate pool as generation proceeds to trade off compute against exploration.

## Results

On the VAR model Infinity2B, TTS-VAR improves GenEval score by 8.7% (0.69 to 0.75).

## Limitations

The abstract does not report cost/latency overhead of the search process, does not compare against alternative test-time scaling strategies for VAR models, and the reported gain (0.69 to 0.75 GenEval) is on a single model (Infinity2B).

## Why it matters here

- **overthinking**: Tangential. It borrows the phrase 'test-time scaling' and the general idea of allocating extra inference-time computation, but the domain is visual auto-regressive image generation (evaluated via GenEval score), not large language model reasoning. It says nothing about reasoning-length, chain-of-thought tokens, overthinking/underthinking, or when a model should stop generating; the mechanism (path search over image tokens) has no connection to LLM reasoning trajectories.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), path search, diversity search, resampling-based selection
- **Methods**: TTS-VAR, clustering-based diversity search, resampling-based potential selection
- **Datasets**: Infinity2B (VAR model), GenEval benchmark

Tags: `test-time-scaling`, `visual-autoregressive`, `image-generation`, `geneval`, `not-llm-reasoning`

## Abstract

Abstract Scaling visual generation models is essential for real-world content creation, yet requires substantial training and computational expenses. Alternatively, test-time scaling has garnered growing attention due to resource efficiency and promising performance. In this work, we present the first general test-time scaling framework for visual auto-regressive (VAR) models, TTS-VAR, modeling the generation process as a path searching problem. Inspired by VAR's hierarchical coarse-to-fine multi-scale generation, our framework integrates two key components: (i) At coarse scales, we observe that generated tokens are hard for evaluation, possibly leading to erroneous acceptance of inferior samples or rejection of superior samples. Noticing that the coarse scales contain sufficient structural information, we propose clustering-based diversity search. It preserves structural variety through semantic feature clustering, enabling later selection on samples with higher potential. (ii) In fine scales, resampling-based potential selection prioritizes promising candidates using potential scores, which are defined as reward functions incorporating multi-scale generation history. To dynamically balance computational efficiency with exploration capacity, we further introduce an adaptive descending batch size schedule throughout the causal generation process. Experiments on the powerful VAR model Infinity2B show a notable 8.7% GenEval score improvement (0.69→0.75). Key insights reveal that early-stage structural features effectively influence final quality, and resampling efficacy varies across generation scales.

---

Record id: `title:bf9d583811300bbd`
