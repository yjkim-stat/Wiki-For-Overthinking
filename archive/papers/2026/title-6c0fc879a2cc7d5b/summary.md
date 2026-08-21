<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61056>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains large reasoning models with self-distillation followed by diversity-aware RL to overcome 'Lazy Reasoning' -- inadequate task decomposition -- in complex tool-use settings.

## Problem

Large reasoning models often fail to adequately decompose complex tasks that require multiple tool calls, a failure mode the authors term 'Lazy Reasoning', limiting their ability to solve complex real-world tool-use problems.

## Contributions

- Identifies and names 'Lazy Reasoning' -- the failure of large reasoning models to adequately decompose complex tool-use tasks
- A self-distillation phase that improves task decomposition ability
- A diversity-aware reinforcement learning phase that restores reflective reasoning
- State-of-the-art accuracy on BFCLv3 with an 8B and a 14B model

## Method

D-CORE uses a two-phase training approach: first, self-distillation to improve the model's ability to break complex tool-use tasks into sub-tasks; second, diversity-aware reinforcement learning to restore reflective reasoning behavior that the distillation phase can suppress.

## Results

The 8B D-CORE model reaches 77.7% accuracy on BFCLv3, outperforming comparable models by 5.7 percentage points; the 14B variant reaches 79.3%, described as a new state of the art on the benchmark.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Shares only the generic 'large reasoning model' keyword with the topic. The paper is about a model's capability to decompose complex tool-use tasks into sub-steps, not about controlling how long a model reasons, the accuracy/efficiency tradeoff of reasoning length, or test-time compute scaling; it does not address stopping or continuing reasoning at the right point.

## Entities

- **Concepts**: Lazy Reasoning, [task decomposition](../../../../wiki/concepts/task-decomposition.md), tool use
- **Methods**: self-distillation, diversity-aware reinforcement learning
- **Datasets**: BFCLv3

Tags: `tool-use`, `task-decomposition`, `reinforcement-learning`, `large-reasoning-model`

---

Record id: `title:6c0fc879a2cc7d5b`
