<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning or Retrieval? A Study of Answer Attribution on Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010758>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Finds that large reasoning models often produce final answers that contradict their own stated reasoning steps, showing both genuine reasoning and memorized-answer retrieval operate jointly with variable dominance, and proposes FARL, an RL training framework suppressing retrieval shortcuts to improve generalization.

## Problem

It is unclear whether large reasoning models' final answers are actually produced through the logical reasoning they display, or are instead retrieved from memorized/stored information with the displayed reasoning being post-hoc or disconnected -- and models can learn to exploit retrieval as a shortcut during training, undermining genuine reasoning.

## Contributions

- an experimental methodology (misleading cues, corrupted data) for attributing an LRM's final answer to reasoning versus retrieval
- a finding that final answers often contradict the model's own stated reasoning steps
- FARL, a training framework combining memory suppression with RL to reduce retrieval-shortcut reliance and improve generalization

## Method

Uses experiments with misleading cues and corrupted data to determine, across problem types, model sizes and training methods, whether answers derive from reasoning or retrieval; proposes FARL, a training framework combining memory suppression with reinforcement learning to discourage reliance on retrieval shortcuts and encourage genuine reasoning.

## Results

Finds models often produce final answers that contradict their own reasoning steps; both reasoning and retrieval mechanisms operate jointly with dominance varying by problem type, model size, and training method; FARL improves generalization by reducing reliance on retrieval shortcuts (aggregate claims; no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the experimental design (misleading cues, corrupted data) used to probe the reasoning-vs-retrieval question.

## Why it matters here

- **overthinking**: Directly relevant to what a reasoning trace actually reflects: the finding that final answers can contradict the model's own reasoning steps -- because the answer came from retrieval, not the displayed reasoning -- bears on whether a long reasoning trace is doing genuine work at all, a foundational question for interpreting overthinking (wasted length in a trace that was never load-bearing for the answer).

## Entities

- **Concepts**: answer attribution (reasoning vs. retrieval), retrieval shortcut exploitation, memory-suppression training
- **Methods**: FARL (memory suppression + reinforcement learning), answer-attribution probing via misleading cues and data corruption
- **Datasets**: _none recorded_

Tags: `large-reasoning-models`, `answer-attribution`, `shortcut-learning`, `interpretability`

---

Record id: `title:db18eb78dcdd333c`
