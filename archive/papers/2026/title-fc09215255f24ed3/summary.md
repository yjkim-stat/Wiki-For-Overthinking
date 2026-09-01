<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006973>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

OneTwoVLA unifies reasoning and action into a single Vision-Language-Action model that adaptively switches between explicitly reasoning at critical moments during task execution and generating actions from the most recent reasoning at other times, trained on synthetic embodied-reasoning data plus robot-specific data, supporting multi-step planning, mistake correction, conversational collaboration, and generalizable visual understanding for tasks like food preparation and beverage mixing.

## Problem

Robotic Vision-Language-Action models typically separate high-level reasoning/planning from low-level action generation into two distinct processes, rather than adaptively deciding, moment to moment during task execution, when explicit reasoning is actually needed versus when the model should simply act on its most recent reasoning.

## Contributions

- OneTwoVLA, a unified VLA model that adaptively switches between explicit reasoning and action generation rather than always separating them into distinct stages
- synthetic embodied-reasoning training data purpose-built for this adaptive-reasoning capability, combined with robot-specific datasets
- demonstrated competency across multi-step planning, mistake correction, conversational collaboration, and generalizable visual understanding in real manipulation tasks

## Method

OneTwoVLA integrates reasoning and action generation into a single unified model that adaptively switches between two modes: explicitly reasoning at critical moments during task execution (e.g. when a decision point or ambiguity arises), and generating actions based on the most recently produced reasoning at other times (avoiding re-reasoning at every step). Trained using synthetic embodied-reasoning data constructed specifically for this purpose, combined with robot-specific action datasets.

## Results

The unified model demonstrates competency across four capability areas: multi-step task planning, mistake identification and correction, conversational human-robot collaboration, and visual understanding that generalizes across different scenarios; it performs sophisticated manipulation tasks including food preparation and beverage mixing (no specific numeric benchmark deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the described capability areas and manipulation task examples (food preparation, beverage mixing).

## Why it matters here

- **overthinking**: Indirectly relevant: a robotics VLA analog of difficulty/moment-adaptive reasoning -- deciding when explicit reasoning is worth the cost versus acting on cached prior reasoning -- structurally the same 'don't always reason from scratch' principle behind adaptive-computation overthinking mitigations for text-based LLM reasoning, applied here to embodied action generation rather than chain-of-thought token generation.

## Entities

- **Concepts**: adaptive reasoning-action mode switching, unified vision-language-action model, critical-moment reasoning trigger
- **Methods**: OneTwoVLA (adaptive reasoning-action switching), synthetic embodied-reasoning data generation
- **Datasets**: _none recorded_

Tags: `vision-language-action`, `adaptive-reasoning`, `robotics`, `embodied-ai`

---

Record id: `title:fc09215255f24ed3`
