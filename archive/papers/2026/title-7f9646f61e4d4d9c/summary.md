<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Internalizing Safety Understanding in Large Reasoning Models via Verification

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63605>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains large reasoning models on safety-verification (critiquing responses against safety principles) rather than direct safe-response mimicry, and shows this generalizes better and gives a stronger RL initialization.

## Problem

Chain-of-thought reasoning can make unsafe outputs harder to detect, and models that appear aligned often lack an intrinsic understanding of safety principles, making them vulnerable to sophisticated or disguised attacks.

## Contributions

- SInternal, a training method that fine-tunes reasoning models exclusively on safety verification tasks, teaching them to critique their own generated answers using expert reasoning trajectories rather than to directly mimic safe outputs.
- A demonstration that learning to verify generalizes to improved response safety against disguised or manipulative prompts.
- Evidence that SInternal provides a better initialization for downstream reinforcement learning than standard safety training.

## Method

The model is trained only on safety-verification tasks: given a response, it must critique and justify why the response violates (or does not violate) safety principles, using expert reasoning trajectories as supervision. This is intended to build an internal understanding of safety principles rather than a learned mapping from harmful-looking requests to refusals, and the resulting checkpoint is then used as an initialization for further reinforcement learning.

## Results

No specific benchmark numbers were available in the retrieved material (no PDF or numeric results found on the paper's ICML page). The claimed results are qualitative: stronger generalization to disguised/manipulative attacks and improved RL initialization compared to standard training.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Not substantively related. The paper is about safety alignment and self-verification of response safety in reasoning models; it does not address reasoning length, the accuracy/efficiency tradeoff, or when a model should stop or continue reasoning. It only shares the generic term 'large reasoning model' with the topic.

## Entities

- **Concepts**: safety verification, self-critique via reasoning, internalized alignment
- **Methods**: SInternal
- **Datasets**: _none recorded_

Tags: `safety`, `alignment`, `verification`, `self-critique`

---

Record id: `title:7f9646f61e4d4d9c`
