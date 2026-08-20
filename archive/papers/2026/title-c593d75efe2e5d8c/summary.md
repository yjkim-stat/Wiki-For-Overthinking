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

- **Concepts**: model compression, quantization, [distillation](../../../../wiki/concepts/distillation.md), pruning, attribution patching, reasoning vs. memorization
- **Methods**: quantization, distillation, pruning, attribution patching, difference of means analysis
- **Datasets**: [AIME 2024](../../../../wiki/datasets/aime-2024.md), FOLIO, Temporal Sequences, MuSiQue

Tags: `model-compression`, `quantization`, `distillation`, `pruning`, `tangential`

---

Record id: `title:c593d75efe2e5d8c`
