<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011693>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces Intervened Preference Optimization (IPO), which trains large reasoning models to detect a small number of critical 'safety trigger' points in a reasoning chain and correct course from them, cutting harmfulness by over 30% versus alternatives without sacrificing reasoning performance.

## Problem

Large reasoning models' chain-of-thought often contains harmful intermediate content even when the final answer looks acceptable, and naive process-level safety rewards fail because reasoning trajectories vary too little and give weak training signal.

## Contributions

- identification that reasoning-chain safety hinges on a small number of critical safety-trigger points
- Intervened Preference Optimization (IPO), constructing training pairs from targeted corrections at those triggers
- a >30% reduction in harmfulness versus alternatives on jailbreak/adversarial benchmarks with preserved reasoning performance

## Method

Identifies that a small number of 'safety triggers' (warning signs predicting problematic continuations) drive most reasoning-chain safety outcomes and that targeted corrections at those points redirect unsafe chains toward safe outcomes; proposes Intervened Preference Optimization (IPO), which substitutes problematic reasoning steps with safety-trigger-based corrections to construct training pairs with a stronger training signal than naive process supervision.

## Results

On jailbreak and adversarial benchmarks, IPO decreases harmfulness by more than 30% relative to alternative methods while maintaining strong reasoning performance across diverse tasks (aggregate figures only, per the fetched abstract).

## Limitations

Not stated in the fetched abstract; no per-benchmark breakdown or discussion of when the small-number-of-triggers assumption might fail.

## Why it matters here

- **overthinking**: Tangential: concerned with the safety content of a reasoning chain rather than its length or the accuracy/efficiency tradeoff, but its finding that a small number of localized intervention points can redirect an entire reasoning trajectory is structurally similar to claims in the overthinking literature that reasoning traces have a few decisive turning points rather than uniformly useful steps.

## Entities

- **Concepts**: safety trigger (reasoning-chain warning sign), process-level safety supervision, Intervened Preference Optimization
- **Methods**: Intervened Preference Optimization (IPO), process-level reward supervision
- **Datasets**: _none recorded_

Tags: `safety-alignment`, `chain-of-thought`, `large-reasoning-models`, `preference-optimization`

---

Record id: `title:3b1dfa6d6e5e2443`
