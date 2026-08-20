<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Zero-Overhead Introspection for Adaptive Test-Time Compute

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010457>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces ZIP-RC, a zero-overhead method that reuses spare logits from the standard forward pass to let an LLM predict its own success likelihood and remaining reasoning length, and uses that to decide when to keep generating or resample.

## Problem

LLMs cannot introspect about how likely they are to succeed on a given partial reasoning attempt or how much more computation it will take, so test-time scaling methods spend compute inefficiently, unable to tell early which reasoning paths are worth continuing and which should be abandoned.

## Contributions

- Identifies that LLMs cannot introspect their own likelihood of success or the compute they still need, which leads to inefficient test-time scaling.
- Proposes ZIP-RC, a method that reuses reserved or otherwise unused logits in the same forward pass as next-token prediction to output a joint distribution over final reward and remaining generation length, at no additional inference cost.
- Uses this introspective signal to drive meta-actions (continue a given prefix or restart sampling) via a computed sampling utility metric, enabling adaptive test-time compute allocation.
- Reports about a 12% accuracy improvement over majority voting at equal or lower average cost on mixed-difficulty math benchmarks, and traces smooth Pareto frontiers between quality, compute and latency.

## Method

ZIP-RC repurposes reserved/unused logits already computed during the standard next-token forward pass to jointly predict, at each generation step, a distribution over the eventual final reward and the remaining length needed to reach an answer. This is obtained without any extra model, architecture change, or additional inference cost ('zero-overhead'). The predicted joint distribution is turned into a sampling utility metric that decides, for each partial reasoning trace, whether to keep extending it or abandon it and resample, enabling adaptive allocation of test-time compute across candidate reasoning paths.

## Results

On mixed-difficulty mathematical benchmarks, ZIP-RC achieves approximately 12% higher accuracy than majority voting at equal or lower average compute cost, and produces smooth Pareto frontiers trading off quality, compute and latency.

## Limitations

Specific benchmark names, model sizes and the exact definition of the sampling utility metric are not given in the available material (poster page summary only, no PDF); the general applicability of 'reserved or unused logits' across different model architectures is not addressed in what was retrieved.

## Why it matters here

- **overthinking**: This paper directly targets the stopping-criterion side of the topic: it gives the model a way to predict, mid-reasoning and at no extra cost, whether a given reasoning trace is likely to succeed and how much length remains, and uses that prediction to decide whether to keep going or restart, which is precisely a mechanism for making a model stop or continue at the right point.

## Entities

- **Concepts**: meta-cognition in LLMs, zero-overhead introspection, sampling utility, Pareto frontier between quality, compute and latency
- **Methods**: ZIP-RC, logit reuse for introspection, sampling utility-based meta-actions
- **Datasets**: mixed-difficulty mathematical benchmarks

Tags: `test-time-compute`, `introspection`, `adaptive-inference`, `sampling-efficiency`, `meta-cognition`

---

Record id: `title:254cc4493a1c8659`
