<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test Time Scaling for Neural Processes

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119684>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

TTSNPs refines Neural Process latent-variable samples at test time with a Sequential Monte Carlo sampler to improve prediction accuracy and uncertainty calibration.

## Problem

Variational posteriors for the global latent variable in Neural Processes are often miscalibrated, which limits both predictive accuracy and the reliability of uncertainty estimates under limited supervision.

## Contributions

- TTSNPs: a test-time sequential inference framework for Neural Processes based on a Sequential Monte Carlo Sampler
- Refines variational latent samples toward the true posterior at test time without retraining the pretrained model
- Improves both predictive accuracy and uncertainty calibration of Neural Process models

## Method

TTSNPs uses a Sequential Monte Carlo Sampler (SMCS) to iteratively transform variational latent samples of a pretrained Neural Process into better approximations of the true posterior, via learned neural transition kernels, applied only at test time and without modifying the pretrained model.

## Results

Reported to significantly improve both prediction quality and uncertainty calibration relative to the base Neural Process; no specific numeric benchmark results are given in the abstract.

## Limitations

Abstract gives no specific numeric results, benchmarks or dataset names, and no discussion of added test-time inference cost from the SMC sampling steps.

## Why it matters here

- **overthinking**: Tangential. 'Test time scaling' here means refining a Neural Process's latent-variable posterior via Sequential Monte Carlo at inference time for better-calibrated uncertainty estimates in meta-learning; it has no connection to large language model reasoning length, chain-of-thought length, or the accuracy/efficiency tradeoff of LLM test-time compute. It matched only on the generic phrase 'test time scaling.'

## Entities

- **Concepts**: uncertainty calibration, meta-learning, sequential Monte Carlo sampling, Neural Processes
- **Methods**: Sequential Monte Carlo Sampler (SMCS), Neural Processes, neural transition kernels
- **Datasets**: _none recorded_

Tags: `neural-processes`, `uncertainty-calibration`, `meta-learning`, `sequential-monte-carlo`

## Abstract

Abstract Uncertainty-aware meta-learning aims not only for rapid adaptation to new tasks but also for reliable uncertainty estimation under limited supervision. Neural Processes (NPs) offer a flexible solution by learning implicit stochastic processes directly from data, often using a global latent variable to capture functional uncertainty. However, we empirically find that variational posteriors for this global latent variable are frequently miscalibrated, limiting both predictive accuracy and the reliability of uncertainty estimates. To address this issue, we propose Test Time Scaling for Neural Processes (TTSNPs), a sequential inference framework based on Sequential Monte Carlo Sampler (SMCS) that refines latent samples at test time without modifying the pre-trained NP model. TTSNPs iteratively transform variational samples into better approximations of the true posterior using neural transition kernels, significantly improving both prediction quality and uncertainty calibration. This makes NPs more robust and trustworthy, extending applicability to various scenarios requiring well-calibrated uncertainty estimates.

---

Record id: `title:9fd93d64582daf6f`
