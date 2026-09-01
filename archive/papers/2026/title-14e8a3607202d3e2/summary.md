<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rethinking Calibration for Early-Exit Neural Networks

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62138>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Challenges the assumption that better-calibrated intermediate classifiers automatically improve early-exit neural networks, and introduces Early-Exit Failure Prediction (EEFP), an evaluation criterion weighing both prediction correctness and computational cost, plus a lightweight EEFP-motivated training procedure that directly replaces calibration and achieves superior cost-accuracy trade-offs.

## Problem

Early-exit neural networks (EENNs) stop computation once an intermediate classifier's prediction is confident enough, and prior work assumes improving classifier calibration automatically improves overall EENN performance, but this assumption has not been rigorously examined and calibration may not actually be the right target for improving cost-accuracy trade-offs.

## Contributions

- a critique of the assumption that improved calibration automatically improves early-exit neural network performance
- Early-Exit Failure Prediction (EEFP), an evaluation criterion jointly weighing prediction correctness and computational cost
- a lightweight EEFP-motivated intermediate-classifier training procedure that directly replaces calibration and achieves better cost-accuracy trade-offs

## Method

Introduces Early-Exit Failure Prediction (EEFP), an evaluation criterion that jointly considers prediction correctness and the computational cost incurred, rather than calibration alone, to more accurately reflect overall EENN performance; develops a lightweight training procedure motivated by EEFP to improve the intermediate classifiers, designed to directly replace standard calibration methods in EENNs.

## Results

The EEFP-motivated procedure achieves superior cost-accuracy trade-offs compared to traditional calibration approaches, and EEFP as an evaluation metric more accurately reflects overall EENN system performance than calibration-based evaluation.

## Limitations

Not stated in the fetched abstract beyond the general EENN evaluation setting.

## Why it matters here

- **overthinking**: Off-topic domain: this is a general early-exit deep neural network calibration/evaluation methodology paper (classification-style EENNs), not about LLM reasoning-trace length; matched to the topic only via the shared term 'early exit', though its core critique -- that calibration alone is the wrong target and cost-aware evaluation matters more -- is a transferable caution for any confidence-based early-exit method proposed for LLM reasoning.

## Entities

- **Concepts**: Early-Exit Failure Prediction (EEFP), calibration vs. cost-aware evaluation for early-exit networks
- **Methods**: Early-Exit Failure Prediction (EEFP), standard calibration methods (baseline, critiqued)
- **Datasets**: _none recorded_

Tags: `early-exit`, `calibration`, `cost-accuracy-tradeoff`, `adaptive-inference`

---

Record id: `title:14e8a3607202d3e2`
