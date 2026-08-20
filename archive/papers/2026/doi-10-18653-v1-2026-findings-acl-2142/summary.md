<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning

- **Authors**: Yansi Li, Gongshen Liu, Zhuosheng Zhang 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.2142>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.2142
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Finds diffusion language models are badly miscalibrated on math reasoning yet rank correct from incorrect far better than autoregressive baselines, because their confidence tracks structural consistency rather than correctness.

## Problem

Diffusion language models offer token-level probabilities under bidirectional context, unlike autoregressive generation, and the semantics of their native uncertainty estimates are underexplored — it is not known what a diffusion confidence value means.

## Contributions

- Identification of a calibration paradox inherent to bidirectional diffusion generation
- Evidence that diffusion confidence is structurally distinct from AR likelihood
- LLaDA-8B at 31.2% ECE yet 0.826 AUROC against 0.611 for comparable single-pass AR baselines
- The diagnosis that diffusion confidence proxies structural consistency rather than correctness probability
- Post-hoc calibration reducing ECE by over 60% while preserving the ranking signal

## Method

A calibration paradox inherent to bidirectional generation is identified and diagnosed. Diffusion confidence is shown to be structurally distinct from AR likelihood, and the diagnosis is that it behaves less like a probability of correctness and more like a proxy for structural consistency, enabled by the model's bidirectional access to the entire solution path. Separating calibration (ECE) from discrimination (AUROC) is what makes the paradox visible: the two properties come apart. Lightweight post-hoc calibration is then applied.

## Results

LLaDA-8B is highly miscalibrated on mathematical reasoning benchmarks at 31.2% ECE, yet has superior discriminative power at 0.826 AUROC, well above comparable AR baselines in single-pass settings at 0.611 AUROC. Lightweight post-hoc calibration reduces ECE by over 60% while preserving the ranking signal.

## Limitations

The main evidence is one model, LLaDA-8B, against unnamed comparable AR baselines. The structural-consistency account is a diagnosis offered to explain the paradox rather than an independently tested mechanism. AR comparison is restricted to single-pass settings, which excludes self-consistency methods that are the practical alternative. Benchmarks are not named.

## Why it matters here

- **reasoning-evaluation**: Separates two properties this archive has been treating as one. A confidence signal can be useless as a probability and excellent as a ranking — 31.2% ECE with 0.826 AUROC — which means every method here that gates on a confidence threshold and every method that selects by confidence ordering are relying on different things, and a miscalibrated model can be fine for the second. That distinction applies directly to the archive's confidence-based early-stopping and difficulty-allocation entries, several of which assume calibration they never check. The bidirectional explanation is also a warning about transferring AR-derived uncertainty intuitions to non-AR architectures.

## Entities

- **Concepts**: [calibration](../../../../wiki/concepts/calibration.md), discrimination, [uncertainty quantification](../../../../wiki/concepts/uncertainty-quantification.md), diffusion language model, bidirectional context, structural consistency, [expected calibration error](../../../../wiki/concepts/expected-calibration-error.md), [answer stabilization](../../../../wiki/concepts/answer-stabilization.md)
- **Methods**: post-hoc calibration, AUROC evaluation, expected calibration error, diffusion language modelling
- **Datasets**: _none recorded_

Tags: `calibration`, `diffusion language model`, `uncertainty`, `auroc`, `math reasoning`

## Abstract

Diffusion large language models (DLLMs) have emerged as a promising alternative to autoregressive (AR) generation, uniquely offering token-level probabilities under bidirectional context. However, the semantics of their native uncertainty estimates remain underexplored. In this work, we uncover a calibration paradox inherent to the bidirectional generation mechanism of state-of-the-art DLLMs. Concretely, we demonstrate that diffusion confidence is structurally distinct from AR likelihood. Notably, LLaDA-8B is highly miscalibrated (31.2% ECE) on mathematical reasoning benchmarks, yet possesses superior discriminative power (0.826 AUROC), significantly outperforming comparable AR baselines in single-pass settings (0.611 AUROC). We diagnose that this paradox arises because diffusion confidence functions less like a probability of correctness and more like a proxy for structural consistency enabled by the model’s bidirectional access to the entire solution path. We further show that lightweight post-hoc calibration can reconcile this gap, reducing ECE by over 60% while preserving the strong ranking signal. Our findings suggest that DLLMs offer a unique, cost-efficient uncertainty signal for reasoning tasks that complements expensive AR approaches.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2142`
