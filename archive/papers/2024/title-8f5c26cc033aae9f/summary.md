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

Derives a compute-optimal recipe for contrastively converting pretrained decoder-only language models into text embedding models, jointly choosing model size, data quantity and fine-tuning method for a given training budget.

## Problem

Text embeddings underpin document retrieval, clustering and semantic similarity, and are commonly obtained by contrastively fine-tuning an existing decoder-only language model. A practitioner with a fixed training budget must decide simultaneously how large a base model to start from, how much contrastive data to use, and whether to fine-tune fully or with a parameter-efficient method -- and no recipe existed that settles those three choices jointly against budget.

## Contributions

- An algorithm that returns optimal configurations of model size, data quantity and fine-tuning method for text-embedding models at a given compute budget
- An empirical recipe for practitioners choosing among pretrained decoder-only models for embedding fine-tuning
- The finding that full fine-tuning is compute-optimal at lower budgets while Low-Rank Adaptation is compute-optimal at higher budgets

## Method

Given a suite of pretrained decoder-only language models, the authors run contrastive embedding fine-tuning across a grid of model sizes, data quantities and fine-tuning methods, and fit an algorithm that returns the optimal configuration of those three variables at a given computational budget level. The output is a practitioner-facing recipe: read off the budget, get the size, data quantity and fine-tuning method to use.

## Results

The abstract reports one qualitative finding and no numbers: full fine-tuning is compute-optimal at lower budgets and Low-Rank Adaptation at higher budgets. No embedding benchmark scores, model sizes, data quantities, FLOP figures or scaling-law coefficients are stated in the material available.

## Limitations

The abstract states no numbers, so the crossover budget at which LoRA overtakes full fine-tuning -- the practically decisive quantity -- is not given here, nor is the evaluation benchmark named. The recipe is fitted over a particular suite of pretrained decoder-only models, so its transfer to encoder architectures or to a different pretraining corpus is not established. Compute-optimality is defined over training budget; inference cost of the resulting embedding model is not part of the objective, though it is what usually dominates in a deployed retrieval system.

## Why it matters here

- **overthinking**: Not relevant to this topic. The match came from the keyword "compute-optimal", which in this paper means allocating a training budget across model size, data quantity and fine-tuning method for text embedding models -- Chinchilla-style training-time scaling. The topic concerns test-time compute: how long a reasoning model thinks on a given problem and when it should stop. Those are different budgets spent at different times on different quantities, and the paper contains no reasoning model, no chain of thought, no inference-length tradeoff and no test-time scaling result. Its subject is retrieval and semantic similarity embeddings. There is no finding here for the group to carry across. File as a false positive of the keyword filter.

## Entities

- **Concepts**: [Compute-Optimal Scaling](../../../../wiki/concepts/compute-optimal-scaling.md), Contrastive Text Embeddings, Parameter-Efficient Fine-Tuning, Training Budget Allocation
- **Methods**: contrastive learning, full fine-tuning, Low-Rank Adaptation (LoRA), compute-optimal scaling analysis, decoder-only language models
- **Datasets**: _none recorded_

Tags: `compute-optimal`, `text embeddings`, `contrastive learning`, `lora`, `fine-tuning`, `scaling laws`, `retrieval`, `off-topic`, `neurips-2024`

## Abstract

Abstract Text embeddings are essential for tasks such as document retrieval, clustering, and semantic similarity assessment. In this paper, we study how to contrastively train text embedding models in a compute-optimal fashion, given a suite of pretrained decoder-only language models. Our innovation is an algorithm that produces optimal configurations of model sizes, data quantities, and fine-tuning methods for text-embedding models at different computational budget levels. The resulting recipe, which we obtain through extensive experiments, can be used by practitioners to make informed design choices for their embedding models. Specifically, our findings suggest that full fine-tuning and Low-Rank Adaptation fine-tuning produce optimal models at lower and higher computational budgets respectively.

---

Record id: `title:8f5c26cc033aae9f`
