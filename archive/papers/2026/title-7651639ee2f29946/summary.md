<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Modeling Hierarchical Thinking in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64487>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Models a large reasoning model's chain-of-thought as transitions among six latent cognitive states and uses that abstraction to steer generation toward better reasoning policies at inference time, without training.

## Problem

The emergent dynamics governing large reasoning models' chain-of-thought trajectories are not well understood, which can lead to reasoning inconsistencies and pathologies; the paper seeks an interpretable, structured abstraction of these dynamics usable for both understanding and control.

## Contributions

- Proposes a memoryless Finite State Machine formulation approximating a large reasoning model's hierarchical reasoning dynamics as transitions among six abstract cognitive states (initialization, deduction, augmentation-strategy, uncertainty-estimation, backtracking, final-conclusion).
- Shows these states and transitions can be read out of the model's latent representations.
- Identifies statistical shifts in state-transition topology that distinguish successful from failed reasoning chains.
- Introduces Q-Value guided steering, a training-free inference-time control method that estimates long-horizon utility of state transitions and applies sparse, orthogonal activation steering at sentence boundaries to align generation with better reasoning policies.

## Method

The paper models a large reasoning model's chain-of-thought as a trajectory through a memoryless Finite State Machine over six abstract cognitive states, decoded from the model's latent activations. It analyzes the topology of transitions between these states to distinguish reasoning chains that succeed from those that fail, and builds on this with Q-Value guided steering: a training-free method that estimates the long-horizon utility of each state transition and nudges generation via sparse, orthogonal activation steering applied at sentence boundaries, treating reasoning as a planning problem over these states.

## Results

Across four benchmarks (AIME25, MATH-500, GSM8K, GPQA Diamond) and three state-of-the-art open reasoning models, Q-Value guided steering achieves performance gains while requiring roughly 25 times fewer interventions than greedy and weighted steering baselines; no absolute accuracy figures were available in the abstract consulted.

## Limitations

The source consulted (arXiv abstract, no PDF available) does not give absolute accuracy numbers for Q-Value steering, only that it needs about 25x fewer interventions than greedy and weighted baselines; details of the three reasoning models used and any domains where the FSM abstraction breaks down are not stated.

## Why it matters here

- **overthinking**: Provides a mechanism for controlling reasoning trajectories (steering toward states associated with successful chains, away from those linked to failure/backtracking loops) at inference time without retraining, which is directly relevant to deciding when a model should stop backtracking/deliberating versus proceed to a conclusion -- though the paper frames this as reasoning-quality control rather than explicitly as a length/compute-budget tradeoff.

## Entities

- **Concepts**: hierarchical reasoning as a finite state machine, latent cognitive states, reasoning as a planning problem
- **Methods**: Finite State Machine reasoning-state model, Q-Value guided steering, [activation steering](../../../../wiki/methods/activation-steering.md)
- **Datasets**: AIME25, [MATH-500](../../../../wiki/datasets/math-500.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [GPQA Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `reasoning-dynamics`, `finite-state-machine`, `activation-steering`, `interpretability`, `inference-time-control`

---

Record id: `title:7651639ee2f29946`
