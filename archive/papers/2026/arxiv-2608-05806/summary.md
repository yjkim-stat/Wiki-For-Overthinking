<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Hierarchical Latent Prediction for Language Models

- **Authors**: Chang Shi, Tim Pearce, Manan Tomar, Siddhartha Sen, John Langford
- **Venue**: cs.CL
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05806>
- **PDF**: <https://arxiv.org/pdf/2608.05806v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Adds a higher-level abstract latent as an auxiliary pretraining target to reduce compounding error in latent-space rollouts, aiming at longer-horizon coherence than multi-token or next-latent prediction.

## Problem

Next-Token Prediction underpins pretraining but its teacher-forced paradigm may not suit long-horizon reasoning and planning. Multi-Token Prediction and Next-Latent prediction were proposed as remedies, but their auxiliary objectives either have a limited horizon or accumulate compounding error over multi-step latent rollouts.

## Contributions

- Hierarchical Latent Prediction, an auxiliary objective adding a higher-level abstract latent above next-latent prediction
- An argument that hierarchical abstraction reduces compounding error in latent rollouts relative to MTP and NextLat
- Reported gains on coding and multi-step reasoning benchmarks and in speculative decoding efficiency

## Method

Hierarchical Latent Prediction introduces an auxiliary higher-level abstract latent, whose role is to reduce error accumulation in latent-space rollouts. The hierarchy is the mechanism: predicting a coarser latent over a longer span is less sensitive to per-step error than chaining fine-grained latent predictions.

## Results

Experiments report longer-horizon coherent belief-state representations, effectiveness across coding and multi-step reasoning benchmarks, and improved speculative decoding efficiency. No numbers are given in the abstract.

## Limitations

No quantitative results, no named benchmarks, and no model scales in the abstract; the description of the abstract latent's construction and supervision is not given at this level of detail. Claims about belief-state coherence are asserted without a stated measurement. Being a pretraining-objective change, cost and any comparison at matched compute are unreported, which is the central question for a pretraining auxiliary loss.

## Why it matters here

- **reasoning-evaluation**: Matched this topic on benchmark vocabulary rather than on evaluation content; it reports multi-step reasoning benchmark results but contributes no evaluation method. Its real bearing is on where reasoning ability comes from: it locates the limitation in the pretraining objective rather than in post-training, which is upstream of everything else this archive tracks. Without numbers the claim cannot be weighed, and the paper would need a full read or a later version before it supports anything.

## Entities

- **Concepts**: next-token prediction, [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), [belief state](../../../../wiki/concepts/belief-state.md), [compounding error](../../../../wiki/concepts/compounding-error.md), planning horizon, teacher forcing
- **Methods**: Hierarchical Latent Prediction, Multi-Token Prediction, Next-Latent prediction, [speculative decoding](../../../../wiki/methods/speculative-decoding.md), auxiliary pretraining objective
- **Datasets**: _none recorded_

Tags: `pretraining objective`, `latent prediction`, `planning`, `speculative decoding`, `thin-evidence`

## Abstract

While standard Next-Token Prediction (NTP) lays the foundation of language model pre- training, its teacher-forced training paradigm may not be optimal for long-horizon reasoning and planning. Recent works such as Multi-Token Prediction (MTP) and Next-Latent prediction (NextLat) try to mitigate the problem through predicting multiple future tokens and self-supervised prediction in the latent space. However, those auxiliary objectives either have a limited horizon or suffer from compounding error from multi-step rollout. We introduce Hierarchical Latent Prediction (HiLP), which introduces an auxiliary higher-level abstract latent to help reduce the error accumulation effect in latent-space rollouts. Experiments show that HiLP can lead to longer-horizon coherent belief state representation and demonstrate the effectiveness of our method across coding and multi-step reasoning benchmarks, and offers more speculative decoding efficiency.

---

Record id: `arxiv:2608.05806`
