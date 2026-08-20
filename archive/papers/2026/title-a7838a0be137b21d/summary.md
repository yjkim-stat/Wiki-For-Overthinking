<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Simple "Motivation" Can Enhance Reinforcement Finetuning of Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011610>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

MeRF injects the reward specification directly into the training prompt as in-context "motivation," aiming to make RLVR finetuning of reasoning models more sample-efficient than standard trial-and-error RL.

## Problem

The current RLVR training paradigm is inefficient: the model explores the reward space by numerously generating responses and learning from fragmented, per-response reward signals, blind to the overall reward pattern.

## Contributions

- Proposes MeRF, which injects the reward specification directly into the training prompt so the model is explicitly aware of the optimization objective during RL finetuning

## Method

Standard RLVR leaves the model blind to the reward structure during generation, learning only from fragmented per-response reward signals through trial and error. MeRF instead directly injects the reward specification into the prompt as in-context "motivation" -- telling the model the "rules of the game" -- so it can be guided by both this inner motivation and the external reward signal during reinforcement finetuning.

## Results

_not recorded_

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Concerns the sample efficiency of RL finetuning itself (a training-time change to how reward information reaches the model), not reasoning length, test-time compute allocation, or when a model stops or continues thinking. The connection to this topic is only the shared "large reasoning model" phrase; it is tangential to overthinking.

## Entities

- **Concepts**: in-context motivation, reward specification awareness, RLVR sample efficiency
- **Methods**: MeRF
- **Datasets**: _none recorded_

Tags: `rlvr`, `reward-shaping`, `reinforcement-finetuning`, `tangential`

---

Record id: `title:a7838a0be137b21d`
