<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64102>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces LLaDA-S, a hierarchical-search-and-self-verification test-time scaling framework for discrete diffusion language models that matches best-of-N accuracy with fewer function evaluations.

## Problem

Test-time scaling methods built for autoregressive models are ill-suited to discrete diffusion language models (dLLMs) because dLLMs decode the entire sequence in parallel rather than token-by-token, so standard step-by-step search and verification strategies do not transfer.

## Contributions

- Introduces LLaDA-S, a test-time scaling framework designed for discrete diffusion language models rather than autoregressive models
- Hierarchical Trajectory Search prunes and reallocates compute across an early-to-mid denoising window
- Self-Verified Feedback replaces an external verifier with self-evaluation prompts scoring intermediate completions
- Local Branching with Partial Remasking explores alternative completions while preserving high-confidence tokens
- Matches best-of-N accuracy with substantially fewer function evaluations

## Method

LLaDA-S combines three components: Hierarchical Trajectory Search, which dynamically prunes and reallocates compute during an early-to-mid denoising window to focus on promising generation paths; Self-Verified Feedback, which scores intermediate completions using the model's own self-evaluation prompts instead of an external verifier; and Local Branching with Partial Remasking, which explores diverse continuations while keeping high-confidence tokens fixed. Together these adapt test-time scaling to the parallel, whole-sequence decoding used by discrete diffusion language models.

## Results

Matches best-of-N performance with substantially fewer function evaluations on mathematical reasoning and code generation benchmarks, tested on LLaDA 8B, Dream 7B, and LLaDA 2.0-mini.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this is a genuine test-time compute/accuracy tradeoff method, but it targets discrete diffusion language models' parallel denoising process (how to allocate search over denoising steps), not chain-of-thought length in autoregressive large reasoning models. It does not address overthinking, underthinking, or when a model should stop reasoning.

## Entities

- **Concepts**: test-time scaling for diffusion LMs, denoising trajectory search, self-verification
- **Methods**: LLaDA-S, Hierarchical Trajectory Search, Self-Verified Feedback, Local Branching with Partial Remasking
- **Datasets**: _none recorded_

Tags: `diffusion-lm`, `test-time-scaling`, `search`, `self-verification`

---

Record id: `title:914a66aec4e7af2f`
