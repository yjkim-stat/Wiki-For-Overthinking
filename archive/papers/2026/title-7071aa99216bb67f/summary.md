<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Wait, Do We Need to Wait? Revisiting Budget Forcing for Sequential Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10012115>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Revisits budget forcing -- forcing a reasoning model to keep thinking or to stop via a keyword like 'Wait' -- and empirically tests how well it generalizes across model families, non-reasoning models, and alternative keywords.

## Problem

It is unclear how well budget forcing, a technique for controlling a reasoning model's thinking budget at inference time, generalizes across model families, whether it works on non-reasoning models, and whether keywords other than 'Wait' can perform the same function.

## Contributions

- Empirically tests how well budget forcing generalizes across different model families and settings
- Tests whether budget forcing works with non-reasoning models
- Tests whether keywords other than 'Wait' can serve the same function
- Reports concrete cases where budget forcing does and does not help, with practical guidance for applying it

## Method

The paper revisits budget forcing, a sequential test-time scaling technique that controls a reasoning model's inference-time reasoning budget by appending a 'Wait' keyword to force continued reasoning, or by forcing a stop once a token budget is exceeded to force an answer. It runs experiments varying model family, model type (reasoning vs. non-reasoning), and the forcing keyword itself to determine when and where the technique is effective.

## Results

The paper reports experimental cases where budget forcing does and does not help across different model families and settings, and evaluates non-reasoning models and alternative forcing keywords, offering practical guidance rather than a single headline benchmark number.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly on-topic: it studies the mechanism used to make a reasoning model keep going or stop at the right point during inference (budget forcing via 'Wait' or a forced stop), including model families and settings where the technique fails to generalize.

## Entities

- **Concepts**: budget forcing, [sequential test-time scaling](../../../../wiki/concepts/sequential-test-time-scaling.md), stopping-keyword control
- **Methods**: [budget forcing](../../../../wiki/methods/budget-forcing.md), sequential test-time scaling
- **Datasets**: _none recorded_

Tags: `budget-forcing`, `test-time-scaling`, `reasoning-length`, `stopping-criterion`

## Abstract

Abstract In this blog post, we revisit the technique of budget forcing — a sequential test-time scaling technique that controls reasoning budget in reasoning models by appending a "Wait" keyword (or equivalently forcing a stop when the budget is exceeded), thereby determining whether the model continues thinking or directly outputs an answer. We explore three main questions: 1. To what extent does budget-forcing generalize across different model families and settings? 2. Does it work with non-reasoning models? 3. Can other keywords serve the same function as "Wait"? We present experimental results, including cases where budget forcing does and does not help and offer practical guidance for applying budget-forcing in test-time scaling.

---

Record id: `title:7071aa99216bb67f`
