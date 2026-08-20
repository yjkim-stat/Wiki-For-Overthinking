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

Adds an uncertainty-triggered switch to Vision-Language-Action robot control models that shifts from reflexive action execution to a deliberation phase scored by a pairwise action critic.

## Problem

Vision-Language-Action models normally act through fast, reflexive processing, which produces poor outcomes on complex manipulation scenarios that require more deliberation; the paper addresses how to give a VLA model adaptive test-time compute without paying the cost of deliberation on every decision.

## Contributions

- An uncertainty-triggered mechanism that switches a Vision-Language-Action model between reflexive action execution and a deliberation phase
- A Relative Action Critic that scores candidate actions via pairwise comparison instead of absolute value estimation
- An automated pipeline that generates preference pairs for the critic without manual labeling

## Method

VLA-ATTC augments a Vision-Language-Action model with an uncertainty-based mechanism that detects when fast, reflexive action execution is unreliable and triggers a deliberation phase. During deliberation, a Relative Action Critic evaluates multiple candidate actions through pairwise comparison rather than absolute value estimates, which simplifies the learning problem. An efficient sampling strategy limits the added compute cost, and preference pairs for training the critic are generated automatically rather than by hand.

## Results

Reduces the failure rate of the state-of-the-art baseline PI0.5 by over 50% on the LIBERO-LONG benchmark, while maintaining responsive control speeds.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Applies an adaptive test-time-compute switch between reflexive and deliberative action selection, a mechanism conceptually parallel to controlling how much a model 'thinks,' but to vision-language-action robot manipulation policies rather than to language-model chain-of-thought reasoning. It does not address reasoning length or LRM stopping behavior. Tangential: it shares only the generic 'test-time compute' keyword; the model class (VLA/robotics) and task (LIBERO-LONG manipulation) are outside this topic's scope.

## Entities

- **Concepts**: adaptive test-time compute for robot control, pairwise action preference learning, reflexive vs deliberative action selection
- **Methods**: VLA-ATTC, Relative Action Critic, uncertainty-triggered cognitive switching
- **Datasets**: LIBERO-LONG

Tags: `vla`, `robotics`, `test-time-compute`, `action-critic`, `tangential`

---

Record id: `title:dc0ea43626fc6cec`
