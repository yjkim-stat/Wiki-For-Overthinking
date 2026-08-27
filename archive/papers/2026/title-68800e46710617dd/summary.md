<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimal Aggregation of LLM and PRM Signals for Efficient Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006667>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Derives and calibrates an optimal weighted combination of LLM self-consistency and PRM signals for selecting responses at test time, cutting compute needed for comparable accuracy.

## Problem

How to best combine signals from an LLM and a process reward model (PRM) when selecting a final answer during test-time scaling is unclear, and naive PRM-based selection can be outperformed by simple majority voting that ignores the PRM entirely.

## Contributions

- A theoretical framework for optimal weighted aggregation of LLM (e.g. self-consistency) and PRM signals for test-time response selection
- Finding that optimal weighting functions differ significantly across LLM-PRM pairs and frequently include negative weights
- A pre-computation method to calibrate the weighting function before inference

## Method

The paper observes that simple majority voting, which ignores PRM signals, occasionally outperforms standard PRM-based selection. It derives a theoretical framework showing that the optimal way to select a response at test time is a weighted aggregation of the LLM's own signal (e.g. self-consistency) and the PRM's signal, rather than relying on either alone. The optimal weighting function is shown to vary by LLM-PRM pair and can include negative weights; it is calibrated via a pre-computation step before inference rather than learned online.

## Results

Testing across multiple models shows the calibrated aggregation method achieves comparable accuracy to standard test-time scaling approaches while reducing the computational requirement to approximately 21% of the standard approach's cost.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Addresses how to spend a fixed test-time compute budget efficiently: the paper's calibrated aggregation of LLM and PRM signals reaches comparable accuracy to standard test-time scaling approaches at roughly 21% of the compute, directly bearing on the accuracy/efficiency tradeoff of test-time compute.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), process reward model (PRM) signals, weighted signal aggregation
- **Methods**: weighted aggregation of LLM and PRM signals, process reward model (PRM) scoring, [self-consistency / majority voting](../../../../wiki/methods/self-consistency-majority-voting.md)
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `prm`, `aggregation`, `efficiency`, `response-selection`

---

Record id: `title:68800e46710617dd`
