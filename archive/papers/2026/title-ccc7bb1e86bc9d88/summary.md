<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Small Generalizable Prompt Predictive Models Can Steer Efficient RL Post-Training of Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/60937>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Generalizable Predictive Prompt Selection (GPS) trains a lightweight generative model on shared optimization history to perform Bayesian inference over prompt difficulty, then uses intermediate-difficulty prioritization and history-anchored diversity to select RL training batches, improving training efficiency, final performance, and test-time efficiency over strong baselines for RL post-training of large reasoning models.

## Problem

Reinforcement learning improves LLM reasoning but is rollout-intensive and computationally expensive, and naive or non-adaptive batch/prompt selection during RL training wastes rollout budget on prompts that are too easy or too hard to provide useful learning signal.

## Contributions

- Generalizable Predictive Prompt Selection (GPS), a lightweight generative model performing Bayesian inference over prompt difficulty from shared optimization history, avoiding costly per-prompt rollout assessment
- a batch-selection strategy combining intermediate-difficulty prioritization with history-anchored diversity
- substantial improvements in RL training efficiency, final performance, and test-time efficiency over strong baselines

## Method

Proposes Generalizable Predictive Prompt Selection (GPS): a lightweight generative model is trained on the shared optimization history (across the RL run) to perform Bayesian inference estimating each candidate prompt's difficulty without needing new rollouts to assess it; batch selection then integrates intermediate-difficulty prioritization (favoring prompts neither too easy nor too hard) with history-anchored diversity (avoiding redundant prompt selection based on what has already been explored).

## Results

GPS demonstrates substantial improvements in training efficiency, final downstream performance, and test-time efficiency versus superior baseline prompt-selection methods for RL post-training of large reasoning models (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the RL-post-training scope and baseline comparison described.

## Why it matters here

- **overthinking**: Indirectly relevant: this targets training-time RL sample-selection efficiency (which prompts to spend rollout budget on) rather than inference-time reasoning length directly, but it explicitly reports gains in 'test-time efficiency' as well as training efficiency, suggesting curriculum-aware RL training may also produce models with better inference-time accuracy/efficiency tradeoffs -- a training-side lever complementary to the archive's inference-time overthinking mitigations.

## Entities

- **Concepts**: Bayesian prompt-difficulty inference, intermediate-difficulty prioritization, history-anchored diversity
- **Methods**: Generalizable Predictive Prompt Selection (GPS), Bayesian inference over prompt difficulty
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `curriculum-selection`, `training-efficiency`, `large-reasoning-models`

---

Record id: `title:ccc7bb1e86bc9d88`
