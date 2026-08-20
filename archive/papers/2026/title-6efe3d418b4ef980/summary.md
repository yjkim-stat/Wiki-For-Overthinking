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

A gradient-free model-merging method that integrates an instruction-tuned model into a large reasoning model to improve instruction following while preserving the reasoning model's thinking format and quality.

## Problem

Large reasoning models produce long chains of reasoning but often fail to faithfully follow instructions about output format or constraints, and naively merging in an instruction-tuned model disrupts the reasoning model's distinct thinking-then-answer output format.

## Contributions

- Finds that the principal subspaces of an instruction-tuned model's (ITM) and a large reasoning model's (LRM) task vectors are nearly orthogonal across key modules
- Shows naive merging of ITM and LRM is fragile because it overlooks the output-format mismatch between LRM (thinking + response) and ITM (answer-only) outputs
- Introduces RAIN-Merging: a gradient-free method that projects the ITM task vector onto the null space of forward features at thinking special tokens, then applies instruction-attention-derived module-specific scaling

## Method

RAIN-Merging integrates an instruction-tuned model (ITM) into a large reasoning model (LRM) via parameter-space merging rather than fine-tuning. Using a small reasoning calibration set, it projects the ITM's task vector onto the null space of forward features computed at the LRM's thinking special tokens, which preserves the LRM's structured reasoning mechanism. Using a small instruction calibration set, it then estimates instruction attention to derive module-specific scaling factors that amplify instruction-relevant components of the merge and suppress leakage into the reasoning pathway.

## Results

Across four instruction-following benchmarks and nine reasoning and general-capability benchmarks, RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality, with gains consistent across model scales and architectures and improved performance in agent settings; exact figures are not given in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential -- shares only the generic 'large reasoning model' keyword. The paper is about merging in instruction-following ability while preserving the format of the thinking segment, not about the length of reasoning, when to stop or continue thinking, or the accuracy/efficiency tradeoff of test-time compute.

## Entities

- **Concepts**: task vector, null-space projection, model merging, thinking-format preservation
- **Methods**: RAIN-Merging, null-space projection, task-vector merging
- **Datasets**: _none recorded_

Tags: `model-merging`, `instruction-following`, `large-reasoning-model`, `task-vectors`

## Abstract

Abstract Large reasoning models (LRMs) excel at a long chain of reasoning but often fail to faithfully follow instructions regarding output format, constraints, or specific requirements. We investigate whether this gap can be closed by integrating an instruction-tuned model (ITM) into an LRM. Analyzing their differences in parameter space, namely task vectors, we find that their principal subspaces are nearly orthogonal across key modules, suggesting a lightweight merging with minimal interference. However, we also demonstrate that naïve merges are fragile because they overlook the output format mismatch between LRMs (with explicit thinking and response segments) and ITMs (answers-only). We introduce RAIN-Merging (Reasoning-Aware Instruction-attention guided Null-space projection Merging), a gradient-free method that integrates instruction following while preserving thinking format and reasoning performance. First, with a small reasoning calibration set, we project the ITM task vector onto the null space of forward features at thinking special tokens, which preserves the LRM's structured reasoning mechanisms. Second, using a small instruction calibration set, we estimate instruction attention to derive module-specific scaling that amplifies instruction-relevant components and suppresses leakage. Across four instruction-following benchmarks and nine reasoning & general capability benchmarks, RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality. The gains are consistent across model scales and architectures, translating to improved performance in agent settings.

---

Record id: `title:6efe3d418b4ef980`
