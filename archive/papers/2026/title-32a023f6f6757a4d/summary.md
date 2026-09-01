<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GTA1: GUI Test-time Scaling Agent

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011639>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GTA1 is a GUI agent that uses test-time scaling to generate and judge multiple candidate action plans before selecting one, paired with an RL-trained visual grounding module rewarded on successful interface interactions, improving both element-grounding and end-to-end task execution.

## Problem

GUI agents face two coupled challenges: strategic planning across a large space of possible actions, and precisely targeting the correct interface element to act on -- and prior work has not addressed both with test-time scaling and reward-driven grounding together.

## Contributions

- test-time-scaled candidate-plan generation and judge-based selection for GUI agent planning
- a reinforcement-learning-based visual grounding module rewarded on successful interface interactions rather than only supervised labels
- improved results on both grounding and task-execution benchmarks for GUI agents

## Method

GTA1 applies test-time scaling to planning by generating multiple candidate action plans and using a judge model to select among them before execution, and separately trains a reinforcement-learning-based visual grounding module that strengthens element localization using reward signals tied to successful interface interactions (rather than only supervised grounding labels).

## Results

GTA1 achieves improved results on both grounding accuracy and end-to-end task-execution benchmarks for GUI agents (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the GUI-agent domain and benchmark scope described.

## Why it matters here

- **overthinking**: Indirectly relevant: a test-time-scaling method in the GUI-agent domain (generating multiple candidate plans and selecting the best via a judge) rather than text reasoning-length control, but it is another example of spending inference compute on structured candidate generation and selection instead of a single longer reasoning trace.

## Entities

- **Concepts**: test-time scaling for GUI action planning, RL-trained visual grounding, judge-model action selection
- **Methods**: GTA1 (test-time scaling + RL-trained grounding), judge-model candidate selection
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `gui-agents`, `visual-grounding`, `reinforcement-learning`

---

Record id: `title:32a023f6f6757a4d`
