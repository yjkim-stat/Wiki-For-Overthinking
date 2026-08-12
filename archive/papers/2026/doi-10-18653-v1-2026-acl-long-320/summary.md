<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SeLaR: Selective Latent Reasoning in Large Language Models

- **Authors**: Renyu Fu, Guibo Luo
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.320>
- **DOI**: 10.18653/V1/2026.ACL-LONG.320
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-faithfulness 0.50

## In one line

Switches to soft-embedding latent reasoning only at low-confidence steps, keeping discrete decoding elsewhere, and pushes the soft embeddings away from the top token to stop them collapsing.

## Problem

CoT is limited by the expressiveness of discrete token sampling. Latent reasoning replaces discrete tokens with soft embeddings or hidden states, but suffers two problems: global activation perturbs high-confidence steps and impairs stability, and soft embeddings collapse toward the highest-probability token, which removes the exploration they were supposed to add.

## Contributions

- Identification of two failure modes in latent reasoning: perturbation of high-confidence steps by global activation, and soft-embedding collapse toward the top token
- SeLaR, a training-free selective latent reasoning framework
- An entropy gate that activates soft embeddings only at low-confidence steps
- Entropy-aware contrastive regularization pushing soft embeddings off the top-token direction
- Reported gains over standard CoT and state-of-the-art training-free methods on five reasoning benchmarks

## Method

SeLaR is lightweight and training-free. An entropy-gated mechanism activates soft embeddings only at low-confidence steps while preserving discrete decoding at high-confidence steps — the gate is what prevents perturbation where the model is already committed. An entropy-aware contrastive regularization pushes soft embeddings away from the highest-probability token's direction, sustaining exploration of multiple latent paths.

## Results

On five reasoning benchmarks, SeLaR consistently outperforms standard CoT and state-of-the-art training-free methods. No numbers, benchmarks or models are given in the abstract.

## Limitations

No quantitative results, benchmarks or models in the abstract. The entropy gate introduces a threshold whose sensitivity is unreported, and the archive's entropy work suggests such thresholds do not transfer across models. Contrastive regularization away from the top token is a heuristic against collapse rather than a guarantee. Being training-free, gains depend on the base model already supporting useful latent variation.

## Why it matters here

- **reasoning-faithfulness**: Interesting to this topic mainly for what it implies about monitoring: reasoning becomes latent exactly at the low-confidence steps, which are the steps a monitor would most want to read. So selective latent reasoning is not a uniform loss of transparency but a targeted one, concentrated where decisions are actually being made. That is a sharper version of the concern in arxiv:2608.04928, which finds monitorability depends on task structure more than reasoning mode — this paper's gating gives a concrete case where mode and decision-point coincide. It also reuses the entropy-as-decision-point signal the archive tracks from the training side, here at inference and without training.

## Entities

- **Concepts**: [latent reasoning](../../../../wiki/concepts/latent-reasoning.md), [implicit reasoning](../../../../wiki/concepts/implicit-reasoning.md), [token-level entropy](../../../../wiki/concepts/token-level-entropy.md), [entropy collapse](../../../../wiki/concepts/entropy-collapse.md), [exploration-exploitation trade-off](../../../../wiki/concepts/exploration-exploitation-trade-off.md), soft embedding, confidence gating
- **Methods**: SeLaR, [latent chain-of-thought](../../../../wiki/methods/latent-chain-of-thought.md), entropy gating, contrastive regularization, [chain of thought](../../../../wiki/methods/chain-of-thought.md)
- **Datasets**: _none recorded_

Tags: `latent reasoning`, `entropy gating`, `training-free`, `exploration`, `chain of thought`

## Abstract

Chain-of-Thought (CoT) has become a cornerstone of reasoning in large language models, yet its effectiveness is constrained by the limited expressiveness of discrete token sampling. Recent latent reasoning approaches attempt to alleviate this limitation by replacing discrete tokens with soft embeddings (probability-weighted mixtures of token embeddings) or hidden states, but they commonly suffer from two issues: (1) global activation injects perturbations into high-confidence steps, impairing reasoning stability; and (2) soft embeddings quickly collapse toward the highest-probability token, limiting exploration of alternative trajectories. To address these challenges, we propose SeLaR (Selective Latent Reasoning), a lightweight and training-free framework. SeLaR introduces an entropy-gated mechanism that activates soft embeddings only at low-confidence steps, while preserving discrete decoding at high-confidence steps. Additionally, we propose an entropy-aware contrastive regularization that pushes soft embeddings away from the highest-probability token’s direction, encouraging sustained exploration of multiple latent reasoning paths. Experiments on five reasoning benchmarks demonstrate that SeLaR consistently outperforms standard CoT and state-of-the-art training-free methods.

---

Record id: `doi:10.18653/v1/2026.acl-long.320`
