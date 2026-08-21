<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Expressive Power of Implicit Models: Rich Equilibria and Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009635>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Provides a mathematical theory showing that implicit (weight-tied, fixed-point) models' expressive power grows with the number of test-time iterations, validated across imaging, scientific computing, operations research and LLM reasoning.

## Problem

It is empirically known that implicit models can match or exceed larger explicit networks by allocating more test-time compute, but why this happens was not theoretically understood.

## Contributions

- Non-parametric mathematical characterization showing a simple, regular implicit operator can progressively express more complex mappings through iteration
- Proves that for a broad class of implicit models, expressive power grows with test-time compute, ultimately matching a much richer function class
- Validates the theory across four domains: imaging, scientific computing, operations research, and LLM reasoning

## Method

Implicit models compute outputs by iterating a single parameter block to a fixed point, forming an infinite-depth, weight-tied network trained with constant memory. The paper gives a non-parametric analysis of expressive power, proving that iterating a simple, regular implicit operator progressively expresses more complex mappings, so that for a broad class of implicit models expressive power grows with the number of test-time iterations.

## Results

Across the four validation domains (imaging, scientific computing, operations research, LLM reasoning), the complexity of the learned mapping rises with more test-time iterations while solution quality simultaneously improves and stabilizes; no benchmark-specific numbers given in the abstract.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: A general expressive-power theory for implicit/equilibrium models under more test-time iterations; only one of four validation domains is LLM reasoning, and the paper does not address reasoning length or the stop/continue decision in large reasoning models. It shares the "test-time scaling" phrase but is tangential to this topic.

## Entities

- **Concepts**: implicit models, [fixed-point iteration](../../../../wiki/concepts/fixed-point-iteration.md), expressive power, weight-tied networks
- **Methods**: _none recorded_
- **Datasets**: _none recorded_

Tags: `implicit-models`, `theory`, `test-time-compute`, `equilibrium-models`, `tangential`

## Abstract

Abstract Implicit models, an emerging model class, compute outputs by iterating a single parameter block to a fixed point. This architecture realizes an infinite-depth, weight-tied network that trains with constant memory, significantly reducing memory needs for the same level of performance compared to explicit models. While it is empirically known that these compact models can often match or even exceed the accuracy of larger explicit networks by allocating more test-time compute, the underlying reasons are not yet well understood. We study this gap through a non-parametric analysis of expressive power. We provide a strict mathematical characterization, showing that a simple and regular implicit operator can, through iteration, progressively express more complex mappings. We prove that for a broad class of implicit models, this process allows the model's expressive power to grow with test-time compute, ultimately matching a much richer function class. The theory is validated across four domains: imaging, scientific computing, operations research, and LLM reasoning, demonstrating that as test-time iterations increase, the complexity of the learned mapping rises, while the solution quality simultaneously improves and stabilizes.

---

Record id: `title:acc0cd457f5fd230`
