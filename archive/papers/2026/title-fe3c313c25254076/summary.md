<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011824>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ParoQuant is a post-training weight quantization method for reasoning LLMs that uses pairwise Givens rotations plus channel-wise scaling to even out per-channel outlier magnitudes, achieving 2.4% higher accuracy than AWQ on reasoning tasks at under 10% inference overhead.

## Problem

Post-training quantization reduces LLM memory and inference cost but outlier weight/activation magnitudes cause substantial quantization error and accuracy loss, and this is especially damaging for reasoning models because errors compound through long chains of reasoning steps; existing outlier-handling methods either handle outliers inadequately or impose heavy inference cost.

## Contributions

- ParoQuant, combining hardware-efficient pairwise Givens rotations with channel-wise scaling for outlier-robust quantization
- co-designed inference kernels maximizing GPU efficiency at low overhead
- 2.4% average accuracy improvement over AWQ on reasoning tasks under weight-only quantization, at <10% overhead

## Method

Introduces ParoQuant, combining hardware-efficient, optimizable independent Givens (pairwise) rotations with channel-wise scaling to even out magnitude differences across channels and narrow the dynamic range within each quantization group, paired with co-designed inference kernels that maximize GPU efficiency while keeping computational overhead minimal.

## Results

Under weight-only quantization, ParoQuant achieves an average 2.4% accuracy improvement over AWQ on reasoning tasks with under 10% inference overhead, and performs comparably to leading weight-activation quantization approaches.

## Limitations

Not stated in the fetched abstract beyond the weight-only-quantization comparison setting; comparison to weight-activation quantization is only described as 'comparable,' with no numeric detail retrieved.

## Why it matters here

- **overthinking**: Directly relevant as a complementary efficiency lever: it notes explicitly that quantization errors compound through long reasoning chains, making reasoning models especially sensitive to outlier-induced quantization error -- tying model-compression fidelity to the same long-generation cost that reasoning-length-focused overthinking mitigations address from the other direction (shortening the chain rather than cheapening each step).

## Entities

- **Concepts**: pairwise (Givens) rotation quantization, channel-wise outlier scaling, outlier-error compounding in reasoning chains
- **Methods**: Givens (pairwise) rotation quantization, channel-wise scaling, post-training quantization
- **Datasets**: _none recorded_

Tags: `quantization`, `efficient-reasoning`, `inference-efficiency`, `large-reasoning-models`

---

Record id: `title:fe3c313c25254076`
