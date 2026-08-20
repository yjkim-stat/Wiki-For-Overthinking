<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Generation as Search Operator for Test-Time Scaling of Diffusion-based Combinatorial Optimization

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119551>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A method that scales diffusion-based combinatorial-optimization solvers by alternating local-search perturbation with diffusion re-generation, rather than just adding denoising steps, achieving large speedups over classical solvers on TSP.

## Problem

Diffusion models for combinatorial optimization saturate quickly when scaled only by adding more denoising steps at inference time; a more cost-efficient inference-time scaling axis was needed.

## Contributions

- Proposes GenSCO, which scales diffusion-based combinatorial optimization solvers along a new inference-time axis (search-driven generation) rather than just adding more denoising steps.
- Combines local-search-based solution disruption with diffusion sampling in a repeated operator cycle to escape local optima.
- Introduces a search-friendly solution-enhancement training procedure using a rectified flow model (via a lightweight transformer) to learn diffusion trajectories from suboptimal to optimal solutions.
- Demonstrates large speedups over the state-of-the-art classical solver LKH3 on TSP.

## Method

GenSCO treats each round of diffusion generation as a search operator rather than a one-shot solving process: a cycle alternates between disrupting the current candidate solution via local search operators and re-generating via diffusion sampling, letting the model escape local optima instead of only refining in place. Generation is trained to be search-friendly via a rectified flow model, implemented with a lightweight transformer, that learns neural ODEs linearizing diffusion trajectories between suboptimal and optimal solutions to speed convergence.

## Results

GenSCO delivers a 141x speedup over LKH3 to reach 0.000% optimality gap on TSP-100, and roughly a 10x speedup to reach 0.02% optimality gap on TSP-500, with orders-of-magnitude improvement over prior neural CO methods.

## Limitations

The abstract does not report results on combinatorial optimization problems other than TSP, nor generalization to problem sizes beyond TSP-500, nor training cost of the rectified flow model.

## Why it matters here

- **overthinking**: Tangential. This is about inference-time compute scaling for diffusion-based combinatorial optimization solvers (TSP), not about large reasoning models' chain-of-thought length or the accuracy/efficiency tradeoff of verbal reasoning. It shares only the generic phrase 'test-time scaling' with the tracked topic; the mechanism (denoising steps vs. search operators) and application domain are unrelated to LRM overthinking/underthinking.

## Entities

- **Concepts**: search-driven generation, rectified flow for solution trajectories, denoising-step scaling saturation
- **Methods**: GenSCO, rectified flow, diffusion sampling for combinatorial optimization, local search operators, neural ODEs
- **Datasets**: TSP-100, TSP-500

Tags: `combinatorial-optimization`, `diffusion-models`, `tsp`, `rectified-flow`, `test-time-scaling`

## Abstract

Abstract While diffusion models have shown promise for combinatorial optimization (CO), their inference-time scaling cost-efficiency remains relatively underexplored. Existing methods improve solution quality by increasing denoising steps, but the performance often becomes saturated quickly. This paper proposes GenSCO to systematically scale diffusion solvers by an orthogonal dimension of inference-time computation beyond denoising step expansion, i.e., search-driven generation. GenSCO takes generation as a search operator rather than a complete solving process, where each operator cycle combines solution disruption (via local search operators) and diffusion sampling, enabling iterative exploration of the learned solution space. Rather than over-refining current solutions, this paradigm encourages the model to leave local optima and explore a broader area of the solution space, ensuring a more consistent scaling effect. The search loop is supported by a search-friendly solution-enhancement training procedure that incorporates a rectified flow model learning to establish diffusion trajectories between suboptimal solutions and the optimal ones. The flow model is empowered by a lightweight transformer architecture to learn neural ODEs that linearize solution trajectories, accelerating convergence of the scaling effect with efficiency. The resulting enhanced scaling efficiency and practical scalability lead to synergistic performance improvements. Extensive experiments show that GenSCO delivers performance improvements by orders of magnitude over previous state-of-the-art neural methods. Notably, GenSCO even achieves significant speedups compared to the state-of-the-art classic mathematical solver LKH3, delivering a 141x speedup to reach 0.000% optimality gap on TSP-100, and approximately a 10x speedup to reach 0.02% on TSP-500.

---

Record id: `title:7981bfb3735c19c7`
