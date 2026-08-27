<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Resolving Discrepancies in Compute-Optimal Scaling of Language Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/96646>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Explains the discrepancy between the Kaplan and Chinchilla compute-optimal scaling laws by identifying and correcting three confounds (last-layer compute cost, warmup duration, scale-dependent optimizer tuning), after which the Kaplan-style reproduction matches the Chinchilla law.

## Problem

The Kaplan et al. and Hoffmann et al. (Chinchilla) scaling laws for compute-optimal model size give substantially different predictions, and it was unclear which was right or why they disagreed.

## Contributions

- identification of three specific confounds explaining the Kaplan/Chinchilla scaling-law discrepancy
- a reproduction showing the corrected Kaplan-style law matches the Chinchilla law
- derived scaling laws for optimal learning rate and batch size, including an AdamW beta2 tuning finding

## Method

Reproduces the Kaplan scaling law on two datasets (OpenWebText2, RefinedWeb) and isolates three factors causing the discrepancy with Chinchilla: last-layer computational cost accounting, warmup duration, and scale-dependent optimizer tuning; also derives scaling laws for the optimal learning rate and batch size.

## Results

After correcting for the three identified factors, the reproduced Kaplan-style scaling law agrees closely with the Chinchilla scaling law; contrary to a hypothesis in Hoffmann et al., careful learning-rate decay is found not to be essential for the Chinchilla law's validity; tuning the AdamW beta2 parameter is found essential at lower batch sizes.

## Limitations

Not stated in the fetched abstract beyond the two pretraining datasets and the AdamW-optimizer setting studied.

## Why it matters here

- **overthinking**: Not relevant beyond the shared keyword 'compute-optimal': this reconciles pretraining-compute scaling laws (model size vs. training compute), unconnected to inference-time reasoning length or test-time compute for reasoning.

## Entities

- **Concepts**: compute-optimal scaling law, Kaplan vs. Chinchilla scaling-law discrepancy, optimizer-tuning confounds in scaling studies
- **Methods**: [scaling-law fitting](../../../../wiki/methods/scaling-law-fitting.md), AdamW optimizer tuning analysis
- **Datasets**: OpenWebText2, RefinedWeb

Tags: `scaling-laws`, `compute-optimal`, `pretraining`, `optimizer-tuning`

## Abstract

Abstract Kaplan et al. and Hoffmann et al. developed influential scaling laws for the optimal model size as a function of the compute budget, but these laws yield substantially different predictions. We explain the discrepancy by reproducing the Kaplan scaling law on two datasets (OpenWebText2 and RefinedWeb) and identifying three factors causing the difference: last layer computational cost, warmup duration, and scale-dependent optimizer tuning. With these factors corrected, we obtain excellent agreement with the Hoffmann et al. (i.e., "Chinchilla") scaling law. Counter to a hypothesis of Hoffmann et al., we find that careful learning rate decay is not essential for the validity of their scaling law. As a secondary result, we derive scaling laws for the optimal learning rate and batch size, finding that tuning the AdamW $\beta_2$ parameter is essential at lower batch sizes.

---

Record id: `title:d494aac6d49ec910`
