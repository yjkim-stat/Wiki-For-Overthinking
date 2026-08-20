<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MindJourney: Test-Time Scaling with World Models for Spatial Reasoning

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118581>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Couples a vision-language model with a video-diffusion world model that synthesizes egocentric views along a VLM-proposed camera trajectory, using the resulting multi-view evidence to improve 3D spatial reasoning at inference time.

## Problem

State-of-the-art vision-language models perceive only 2D images and lack an internal model of 3D dynamics, so they struggle to anticipate how a scene will look after an egocentric motion.

## Contributions

- Couples a VLM with a controllable video-diffusion world model to gather multi-view evidence at inference time, without fine-tuning
- Shows a plug-and-play route to 3D spatial reasoning by pairing VLMs with world models for test-time scaling

## Method

The VLM iteratively sketches a concise camera trajectory; a controllable world model based on video diffusion synthesizes the corresponding view at each step; the VLM then reasons over the multi-view evidence gathered during this interactive exploration, requiring no fine-tuning.

## Results

Average 7.7% performance boost on the SAT spatial reasoning benchmark with no fine-tuning; also improves on VLMs already trained with reinforcement learning for test-time inference.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Uses "test-time scaling" to mean adding extra visual-exploration steps via a world model for 3D spatial reasoning in VLMs, not language reasoning length or a stop/continue decision in a large reasoning model's chain of thought. The connection to this topic is the shared phrase only; the paper is tangential to reasoning-length overthinking.

## Entities

- **Concepts**: world model, [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), egocentric camera trajectory, multi-view reasoning
- **Methods**: SpatialNavigator, video diffusion world model
- **Datasets**: SAT (spatial reasoning benchmark)

Tags: `spatial-reasoning`, `world-model`, `vlm`, `test-time-scaling`, `tangential`

## Abstract

Abstract Spatial reasoning in 3D space is central to human cognition and indispensable for embodied tasks such as navigation and manipulation. However, state-of-the-art vision–language models (VLMs) struggle frequently with tasks as simple as anticipating how a scene will look after an egocentric motion: they perceive 2D images but lack an internal model of 3D dynamics. We therefore propose SpatialNavigator, a test-time scaling framework that grants a VLM with this missing capability by coupling it to a controllable world model based on video diffusion. The VLM iteratively sketches a concise camera trajectory, while the world model synthesizes the corresponding view at each step. The VLM then reasons over this multi-view evidence gathered during the interactive exploration. Without any fine-tuning, our SpatialNavigator achieves an average 7.7\% performance boost on the representative spatial reasoning benchmark SAT, showing that pairing VLMs with world models for test-time scaling offers a simple, plug-and-play route to robust 3D reasoning. Meanwhile, our method also improves upon the test-time inference VLMs trained through reinforcement learning, which demonstrates the potential of our method that utilizes world models for test-time scaling.

---

Record id: `title:9fd5690d024b72bf`
