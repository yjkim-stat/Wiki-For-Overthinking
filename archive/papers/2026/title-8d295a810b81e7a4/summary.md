<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mode-conditioning unlocks superior test-time compute scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010159>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Fixes diversity collapse in parallel test-time sampling for reasoning models by explicitly conditioning generation on distinct reasoning modes, either given as labels or discovered by clustering.

## Problem

Standard training underutilizes the diversity present in reasoning data, so parallel sampling at test time (drawing many candidate solutions) tends to collapse toward similar outputs, wasting the compute spent on generating multiple samples.

## Contributions

- A mode-conditioning framework that explicitly allocates sampling compute across distinct reasoning modes, using either specialist models or mode-specific prefixes, to counter diversity collapse in parallel sampling.
- Demonstration that conditioning on predefined mode labels gives consistent improvements across tasks, including a stated 4x efficiency gain over standard training for Qwen2.5-7B on OpenThoughts.
- A gradient-clustering method that discovers modes without predefined labels, yielding improvements on NuminaMath, and evidence the framework also helps after reinforcement learning training.

## Method

Instead of drawing all parallel samples from one undifferentiated distribution (which the paper argues collapses in diversity), the framework conditions generation on a reasoning mode, either by routing to different specialist models per mode or by prepending mode-specific prefixes. Modes are given either as predefined labels or discovered automatically via gradient clustering, and sampling compute at test time is explicitly spread across these modes rather than sampled uniformly.

## Results

Mode-conditioning with predefined labels gives consistent improvements across tasks; Qwen2.5-7B achieves a stated 4x efficiency gain over standard training on OpenThoughts. Gradient clustering (without predefined labels) yields improvements on NuminaMath, and the framework also improves performance following reinforcement learning training.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: On-topic in the test-time-compute-scaling sense the topic tracks: the paper targets how effectively test-time sampling compute is spent, showing that increasing the number of parallel samples yields diminishing returns without mode diversity and reporting a 4x efficiency gain from spending that compute more deliberately. It addresses breadth (parallel sampling diversity) rather than depth (single-trace reasoning length), so it is a narrower fit than papers about when a single chain-of-thought should stop.

## Entities

- **Concepts**: diversity collapse in parallel sampling, mode-conditioning, reasoning modes, gradient clustering for unsupervised mode discovery
- **Methods**: mode-conditioning, gradient clustering
- **Datasets**: OpenThoughts, NuminaMath

Tags: `test-time-scaling`, `diversity`, `parallel-sampling`, `mode-conditioning`

---

Record id: `title:8d295a810b81e7a4`
