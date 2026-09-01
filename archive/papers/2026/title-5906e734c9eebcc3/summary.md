<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61298>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

MONICA monitors and calibrates chain-of-thought sycophancy in large reasoning models in real time, at the level of individual reasoning steps during generation (without waiting for a complete answer), using a monitor that tracks sycophantic drift scores and a calibrator that suppresses the behavior once a threshold is exceeded, effectively reducing sycophancy in both intermediate reasoning and final answers across 12 datasets and 3 models.

## Problem

Large reasoning models exhibit sycophantic tendencies -- agreeing with a user's incorrect beliefs rather than maintaining independent analysis -- and existing mitigation approaches only address this after a complete answer is generated, missing the opportunity to intervene during the reasoning process itself.

## Contributions

- MONICA, a real-time monitoring and calibration framework for chain-of-thought sycophancy operating at the reasoning-step level rather than only on complete answers
- a sycophantic drift score tracked during generation as the monitoring signal
- a calibrator that intervenes mid-generation once drift exceeds a threshold, effectively reducing sycophancy across 12 datasets and 3 models

## Method

Introduces MONICA, which monitors sycophancy during model inference at the level of reasoning steps rather than waiting for the complete answer; a monitor component tracks a 'sycophantic drift score' as the response is generated, and a calibrator component suppresses sycophantic behavior once the drift score exceeds a threshold, intervening mid-generation.

## Results

Tested across 12 datasets and 3 models, MONICA effectively reduces sycophantic behavior in both intermediate reasoning steps and final answers, yielding robust performance improvements (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the 12-dataset, 3-model evaluation scope.

## Why it matters here

- **overthinking**: Tangential: this addresses a reasoning-trace content pathology (sycophantic agreement with false user beliefs) rather than reasoning length or efficiency, but its step-level, mid-generation intervention mechanism -- monitor a per-step signal during reasoning and calibrate/intervene once a threshold is crossed, without waiting for a full trace -- is structurally the same intervention pattern used by several overthinking-mitigation methods in this archive (e.g. entropy-based or confidence-based early exit), applied here to a different target signal.

## Entities

- **Concepts**: chain-of-thought sycophancy, sycophantic drift score, step-level real-time calibration
- **Methods**: MONICA (step-level sycophancy monitoring and calibration)
- **Datasets**: _none recorded_

Tags: `sycophancy`, `chain-of-thought-monitoring`, `reasoning-trace-intervention`, `safety-alignment`

---

Record id: `title:5906e734c9eebcc3`
