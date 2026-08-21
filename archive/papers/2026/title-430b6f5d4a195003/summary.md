<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# WAVE: Window-Aware Vocabulary-Efficient Early-Exit for Training-Free LLM Acceleration

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62373>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A training-free early-exit scheme for autoregressive decoding that restricts exit checks to a calibrated window of layers and evaluates them against a reduced-vocabulary proxy LM head, giving up to 1.4x speedup on Llama-2 7B.

## Problem

Every generated token costs a full forward pass through all layers. Early exit at an intermediate layer should help, but the three existing families each fail: confidence-based exits must run the full LM head at every candidate layer, and that overhead can cancel the saving; schedule-based exits avoid the head cost but their monotonically decreasing layer allocation collapses toward shallow layers, which constrains maximum generation length; and learned exit predictors need task-specific training and break under distribution shift.

## Contributions

- Exit window scheduling: an offline-calibrated layer range for early-exit decisions, avoiding both per-layer checking and the shallow-layer collapse of fixed schedules
- A proxy LM head over a reduced vocabulary subset at the window's starting layer, cutting per-layer exit overhead by 87%
- A training-free early-exit framework needing only a brief calibration phase
- Reported 1.4x average speedup on Llama-2 7B, compatible with W4A16 quantization

## Method

Two components, neither requiring gradient training. First, exit window scheduling: an offline calibration pass identifies a layer range within which exit decisions are worth making, so checks are confined to that window instead of every layer -- this both cuts the number of checks and stops the schedule from collapsing to shallow layers. Second, a proxy LM head built at the window's starting layer over a lightweight subset of the vocabulary rather than the full one, so each exit check is cheap; the paper reports 87% less per-layer exit overhead than evaluating the full LM head. Deployment needs only the brief calibration phase.

## Results

Experiments on Llama-2 7B: up to 1.4x average speedup while preserving output quality, and full compatibility with W4A16 quantization. Per-layer exit overhead is reduced by 87% relative to the full LM head. The material available gives no per-benchmark accuracy table, no baseline-by-baseline speedup comparison, and no results on any model other than Llama-2 7B.

## Limitations

Not stated in the material available; no PDF or preprint could be located, so this record rests on the conference abstract and the paper's own listing. What a reader should notice: the evaluation is a single 7B model of a previous generation, so nothing here speaks to reasoning models or to long-output workloads; 'preserving output quality' is asserted without numbers in the abstract; and the exit window depends on offline calibration, which reintroduces in weaker form the distribution-shift exposure the paper criticises in learned predictors -- a window calibrated on one workload need not suit another.

## Why it matters here

- **overthinking**: Tangential, and on the same side as the KV-cache work already in the archive (AsyncSpade, BeaconKV, ThinKV): it reduces the cost of producing each token, and does not touch how many tokens get produced. 'Early exit' here means exiting the layer stack for one token, not exiting a reasoning trace -- the depth axis, not the length axis -- so despite the keyword it is not a stopping criterion in the sense the topic tracks. There is one point of contact worth noting because it is a caution rather than a contribution: the paper reports that schedule-based early exit collapses to shallow layers and thereby constrains maximum generation length, i.e. a per-token efficiency mechanism can silently truncate output. That is an interaction anyone stacking depth-wise acceleration on top of length control should know about. Evaluation is on Llama-2 7B with no reasoning-model results.

## Entities

- **Concepts**: early exit, vocabulary pruning, layer-wise confidence, training-free inference acceleration, offline calibration
- **Methods**: WAVE, exit window scheduling, proxy LM head, [early exit](../../../../wiki/methods/early-exit.md), W4A16 quantization
- **Datasets**: _none recorded_

Tags: `early-exit`, `inference-efficiency`, `training-free`, `vocabulary-pruning`, `decoding`, `tangential`

---

Record id: `title:430b6f5d4a195003`
