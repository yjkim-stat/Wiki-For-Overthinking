<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimizing Test-Time Compute via Meta Reinforcement Finetuning

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/45154>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Casts test-time compute optimization as a meta reinforcement learning problem and fine-tunes reasoning models with an information-gain-based dense reward so each block of reasoning measurably progresses toward the answer.

## Problem

Reasoning models generate extended outputs at inference time, but standard outcome-only reward training gives no signal about whether intermediate reasoning is actually making progress, so models can spend tokens without improving their odds of a correct answer.

## Contributions

- A formalization of optimizing test-time compute as a meta reinforcement learning problem, framed around the exploration-exploitation tradeoff over sequential token blocks.
- MRT (Meta Reinforcement Fine-Tuning), which fine-tunes with a dense reward bonus based on information gain to ensure each block of tokens makes measurable progress toward the answer.
- A cumulative-regret formulation of efficiency, measuring progress across the whole generation rather than only the final outcome.

## Method

The model's extended generation is treated as a sequence of token blocks produced under a meta-RL objective: rather than rewarding only the final answer, MRT adds a dense reward bonus proportional to the information gain of each block toward the correct answer, and optimizes for low cumulative regret across the generation. This is intended to make each segment of reasoning purposeful rather than just extending the trace.

## Results

On a token-matched evaluation on AIME, MRT-B improves over iterated STaR by 30% and over GRPO by 38%. MRT gives roughly a 2-3x relative gain in performance and about a 1.5x gain in token efficiency for math reasoning compared to outcome-reward RL, achieving higher accuracy while generating fewer tokens (arXiv:2503.07572).

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly on-topic: this is exactly the accuracy/token-efficiency tradeoff the topic tracks. MRT is trained so that generating fewer tokens is rewarded when it does not sacrifice progress, targeting the core question of when a model should keep reasoning versus stop, using cumulative regret over reasoning progress as the efficiency lens.

## Entities

- **Concepts**: test-time compute as meta reinforcement learning, exploration-exploitation in reasoning, cumulative regret as an efficiency metric, information-gain reward
- **Methods**: MRT (Meta Reinforcement Fine-Tuning)
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md)

Tags: `meta-rl`, `test-time-compute`, `token-efficiency`, `reward-shaping`

---

Record id: `title:86af300fcc089e57`
