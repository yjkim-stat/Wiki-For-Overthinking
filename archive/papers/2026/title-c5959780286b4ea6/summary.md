<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008968>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces the Reasoning Score, a metric based on divergence between logits from late-layer projections onto the vocabulary space, to detect 'Reasoning Hallucination' -- logically coherent but factually wrong reasoning chains -- and pairs it with GRPO-R, an RL method using step-level deep-reasoning rewards to reduce it.

## Problem

Large reasoning models produce a distinct failure mode, 'Reasoning Hallucination,' where logically sound but factually flawed reasoning chains yield convincing wrong answers; because the errors are embedded in otherwise-coherent multi-step reasoning, they are harder to detect than typical hallucinations and can cause more harm.

## Contributions

- the Reasoning Score, a mechanistic metric for reasoning depth from late-layer logit divergence
- ReTruthQA, a dataset supporting analysis of Reasoning Hallucination patterns, and the RHD detection framework
- GRPO-R, an RL method with step-level deep-reasoning rewards that reduces hallucination while improving reasoning quality

## Method

Introduces the Reasoning Score, which evaluates reasoning depth by measuring divergence between logits when projecting late network layers onto vocabulary space, separating surface-level pattern matching from genuine deep reasoning; builds the ReTruthQA dataset and the RHD detection framework from analysis of two hallucination patterns (early fluctuations in reasoning depth, and problematic backtracking to prior flawed steps); proposes GRPO-R, an RL method adding step-level deep-reasoning rewards via potential-based shaping.

## Results

Analysis of ReTruthQA identifies two central Reasoning Hallucination patterns (early depth fluctuation, backtracking to flawed steps); the RHD framework achieves leading-edge detection results across domains; GRPO-R strengthens theoretical generalization guarantees while improving reasoning quality and reducing hallucinations (aggregate claims; no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the ReTruthQA dataset scope.

## Why it matters here

- **overthinking**: Directly relevant to reasoning-trace pathology: 'Reasoning Hallucination' (coherent-but-wrong reasoning) and its two failure patterns -- early fluctuation in reasoning depth and backtracking to already-flawed steps -- describe exactly the kind of unproductive or misleading trace structure the overthinking literature is concerned with measuring and mitigating, from a mechanistic-interpretability angle rather than a token-budget angle.

## Entities

- **Concepts**: [Reasoning Hallucination](../../../../wiki/concepts/reasoning-hallucination.md), Reasoning Score (logit-divergence reasoning-depth metric), step-level deep-reasoning reward shaping
- **Methods**: mechanistic logit-divergence analysis, GRPO-R (potential-based step-level reward shaping)
- **Datasets**: ReTruthQA (new)

Tags: `hallucination`, `mechanistic-interpretability`, `large-reasoning-models`, `reinforcement-learning`

---

Record id: `title:c5959780286b4ea6`
