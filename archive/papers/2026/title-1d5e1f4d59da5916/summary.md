<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010752>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Benchmarks model-based, training-based and N-gram-based speculative decoding methods as ways to accelerate token generation during LLM test-time scaling (Best-of-N, iterative reasoning), finding N-gram methods best exploit repetitive patterns.

## Problem

Test-time scaling methods (e.g. Best-of-N, iterative reasoning) improve LLM performance but generate many tokens, and it is unclear which speculative decoding approach best accelerates this generation without a dedicated evaluation.

## Contributions

- Presents what is described as the first comprehensive evaluation framework for speculative decoding methods specifically within LLM test-time scaling
- Benchmarks three categories of speculative decoding approaches (model-based, training-based, N-gram-based) across multiple test-time scaling paradigms including Best-of-N sampling and iterative reasoning
- Finds N-gram-based methods are particularly effective at exploiting repetitive patterns that arise during test-time scaling, and suggests combining N-gram with other methods to handle both repetitive and varied reasoning

## Method

Constructs a benchmark evaluating speculative decoding methods (model-based, training-based, N-gram-based drafting) as accelerators for LLM test-time scaling paradigms such as Best-of-N sampling and iterative reasoning, comparing their effectiveness at exploiting redundancy in generated tokens across these paradigms.

## Results

No specific numeric speedup or accuracy results were available from the accessible abstract beyond the qualitative finding that N-gram-based methods are particularly effective at exploiting repetitive patterns during test-time scaling.

## Limitations

No PDF was attached; the abstract does not give specific benchmark datasets, models, or numeric speedup figures, so these could not be extracted from the accessible source material.

## Why it matters here

- **overthinking**: This paper accelerates the token-by-token generation underlying existing test-time-scaling paradigms via speculative decoding; it does not address how much a model should reason, when it should stop, or the accuracy/efficiency tradeoff of reasoning length itself. It is an inference-speed benchmark orthogonal to length-calibration methods, connected to the topic only through the shared umbrella of 'test-time scaling' efficiency. Tangential.

## Entities

- **Concepts**: speculative decoding, [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), best-of-N sampling
- **Methods**: [speculative decoding](../../../../wiki/methods/speculative-decoding.md), N-gram drafting, [Best-of-N sampling](../../../../wiki/methods/best-of-n-sampling.md), iterative reasoning
- **Datasets**: _none recorded_

Tags: `speculative-decoding`, `test-time-scaling`, `inference-efficiency`, `benchmark`, `best-of-n`

---

Record id: `title:1d5e1f4d59da5916`
