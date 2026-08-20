<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Robust Federated Learning Against Adaptive Compression

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61991>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes parameter-free federated learning algorithms (ParFreFL, ComParFreFL) that stay robust to biased, adaptive gradient compression while cutting communication cost.

## Problem

Federated learning needs communication-efficient optimization that does not require expert hyperparameter tuning and remains robust when clients use biased compressors whose compression ratio may vary or be unknown, under heterogeneous data and partial client participation.

## Contributions

- ParFreFL, a communication-efficient parameter-free federated learning algorithm that halves the communication requirements of PAdaMFed
- ComParFreFL, which adds momentum and error feedback to support biased gradient compression without needing to know the compression ratio in advance
- Convergence guarantees under arbitrary data heterogeneity, partial client participation, and linear speedup

## Method

The paper studies federated learning with communication compression: ParFreFL removes the need for manual learning-rate tuning while cutting communication cost relative to PAdaMFed, and ComParFreFL extends it with momentum and error-feedback so that clients can use biased gradient compressors of unknown or adaptively changing compression ratio while retaining convergence guarantees.

## Results

Claims ParFreFL halves the communication requirement of PAdaMFed while matching its automatic parameter-tuning behavior, and states ComParFreFL is the first algorithm in the compressed FL literature to achieve robustness independent of the compression ratio, with linear speedup under partial participation and heterogeneous data.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this is a federated-learning optimization paper about compressing gradient/parameter communication between clients and a server. It only shares the generic phrase 'adaptive compression' with the topic's keyword list; it says nothing about reasoning chains, large reasoning models, or the length/stopping of test-time inference.

## Entities

- **Concepts**: federated learning, gradient compression, parameter-free optimization, error feedback, biased compression
- **Methods**: ParFreFL, ComParFreFL, PAdaMFed (baseline)
- **Datasets**: _none recorded_

Tags: `federated-learning`, `gradient-compression`, `communication-efficiency`, `tangential`

---

Record id: `title:b6e7ba6c24dddb51`
