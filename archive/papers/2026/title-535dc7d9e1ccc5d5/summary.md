<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SmartThinker: Progressive Chain-of-Thought Length Calibration for Efficient Large Language Model Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64022>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A GRPO-based training method that dynamically calibrates the target chain-of-thought length per problem to cut redundant reasoning without penalizing correct long answers.

## Problem

Long chain-of-thought reasoning in large reasoning models is often verbose and redundant (overthinking), and prior GRPO-based length-reduction methods use static length rewards that do not adapt to problem difficulty or the response-length distribution, causing over-compression and accuracy loss.

## Contributions

- Proposes SmartThinker, a GRPO-based reinforcement learning method that calibrates chain-of-thought length per problem instead of applying a static length target
- Dynamically estimates, during training, the response length at which accuracy peaks and guides overlong responses toward that length
- Adaptively modulates the length-reward coefficient so the length penalty does not punish correct long reasoning paths

## Method

SmartThinker builds on GRPO (Group Relative Policy Optimization). During training it estimates, per problem, the response length associated with peak accuracy, and steers responses that exceed that length back toward the target through a length-based reward term. Rather than using a fixed length penalty, it adaptively modulates the strength of this length-reward coefficient, so correct reasoning that happens to be long is not penalized as heavily as incorrect or genuinely redundant reasoning.

## Results

Up to 52.5% average length compression compared to baseline while improving accuracy; up to 16.6% accuracy improvement on AIME25, described as a challenging benchmark.

## Limitations

The material reviewed (abstract-level) does not state failure modes, ablations, or classes of problems where the method underperforms; only headline compression and accuracy numbers were available.

## Why it matters here

- **overthinking**: Directly targets the accuracy/efficiency tradeoff of reasoning length: it trains a model to calibrate its own chain-of-thought length per problem rather than applying a fixed budget, addressing the core failure mode of static length-reward methods (over-compression that harms accuracy). Reports up to 52.5% average length compression together with accuracy gains, including up to 16.6% on AIME25.

## Entities

- **Concepts**: progressive length calibration, adaptive length reward, [overthinking](../../../../wiki/concepts/overthinking.md), response-length compression
- **Methods**: GRPO, SmartThinker, progressive chain-of-thought length calibration
- **Datasets**: AIME25

Tags: `overthinking`, `chain-of-thought`, `grpo`, `length-calibration`, `efficient-reasoning`

---

Record id: `title:535dc7d9e1ccc5d5`
