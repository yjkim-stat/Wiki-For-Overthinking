<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Scaling with Reflective Generative Model

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006997>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes a reasoning model (MetaStone-S1) whose policy and process-reward model share one backbone, and which exposes selectable low/medium/high reasoning-effort modes that trade off thinking length against test-time performance, matching OpenAI o3-mini on math benchmarks at 32B parameters.

## Problem

Effective test-time scaling for reasoning models typically requires a separately trained process reward model with costly step-level annotations; the paper seeks a way to get process-level supervision and controllable reasoning length without that cost.

## Contributions

- Introduces SPRM (self-supervised process reward model), which shares a backbone network with the policy model and adds task-specific heads for next-token prediction and process scoring, unifying policy and PRM without process-level annotation and reducing PRM parameters by over 99%
- Provides three reasoning-effort modes (low, medium, high) based on controllable thinking length for test-time scaling
- Empirically establishes a scaling law relating total thinking computation to test-time-scaling performance
- Releases MetaStone-S1 (32B parameters), reported to match OpenAI o3-mini-series performance, open-sourced

## Method

Builds a Reflective Generative Model in which the policy model and a process reward model share one backbone network, with separate lightweight task-specific heads for next-token prediction and process scoring (the self-supervised process reward model, SPRM), trained without explicit process-level annotations by deriving process scores from the outcome reward. This unified model supports test-time scaling by offering three selectable reasoning-effort modes (low/medium/high) that control how long the model thinks, and the authors measure how test-time performance scales with total thinking computation.

## Results

MetaStone-S1 (32B parameters) is reported to achieve performance comparable to OpenAI o3-mini's series; on AIME24 it is reported at 84.2% versus 79.6% for o3-mini. SPRM adds roughly 50M extra parameters versus a full process reward model, a reduction of over 99% in PRM parameter count.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Bears on the topic through its controllable reasoning-effort modes (low/medium/high) and an empirical scaling law tying total thinking computation to test-time performance, i.e. a concrete mechanism for choosing how long a model should think. However, the paper's core contribution is architectural (a shared-backbone policy/process-reward model reducing PRM parameter cost) rather than an analysis of when or why extended thinking stops helping — it treats more thinking compute as generally beneficial via its effort modes rather than studying overthinking/underthinking degradation directly.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), [process reward model](../../../../wiki/concepts/process-reward-model.md), self-supervised process reward model (SPRM), reasoning-effort modes, scaling law for thinking compute
- **Methods**: Reflective Generative Model (RGM), self-supervised process reward model (SPRM), MetaStone-S1
- **Datasets**: AIME24

Tags: `test-time-scaling`, `process-reward-model`, `reasoning-length`, `scaling-law`, `reasoning-effort-modes`

---

Record id: `title:5ff343d0a198bd25`
