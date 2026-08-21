<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# On Reasoning Strength Planning in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118916>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

Finds that large reasoning models pre-plan how much to reason via a directional vector in their activations, whose magnitude causally sets reasoning length.

## Problem

LRMs are known to allocate more reasoning tokens to harder problems (difficulty-awareness), but the mechanism behind this automatic allocation was unexplored.

## Contributions

- Shows the number of reasoning tokens an LRM will generate is predictable from question activations alone, using linear probes, before generation starts
- Identifies a pre-allocated directional vector in model activations whose magnitude causally controls reasoning strength
- Demonstrates that subtracting the vector reduces reasoning tokens and performance, while adding it increases reasoning tokens and can improve performance
- Shows the vector modifies the logits of the end-of-reasoning token to affect reasoning length
- Applies the findings to detect overthinking behavior and to enable efficient reasoning on simple problems

## Method

Trains linear probes on question activations to predict reasoning token count before generation, then identifies a directional vector embedded in activation space whose magnitude modulates reasoning strength. The vector is added to or subtracted from activations to causally test its effect on reasoning length and task performance, and its influence on the end-of-reasoning token's logits is examined.

## Results

Subtracting the identified directional vector reduces reasoning token count and lowers task performance; adding it increases reasoning token count and can improve performance. Linear probes on question activations predict reasoning token counts. No specific benchmark accuracy or token-count numbers are given in the abstract.

## Limitations

The abstract does not report which models, benchmarks, or quantitative accuracy/token-count figures were used to validate the probing and vector-intervention claims; effect sizes are not given.

## Why it matters here

- **overthinking**: Provides a mechanistic, activation-level explanation for why LRMs vary reasoning length by difficulty, and demonstrates a concrete intervention (adding/subtracting a directional vector) that can shorten or lengthen reasoning, offering a tool for detecting overthinking and for triggering efficient reasoning on easy problems.

## Entities

- **Concepts**: reasoning strength pre-planning, directional activation vector for reasoning length, linear probing of question activations, end-of-reasoning token logit control
- **Methods**: [linear probing](../../../../wiki/methods/linear-probe.md), activation steering (vector addition/subtraction)
- **Datasets**: _none recorded_

Tags: `reasoning-length`, `interpretability`, `activation-steering`, `overthinking`, `difficulty-awareness`

## Abstract

Abstract Recent studies empirically reveal that large reasoning models (LRMs) can automatically allocate more reasoning strengths (\ie the number of reasoning tokens) for harder problems, exhibiting difficulty-awareness for better task performance. While this automatic reasoning strength allocation phenomenon has been widely observed, its underlying mechanism remains largely unexplored. To this end, we provide explanations for this phenomenon from the perspective of model activations. \textbf{We find evidence that LRMs pre-plan the reasoning strengths in their activations even before generation, with this reasoning strength causally controlled by the magnitude of a pre-allocated directional vector.} Specifically, we show that the number of reasoning tokens is predictable solely based on the question activations using linear probes, indicating that LRMs estimate the required reasoning strength in advance. We then uncover that LRMs encode this reasoning strength through a pre-allocated directional vector embedded in the activations of the model, where the vector’s magnitude modulates the reasoning strength. Subtracting this vector can lead to reduced reasoning token number and performance, while adding this vector can lead to increased reasoning token number and even improved performance. We further reveal that this direction vector consistently yields positive reasoning length prediction, and it modifies the logits of end-of-reasoning token \texttt{} to affect the reasoning length. Finally, we demonstrate two potential applications of our findings: overthinking behavior detection and enabling efficient reasoning on simple problems. Our work provides new insights into the internal mechanisms of reasoning in LRMs and offers practical tools for controlling their reasoning behaviors. Our code is available at \url{https://anonymous.4open.science/r/LRM-plans-CoT-7E04}.

---

Record id: `title:11c0c9193baf1d69`
