<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DTS: Enhancing Large Reasoning Models via Decoding Tree Sketching

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61328>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A decoding-time framework that sketches a reasoning tree via selective branching and terminates long, low-accuracy reasoning trajectories early, using an observed length-accuracy anti-correlation.

## Problem

Large reasoning models achieve inference-time gains via parallel thinking, but existing multi-trajectory methods rely on redundant sampling of reasoning trajectories, exploring the reasoning space inefficiently and producing excessively long, overthinking traces that raise inference cost without reliably improving accuracy.

## Contributions

- Decoding Tree Sketching: a plug-and-play decoding framework that sketches a backbone reasoning tree by selectively branching at decision tokens instead of fully independent resampling
- Early-termination rule guided by an observed length-accuracy anti-correlation, prioritizing short, reliable trajectories during decoding
- Demonstration that the method lets smaller models outperform models roughly 10x their size

## Method

For reasoning exploration, DTS sketches a backbone decoding tree by selectively branching at decision tokens rather than sampling fully independent trajectories, reducing redundant sampling. For reasoning selection, it exploits an observed anti-correlation between trajectory length and accuracy to terminate long trajectories early, prioritizing short, reliable ones. It is described as plug-and-play, requiring no retraining of the underlying model.

## Results

Across four large reasoning models and multiple datasets, DTS improves accuracy by 14% on average and reduces repetitive generation by 8% on average; it also enables smaller models to outperform models about 10x their size.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly addresses overthinking: it identifies a length-accuracy anti-correlation in reasoning trajectories and builds an early-termination decoding rule that stops unpromising, overly long reasoning paths in favor of short, reliable ones, reporting a 14% average accuracy gain alongside an 8% reduction in repetitive generation.

## Entities

- **Concepts**: length-accuracy anti-correlation, [overthinking](../../../../wiki/concepts/overthinking.md), tree-structured decoding, early termination
- **Methods**: Decoding Tree Sketching (DTS)
- **Datasets**: _none recorded_

Tags: `overthinking`, `test-time-compute`, `decoding`, `reasoning-trajectories`, `early-termination`

---

Record id: `title:c614f5d4c1a5c21d`
