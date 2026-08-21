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

QuRL runs the rollout phase of RL-with-verifiable-rewards training with an INT8 or FP8 quantized copy of the actor, adding an adaptive clipping range and an invariant weight-scaling trick to keep the low-precision policy from collapsing, for 20-80% faster rollout.

## Problem

In RLVR training of reasoning models the rollout - autoregressively decoding sampled completions - takes up to 70% of total training time. Quantizing the actor used for rollout would speed it up, but the quantized policy diverges from the full-precision policy in two ways: the mismatch destabilises the importance-ratio clipping and eventually collapses training, and the per-step weight updates in RL are so small that quantization rounds them away entirely, so the actor stops learning.

## Contributions

- Quantized-actor rollout for RLVR training, with the full-precision actor retained for updates
- Adaptive Clipping Range, which sets the clipping ratio from the measured policy ratio between full-precision and quantized actors, preventing long-horizon training collapse
- Identification of the weight-update problem, where per-step RL weight changes are too small for the quantizer to represent, and an invariant scaling fix for it
- INT8 and FP8 results on DeepScaleR and DAPO showing 20-80% faster rollout at near-baseline accuracy

## Method

Training keeps a full-precision actor for the gradient update but generates rollouts with a quantized (INT8 or FP8) copy of it. Adaptive Clipping Range measures the policy ratio between the full-precision and quantized actors and widens or narrows the PPO-style clipping ratio accordingly, so that the off-policy gap introduced by quantization is absorbed by the clip rather than accumulating into collapse. Invariant scaling addresses the weight-update problem: because consecutive RL steps change weights by very little, a fixed quantization grid maps both to the same integer; rescaling the weights before quantization (scaling factor s=1.5 in the reported runs) lowers quantization noise and lets small updates register.

## Results

Rollout throughput improved 20-80%, scaling with model size - roughly 20-30% at 7B and 70-90% at 32B on H100. Accuracy is close to the BF16 baseline: GSM8K 55.35% (BF16) vs 53.55% (INT8) and 54.28% (FP8); AIME 2024 31.67% (BF16) vs 31.25% (INT8) and 33.27% (FP8); DeepScaleR average 56.40% (BF16) vs 55.48% (INT8). INT8 leaves a 1-2 point gap on some tasks; FP8 is roughly on par. Models used are Qwen2.5-0.5B, Qwen2.5-7B-Math and DeepSeek-Distill-Qwen at 7B/14B/32B.

## Limitations

The speedup applies only to rollout inside training, not to inference-time decoding, so a model trained with QuRL is no cheaper to run. FP8 KV-cache quantization was excluded because the implementation was not good enough. The weight scaling factor is fixed at s=1.5 and ablations show the method is sensitive to it. The INT8 accuracy gap of 1-2 points on GSM8K and DeepScaleR is a real cost, not noise, and it is FP8 rather than INT8 that carries the near-lossless claim.

## Why it matters here

- **overthinking**: Tangential, and the title is misleading for this topic. 'Efficient reasoning' here means numerical precision during RL training, not reasoning length at inference: QuRL makes the rollout phase 20-80% faster in wall-clock terms and explicitly does not touch inference-time decoding, so the trained model emits the same chains of thought at the same cost. It says nothing about whether a model thinks longer than a problem needs, about test-time compute scaling, or about stopping criteria. Its one indirect bearing on the topic is that rollout is 70% of RLVR training time and long reasoning traces are what make rollout expensive - so anything that trains length-adaptive behaviour by RL inherits this bottleneck, and cheaper rollout makes such experiments cheaper to run. That is an enabler, not a finding about overthinking.

## Entities

- **Concepts**: Quantized Rollout, Policy Ratio Clipping, [Reinforcement Learning with Verifiable Rewards](../../../../wiki/concepts/reinforcement-learning-with-verifiable-rewards.md), Quantization Noise, Training-Time Compute Bottleneck
- **Methods**: QuRL, Adaptive Clipping Range (ACR), invariant scaling, RLVR, INT8 quantization, FP8 quantization, [DAPO](../../../../wiki/methods/dapo.md), GRPO-style clipped policy optimization
- **Datasets**: [DeepScaleR](../../../../wiki/datasets/deepscaler.md), DAPO, [GSM8K](../../../../wiki/datasets/gsm8k.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [MATH 500](../../../../wiki/datasets/math-500.md), AMC 2023, [Minerva Math](../../../../wiki/datasets/minerva-math.md), Olympiad Bench, [Omni-Math](../../../../wiki/datasets/omni-math.md), [Still](../../../../wiki/datasets/still.md)

Tags: `quantization`, `rlvr`, `training-efficiency`, `int8`, `fp8`, `rollout`, `false-positive-match`

---

Record id: `title:9b034ca49bd46f6f`
