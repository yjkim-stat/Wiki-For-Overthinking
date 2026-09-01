<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Distilled Pretraining: A modern lens of Data, In-Context Learning and Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009683>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows distillation-based LLM pretraining improves test-time scaling capability but reduces in-context learning performance (particularly induction-head-driven ICL), tracing this tradeoff to underlying bigram-model dynamics and offering pretraining design recommendations.

## Problem

How knowledge distillation during LLM pretraining affects downstream capabilities -- specifically test-time scaling and in-context learning -- and whether these effects trade off against each other, was not well characterized.

## Contributions

- identification of a tradeoff where distillation-based pretraining improves test-time scaling but degrades in-context learning (particularly induction-head function)
- a bigram-model analysis explaining the mechanistic basis of this tradeoff
- practical pretraining design recommendations informed by the analysis

## Method

Analyzes distilled pretraining through data, in-context-learning, and test-time-scaling lenses, using a bigram-model analysis to explain observed effects mechanistically.

## Results

Distilled models show enhanced test-time scaling capabilities, but this comes paired with reduced in-context learning performance, particularly affecting induction heads; a bigram-model analysis reveals the underlying dynamics explaining this tradeoff.

## Limitations

Not stated in the fetched abstract beyond the bigram-model analytical framework used to explain the tradeoff.

## Why it matters here

- **overthinking**: Indirectly relevant: this is a pretraining-methodology tradeoff study (distillation's effect on test-time scaling vs. in-context learning) rather than an inference-time reasoning-length method, but its finding that improving test-time-scaling capability can come at a measurable cost to another capability is a caution relevant to any overthinking-mitigation approach that optimizes purely for the accuracy/token tradeoff without checking for side effects on other capabilities.

## Entities

- **Concepts**: distilled pretraining, test-time-scaling / in-context-learning tradeoff, induction heads, bigram-model analysis
- **Methods**: distilled pretraining, bigram-model analysis
- **Datasets**: _none recorded_

Tags: `distillation`, `test-time-scaling`, `in-context-learning`, `pretraining`

---

Record id: `title:5d210749910cf061`
