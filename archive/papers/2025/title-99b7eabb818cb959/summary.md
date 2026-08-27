<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning Models Hallucinate More: Factuality-Aware Reinforcement Learning for Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118780>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows that reasoning-oriented RL fine-tuning of LLMs significantly increases hallucination, traces this to high-variance gradients, entropy-induced randomness and spurious local optima, and proposes Factuality-aware Step-wise Policy Optimization (FSPO) to reduce hallucination while improving reasoning accuracy.

## Problem

Reasoning-oriented RL fine-tuning improves LLM performance on reasoning benchmarks but the paper's empirical analysis reveals it significantly increases the prevalence of hallucinations, and the training-dynamics cause of this was unclear.

## Contributions

- an empirical finding that reasoning-oriented RL fine-tuning significantly increases hallucination
- a theoretical account of the RL training-dynamics causes (gradient variance, entropy-induced randomness, spurious local optima)
- Factuality-aware Step-wise Policy Optimization (FSPO), reducing hallucination while improving reasoning accuracy on Qwen2.5 and Llama models

## Method

Theoretically analyzes RL training dynamics for reasoning fine-tuning, identifying high-variance gradients, entropy-induced randomness, and susceptibility to spurious local optima as key factors driving hallucination; proposes Factuality-aware Step-wise Policy Optimization (FSPO), which incorporates explicit factuality verification against given evidence at each reasoning step, dynamically adjusting token-level advantage values to reward factual correctness throughout reasoning.

## Results

Across mathematical-reasoning and hallucination benchmarks using Qwen2.5 and Llama models, FSPO effectively reduces hallucinations while enhancing reasoning accuracy, improving both reliability and performance versus standard reasoning-RL fine-tuning (aggregate claims; no specific deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract; the factuality-verification step requires evidence to verify against, whose availability/quality is not discussed in the excerpt retrieved.

## Why it matters here

- **overthinking**: Directly relevant as a side-effect finding about the same RL-for-reasoning training pipeline the overthinking literature studies: it shows reasoning-oriented RL has a cost (increased hallucination) beyond the accuracy/length tradeoff usually discussed, and its training-dynamics account (variance, entropy-induced randomness, spurious optima) is a candidate mechanism for other reasoning pathologies including overthinking.

## Entities

- **Concepts**: reasoning-induced hallucination, step-wise factuality verification, token-level advantage shaping
- **Methods**: Factuality-aware Step-wise Policy Optimization (FSPO), reinforcement learning (RL) fine-tuning
- **Datasets**: _none recorded_

Tags: `hallucination`, `reinforcement-learning`, `large-reasoning-models`, `factuality`

## Abstract

Abstract Large language models (LLMs) have significantly advanced in reasoning tasks through reinforcement learning (RL) optimization, achieving impressive capabilities across various challenging benchmarks. However, our empirical analysis reveals a critical drawback: reasoning-oriented RL fine-tuning significantly increases the prevalence of hallucinations. We theoretically analyze the RL training dynamics, identifying high-variance gradient, entropy-induced randomness, and susceptibility to spurious local optima as key factors leading to hallucinations. To address this drawback, we propose Factuality-aware Step-wise Policy Optimization (FSPO), an innovative RL fine-tuning algorithm incorporating explicit factuality verification at each reasoning step. FSPO leverages automated verification against given evidence to dynamically adjust token-level advantage values, incentivizing factual correctness throughout the reasoning process. Experiments across mathematical reasoning and hallucination benchmarks using Qwen2.5 and Llama models demonstrate that FSPO effectively reduces hallucinations while enhancing reasoning accuracy, substantially improving both reliability and performance.

---

Record id: `title:99b7eabb818cb959`
