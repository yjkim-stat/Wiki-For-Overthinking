<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# UniScale: Adaptive Unified Inference Scaling via Online Joint Optimization of Model Routing and Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/60578>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

An online bandit controller that jointly decides which model to route a query to and how much test-time compute to spend, to optimize the quality-cost tradeoff.

## Problem

Balancing inference quality against compute cost is handled today by two separate levers: routing between differently-sized models (discrete choices) and scaling test-time compute within one model (diminishing returns); the paper argues joint optimization of both does better than either alone.

## Contributions

- Unifies model routing (choosing among differently-sized models) and test-time compute scaling into a single joint online optimization instead of treating them separately
- Formulates the joint decision as a contextual multi-armed bandit solved with LinUCB
- Adds efficiency-aware learning and cost modeling to keep the bandit stable over a high-dimensional joint decision space
- Demonstrates better quality-cost tradeoffs than routing-only or scaling-only baselines across varied, dynamic inference scenarios

## Method

UniScale casts the choice of which model to route a request to, together with how much test-time compute to spend on it, as one contextual multi-armed bandit problem, learned online via LinUCB. Efficiency-aware learning and a cost model are used to stabilize the policy across the resulting high-dimensional action space, exploiting synergies between routing and scaling that separate approaches miss.

## Results

Reports superior quality-cost tradeoffs versus model-routing-only and test-time-scaling-only baselines across varied, dynamic inference scenarios; no specific numeric results or benchmark names are given in the available abstract.

## Limitations

Not stated in the available material (abstract only; no PDF attached).

## Why it matters here

- **overthinking**: Directly targets the accuracy/compute tradeoff the topic tracks by treating test-time compute allocation as a controllable knob to be optimized per query, jointly with model choice, via an online bandit. It is a system-level scaling controller rather than an analysis of a single model's chain-of-thought length or an intervention that makes a model stop reasoning at the right point, but the core question -- how much test-time compute a query should get -- is squarely the topic's concern.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), model routing, quality-cost tradeoff, [contextual bandits](../../../../wiki/concepts/contextual-bandits.md), online optimization
- **Methods**: UniScale, LinUCB, contextual multi-armed bandit
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `model-routing`, `bandit-optimization`, `inference-cost`, `on-topic`

---

Record id: `title:3b024853a8e7324c`
