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

An early-exit neural architecture for single-channel speech separation and enhancement, paired with a probabilistic model of the clean signal and its error variance that turns a target signal-to-noise ratio into an exit condition.

## Problem

Deep single-channel speech separation architectures are designed with a fixed compute and parameter budget, so a trained model cannot scale to the compute available on a given device or to varying demand. That blocks deployment on embedded and heterogeneous hardware such as mobile phones and hearables, where the budget differs across devices and over time.

## Contributions

- A single-channel speech separation and enhancement architecture that supports exiting at intermediate depths
- A probabilistic framework that jointly models the clean speech signal and the error variance of the estimate
- Early-exit conditions expressed directly as a desired signal-to-noise ratio, derived from the modelled error variance
- Evidence that training on variable-length audio yields well-calibrated exit conditions and that early exit does not degrade reconstruction

## Method

The authors design a speech separation and enhancement network capable of exiting at intermediate depths, and wrap it in an uncertainty-aware probabilistic framework that jointly models the clean speech signal and the error variance of the current estimate. Because the framework predicts the variance of its own reconstruction error, an exit condition can be stated in terms of a desired signal-to-noise ratio rather than as an opaque confidence threshold: the network continues until the modelled error variance implies the requested SNR has been reached. Training on variable-length audio is what makes these conditions calibrated, so compute is scaled dynamically at test time per input.

## Results

_not recorded_

## Limitations

The abstract reports directions rather than numbers: it states that early-exit capability is introduced without compromising reconstruction, that the exit conditions are well calibrated when trained on variable-length audio, and that compute savings are considerable, but names no SNR figures, no MAC or latency measurements, no separation baselines and no datasets. Calibration is stated as conditional on variable-length training, which implies the conditions may not be calibrated under fixed-length training. No on-device measurement is reported for the embedded and hearable settings that motivate the work.

## Why it matters here

- **overthinking**: Not relevant to this topic. The match came from the keyword "early exit", which here means terminating a forward pass through a speech separation network at an intermediate layer, not stopping a language model's chain of thought. There is no language model, no reasoning trace, no token budget and no accuracy/reasoning-length tradeoff anywhere in the paper; the quantity being traded is layers of signal processing against reconstruction SNR on audio. The only shared structure is the abstract shape of the question -- deciding at run time when further computation stops paying -- and the fact that the stopping rule is derived from a calibrated uncertainty estimate rather than a fixed budget. That is a loose analogy at the level of framing, not a result the group can carry over: nothing about SNR-thresholded layer exit transfers to when a reasoning model should stop generating. File as a false positive of the keyword filter.

## Entities

- **Concepts**: Early Exit, Predictive Uncertainty, Calibration, Dynamic Compute Allocation, Anytime Inference
- **Methods**: early-exit neural networks, probabilistic / uncertainty-aware signal modelling, joint modelling of signal and error variance, SNR-based exit conditions, dynamic test-time compute scaling
- **Datasets**: _none recorded_

Tags: `early exit`, `speech separation`, `speech enhancement`, `uncertainty`, `calibration`, `on-device`, `signal processing`, `off-topic`, `iclr-2026`

---

Record id: `title:8342bedc3c993484`
