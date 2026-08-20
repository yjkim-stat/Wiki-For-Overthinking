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

Shows that RL fine-tuning for reasoning increases hallucination and proposes FSPO, a step-wise factuality-verified RL objective that reduces it while improving accuracy.

## Problem

Reinforcement learning fine-tuning improves LLM reasoning benchmark performance but empirically increases the rate of hallucination; the paper analyzes RL training dynamics (high-variance gradients, entropy-induced randomness, spurious local optima) as the cause and asks how to fine-tune for reasoning without this side effect.

## Contributions

- Shows empirically that reasoning-oriented RL fine-tuning increases hallucination prevalence in LLMs
- Theoretically links this to high-variance gradients, entropy-induced randomness, and susceptibility to spurious local optima during RL training
- Proposes FSPO (Factuality-aware Step-wise Policy Optimization), which verifies factuality at each reasoning step against evidence and adjusts token-level advantages accordingly
- Demonstrates reduced hallucination alongside improved reasoning accuracy on Qwen2.5 and Llama models

## Method

FSPO augments RL fine-tuning with automated, step-level factuality verification against supplied evidence during training. Each reasoning step is checked, and the outcome is used to dynamically adjust token-level advantage values, so the policy is rewarded for factual correctness throughout the chain of reasoning rather than only for the final answer.

## Results

FSPO reduces hallucinations while improving reasoning accuracy on mathematical reasoning and hallucination benchmarks using Qwen2.5 and Llama models; no specific numeric deltas were stated in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this paper studies how RL post-training affects factual correctness and hallucination rate, not reasoning length, test-time compute allocation, or when a model should stop reasoning. It shares only the 'large reasoning model' keyword with the topic.

## Entities

- **Concepts**: RL training dynamics, hallucination, step-wise factuality verification
- **Methods**: Factuality-aware Step-wise Policy Optimization (FSPO), token-level advantage shaping
- **Datasets**: mathematical reasoning benchmarks, hallucination benchmarks

Tags: `hallucination`, `reinforcement-learning`, `factuality`, `reward-shaping`

## Abstract

Abstract Large language models (LLMs) have significantly advanced in reasoning tasks through reinforcement learning (RL) optimization, achieving impressive capabilities across various challenging benchmarks. However, our empirical analysis reveals a critical drawback: reasoning-oriented RL fine-tuning significantly increases the prevalence of hallucinations. We theoretically analyze the RL training dynamics, identifying high-variance gradient, entropy-induced randomness, and susceptibility to spurious local optima as key factors leading to hallucinations. To address this drawback, we propose Factuality-aware Step-wise Policy Optimization (FSPO), an innovative RL fine-tuning algorithm incorporating explicit factuality verification at each reasoning step. FSPO leverages automated verification against given evidence to dynamically adjust token-level advantage values, incentivizing factual correctness throughout the reasoning process. Experiments across mathematical reasoning and hallucination benchmarks using Qwen2.5 and Llama models demonstrate that FSPO effectively reduces hallucinations while enhancing reasoning accuracy, substantially improving both reliability and performance.

---

Record id: `title:99b7eabb818cb959`
