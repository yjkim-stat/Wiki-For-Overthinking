<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Test-Time Compute Without Verification or RL is Suboptimal

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/44733>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A theoretical and empirical argument that scaling test-time compute via verification/RL beats scaling via imitation of successful reasoning traces, with the gap growing as sqrt(token budget).

## Problem

How test-time compute should be scaled to keep improving model performance: by distilling/imitating successful reasoning traces, or by using verifiers and outcome rewards to guide RL and search. It was unresolved which approach scales better as more test-time compute is allocated.

## Contributions

- Proves theoretically that verifier-based (RL/outcome-reward) test-time compute scaling outperforms verifier-free imitation of successful traces as compute grows.
- Shows the performance gap between verification-based and imitation-based scaling widens proportionally to the square root of the test-time token budget H.
- Uses anti-concentration theory to derive asymptotic advantages of verification over imitation under heterogeneous solution traces and non-sharp reward distributions.
- Validates the theory empirically on mathematical reasoning tasks with 3B, 8B, and 32B parameter models.

## Method

Theoretical comparison of two approaches to scaling test-time compute: (i) distilling successful search or thinking traces (verifier-free imitation), and (ii) using verifiers or outcome rewards to guide RL and search. The analysis applies anti-concentration theory to show that when language models produce heterogeneous solution traces and reward distributions are not sharply peaked, verifier-guided methods scale better with the test-time token budget than imitation-based methods.

## Results

Verification-trained models continue to improve with additional test-time compute on mathematical reasoning tasks (3B, 8B, 32B models), while supervised imitation/distillation approaches plateau. The theoretical performance gap between the two approaches grows proportionally to sqrt(H), where H is the test-time token budget.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly addresses the mechanics of test-time compute scaling for reasoning models: it gives a theoretical account of why verifier-guided allocation of additional reasoning/search compute keeps improving performance while imitation-based scaling plateaus, which bears on how much test-time compute a method should spend and how it should be spent.

## Entities

- **Concepts**: [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), verification-guided RL, distillation of reasoning traces, anti-concentration theory
- **Methods**: verifier-guided RL, rejection-sampling/distillation of successful traces, test-time search
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `verification`, `reinforcement-learning`, `scaling`, `reasoning`

---

Record id: `title:41c888011fbb9bc3`
