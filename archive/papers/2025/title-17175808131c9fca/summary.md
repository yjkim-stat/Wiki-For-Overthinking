<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116060>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Adapts the number of diffusion/flow integration steps a robot control policy uses at each control cycle based on a learned difficulty estimate, cutting computation 2.6-4.4x at comparable success rates.

## Problem

Diffusion- and flow-based robot control policies use a fixed inference budget at every control step regardless of task complexity, wasting computation on easy subtasks while potentially underperforming on hard ones.

## Contributions

- Introduces Difficulty-Aware Stochastic Interpolant Policy (DA-SIP), which adapts the integration horizon of a diffusion/flow-based robot control policy in real time based on task difficulty
- Uses a difficulty classifier over RGB-D observations to select step budget, solver variant and ODE/SDE integration mode at each control cycle
- Reports 2.6-4.4x reduction in total computation time while maintaining task-success rates comparable to fixed maximum-computation baselines across manipulation benchmarks

## Method

A difficulty classifier analyzes RGB-D observations at each control step and dynamically selects the number of integration steps, the ODE/SDE solver variant, and the integration mode for a stochastic-interpolant-based diffusion/flow control policy, allocating more inference compute to harder subtasks and less to easy ones.

## Results

2.6-4.4x reduction in total computation time versus fixed maximum-computation baselines, with task-success rates reported as comparable; specific per-task numbers were not available in the accessible material.

## Limitations

No PDF was attached; the abstract does not state limitations, and specific benchmark names or task-success numbers beyond the aggregate speedup figure were not available.

## Why it matters here

- **overthinking**: This paper's 'test-time compute scaling' is about the number of denoising/integration steps a diffusion or flow-based robotic control policy runs per control cycle, not about large language or reasoning models generating chain-of-thought text. It shares only the generic phrase 'test-time compute' with the tracked topic; the domain (robotic manipulation policies) and mechanism (adaptive ODE/SDE step budgets) are unrelated to LLM reasoning-length tradeoffs or stopping criteria. Tangential.

## Entities

- **Concepts**: difficulty-aware adaptive computation, stochastic interpolants
- **Methods**: stochastic interpolants, diffusion policy, flow-based policy, difficulty classification
- **Datasets**: unspecified robotic manipulation benchmarks (named tasks not given in the accessible abstract)

Tags: `robotics`, `diffusion-policy`, `flow-matching`, `adaptive-compute`, `manipulation`

## Abstract

Abstract Diffusion- and flow-based policies deliver state-of-the-art performance on long-horizon robotic manipulation and imitation-learning tasks. However, these controllers employ a fixed inference budget at every control step, regardless of task complexity, leading to computational inefficiency for simple subtasks while potentially underperforming on challenging ones. To address these issues, we introduce Difficulty-Aware Stochastic Interpolant Policy (DA-SIP), a framework that enables robotic controllers to adaptively adjust their integration horizon in real-time based on task difficulty. Our approach employs a difficulty classifier that analyzes RGB-D observations to dynamically select the step budget, the optimal solver variant, and ODE/SDE integration at each control cycle. DA-SIP builds upon the stochastic interpolant formulation to provide a unified framework that unlocks diverse training and inference configurations for diffusion- and flow-based policies. Through comprehensive benchmarks across diverse manipulation tasks, DA-SIP achieves 2.6-4.4× reduction in total computation time while maintaining task-success rates comparable to fixed maximum-computation baselines. By implementing adaptive computation within this framework, DA-SIP transforms generative robot controllers into efficient, task-aware systems that intelligently allocate inference resources where they provide the greatest benefit.

---

Record id: `title:17175808131c9fca`
