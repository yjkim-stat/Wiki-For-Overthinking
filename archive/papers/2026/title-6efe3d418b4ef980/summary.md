<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009681>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

RAIN-Merging is a gradient-free method that merges an instruction-tuned model with a reasoning model by exploiting their near-orthogonal principal parameter subspaces, improving instruction-following in large reasoning models while preserving their thinking format and reasoning quality.

## Problem

Large reasoning models excel at complex reasoning but often fail to follow specific formatting instructions, and naive merging with instruction-tuned models fails because reasoning models separately emit thinking and response segments while instruction-tuned models answer directly.

## Contributions

- an analysis showing instruction-tuned and reasoning-model parameter differences occupy nearly orthogonal principal subspaces
- RAIN-Merging, a gradient-free merge that improves instruction-following while preserving reasoning-model thinking format
- validation across thirteen benchmarks and multiple model sizes/architectures

## Method

Analyzes the parameter difference between an instruction-tuned model and a reasoning model, finding their principal subspaces are nearly orthogonal across key modules; proposes RAIN-Merging, a gradient-free merge using a small reasoning-calibration dataset to protect the model's thinking process and a small instruction-calibration set to identify which components handle instruction-following, merging only along the relevant subspaces.

## Results

Across thirteen benchmarks and multiple model sizes/architectures, RAIN-Merging consistently improves instruction-following while maintaining reasoning capabilities (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract; relies on the empirical near-orthogonality of principal subspaces holding across model families, which is not guaranteed to generalize.

## Why it matters here

- **overthinking**: Tangential: concerned with instruction-following fidelity of reasoning models via merging, not reasoning length or the accuracy/efficiency tradeoff, but relevant background on how a reasoning model's 'thinking' segment can be preserved as a first-class structural object while other capabilities are edited in.

## Entities

- **Concepts**: gradient-free model merging, principal subspace orthogonality, thinking-format preservation
- **Methods**: gradient-free model merging, principal component / subspace analysis
- **Datasets**: _none recorded_

Tags: `model-merging`, `instruction-following`, `large-reasoning-models`, `thinking-format`

---

Record id: `title:6efe3d418b4ef980`
