<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mind the Budget: Accelerating Deep Reinforcement Learning using Constrained Early Exit Neural Networks

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61963>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

BEXA adds early-exit branches to the actor network of an off-policy actor-critic agent and picks the exit per state by solving a constrained linear program during training, then amortizes that solution for cheap runtime inference.

## Problem

Early exit networks adapt computation to input complexity and work in supervised learning, but are largely unexplored in deep reinforcement learning. The paper's premise is that the computation needed to select an optimal action varies with the state, so a fixed-depth actor spends the same compute everywhere; what was missing is a principled way to trade policy performance against inference cost in the RL setting.

## Contributions

- Proposes BEXA, an actor-critic architecture with early exit branches in the actor, for deep reinforcement learning.
- Formulates the exit decision as a constrained linear program during training and amortizes its solution for efficient runtime execution.
- Exposes the performance/compute trade-off through a single interpretable budget parameter, compatible with any off-policy actor-critic method.
- Demonstrates the approach with SAC and TD3 on MuJoCo tasks.

## Method

Budgeted EXit Actor (BEXA) is an actor-critic architecture with early exit branches inserted into the actor network — exits placed after every layer, giving K = 3 exits in the reported variants. The choice of which exit to use is formulated during training as a constrained linear program that makes the trade-off between performance and inference expenditure explicit and is governed by a single interpretable budget parameter; the solution of that program is then amortized so that at runtime the exit decision is cheap. The construction is independent of the learning algorithm and is compatible with any off-policy actor-critic method.

## Results

Integrated with SAC and TD3 and evaluated on a suite of MuJoCo tasks. The available abstract reports a substantial improvement in inference efficiency with minimal or no loss in performance; it states no numbers. The full paper was not reachable (the OpenReview PDF is behind a verification page and no preprint was found), so no per-environment returns, exit rates or FLOP reductions are recorded here.

## Limitations

No limitations were available in the material consulted. The reader should note that the evidence base is thin as recorded: continuous-control MuJoCo tasks only, two base algorithms, three exits, and no numeric results in the abstract, so the size of the efficiency gain and the exact performance cost are unknown from what was read. The claim that state-dependent action-selection difficulty exists is asserted as a property of function approximation rather than measured in the abstract.

## Why it matters here

- **overthinking**: Not relevant as tracked — a keyword false positive on 'early exit' and 'budget'. Both terms here have their ordinary deep-learning meaning: skipping layers of a small MLP actor in a MuJoCo control agent. There is no language model, no chain of thought, and no notion of reasoning length; the compute being saved is per-forward-pass depth, not tokens generated. The one transferable idea is structural rather than empirical: the exit decision is posed as a constrained program with an explicit budget parameter and then amortized, which is a cleaner formulation of the same 'stop when further computation will not change the answer' question that adaptive-length reasoning work handles with heuristics. That is an analogy worth noting, not evidence about reasoning models, and the paper supplies no numbers that bear on this topic.

## Entities

- **Concepts**: Early exit, Input-adaptive computation, Constrained optimization for compute budgets, Amortized decision policies, Off-policy actor-critic
- **Methods**: Budgeted EXit Actor (BEXA), early exit neural networks, constrained linear program, policy amortization, SAC, TD3
- **Datasets**: MuJoCo continuous-control tasks

Tags: `early-exit`, `reinforcement-learning`, `adaptive-computation`, `mujoco`, `off-topic`, `icml-2026`

---

Record id: `title:1c8c5064463b1075`
