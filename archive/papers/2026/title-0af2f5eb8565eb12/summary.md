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

Selects which training prompts to use for RL finetuning of large reasoning models by predicting their learning dynamics with a hidden Markov model, instead of evaluating every candidate with rollouts.

## Problem

RL finetuning of reasoning models benefits from training on moderately difficult problems, but identifying which problems are informative normally requires expensive per-candidate model evaluation.

## Contributions

- A method that predicts a training example's learning dynamics via a hidden Markov model over past reward signals, before running rollouts on it
- An online scheme for selecting informative prompts for RL finetuning of reasoning models without exhaustively evaluating every candidate
- Empirical demonstration across math, planning and geometry tasks that this reduces wasted rollouts and speeds up RL training

## Method

Models each training prompt's expected reward trajectory during RL finetuning as a hidden Markov process, using Bayesian inference over historical reward signals to predict how a candidate prompt would progress if trained on, so prompts can be selected for their informativeness without first running costly rollouts.

## Results

No specific numeric results were available from the source material beyond a general claim of reduced computation and improved final performance across math, planning and geometry tasks; exact benchmarks and numbers were not stated in the accessible abstract.

## Limitations

The abstract page gives only a high-level summary; no PDF was attached and no numeric results, benchmark names, or stated limitations were available to extract.

## Why it matters here

- **overthinking**: This is about which training prompts to spend RL rollouts on during finetuning, not about how long a model reasons at inference time or when it should stop; it does not address the accuracy/efficiency tradeoff of reasoning length or test-time stopping criteria. It only shares the generic 'large reasoning model' keyword with the tracked topic.

## Entities

- **Concepts**: active learning for RL data selection, learning-dynamics prediction, hidden Markov model over reward trajectories
- **Methods**: Bayesian inference, hidden Markov model, reinforcement learning finetuning
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `active-learning`, `data-selection`, `training-efficiency`

---

Record id: `title:0af2f5eb8565eb12`
