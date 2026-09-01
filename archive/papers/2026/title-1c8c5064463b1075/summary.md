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

BEXA is an actor-critic deep RL architecture that adds early-exit branches to the actor network, formulating the exit decision as a constrained linear program during training (amortized to an efficient runtime policy) with an interpretable budget parameter, achieving substantial inference-efficiency gains with minimal or no performance loss on MuJoCo tasks with SAC and TD3.

## Problem

Deep reinforcement learning policies incur inference cost from their full network forward pass at every control step, but no prior work formulates early-exit for the actor network as a principled, budget-constrained optimization compatible with arbitrary off-policy actor-critic methods.

## Contributions

- BEXA, an actor-critic architecture incorporating early-exit branches into the actor network, compatible with any off-policy actor-critic method
- formulation of the early-exit decision as a constrained linear program during training, amortized to an efficient runtime policy
- an interpretable budget parameter for the efficiency-performance trade-off, validated on MuJoCo with SAC and TD3 showing substantial inference speedups at minimal performance cost

## Method

Adds early-exit branches to the actor network in an actor-critic architecture (BEXA); formulates the exit decision as a constrained linear program during training, whose solution is subsequently amortized into a lightweight runtime exit policy for efficient execution; introduces an interpretable budget parameter controlling the inference-cost/performance trade-off; designed to be compatible with any off-policy actor-critic method (evaluated with SAC and TD3).

## Results

On MuJoCo continuous-control tasks with both SAC and TD3, BEXA achieves substantial improvement in inference efficiency with minimal or no loss in performance versus the full (no-early-exit) actor network.

## Limitations

Not stated in the fetched abstract beyond the MuJoCo/SAC/TD3 evaluation setting.

## Why it matters here

- **overthinking**: Off-topic domain: this is an early-exit method for deep RL actor networks in continuous control (MuJoCo), unrelated to LLM reasoning-trace length or the accuracy/efficiency tradeoff of text-based reasoning; matched to the topic only via the shared term 'early exit'.

## Entities

- **Concepts**: early-exit actor network, constrained-linear-program exit decision, interpretable inference budget parameter
- **Methods**: BEXA (early-exit actor-critic), SAC (baseline algorithm), TD3 (baseline algorithm)
- **Datasets**: MuJoCo

Tags: `early-exit`, `deep-reinforcement-learning`, `actor-critic`, `inference-efficiency`

---

Record id: `title:1c8c5064463b1075`
