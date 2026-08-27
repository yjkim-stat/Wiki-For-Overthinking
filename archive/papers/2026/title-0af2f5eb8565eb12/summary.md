<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006780>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Dynamics-Predictive Sampling (DPS) forecasts, from a hidden-Markov model of each prompt's historical reward trajectory, which prompts are worth including in RL fine-tuning of large reasoning models before running any rollouts, cutting wasted rollouts and speeding up training.

## Problem

Online prompt-selection methods for RL fine-tuning of LLMs focus training on moderately difficult prompts but require extensive rollouts to judge prompt difficulty, which is computationally expensive.

## Contributions

- Dynamics-Predictive Sampling (DPS), forecasting prompt value from historical reward dynamics without extra rollouts
- a Bayesian hidden-Markov-model formulation of per-prompt solving progress
- empirical reduction of redundant rollouts and training-time speedup across math, planning and visual-geometry tasks

## Method

Models each prompt's solving-progress-over-training as a dynamical system via a hidden Markov model, using Bayesian inference over historical reward data to predict which prompts merit inclusion prior to costly rollouts, avoiding heavy per-step rollout-based filtering.

## Results

Across mathematics, planning, and visual-geometry tasks, DPS substantially reduces redundant rollouts, accelerates training, and achieves superior reasoning performance versus prior online prompt-selection baselines (no specific numbers given in the fetched abstract).

## Limitations

Not stated in the source; the fetched material gives no numeric comparison or discussion of failure cases.

## Why it matters here

- **overthinking**: Indirectly relevant: it targets training-time compute efficiency (which prompts to spend RL rollouts on) rather than inference-time reasoning length, but shares the topic's general concern with not wasting compute on cases that do not need it -- here applied to curriculum/data selection instead of per-query reasoning budget.

## Entities

- **Concepts**: dynamics-predictive prompt selection, active RL fine-tuning, hidden Markov model of training dynamics
- **Methods**: hidden Markov model, Bayesian inference, active/online prompt selection for RL fine-tuning
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `active-sampling`, `large-reasoning-models`, `training-efficiency`

---

Record id: `title:0af2f5eb8565eb12`
