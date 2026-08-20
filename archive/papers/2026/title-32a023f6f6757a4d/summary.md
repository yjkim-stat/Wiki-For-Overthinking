<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GTA1: GUI Test-time Scaling Agent

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011639>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A GUI agent that samples and judges multiple candidate actions at test time and uses RL-trained click rewards to ground actions on interface elements more precisely.

## Problem

GUI agents must select the right action from a large space of possibilities and precisely target visual elements in complex interfaces; the paper addresses both action selection and grounding accuracy.

## Contributions

- Test-time scaling procedure that samples and evaluates multiple candidate GUI actions before committing to one
- Reinforcement learning approach that rewards successful clicks on interface elements to improve grounding accuracy
- Claimed state-of-the-art results on GUI grounding and task execution benchmarks

## Method

GTA1 applies test-time scaling by sampling multiple candidate action sequences for a GUI task and evaluating them to pick the best one, and separately trains element grounding with reinforcement learning that rewards clicks landing successfully on the intended interface element.

## Results

Abstract claims state-of-the-art results on GUI grounding and task execution benchmarks; no specific benchmark names or numeric scores are given in the available material.

## Limitations

Not stated in the available material (abstract only; no PDF attached).

## Why it matters here

- **overthinking**: Only shares the phrase 'test-time scaling' with the topic. Here it refers to sampling and judging multiple candidate GUI actions for element grounding, not to calibrating how long a model reasons or trading off chain-of-thought length against accuracy. No treatment of reasoning-length, stopping criteria, or compute/accuracy tradeoffs for reasoning models. Tangential keyword match only.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), GUI grounding, sample-and-evaluate action selection, RL for click grounding
- **Methods**: GTA1
- **Datasets**: _none recorded_

Tags: `gui-agent`, `test-time-scaling`, `grounding`, `reinforcement-learning`, `tangential`

---

Record id: `title:32a023f6f6757a4d`
