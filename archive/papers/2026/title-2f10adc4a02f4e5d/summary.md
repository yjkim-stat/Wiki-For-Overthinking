<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/64926>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes a sample-based (rather than gradient-based) test-time guidance method for diffusion image models, matching gradient-guidance reward alignment on SDXL at a 9.5x speedup.

## Problem

Guiding pretrained diffusion models toward reward-aligned outputs at inference time typically requires expensive gradient-based backpropagation through the sampling chain; the paper seeks a cheaper alternative.

## Contributions

- Proposes computing expected future reward using only marginal samples from a pre-trained diffusion model, avoiding the expensive sequential backpropagation used by gradient-based guidance.
- Introduces LiDAR sampling, which uses a lookahead strategy to collect marginal samples and a solver that steers particles toward high-reward predictions.
- Demonstrates on SDXL that 3 samples with a 3-step lookahead matches recent gradient-guidance approaches in reward alignment while giving a 9.5x speedup.

## Method

Instead of backpropagating gradients through the diffusion sampling chain to guide generation toward high-reward outputs, the method estimates the expected future reward of an intermediate state using marginal samples drawn from the pretrained diffusion model itself, removing the need for a differentiable dependency between intermediate states and the reward. A lookahead strategy (LiDAR sampling) collects these marginal samples a few steps ahead and a solver directs particles toward the highest-reward predictions, giving a closed-form, sample-based guidance signal.

## Results

On SDXL, using 3 samples with a 3-step lookahead achieves reward-alignment performance matching recent gradient-guidance methods, with a 9.5x speedup.

## Limitations

Only a third-party-extracted summary of the abstract was available (no PDF attachment); specific reward models, prompt sets, and any stated failure modes of the lookahead/marginal-sampling approximation are not available from this source.

## Why it matters here

- **overthinking**: This paper is about test-time inference-time guidance for image diffusion models (steering image generation toward higher-reward outputs), not about large reasoning models, chain-of-thought length, or the accuracy/efficiency tradeoff of reasoning. It only shares the generic phrase 'test-time scaling' with the tracked topic; the underlying subject (diffusion image generation guidance) has no substantive connection to overthinking/underthinking in reasoning models. This looks like a keyword-match false positive that should have been filtered out.

## Entities

- **Concepts**: reward-guided diffusion sampling, marginal-sample expected future reward, lookahead guidance, closed-form guidance without backpropagation
- **Methods**: LiDAR sampling, lookahead sample reward guidance
- **Datasets**: SDXL (Stable Diffusion XL) generation benchmark

Tags: `diffusion-models`, `test-time-guidance`, `image-generation`, `reward-alignment`, `tangential`, `off-topic`

---

Record id: `title:2f10adc4a02f4e5d`
