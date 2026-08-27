<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute-Optimal Quantization-Aware Training

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009552>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives scaling laws for how to optimally split a fixed compute budget between full-precision training and quantization-aware training (QAT), finding the loss-optimal QAT fraction grows with total compute.

## Problem

Practitioners lack a principled way to allocate a fixed training compute budget between full-precision training and quantization-aware training to obtain the best final quantized model.

## Contributions

- a scaling law for the loss-optimal ratio of QAT to full-precision training as a function of total compute
- a tokens-per-parameter-byte statistic predicting the optimal QAT fraction
- a cooldown-QAT fusion method combining learning-rate decay with quantization training

## Method

Runs experiments across model sizes from 86.0M to 2.2B parameters and multiple bit widths, fitting a scaling law that predicts the optimal QAT-to-FP-training ratio and resulting performance, including a tokens-per-parameter-byte statistic and a cooldown-QAT fusion technique combining learning-rate decay with quantization training.

## Results

The loss-optimal ratio of QAT to full-precision training increases with total compute; the derived scaling law predicts optimal QAT ratios and final performance, identifies optimal bit widths under memory constraints, and the cooldown-QAT fusion approach lets practitioners train higher-quality quantized models under the same compute budget.

## Limitations

Not stated in the fetched abstract beyond the tested parameter range (86.0M-2.2B); no discussion of transfer to architectures or bit-width regimes outside those tested.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is about training-time compute allocation between full-precision and quantized training phases, unrelated to inference-time reasoning length or the accuracy/efficiency tradeoff of LLM reasoning traces.

## Entities

- **Concepts**: compute-optimal quantization-aware training, cooldown-QAT fusion, tokens-per-parameter-byte scaling statistic
- **Methods**: quantization-aware training (QAT), [scaling-law fitting](../../../../wiki/methods/scaling-law-fitting.md)
- **Datasets**: _none recorded_

Tags: `quantization`, `compute-optimal`, `scaling-laws`, `training-efficiency`

---

Record id: `title:19ebd4d7f589cbd8`
