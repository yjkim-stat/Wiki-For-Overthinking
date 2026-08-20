<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Models Have Thought Enough: Training Large Reasoning Models to Stop Overthinking

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011695>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Trains large reasoning models via RL to proactively stop reasoning once they have accumulated enough evidence, cutting output length by 46.3% while improving accuracy by 4.6% on the Olympiad benchmark.

## Problem

Large reasoning models incur substantial computational cost from long reasoning traces, and existing reinforcement learning methods for efficient reasoning struggle to construct short reasoning paths during the rollout stage, limiting how effectively they can learn to reason concisely.

## Contributions

- Identifies, drawing on Evidence Accumulation Models, that LRMs accumulate sufficient information early in reasoning, making later reasoning steps redundant
- Proposes Just-Enough Thinking (JET), which trains models via reinforcement learning to proactively terminate unnecessary reasoning
- Introduces trajectory truncation during RL rollout to expose the model to short, distributionally consistent reasoning paths, addressing the difficulty existing RL methods have constructing short reasoning paths during rollout
- Introduces a quality-controlled length reward that encourages concise reasoning while maintaining correctness
- Reports a 4.6% accuracy improvement while reducing output length by 46.3% on the Olympiad benchmark using DeepSeek-R1-Distill-Qwen-1.5B

## Method

Motivated by Evidence Accumulation Models, JET performs trajectory truncation during reinforcement learning rollout to expose the model to short, distributionally consistent reasoning paths, addressing the rollout-stage difficulty existing RL methods have in producing short paths. It combines this with a quality-controlled length reward during training so the model learns to stop reasoning once it has accumulated enough evidence, without sacrificing correctness.

## Results

4.6% accuracy improvement combined with a 46.3% reduction in output length on the Olympiad benchmark, using DeepSeek-R1-Distill-Qwen-1.5B.

## Limitations

Numeric results in the abstract are reported for a single model (DeepSeek-R1-Distill-Qwen-1.5B) and a single benchmark (Olympiad); generalization to other model sizes or benchmark domains is not stated in the abstract.

## Why it matters here

- **overthinking**: Directly targets overthinking: it shows LRMs often accumulate sufficient evidence early and continue reasoning past that point, and proposes an RL training method (trajectory truncation plus a length-quality reward) that teaches the model to stop at the right point, reducing output length by 46.3% while improving accuracy by 4.6% on one benchmark.

## Entities

- **Concepts**: Evidence Accumulation Models applied to LRM reasoning, trajectory truncation during RL rollout, quality-controlled length reward, just-enough thinking / proactive reasoning termination
- **Methods**: Just-Enough Thinking (JET), reinforcement learning with trajectory truncation, quality-controlled length reward
- **Datasets**: Olympiad benchmark

Tags: `overthinking`, `reinforcement-learning`, `reasoning-length`, `trajectory-truncation`, `efficient-reasoning`

## Abstract

Abstract Large Reasoning Models (LRMs) have achieved impressive performance on challenging tasks, yet their deep reasoning often incurs substantial computational costs. To achieve efficient reasoning, existing reinforcement learning methods still struggle to construct short reasoning path during the rollout stage, limiting effective learning. Inspired by Evidence Accumulation Models, we find that LRMs have accumulated sufficient information early in reasoning, making further reasoning steps redundant. Based on this insight, we propose Just-Enough Thinking (JET), which trains models to proactively terminate unnecessary reasoning. JET performs trajectory truncation during rollout to expose the model to short, distributionally consistent reasoning paths. Besides, it uses a quality-controlled length reward to better encourage concise reasoning while maintaining correctness. Extensive experiments demonstrate that JET significantly improves reasoning efficiency without sacrificing accuracy. In particular, JET delivers a 4.6% accuracy improvement while reducing the output length by 46.3% on the Olympiad benchmark using DeepSeek-R1-Distill-Qwen-1.5B. Our code is available in the GitHub.

---

Record id: `title:92690cf46de29df1`
