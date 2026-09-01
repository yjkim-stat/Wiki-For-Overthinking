<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Conformal Prediction for Early Stopping in Mixed Integer Optimization

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61715>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains a neural network to estimate a mixed-integer-optimization solver's true optimality gap from its internal state, then applies conformal prediction calibration to derive stopping thresholds with rigorous probabilistic guarantees, cutting solve times by over 60% while keeping solutions within 0.1% of optimal with 95% probability across six Distributional MIPLIB problem families.

## Problem

Mixed-integer optimization solvers frequently find the optimal (or near-optimal) solution early but then spend the majority of their computation time proving optimality, and there is no principled way to decide when to stop early with a rigorous guarantee on solution quality.

## Contributions

- a neural network trained to estimate a MIP solver's true optimality gap from its internal state
- a conformal-prediction calibration procedure converting gap estimates into early-stopping thresholds with rigorous probabilistic guarantees
- over 60% solve-time reduction while keeping solutions within 0.1% of optimal at 95% probability across six problem families

## Method

Trains a neural network to estimate the true optimality gap from the solver's internal state at any point during solving, then applies conformal prediction calibration to the network's gap estimates to derive early-stopping thresholds that carry rigorous, distribution-free probabilistic guarantees on solution quality.

## Results

Across six problem families from the Distributional MIPLIB library, the method reduces solve times by over 60% while maintaining solutions within 0.1% of optimal with 95% probability for new instances drawn from matching distributions.

## Limitations

Not stated in the fetched abstract beyond the requirement that new instances be drawn from a distribution matching the calibration data (a standard conformal-prediction assumption).

## Why it matters here

- **overthinking**: Off-topic domain: this is an early-stopping method for classical mixed-integer optimization solvers, not LLM reasoning; matched to the topic only via the shared concept of 'early stopping', though the underlying pattern -- estimate remaining-work/confidence from internal state, then stop once a calibrated threshold is crossed -- is structurally similar to confidence-based early-exit methods proposed for LLM reasoning traces.

## Entities

- **Concepts**: conformal prediction for early stopping, optimality-gap estimation from solver state, distribution-free probabilistic stopping guarantee
- **Methods**: [conformal prediction](../../../../wiki/methods/conformal-prediction.md), neural-network-based optimality-gap estimation, early stopping
- **Datasets**: Distributional MIPLIB (six problem families)

Tags: `early-stopping`, `mixed-integer-optimization`, `conformal-prediction`, `solver-efficiency`

---

Record id: `title:878a7bd3c031c8b1`
