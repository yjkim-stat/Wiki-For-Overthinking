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

Analyzes how quantization, distillation, and pruning affect the reasoning versus memorization abilities of large reasoning models such as DeepSeek-R1, and proposes protecting a small subset of weights to recover accuracy under quantization.

## Problem

It is unclear how different model-compression techniques (quantization, distillation, pruning) differentially affect a large reasoning model's ability to reason versus its ability to recall memorized knowledge, which matters for deploying compressed LRMs without silently degrading reasoning.

## Contributions

- An analysis of how quantization, distillation, and pruning of DeepSeek-R1-style large reasoning models affect reasoning versus factual-memorization performance separately
- Identification of the MLP up-projection in the final layers of distilled models as particularly important for maintaining reasoning performance
- A targeted-protection method that preserves a small fraction of weights during quantization to recover accuracy

## Method

The paper compresses large reasoning models via quantization, distillation, and pruning, then uses difference-of-means and attribution patching techniques to trace which weights and components are causally responsible for reasoning versus knowledge-memorization performance, evaluating the compressed models on four reasoning datasets.

## Results

Finds that weight count has a greater impact on LRMs' knowledge memorization than on reasoning; the MLP up-projection in final layers of distilled models is particularly important; protecting just 2% of heavily compressed weights in final-layer modules and MLP gate projections during quantization yields a 6.57% accuracy improvement over prior state-of-the-art quantization methods, measured on AIME 2024, FOLIO, Temporal Sequences, and MuSiQue.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this paper matched only on the generic phrase 'large reasoning model.' Its subject is how post-training compression (quantization/distillation/pruning) affects reasoning accuracy and which weights matter for it - it does not address reasoning chain length, the accuracy/efficiency tradeoff of test-time compute, or when a model should stop or continue reasoning.

## Entities

- **Concepts**: model compression, quantization, distillation, pruning, attribution patching, reasoning vs. memorization
- **Methods**: quantization, [distillation](../../../../wiki/methods/knowledge-distillation.md), pruning, attribution patching, difference of means analysis
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), FOLIO, Temporal Sequences, MuSiQue

Tags: `model-compression`, `quantization`, `distillation`, `pruning`, `tangential`

## Abstract

Abstract Compression methods, including quantization, distillation, and pruning, improve the computational efficiency of large reasoning models (LRMs). However, existing studies either fail to sufficiently compare all three compression methods on LRMs or lack in-depth interpretation analysis. In this paper, we investigate how the reasoning capabilities of LRMs are compromised during compression, through performance benchmarking and mechanistic interpretation. To uncover the effects of compression on reasoning performance, we benchmark quantized, distilled, and pruned DeepSeek-R1 models on four reasoning datasets (AIME 2024, FOLIO, Temporal Sequences, and MuSiQue). To precisely locate compression effects on model weights, we adapt difference of means and attribution patching techniques, focusing on the activation of every linear component in compressed LRMs, to interpret fine-grained causal relationships between weights and various reasoning capabilities. This fine-grained interpretation addresses a fundamental question of compression: which weights are the most important for reasoning? Overall, we find dynamically quantized 2.51-bit R1 reaches close-to-R1 performance. With empirical verification, we present three main findings that generalize across both R1 and non-R1 LRMs: (1) Weight count has a greater impact on LRMs' knowledge memorization than reasoning, highlighting the risks of pruning and distillation; (2) The MLP up projection in the final layer of distilled LRMs is one of the most important components, offering a new perspective on locating critical weights - a fundamental problem in model compression; and (3) Current quantization methods overly compress the final-layer modules and MLP gate projections, so protecting just 2% of all weights that are excessively compressed can raise average accuracy by 6.57%, greatly surpassing the state-of-the-art.

---

Record id: `title:c593d75efe2e5d8c`
