<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Better, Faster: Harnessing Self-Improvement in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64514>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces HSIR, a self-improvement RL framework for large reasoning models that samples hard problems more efficiently and rewards concise, non-redundant reasoning via an overthinking-aware diversity score.

## Problem

Self-improvement training for large reasoning models is limited by low diversity in generated training data (most sampled solutions are for easy problems while hard-problem solutions are rare) and by redundant, overthinking-prone reasoning patterns in the generated solutions.

## Contributions

- Verify-then-exit sampling strategy for efficiently collecting accurate solutions to difficult queries
- Intrinsic Diversity score that quantifies overthinking to filter out redundant solutions from self-improvement training data
- H-GRPO, a GRPO variant that adds the diversity metric as an RL reward to promote concise and diverse reasoning

## Method

HSIR is a self-improvement training framework for large reasoning models. It combines a verify-then-exit sampling strategy that collects more accurate solutions for difficult queries more efficiently, with an Intrinsic Diversity score that measures overthinking and is used to eliminate undesired, redundant solutions from the training pool. H-GRPO extends GRPO by incorporating this diversity metric directly as a reinforcement-learning reward, pushing the model toward concise and diverse reasoning.

## Results

Up to +10.9% average performance gain in reasoning accuracy and up to 42.4% reduction in inference overhead, reported across seven models and five tasks.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly targets overthinking: defines an Intrinsic Diversity score to detect and filter redundant reasoning traces during self-improvement training, and trains with H-GRPO, a GRPO variant that rewards concise reasoning, reducing inference overhead by up to 42.4% while improving accuracy by up to 10.9%.

## Entities

- **Concepts**: self-improvement training, overthinking measured as solution diversity, GRPO reward shaping for conciseness
- **Methods**: HSIR, H-GRPO, verify-then-exit sampling, Intrinsic Diversity score
- **Datasets**: _none recorded_

Tags: `overthinking`, `self-improvement`, `reinforcement-learning`, `grpo`, `reasoning-efficiency`

---

Record id: `title:da23463210717567`
