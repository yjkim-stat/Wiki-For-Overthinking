<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning Generalized Trackers with Elastic Token Budgets

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63126>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

ETBTrack is the first elastic-token-budget training framework for visual object tracking, using a result-driven token-importance metric and budget-collaborative optimization so a single tracker adapts its inference cost across multiple computational budgets instead of being fixed to one.

## Problem

Conventional visual trackers are trained with manually pruned image tokens under a single fixed computational budget, making them inflexible and unable to adapt to varying real-world computational constraints.

## Contributions

- ETBTrack, described as the first exploration of elastic token budget training for visual tracking
- a result-driven, localization-accuracy-guided policy network for token importance
- a budget-collaborative optimization strategy enabling a single tracker to adapt across multiple computational budgets

## Method

Introduces ETBTrack, an elastic token budget training framework with (1) a result-driven importance metric using a policy network guided by localization accuracy to score which image tokens matter, and (2) a budget-collaborative optimization strategy that simultaneously trains the tracker across diverse budget scenarios rather than a single fixed one.

## Results

Extensive benchmark testing confirms ETBTrack's effectiveness at enabling flexible, adaptive-budget inference while maintaining tracking performance across the tested budget range (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the visual-tracking domain and benchmark evaluation described.

## Why it matters here

- **overthinking**: Off-topic domain: this is a visual object-tracking token-budget adaptation method, unrelated to LLM reasoning-trace length; matched to the topic only via the shared term 'token budget'.

## Entities

- **Concepts**: elastic token budget training, result-driven token-importance metric, budget-collaborative optimization
- **Methods**: ETBTrack (elastic token budget training)
- **Datasets**: _none recorded_

Tags: `visual-tracking`, `adaptive-computation`, `token-pruning`, `elastic-inference`

---

Record id: `title:4b66f999d176e2b1`
