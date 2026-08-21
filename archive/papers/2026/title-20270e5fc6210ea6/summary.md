<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63795>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes a budget-aware Monte Carlo Tree Search policy (BG-MCTS) that reallocates exploration versus refinement as a fixed per-query token budget is consumed, for test-time scaling of LLMs.

## Problem

Tree-search decoding is an effective form of test-time scaling for LLMs, but real deployments impose a fixed per-query token budget that current tree-search methods do not account for, leading to over-branching late in the search or premature termination before a good answer is found.

## Contributions

- Identifies that existing tree-search decoding methods ignore fixed per-query token budgets, causing late-stage over-branching or premature termination.
- Proposes Budget-Guided MCTS (BG-MCTS), a tree-search policy that adapts its exploration/exploitation balance to the remaining token budget as the search proceeds.
- Shows BG-MCTS outperforms budget-agnostic tree-search baselines across a range of inference budgets on mathematical and physics reasoning benchmarks.

## Method

Budget-Guided MCTS (BG-MCTS) aligns a tree-search decoding policy with the remaining token budget during Monte Carlo Tree Search: it starts with broad exploration when budget is plentiful, then shifts toward refinement and answer completion as the remaining budget shrinks, reducing late-stage branching from shallow nodes so the search does not run out of budget mid-exploration or terminate too early.

## Results

BG-MCTS outperforms budget-agnostic tree-search baselines across inference budgets on mathematical reasoning benchmarks and an additional physics reasoning benchmark with open-weight LLMs; no specific accuracy numbers are given in the available abstract.

## Limitations

Specific benchmark names, numeric results and model sizes are not given in the available material (poster page abstract only, no PDF); the abstract itself gives no quantitative results, only that BG-MCTS 'outperforms' baselines.

## Why it matters here

- **overthinking**: This is a direct treatment of the test-time compute tradeoff: it studies how to spend a fixed reasoning/search token budget across a tree-search process so the model neither over-explores (wasting budget on late-stage branching) nor stops too early (premature termination), which is exactly the stop/keep-going calibration problem the topic tracks.

## Entities

- **Concepts**: fixed token budget, budget-aware tree search, [test-time scaling](../../../../wiki/concepts/test-time-scaling.md)
- **Methods**: Budget-Guided MCTS (BG-MCTS), [Monte Carlo Tree Search](../../../../wiki/methods/monte-carlo-tree-search.md), tree-search decoding
- **Datasets**: mathematical reasoning benchmarks, a physics reasoning benchmark

Tags: `test-time-scaling`, `tree-search`, `mcts`, `token-budget`, `inference-cost`

## Abstract

Abstract Tree-search decoding is an effective form of test-time scaling for large language models (LLMs), but real-world deployment often imposes a fixed per-query token budget that varies across settings. Existing tree-search policies are largely budget-agnostic, treating the budget merely as a termination condition, thereby risking late-stage over-branching or premature termination. We propose Budget-Guided MCTS (BG-MCTS), a tree-search decoding algorithm that aligns its search policy with the remaining token budget: it starts with broad exploration, then prioritizes refinement and answer completion as the remaining budget decreases while reducing late-stage branching from shallow nodes. BG-MCTS consistently outperforms budget-agnostic tree-search baselines across inference budgets on mathematical reasoning benchmarks and an additional physics reasoning benchmark with open-weight LLMs.

---

Record id: `title:20270e5fc6210ea6`
