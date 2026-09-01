<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008335>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

QuRL accelerates RL training for LLM reasoning by using a quantized (INT8/FP8) actor for the rollout phase -- which consumes up to 70% of total RL training time -- introducing Adaptive Clipping Range to prevent instability from the full-precision/quantized-actor mismatch and an invariant scaling technique for small inter-step weight updates, achieving 20-80% faster rollout on DeepScaleR and DAPO.

## Problem

The rollout (generation) phase is the dominant efficiency bottleneck in RL training for LLM reasoning, consuming up to 70% of total training time, and naively quantizing the actor model to speed up rollout risks training instability from the precision mismatch between the full-precision policy being updated and the quantized actor generating rollouts.

## Contributions

- identification of RL rollout as consuming up to 70% of total training time, motivating actor quantization as a targeted efficiency lever
- Adaptive Clipping Range (ACR), dynamically adjusting clipping between full-precision and quantized actors to preserve training stability
- an invariant scaling technique addressing the small-weight-update problem under quantization, achieving 20-80% rollout speedup on DeepScaleR and DAPO

## Method

Uses a quantized actor (INT8 or FP8) to accelerate the RL rollout phase; introduces Adaptive Clipping Range (ACR), which dynamically adjusts the policy-gradient clipping ratio between the full-precision and quantized actors to prevent training instability from their distributional mismatch; adds an invariant scaling technique addressing the problem that per-RL-step weight updates are typically very small relative to quantization granularity.

## Results

Using INT8 and FP8 quantization on DeepScaleR and DAPO training setups, QuRL achieves 20% to 80% faster rollout during RL training versus full-precision rollout, without the instability that naive actor quantization would otherwise introduce.

## Limitations

Not stated in the fetched abstract beyond the DeepScaleR/DAPO evaluation setting and INT8/FP8 quantization schemes tested.

## Why it matters here

- **overthinking**: Indirectly relevant: this targets training-time efficiency of the RL rollout phase used to produce reasoning models (via quantization), not inference-time reasoning-trace length -- a different, upstream lever for making the same RL-for-reasoning pipeline this archive's overthinking-mitigation methods build on cheaper to run, complementary to but distinct from length-penalty or early-exit approaches.

## Entities

- **Concepts**: quantized-actor RL rollout acceleration, Adaptive Clipping Range (ACR), invariant scaling for small weight updates
- **Methods**: QuRL (quantized-actor RL), Adaptive Clipping Range (ACR), INT8/FP8 quantization
- **Datasets**: [DeepScaleR](../../../../wiki/datasets/deepscaler.md), DAPO

Tags: `low-precision-training`, `reinforcement-learning`, `rollout-efficiency`, `quantization`

---

Record id: `title:9b034ca49bd46f6f`
