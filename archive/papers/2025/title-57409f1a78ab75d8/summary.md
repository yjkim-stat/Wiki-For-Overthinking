<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/46117>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Scales test-time compute by running and aggregating multiple pruned reasoning trees per problem, using sparse activation and consensus to balance accuracy against added compute.

## Problem

Chain-of-Thought and Tree-of-Thought methods perform a single pass of reasoning and cannot revisit flawed paths once taken, which limits accuracy on complex logical problems; the paper addresses how to use additional test-time compute (multiple reasoning trees) without an unbounded increase in cost.

## Contributions

- Proposes Forest-of-Thought (FoT), a framework that combines multiple reasoning trees and aggregates them via collective decision-making
- Introduces a sparse activation strategy to select only the most relevant reasoning paths across the trees
- Introduces a dynamic self-correction strategy for real-time error correction within a reasoning path
- Introduces consensus-guided decision-making across trees to balance correctness against computational resource use

## Method

Forest-of-Thought runs multiple independent reasoning trees (extending Tree-of-Thought, which performs a single pass and cannot revisit flawed paths) for the same problem. A sparse activation mechanism prunes each tree down to its most relevant paths rather than exploring all branches, which is intended to control the added compute cost of running multiple trees. A dynamic self-correction step lets a tree revise a path in real time when an error is detected, and a consensus mechanism aggregates answers across trees to produce a final decision.

## Results

The abstract-level material available states that FoT improves LLM reasoning precision and efficiency over single-pass methods, but no specific benchmark accuracy or compute-cost numbers were given in the material reviewed.

## Limitations

The material reviewed (abstract-level, no attached PDF) does not give specific benchmark numbers, token/compute cost figures, or stated failure cases, so the accuracy/efficiency tradeoff cannot be quantified from what was available.

## Why it matters here

- **overthinking**: This is a test-time-compute-scaling method, but it scales in the opposite direction from most of the topic's focus: it adds more parallel reasoning trees to raise accuracy, using sparse activation to prune unpromising branches for efficiency, rather than addressing when a single chain has reasoned enough or should stop early. The connection is the shared object (test-time compute versus accuracy) but not the overthinking/stopping-criterion question central to this topic, and no quantitative compute-accuracy tradeoff was available in the abstract-level material reviewed.

## Entities

- **Concepts**: forest-of-thought, sparse activation, consensus-guided decision-making, reasoning-tree aggregation
- **Methods**: Forest-of-Thought, sparse activation, [dynamic self-correction](../../../../wiki/methods/dynamic-self-correction.md), consensus-guided decision-making
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `tree-of-thought`, `sparse-activation`, `consensus`, `reasoning-search`

---

Record id: `title:57409f1a78ab75d8`
