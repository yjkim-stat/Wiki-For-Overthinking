<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011162>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Proposes Length Controlled Preference Optimization (LCPO), a small-scale preference-tuning method that cuts large reasoning models' average output length by over 50% while preserving reasoning performance.

## Problem

Long chain-of-thought reasoning in large reasoning models raises computational cost and can lead to overthinking, and existing fixes for shortening reasoning either degrade quality or require heavy retraining resources.

## Contributions

- Analyzes generation path distributions and filters generated trajectories via difficulty estimation
- Analyzes convergence characteristics of several preference optimization objectives under a unified Bradley-Terry loss framework
- Proposes Length Controlled Preference Optimization (LCPO), which directly balances the implicit reward tied to NLL loss to learn a length preference with limited data and training
- Reduces average LRM output length by over 50% across multiple benchmarks while maintaining reasoning performance

## Method

Filters generated reasoning trajectories by estimated difficulty, then studies how different preference optimization objectives converge under a shared Bradley-Terry loss formulation. Based on this analysis, proposes Length Controlled Preference Optimization (LCPO), which optimizes the implicit reward associated with negative log-likelihood loss so that the model learns a preference for shorter reasoning chains using a small amount of data and limited additional training.

## Results

Reduces the average output length of large reasoning models by over 50% across multiple benchmarks while maintaining reasoning performance, per the paper's stated experiments.

## Limitations

Only the abstract was available (no PDF attachment); specific benchmark names, model sizes, and failure cases of LCPO are not stated in the abstract.

## Why it matters here

- **overthinking**: Addresses the topic directly: it proposes a lightweight preference-optimization method (LCPO) that explicitly targets reasoning-length reduction, cutting average output length by over 50% across multiple benchmarks while maintaining accuracy, i.e. a concrete method for stopping a model at the right point.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), chain-of-thought length control, preference optimization, implicit reward
- **Methods**: Length Controlled Preference Optimization (LCPO), Bradley-Terry loss framework, difficulty-based trajectory filtering, [preference optimization](../../../../wiki/methods/preference-optimization.md)
- **Datasets**: _none recorded_

Tags: `overthinking`, `length-control`, `preference-optimization`, `chain-of-thought`, `efficient-reasoning`

## Abstract

Abstract Recent advances in Large Reasoning Models (LRMs) have demonstrated strong performance on complex tasks through long Chain-of-Thought (CoT) reasoning. However, their lengthy outputs increase computational costs and may lead to overthinking, raising challenges in balancing reasoning effectiveness and efficiency. Current solutions often compromise reasoning quality or require extensive resources. In this paper, we investigate how to reduce the generation length of LRMs with limited tuning. We analyze generation path distributions and filter generated trajectories through difficulty estimation. Subsequently, we analyze the convergence characteristics of various preference optimization objectives under a unified Bradley-Terry loss based framework. Based on the analysis, we propose Length Controlled Preference Optimization (LCPO) that directly balances the implicit reward related to NLL loss. LCPO can effectively learn length preference with limited data and training. Extensive experiments demonstrate that our method significantly reduces the average output length of LRMs by over 50\% across multiple benchmarks while maintaining the reasoning performance. Our work highlights the potential for computationally efficient approaches in guiding LRMs toward efficient reasoning.

---

Record id: `title:0694f0010d7ac51f`
