<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008968>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes a mechanistic score and detection framework for logically coherent but factually incorrect reasoning traces in large reasoning models, plus an RL method to reduce them.

## Problem

Large reasoning models produce logically coherent but factually incorrect reasoning traces that read as persuasive conclusions, making this form of hallucination harder to detect than standard hallucination because it is embedded in an otherwise valid-looking reasoning structure.

## Contributions

- Reasoning Score metric that uses logit divergence across model layers to distinguish genuine reasoning depth from surface-level pattern matching
- Identification of two hallucination patterns in reasoning traces: initial reasoning-depth instability and retreat to earlier flawed reasoning
- RHD (Reasoning Hallucination Detection) framework for detecting these patterns
- GRPO-R, a reinforcement-learning method that adds step-level reasoning rewards to mitigate hallucination

## Method

Analyzes logit divergence across model layers to compute a Reasoning Score that separates genuine reasoning depth from surface pattern matching. Uses this to identify two failure patterns in reasoning traces (initial depth instability, retreat to earlier flawed reasoning), detected via the RHD framework, and mitigated by GRPO-R, a reinforcement-learning approach that adds step-level rewards for reasoning quality.

## Results

Reports state-of-the-art ('advanced') detection performance across multiple domains and reduced hallucination rates with improved reasoning quality after applying GRPO-R; the paper also claims theoretical generalization guarantees. No specific benchmark numbers were available in the fetched material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Concerns detecting and mitigating factually incorrect reasoning content (hallucination), not the length or amount of reasoning a model performs. It does not address reasoning-length/accuracy tradeoffs, test-time compute scaling, or stopping criteria. It shares only the term 'large reasoning model' with the topic and is tangential to overthinking.

## Entities

- **Concepts**: reasoning hallucination, logit divergence across layers, step-level reasoning reward
- **Methods**: Reasoning Score, RHD (Reasoning Hallucination Detection), GRPO-R
- **Datasets**: _none recorded_

Tags: `hallucination`, `large-reasoning-models`, `mechanistic-interpretability`, `reinforcement-learning`

---

Record id: `title:c5959780286b4ea6`
