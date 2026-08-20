<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# LIMOPro: Reasoning Refinement for Efficient and Effective Test-time Scaling

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117621>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

PIR scores reasoning steps by their effect on answer confidence and prunes only low-importance verification/error-correction steps from distilled chain-of-thought data, producing models that reason more concisely without losing accuracy.

## Problem

Chain-of-thought traces distilled from large reasoning models mix an essential progressive reasoning path with functional elements (verification, alternative solutions, error correction) that inflate token usage at test time; removing verbosity indiscriminately risks cutting reasoning that matters.

## Contributions

- PIR (Perplexity-based Importance Refinement), a framework that scores each reasoning step's importance by its impact on answer prediction confidence
- A method to selectively prune low-importance functional reasoning steps (verification, alternative approaches, error correction) while preserving the progressive reasoning path
- Refined CoT training data (LIMOPro) that yields models with more concise reasoning chains and improved accuracy after fine-tuning

## Method

Reasoning chains distilled from large reasoning models are split into progressive reasoning (the essential solution path) and functional elements (verification, alternative solutions, error correction). PIR quantifies each step's importance via its effect on answer prediction confidence (perplexity-based), then prunes low-importance functional steps while keeping all progressive reasoning steps, producing refined training data. Models are then fine-tuned on this pruned data.

## Results

Models fine-tuned on PIR-refined data show +0.9% to +6.6% accuracy gains and -3% to -41% token usage reductions across AIME, AMC, and GPQA Diamond, with the approach generalizing across model sizes, data sources, and token budgets.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Addresses overthinking directly by distinguishing which parts of a reasoning trace are load-bearing (progressive reasoning) versus verbose overhead (functional elements), and by selectively pruning only the latter from training data so fine-tuned models produce shorter, still-accurate reasoning at test time.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), progressive reasoning, functional reasoning elements, chain-of-thought distillation, step importance estimation
- **Methods**: PIR (Perplexity-based Importance Refinement), chain-of-thought distillation
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md), [AMC](../../../../wiki/datasets/amc.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `overthinking`, `chain-of-thought-pruning`, `test-time-scaling`, `reasoning-efficiency`

## Abstract

Abstract Large language models (LLMs) have demonstrated remarkable reasoning capabilities through test-time scaling approaches, particularly when fine-tuned with chain-of-thought (CoT) data distilled from more powerful large reasoning models (LRMs). However, these reasoning chains often contain verbose elements that mirror human problem-solving, categorized as progressive reasoning (the essential solution development path) and functional elements (verification processes, alternative solution approaches, and error corrections). While progressive reasoning is crucial, the functional elements significantly increase computational demands during test-time inference. We introduce PIR (Perplexity-based Importance Refinement), a principled framework that quantitatively evaluates the importance of each reasoning step based on its impact on answer prediction confidence. PIR systematically identifies and selectively prunes only low-importance functional steps while preserving all progressive reasoning components, creating optimized training data that maintains the integrity of the core solution path while reducing verbosity. Models fine-tuned on PIR-optimized data exhibit superior test-time scaling properties, generating more concise reasoning chains while achieving improved accuracy (+0.9\% to +6.6\%) with significantly reduced token usage (-3\% to -41\%) across challenging reasoning benchmarks (AIME, AMC, and GPQA Diamond). Our approach demonstrates strong generalizability across different model sizes, data sources, and token budgets, offering a practical solution for deploying reasoning-capable LLMs in scenarios where efficient test-time scaling, response time, and computational efficiency are valuable constraints. Code and dataset are available at the LIMOPro GitHub repository.

---

Record id: `title:f14f82d5eba9e811`
