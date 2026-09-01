<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute-Optimal LLMs Provably Generalize Better with Scale

- **Authors**: _unknown_
- **Venue**: ICLR 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2025/poster/29945>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives theoretical generalization bounds for compute-optimal (Chinchilla-scaling-law) LLM pretraining using a novel empirical Freedman-type martingale concentration inequality, showing larger models have provably smaller generalization gaps because loss variance and quantization error decline with scale even as the parameters-per-token ratio stays fixed.

## Problem

It is empirically well known that larger language models generalize better, but a theoretical explanation for why this holds specifically in the compute-optimal (Chinchilla) scaling regime, accounting for the actual training dynamics (loss variance, quantization) rather than only capacity, is lacking.

## Contributions

- a novel fully empirical Freedman-type martingale concentration inequality improving on prior generalization bounds by incorporating loss variance
- a theoretical account of why compute-optimal LLMs generalize better with scale, via three identified factors: parameters per token, loss variance, and quantization error
- an information-theoretic explanation for larger models' greater quantizability
- a derived scaling law for the generalization gap itself

## Method

Introduces a novel, fully empirical Freedman-type martingale concentration inequality that improves on prior generalization bounds by explicitly incorporating loss variance, then applies it to LLM pretraining under the compute-optimal (fixed parameters-per-token) scaling regime; identifies three factors governing the generalization bound -- parameters per token, loss variance, and quantization error -- and analyzes how each evolves with scale from an information-theoretic perspective (the model's information-integration rate growing more slowly than its capacity at the compute-optimal frontier).

## Results

At the compute-optimal frontier, as models scale, the parameters-to-data ratio stays constant, but both loss variance and quantization error decline, implying provably smaller generalization gaps for larger models; the paper concludes with a scaling law for the generalization gap itself, showing the derived bounds decrease in a predictable, quantifiable way with scale, and offers an information-theoretic explanation for why larger models are also more quantizable.

## Limitations

Not stated in the fetched abstract; the analysis is specific to the compute-optimal (Chinchilla) scaling regime and theoretical/empirical bound framework described.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is a theoretical generalization-bound analysis of pretraining-compute scaling, unconnected to inference-time reasoning length or test-time compute for LLM reasoning.

## Entities

- **Concepts**: Freedman-type martingale concentration inequality, compute-optimal (Chinchilla) generalization bound, quantization error as a generalization factor, information-integration rate vs. capacity
- **Methods**: Freedman-type martingale concentration inequality, compute-optimal (Chinchilla) scaling analysis
- **Datasets**: _none recorded_

Tags: `generalization-theory`, `compute-optimal`, `scaling-laws`, `quantization`

---

Record id: `title:0928f999b4f927ff`
