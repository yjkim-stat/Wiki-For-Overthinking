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

Trains a small, prompt-generic Bayesian predictor of prompt difficulty from shared RL optimization history to select informative training prompts and reduce rollout cost when RL-training large reasoning models.

## Problem

Reinforcement learning post-training improves LLM reasoning but is expensive because it is rollout-intensive; existing online prompt-selection methods either require costly exact difficulty evaluation or use prompt-specific predictors that do not generalize across prompts.

## Contributions

- GPS: a lightweight, prompt-generic Bayesian predictive model of prompt difficulty, trained on optimization history shared across prompts
- A batch-selection acquisition principle combining intermediate-difficulty prioritization with history-anchored diversity
- Demonstration that the predictor generalizes to unseen prompts and to test-time computational allocation

## Method

Trains a small generative model on optimization history shared across prompts to perform Bayesian inference of prompt difficulty, avoiding the need for costly exact per-prompt evaluation or prompt-specific predictors that do not generalize. Uses this predictor in an acquisition principle that prioritizes intermediate-difficulty prompts and rewards diversity anchored to prior history, to select informative prompt batches for RL rollouts. The same lightweight predictor is also applied at test time for computational allocation.

## Results

Reports improvements in training efficiency, final performance, and test-time efficiency over baseline prompt-selection methods across multiple reasoning benchmarks; no specific numeric results were available in the fetched abstract.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Its core contribution is selecting which prompts to train on during RL post-training to cut rollout cost, not controlling how long a trained model reasons at inference. It claims the predictor also 'generalizes at test-time for efficient computational allocation,' which touches the test-time-compute angle of the topic, but no detail is given on reasoning length, stopping behavior, or accuracy/length tradeoffs, so its connection to overthinking specifically is thin.

## Entities

- **Concepts**: prompt difficulty prediction, online prompt selection, [Bayesian inference](../../../../wiki/concepts/bayesian-inference.md), RL post-training efficiency
- **Methods**: Generalizable Predictive Prompt Selection (GPS)
- **Datasets**: _none recorded_

Tags: `rl-post-training`, `prompt-selection`, `reasoning-models`, `training-efficiency`

---

Record id: `title:ccc7bb1e86bc9d88`
