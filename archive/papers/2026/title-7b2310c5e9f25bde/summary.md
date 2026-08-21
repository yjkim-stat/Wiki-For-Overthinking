<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TEST-TIME SCALING IN DIFFUSION LLMS VIA HIDDEN SEMI-AUTOREGRESSIVE EXPERTS

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010063>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows diffusion LLMs implicitly contain a mixture of semi-autoregressive generation experts and introduces a training-free method that majority-votes across multiple block generation schedules to substantially boost accuracy.

## Problem

It is unclear how to best use test-time flexibility in diffusion-based LLMs' generation order; committing to a single fixed inference schedule, the common practice, discards specialized behaviors available under different generation orders.

## Contributions

- Identifies that diffusion large language models (dLLMs) trained on text implicitly learn a mixture of semi-autoregressive experts, where different generation orders reveal different specialized behaviors.
- Shows that committing to a single fixed inference-time generation schedule collapses performance by not leveraging this latent ensemble.
- Introduces HEX, a training-free inference method that ensembles across heterogeneous block schedules via majority vote to avoid failure modes tied to any one fixed schedule.
- Reports large accuracy gains on reasoning and QA benchmarks without additional training.

## Method

HEX (Hidden semi-autoregressive EXperts) treats a diffusion LLM's choice of block-generation schedule (the order/granularity in which masked tokens are filled in) as selecting among an implicit ensemble of semi-autoregressive experts. Instead of committing to one fixed schedule, HEX runs generation under several heterogeneous block schedules and takes a majority vote over the resulting outputs, without any additional training.

## Results

On GSM8K, HEX boosts accuracy from 24.72% to 88.10% (up to 3.56x); on MATH from 16.40% to 40.00%; on ARC-C from 54.18% to 87.80%; on TruthfulQA from 28.36% to 57.46%; outperforms top-K margin inference and GRPO-based fine-tuning without additional training.

## Limitations

The abstract does not report the inference-time/compute overhead of running the majority vote across multiple block schedules, nor which specific dLLM model(s) were tested, nor behavior on tasks outside these four benchmarks.

## Why it matters here

- **overthinking**: Tangential. This addresses test-time scaling for diffusion language models by ensembling over token-generation *orders/schedules*, not the length of a reasoning chain or when a reasoning model should stop or keep deliberating. It shares only the generic phrase 'test-time scaling' with the tracked topic; there is no treatment of the accuracy/reasoning-length tradeoff central to overthinking.

## Entities

- **Concepts**: mixture of semi-autoregressive experts (dLLMs), block generation schedule, ensembling over generation orders
- **Methods**: HEX (Hidden semi-autoregressive Experts), majority-vote ensembling, block-schedule diffusion generation
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), ARC-C, [TruthfulQA](../../../../wiki/datasets/truthfulqa.md)

Tags: `diffusion-llm`, `test-time-scaling`, `ensembling`, `block-schedule`, `training-free`

## Abstract

Abstract Diffusion-based large language models (dLLMs) are trained to model extreme flexibility/dependence in the data-distribution; however, how to best utilize this at inference time remains an open problem. In this work, we uncover an interesting property of these models: dLLMs {trained on textual data} implicitly learn a mixture of semi-autoregressive experts, where different generation orders reveal different specialized behaviors. We show that committing to any single, fixed inference time schedule, a common practice, collapses performance by failing to leverage this latent ensemble. To address this, we introduce HEX (Hidden semi-autoregressive EXperts for test-time scaling), a training-free inference method that ensembles across heterogeneous block schedules. By doing a majority vote over diverse block-sized generation paths, HEX robustly avoids failure modes associated with any single fixed schedule. On reasoning benchmarks such as GSM8K, it boosts accuracy by up to 3.56× (from 24.72\% to 88.10\%), outperforming top-K margin inference and specialized fine-tuned methods like GRPO, without additional training. HEX even yields significant gains on MATH benchmark from 16.40\% to 40.00\%, scientific reasoning on ARC-C from 54.18\% to 87.80\%, and TruthfulQA from 28.36\% to 57.46\%. Our results establish test-time scaling as a powerful principle for dLLMs, showing that the sequence in which masking is done can play a significant role in test-time scaling/inferencing of dLLMs.

---

Record id: `title:7b2310c5e9f25bde`
