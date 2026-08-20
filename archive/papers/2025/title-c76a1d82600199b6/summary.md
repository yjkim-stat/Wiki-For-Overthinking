<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119207>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Trains a hypernetwork to modulate initial noise in distilled diffusion models so that test-time-scaling quality gains are baked into a single forward pass instead of requiring explicit inference-time reward optimization.

## Problem

Test-time scaling improves diffusion/generative vision model outputs by spending extra inference-time computation (e.g. reward-guided noise search), but this makes inference slow and impractical; the paper asks how to retain the quality benefit while removing the inference-time overhead.

## Contributions

- Proposes a Noise Hypernetwork that modulates the initial input noise of a distilled diffusion generator to replace explicit reward-guided test-time noise optimization
- Gives a theoretically grounded, tractable noise-space objective for learning a reward-tilted distribution while keeping fidelity to the base model
- Shows a substantial portion of the quality gains from explicit test-time optimization can be recovered at a fraction of the computational cost

## Method

The approach amortizes test-time scaling into a post-training step: a Noise Hypernetwork learns to modulate the initial input noise fed to a distilled diffusion generator, so that at inference the model draws from a reward-tilted distribution without running explicit reward-guided noise optimization. The hypernetwork is trained with a tractable noise-space objective that balances optimizing for desired reward characteristics against staying faithful to the base model's distribution.

## Results

The abstract states the method 'recovers a substantial portion of the quality gains from explicit test-time optimization at a fraction of the computational cost,' without giving specific benchmark numbers.

## Limitations

The abstract does not report which benchmarks or metrics were used to measure 'quality gains', does not quantify the fraction of computational cost or the exact portion of gains recovered, and does not name the base diffusion/generator model used.

## Why it matters here

- **overthinking**: Tangential. It reuses the phrase 'test-time compute' and the general concept of trading inference computation for output quality, but the setting is image/diffusion generation guided by a reward-tilted noise distribution, not large language model reasoning length. It does not address chain-of-thought length, overthinking/underthinking, or when a reasoning model should stop generating tokens.

## Entities

- **Concepts**: test-time compute amortization, reward-tilted distribution, noise-space objective
- **Methods**: Noise Hypernetwork, reward-tilted distribution learning, diffusion model distillation
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `diffusion-models`, `hypernetwork`, `amortization`, `not-llm-reasoning`

## Abstract

Abstract The new paradigm of test-time scaling has yielded remarkable breakthroughs in Large Language Models (LLMs) (e.g. reasoning models) and in generative vision models, allowing models to allocate additional computation during inference to effectively tackle increasingly complex problems. Despite the improvements of this approach, an important limitation emerges: the substantial increase in computation time makes the process slow and impractical for many applications. Given the success of this paradigm and its growing usage, we seek to preserve its benefits while eschewing the inference overhead. In this work we propose one solution to the critical problem of integrating test-time scaling knowledge into a model during post-training. Specifically, we replace reward guided test-time noise optimization in diffusion models with a Noise Hypernetwork that modulates initial input noise. We propose a theoretically grounded framework for learning this reward-tilted distribution for distilled generators, through a tractable noise-space objective that maintains fidelity to the base model while optimizing for desired characteristics. We show that our approach recovers a substantial portion of the quality gains from explicit test-time optimization at a fraction of the computational cost.

---

Record id: `title:c76a1d82600199b6`
