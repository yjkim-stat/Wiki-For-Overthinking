<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# UnMaskFork: Test-Time Scaling for Masked Diffusion via Deterministic Action Branching

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/66823>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Uses Monte Carlo Tree Search over deterministic partial-unmasking actions to scale test-time compute for masked diffusion language models on coding and math tasks.

## Problem

Test-time scaling strategies have improved reasoning in autoregressive LLMs, but it is unclear whether Masked Diffusion Language Models, which generate non-autoregressively through iterative unmasking, can benefit from similar search-based test-time scaling.

## Contributions

- Formulates masked diffusion language model generation as a search tree amenable to Monte Carlo Tree Search
- Proposes deterministic partial-unmasking actions across multiple MDLMs as an alternative to the stochastic sampling used by standard test-time scaling methods

## Method

UnMaskFork (UMF) formulates the unmasking trajectory of a Masked Diffusion Language Model as a search tree and applies Monte Carlo Tree Search to choose the generation path. Instead of relying on stochastic sampling, as standard test-time scaling methods do, it explores the search space through deterministic partial-unmasking actions carried out by multiple MDLMs.

## Results

Reported to outperform existing test-time scaling baselines on complex coding benchmarks and to show strong scalability on mathematical reasoning tasks; no specific benchmark names or numeric scores are given in the available material.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Applies test-time-compute scaling to masked diffusion language models via search over the unmasking order of a non-autoregressive generation process, not to autoregressive reasoning-length control. It does not address the accuracy/length tradeoff, overthinking, or when a model should stop reasoning. Tangential: it shares only the generic 'test-time scaling' keyword with the topic; the model class (masked diffusion) and mechanism (MCTS over unmasking actions) are unrelated to LRM chain-of-thought length.

## Entities

- **Concepts**: test-time scaling for diffusion generation, search over unmasking trajectories, deterministic action branching
- **Methods**: [Monte Carlo Tree Search](../../../../wiki/methods/monte-carlo-tree-search.md), Masked Diffusion Language Models, UnMaskFork (UMF)
- **Datasets**: _none recorded_

Tags: `diffusion`, `test-time-scaling`, `mcts`, `masked-diffusion`, `tangential`

---

Record id: `title:d9e74e95d6430dc0`
