<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CaTS: Calibrated Test-Time Scaling for Efficient LLM Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10007848>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes CaTS, a calibrated test-time scaling framework that uses a self-distilled confidence signal to adaptively allocate sampling budget per query, including early stopping once the model is confident.

## Problem

Fixed-budget test-time scaling methods (Best-of-N, Self-Consistency) waste computation on easy queries and may underexplore hard ones because they sample the same number of responses regardless of query difficulty.

## Contributions

- Proposes Self-Calibration, distilling Self-Consistency-derived confidence into the model itself so it can produce reliable confidence estimates with little extra computation
- Proposes CaTS, a framework that adapts the amount of test-time computation (number of sampled responses) to per-query difficulty using the calibrated confidence
- Introduces a confidence-based Early Stopping variant that halts sampling once the model is sufficiently confident
- Provides a theoretical guarantee that CaTS-SC outperforms vanilla self-consistency

## Method

Standard test-time scaling methods such as Best-of-N and Self-Consistency sample a fixed number of responses per query regardless of difficulty. CaTS first trains the model via Self-Calibration to internalize confidence estimates that would otherwise require running full Self-Consistency, then uses these calibrated confidence scores at inference time to decide, per query, how many samples to draw or when to stop sampling early (confidence-based Early Stopping), so easy queries use fewer samples and hard queries use more.

## Results

Confidence-based Early Stopping applied to Best-of-N improves MathQA accuracy from 73.7 to 83.6 at a sample budget of 16 responses; evaluated across three LLMs and nine datasets; CaTS-SC is shown, with theoretical guarantees, to outperform vanilla self-consistency.

## Limitations

Details on computational overhead of the calibration step, failure cases, and models beyond the three tested were not available from the summarized source (poster/abstract page rather than full text).

## Why it matters here

- **overthinking**: Directly targets the topic's core question of when to stop test-time compute: it replaces fixed sampling budgets with confidence-calibrated early stopping, cutting wasted computation on easy queries while allocating more to hard ones, reported to raise MathQA accuracy from 73.7 to 83.6 at a 16-sample budget.

## Entities

- **Concepts**: confidence calibration, adaptive test-time compute, self-consistency, early stopping
- **Methods**: Self-Calibration, CaTS, CaTS-SC, [confidence-based early stopping](../../../../wiki/methods/confidence-based-early-stopping.md), [Best-of-N](../../../../wiki/methods/best-of-n.md), [Self-Consistency](../../../../wiki/methods/self-consistency.md)
- **Datasets**: MathQA, eight other datasets (nine total, not individually named in the summarized source)

Tags: `test-time-scaling`, `early-stopping`, `calibration`, `self-consistency`, `efficiency`

---

Record id: `title:03232c54fde9b57f`
