<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ROC-n-reroll: How verifier imperfection affects test-time scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011656>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proves that verifier ROC-curve geometry determines the accuracy of Best-of-N and Rejection Sampling under a fixed compute budget, and shows RS beats BoN at fixed compute while both converge in the infinite-compute limit.

## Problem

There is little theoretical understanding of how an imperfect verifier affects the performance of verifier-based test-time scaling methods like Best-of-N and Rejection Sampling.

## Contributions

- Proves that the instance-level accuracy of Best-of-N (BoN) and Rejection Sampling (RS) is precisely characterized by the geometry of the verifier's ROC curve
- Shows RS outperforms BoN for fixed compute, while both converge to the same accuracy in the infinite-compute limit
- Shows it is generally impossible to predict high-compute performance of either method from low-compute observations

## Method

The paper develops a theoretical characterization of how an imperfect verifier's quality, expressed via its ROC curve geometry, determines the instance-level accuracy achievable by Best-of-N and Rejection Sampling at a given compute budget. The theory is tested empirically with Qwen and LLaMA models on GSM8K and MATH500.

## Results

Confirmed with Qwen and LLaMA models on GSM8K and MATH500: Rejection Sampling outperforms Best-of-N under a fixed compute budget, both converge to the same accuracy as compute goes to infinity, and high-compute performance of either method is generally not predictable from observations made in the low-compute regime.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Provides a theoretical account of when spending more test-time compute on verifier-guided sampling (BoN/RS) actually helps: it shows accuracy gains from added compute are bounded by verifier ROC geometry, that the two methods converge at high compute, and that high-compute performance cannot be extrapolated from low-compute runs -- directly informing the accuracy/efficiency tradeoff of test-time scaling.

## Entities

- **Concepts**: verifier ROC geometry, Best-of-N sampling, rejection sampling, test-time scaling under imperfect verifiers
- **Methods**: Best-of-N (BoN), Rejection Sampling (RS)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500

Tags: `test-time-scaling`, `verifier`, `roc-curve`, `best-of-n`, `rejection-sampling`

## Abstract

Abstract Test-time scaling aims to improve language model performance by leveraging additional compute during inference. Many works have empirically studied techniques such as Best-of-N (BoN) and Rejection Sampling (RS) that make use of a verifier to enable test-time scaling. However, to date there is little theoretical understanding of how verifier imperfection affects performance — a gap we address in this work. Specifically, we prove that the instance-level accuracy of these methods is precisely characterized by the geometry of the verifier’s ROC curve. Our theory has two important takeaways, confirmed by experiments with Qwen and LLama models on GSM8K and MATH500. First, RS outperforms BoN for fixed compute, while both methods converge to the same accuracy in the infinite-compute limit. Second, it is generally impossible to predict the high-compute performance of either method based on observations in the low-compute regime.

---

Record id: `title:6b3727a0a0ac9a23`
