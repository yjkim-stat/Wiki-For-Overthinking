<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116088>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Analyzes large reasoning models by clustering their hidden states into a 'reasoning graph' and studying how its cyclicity, diameter and small-world structure relate to task difficulty, model scale and accuracy.

## Problem

The internal mechanisms behind large reasoning models' success on hard math benchmarks are poorly understood; the paper asks what structural properties of the reasoning process (as a graph over hidden states) distinguish stronger reasoners.

## Contributions

- Introduces the 'reasoning graph', built by clustering hidden-state representations at each reasoning step, as a structural object for analyzing large reasoning models
- Shows that distilled reasoning models (e.g. DeepSeek-R1-Distill-Qwen-32B) have about 5 recurrent cycles per sample, substantially larger graph diameters, and about 6x stronger small-world characteristics than their base counterparts
- Finds these structural properties grow with task difficulty and model capacity, with cycle detection peaking at 14B scale and diameter maximized at 32B, correlating positively with accuracy
- Shows supervised fine-tuning on an improved dataset expands reasoning graph diameter alongside performance gains, offering guidance for dataset design

## Method

Extracts hidden-state representations at each reasoning step of a model's chain of thought, clusters them into nodes, and connects them by generation order to form a 'reasoning graph'; analyzes graph-theoretic properties (cyclicity, diameter, small-world index) across models and tasks and correlates them with accuracy.

## Results

Distilled models show about 5 recurrent cycles per sample versus fewer in base models, roughly 6x higher small-world index, and larger graph diameters; cycle detection peaks at 14B scale and diameter is maximized at 32B; these properties correlate positively with accuracy on GSM8K, MATH500 and AIME 2024. Supervised fine-tuning on an improved dataset expands diameter alongside accuracy gains.

## Limitations

The abstract does not state limitations explicitly; no PDF was attached, so method details beyond the abstract (e.g. clustering procedure, statistical significance, generalization beyond math tasks) could not be verified.

## Why it matters here

- **overthinking**: This studies the structure of a model's reasoning trace (recurrent cycles, exploration diameter) and how it scales with task difficulty and model size, which touches on how much and in what pattern a model reasons, but it is an interpretability study of reasoning structure and accuracy correlation, not a treatment of the accuracy/efficiency tradeoff, reasoning-length control, or stopping criteria that the topic centers on. The connection is adjacent rather than direct: more recurrent cycles could be read as redundant (overthinking-like) reasoning, but the paper does not frame or measure it that way.

## Entities

- **Concepts**: [reasoning graph](../../../../wiki/concepts/reasoning-graph.md), cyclicity, graph diameter, small-world index
- **Methods**: [reasoning graph extraction](../../../../wiki/methods/reasoning-graph-extraction.md), hidden-state clustering, graph-theoretic analysis (cyclicity, diameter, small-world index)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, [AIME 2024](../../../../wiki/datasets/aime-2024.md)

Tags: `interpretability`, `reasoning-graph`, `hidden-states`, `graph-theory`, `scaling`

## Abstract

Abstract Recent large-scale reasoning models have achieved state-of-the-art performance on challenging mathematical benchmarks, yet the internal mechanisms underlying their success remain poorly understood. In this work, we introduce the notion of a reasoning graph, extracted by clustering hidden‐state representations at each reasoning step, and systematically analyze three key graph-theoretic properties: cyclicity, diameter, and small-world index, across multiple tasks (GSM8K, MATH500, AIME~2024). Our findings reveal that distilled reasoning models (e.g., DeepSeek-R1-Distill-Qwen-32B) exhibit significantly more recurrent cycles (about 5 per sample), substantially larger graph diameters, and pronounced small-world characteristics (about 6x) compared to their base counterparts. Notably, these structural advantages grow with task difficulty and model capacity, with cycle detection peaking at the 14B scale and exploration diameter maximized in the 32B variant, correlating positively with accuracy. Furthermore, we show that supervised fine-tuning on an improved dataset systematically expands reasoning graph diameters in tandem with performance gains, offering concrete guidelines for dataset design aimed at boosting reasoning capabilities. By bridging theoretical insights into reasoning graph structures with practical recommendations for data construction, our work advances both the interpretability and the efficacy of large reasoning models.

---

Record id: `title:11c5eb0da4499b68`
