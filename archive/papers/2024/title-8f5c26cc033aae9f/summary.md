<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/93887>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives a compute-optimal recipe for contrastively fine-tuning pretrained decoder-only LLMs into text-embedding models, finding full fine-tuning is optimal at lower compute budgets and LoRA fine-tuning at higher ones.

## Problem

Practitioners lack a principled, compute-optimal recipe for repurposing pretrained decoder-only language models into text-embedding models via contrastive training, across different model sizes, data quantities and fine-tuning methods.

## Contributions

- an algorithm producing compute-optimal model size / data quantity / fine-tuning method configurations for text-embedding training
- an empirical finding that full fine-tuning wins at lower budgets and LoRA at higher budgets
- a practical recipe for repurposing decoder-only LLMs into embedding models at a given compute level

## Method

Runs extensive experiments over a suite of pretrained decoder-only LLMs, varying model size, contrastive training data quantity, and fine-tuning method (full fine-tuning vs. Low-Rank Adaptation), fitting an algorithm that produces optimal configurations at different computational budget levels.

## Results

Full fine-tuning produces optimal embedding models at lower computational budgets, while LoRA fine-tuning is optimal at higher computational budgets; the resulting recipe gives practitioners informed design choices for embedding-model training at a given compute level.

## Limitations

Not stated in the fetched abstract beyond the tested fine-tuning methods (full FT, LoRA) and the decoder-only-LLM starting point.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this is about training-time compute allocation for building embedding models from decoder-only LLMs, unconnected to inference-time reasoning length or test-time compute for reasoning.

## Entities

- **Concepts**: compute-optimal fine-tuning recipe, contrastive text-embedding training, LoRA vs. full fine-tuning tradeoff
- **Methods**: contrastive training, full fine-tuning, Low-Rank Adaptation (LoRA)
- **Datasets**: _none recorded_

Tags: `compute-optimal`, `text-embeddings`, `fine-tuning`, `training-efficiency`

## Abstract

Abstract Text embeddings are essential for tasks such as document retrieval, clustering, and semantic similarity assessment. In this paper, we study how to contrastively train text embedding models in a compute-optimal fashion, given a suite of pretrained decoder-only language models. Our innovation is an algorithm that produces optimal configurations of model sizes, data quantities, and fine-tuning methods for text-embedding models at different computational budget levels. The resulting recipe, which we obtain through extensive experiments, can be used by practitioners to make informed design choices for their embedding models. Specifically, our findings suggest that full fine-tuning and Low-Rank Adaptation fine-tuning produce optimal models at lower and higher computational budgets respectively.

---

Record id: `title:8f5c26cc033aae9f`
