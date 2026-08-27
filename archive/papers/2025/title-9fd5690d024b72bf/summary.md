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

SpatialNavigator (MindJourney) couples a vision-language model with a controllable video-diffusion world model, iteratively sketching camera trajectories and synthesizing corresponding views for the VLM to reason over, boosting spatial-reasoning benchmark performance 7.7% without any fine-tuning.

## Problem

Vision-language models perceive only static 2D images and lack an internal model of 3D scene dynamics, so they struggle even with simple spatial-reasoning tasks like anticipating how a scene looks after an egocentric motion.

## Contributions

- SpatialNavigator, coupling a VLM with a video-diffusion world model for test-time spatial reasoning
- a plug-and-play route to 3D spatial reasoning requiring no fine-tuning of the VLM
- a 7.7% average gain on the SAT spatial-reasoning benchmark, improving even over RL-trained test-time-inference VLMs

## Method

SpatialNavigator is a test-time scaling framework in which a VLM iteratively proposes a concise camera trajectory, a video-diffusion-based controllable world model synthesizes the corresponding view at each step, and the VLM reasons over the resulting multi-view evidence gathered through this interactive exploration -- all without fine-tuning the VLM.

## Results

On the SAT spatial-reasoning benchmark, SpatialNavigator achieves an average 7.7% performance boost with no fine-tuning, and also improves upon VLMs already trained for test-time inference via reinforcement learning.

## Limitations

Not stated in the fetched abstract; evaluated primarily on the SAT benchmark, so generality across other spatial-reasoning tasks is not established in the excerpt retrieved.

## Why it matters here

- **overthinking**: Indirectly relevant: it is test-time scaling in the spatial/embodied domain (spending more inference compute generating and reasoning over synthesized views) rather than the token-length scaling the overthinking topic mostly tracks, but it is another example of test-time compute buying accuracy through additional structured computation rather than a longer text chain-of-thought.

## Entities

- **Concepts**: controllable world model (video diffusion), test-time scaling via interactive exploration, iterative camera-trajectory sketching
- **Methods**: video diffusion world model, test-time scaling, iterative multi-view exploration
- **Datasets**: SAT (spatial-reasoning benchmark)

Tags: `test-time-scaling`, `spatial-reasoning`, `world-model`, `vision-language-models`

## Abstract

Abstract Spatial reasoning in 3D space is central to human cognition and indispensable for embodied tasks such as navigation and manipulation. However, state-of-the-art vision–language models (VLMs) struggle frequently with tasks as simple as anticipating how a scene will look after an egocentric motion: they perceive 2D images but lack an internal model of 3D dynamics. We therefore propose SpatialNavigator, a test-time scaling framework that grants a VLM with this missing capability by coupling it to a controllable world model based on video diffusion. The VLM iteratively sketches a concise camera trajectory, while the world model synthesizes the corresponding view at each step. The VLM then reasons over this multi-view evidence gathered during the interactive exploration. Without any fine-tuning, our SpatialNavigator achieves an average 7.7\% performance boost on the representative spatial reasoning benchmark SAT, showing that pairing VLMs with world models for test-time scaling offers a simple, plug-and-play route to robust 3D reasoning. Meanwhile, our method also improves upon the test-time inference VLMs trained through reinforcement learning, which demonstrates the potential of our method that utilizes world models for test-time scaling.

---

Record id: `title:9fd5690d024b72bf`
