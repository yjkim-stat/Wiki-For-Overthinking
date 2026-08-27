<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009506>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes an uncertainty-aware probabilistic early-exit framework for speech separation/enhancement networks that lets inference stop once a desired signal-to-noise ratio is probabilistically achieved, saving compute without degrading reconstruction quality.

## Problem

Neural speech separation/enhancement networks apply a fixed amount of computation regardless of how easy or hard a given input is to separate, and no prior early-exit mechanism for this domain models the uncertainty of intermediate outputs to decide when to stop.

## Contributions

- an uncertainty-aware probabilistic early-exit framework for speech separation/enhancement
- probabilistic exit conditions calibrated to a target signal-to-noise ratio
- demonstration of compute savings with no reconstruction-quality degradation on variable-length audio

## Method

Combines a speech separation/enhancement network architecture capable of early-exit with an uncertainty-aware probabilistic framework that models both the clean speech signal and its error variance at each potential exit point, enabling probabilistic exit conditions targeting a desired signal-to-noise ratio.

## Results

Early-exit functionality is incorporated without degrading reconstruction quality; when trained on variable-length audio, the exit conditions are well calibrated and deliver considerable compute savings during dynamic test-time scaling while remaining interpretable (no specific numeric savings given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the domain (speech separation/enhancement networks).

## Why it matters here

- **overthinking**: Off-topic domain (speech separation, not LLM reasoning), matched only via the shared term 'early exit'; relevant only as a cross-domain example that uncertainty-calibrated early-exit conditions can save compute without quality loss, a pattern also explored for LLM reasoning-length control.

## Entities

- **Concepts**: probabilistic early exit, uncertainty-aware inference, signal-to-noise-ratio-targeted exit condition
- **Methods**: early-exit neural network, probabilistic uncertainty modeling
- **Datasets**: _none recorded_

Tags: `early-exit`, `speech-separation`, `adaptive-inference`, `uncertainty-quantification`

---

Record id: `title:8342bedc3c993484`
