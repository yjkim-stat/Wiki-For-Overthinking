<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/94731>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Replaces the cosine learning-rate schedule with a constant learning rate followed by a cooldown, so that scaling-law experiments can reuse a single training run across many training durations.

## Problem

Scaling-law studies fit compute-optimal model/data tradeoffs, but the standard cosine learning-rate schedule must be set to the total training length in advance, so a run stopped early is not a valid shorter run. Every (model size, token count) point therefore needs its own training run, which makes scaling experiments expensive.

## Contributions

- Argues that reliance on the cosine schedule is what forces one training run per training duration in scaling research
- Shows constant learning rate plus cooldown scales comparably to cosine while allowing a run to be ended at any point
- Shows stochastic weight averaging improves checkpoints along the trajectory at no extra training cost across scales
- Demonstrates scaling experiments run with fewer, reusable training runs and correspondingly less compute; code released at https://github.com/epfml/schedules-and-scaling/

## Method

Train with a constant learning rate for most of the run, then apply a short cooldown (decay) at whatever point the run is to end. Because the constant phase is schedule-agnostic, one long run can be branched at several points, each branch cooled down to produce a valid endpoint, so several durations are obtained from largely shared compute. The paper compares the scaling behaviour of this constant+cooldown schedule against cosine across model sizes and durations, and additionally applies stochastic weight averaging along the trajectory, which yields better checkpoints at no extra training cost.

## Results

The abstract states that constant learning rate with cooldowns scales predictably and reliably similarly to cosine, that stochastic weight averaging improves performance along the training trajectory across different scales at no additional training cost, and that scaling experiments can be run with significantly reduced compute and GPU hours by using fewer but reusable runs. No specific benchmark numbers, loss values or GPU-hour savings are given in the material available here.

## Limitations

None stated in the available material. A reader should notice that the claim is an equivalence claim about scaling behaviour of two learning-rate schedules, established empirically over the model sizes and datasets the authors trained; nothing here quantifies how far it extends beyond that range, and the compute-saving figure is asserted without a number in the abstract.

## Why it matters here

- **overthinking**: Tangential: this matched only on the phrase 'compute-optimal', which here means the pretraining sense (how to spend a training FLOP budget across model size and token count), not test-time compute. The paper is about learning-rate schedules during pretraining and contains no inference-time reasoning, no reasoning length, and no stopping criterion for a model's chain of thought. It is a keyword false positive for this topic; the only connection is that the phrase 'compute-optimal' is shared vocabulary between the pretraining-scaling and test-time-scaling literatures.

## Entities

- **Concepts**: [Scaling Laws](../../../../wiki/concepts/scaling-laws.md), Compute-Optimal Training, Learning Rate Schedule, Stochastic Weight Averaging
- **Methods**: constant learning rate with cooldown, cosine learning rate schedule, stochastic weight averaging, scaling laws
- **Datasets**: _none recorded_

Tags: `scaling-laws`, `pretraining`, `learning-rate-schedule`, `weight-averaging`, `training-efficiency`

## Abstract

Abstract Scale has become a main ingredient in obtaining strong machine learning models. As a result, understanding a model's scaling properties is key to effectively designing both the right training setup as well as future generations of architectures. In this work, we argue that scale and training research has been needlessly complex due to reliance on the cosine schedule, which prevents training across different lengths for the same model size. We investigate the training behavior of a direct alternative --- constant learning rate and cooldowns --- and find that it scales predictably and reliably similar to cosine. Additionally, we show that stochastic weight averaging yields improved performance along the training trajectory, without additional training costs, across different scales. Importantly, with these findings we demonstrate that scaling experiments can be performed with significantly reduced compute and GPU hours by utilizing fewer but reusable training runs. Our code is available at https://github.com/epfml/schedules-and-scaling/.

---

Record id: `title:5eb9089f909af3c1`
