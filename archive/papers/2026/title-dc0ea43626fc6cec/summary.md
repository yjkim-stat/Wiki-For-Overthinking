<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61157>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

VLA-ATTC gives Vision-Language-Action robotic manipulation models an adaptive test-time compute mechanism that switches from fast, instinctive action selection to deliberative reasoning based on an uncertainty signal, using a Relative Action Critic that compares candidate actions pairwise rather than estimating absolute values, cutting the failure rate of the SOTA model PI0.5 by over 50% on LIBERO-LONG.

## Problem

Vision-Language-Action models for robotic manipulation typically make decisions via a fast, instinctive process lacking deliberation, which can fail on harder or more uncertain situations that would benefit from more careful reasoning before acting.

## Contributions

- an uncertainty-based mechanism enabling VLA models to adaptively shift from instinctive to deliberative action selection at test time
- a Relative Action Critic model selecting actions via pairwise comparison rather than absolute value estimation
- efficient sampling and an automated preference-generation data pipeline, cutting PI0.5's LIBERO-LONG failure rate by over 50%

## Method

VLA-ATTC introduces an uncertainty-based mechanism that adaptively shifts a VLA model from fast, instinctive action selection to deliberative test-time reasoning when the situation warrants it; a Relative Action Critic model evaluates and selects candidate actions via pairwise comparisons (rather than estimating each action's absolute value independently), paired with efficient sampling strategies and an automated preference-data generation pipeline for training the critic.

## Results

On the LIBERO-LONG benchmark, VLA-ATTC reduces the failure rate of the state-of-the-art model PI0.5 by over 50%.

## Limitations

Not stated in the fetched abstract beyond the LIBERO-LONG benchmark result reported.

## Why it matters here

- **overthinking**: Indirectly relevant: a robotics/VLA analog of difficulty-adaptive test-time compute -- deciding when to switch from fast action selection to deliberative reasoning based on uncertainty -- structurally the same 'don't always spend maximum compute' principle as difficulty-aware overthinking mitigations for LLM reasoning, applied to robotic action selection rather than text generation.

## Entities

- **Concepts**: adaptive test-time compute for robotic action, Relative Action Critic (pairwise action comparison), uncertainty-triggered deliberation
- **Methods**: VLA-ATTC (adaptive test-time compute), Relative Action Critic model, PI0.5 (baseline model improved upon)
- **Datasets**: [LIBERO-LONG](../../../../wiki/datasets/libero-long.md)

Tags: `vision-language-action`, `test-time-scaling`, `robotic-manipulation`, `adaptive-computation`

---

Record id: `title:dc0ea43626fc6cec`
