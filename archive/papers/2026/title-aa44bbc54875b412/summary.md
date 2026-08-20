<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Conditional Advantage Estimation for Reinforcement Learning in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010855>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

CANON regroups sampled RLVR rollouts by higher or lower value of a target metric such as entropy or response length to shape advantages without a hand-crafted directional assumption, improving both accuracy and token efficiency.

## Problem

Training metrics like entropy or response length correlate with different reasoning behaviors under RLVR, and prior methods incorporate this via hand-crafted reward or advantage shaping with fixed higher-is-better/lower-is-better assumptions, which risks failure without careful tuning.

## Contributions

- Proposes CANON, a conditional advantage estimation method that shapes advantages from a target metric without assuming a fixed directional bias
- Applies CANON to entropy, outperforming prior hand-crafted shaping methods across three LLMs on math and logic tasks
- Applies CANON to response length, improving token efficiency and the performance-cost Pareto frontier

## Method

Prior work shapes RLVR rewards or advantages using hand-crafted, fixed directional assumptions about a target metric (e.g., "shorter is better"), which risks failure without careful tuning. CANON instead regroups sampled responses into two groups based on whether they have a higher or lower value of the target metric (e.g., entropy or response length), compares performance between the two groups to identify which direction is actually beneficial, and shapes the advantage accordingly rather than presuming a direction in advance.

## Results

CANON based on entropy outperforms prior shaping methods across three LLMs on math reasoning and high-complexity logic tasks, with up to a 1.9-point gain in math accuracy and a 5.2-point gain on challenging logic tasks. Applied to response length, it reduces token consumption by 33.8% compared to prior methods while improving the performance-cost Pareto frontier.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Applies conditional advantage estimation to response length as the shaped metric: reduces token consumption by 33.8% compared to prior length-shaping methods while improving accuracy, giving a better performance-cost Pareto frontier -- a direct reinforcement-learning method for the accuracy/efficiency reasoning-length tradeoff.

## Entities

- **Concepts**: advantage shaping, entropy and response length as reasoning-behavior correlates, performance-cost pareto frontier
- **Methods**: CANON (Conditional Advantage Estimation)
- **Datasets**: _none recorded_

Tags: `overthinking`, `rlvr`, `advantage-estimation`, `token-efficiency`

---

Record id: `title:aa44bbc54875b412`
