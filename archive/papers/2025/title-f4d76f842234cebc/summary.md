<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119216>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

FreqExit enables dynamic early-exit inference for Visual AutoRegressive (VAR) image generation models by exploiting that high-frequency image details emerge only in later decoding stages, using curriculum-based layer-dropout supervision and a wavelet-domain frequency-consistency loss, achieving up to 2x speedup with minor quality loss.

## Problem

Visual AutoRegressive models' coarse-to-fine, next-scale decoding paradigm violates the two assumptions (semantic stability, monotonic locality) that conventional dynamic-inference/early-exit methods rely on, making existing early-exit techniques ineffective for VAR models.

## Contributions

- identification of why conventional early-exit assumptions fail for Visual AutoRegressive models
- FreqExit, a training framework enabling dynamic early exit in VAR without architecture changes
- up to 2x speedup (minor quality loss) or 1.3x speedup (no perceptible loss) on ImageNet 256x256

## Method

Observes that high-frequency image details are crucial for perceptual quality but only emerge in later VAR decoding stages, and designs FreqExit, a training framework with three components: curriculum-based supervision with progressive layer dropout and an early-exit loss, a wavelet-domain high-frequency consistency loss aligning spectral content across generation steps, and a lightweight self-supervised frequency-gated module guiding adaptive learning of structural and detailed spectral components -- without altering the VAR architecture.

## Results

On ImageNet 256x256, FreqExit achieves up to 2x speedup with only minor quality degradation, and delivers 1.3x acceleration with no perceptible quality loss, enabling runtime-adaptive acceleration within a single unified model.

## Limitations

Not stated in the fetched abstract beyond the ImageNet 256x256 evaluation setting for VAR image generation.

## Why it matters here

- **overthinking**: Off-topic domain (image generation via Visual AutoRegressive models, not text reasoning), matched via 'early exit'; relevant only as a cross-modal example that early-exit/adaptive-computation techniques must be redesigned when the generation paradigm's structural assumptions differ, a caution potentially applicable when adapting LLM early-exit or stopping methods across reasoning-model architectures.

## Entities

- **Concepts**: frequency-aware dynamic inference, curriculum layer-dropout supervision, wavelet-domain consistency loss
- **Methods**: Visual AutoRegressive (VAR) modeling, [early-exit inference](../../../../wiki/methods/early-exit-inference.md), wavelet-domain frequency-consistency loss
- **Datasets**: ImageNet 256x256

Tags: `early-exit`, `image-generation`, `visual-autoregressive`, `adaptive-inference`

## Abstract

Abstract Visual AutoRegressive (VAR) modeling employs a next-scale decoding paradigm that progresses from coarse structures to fine details. While enhancing fidelity and scalability, this approach challenges two fundamental assumptions of conventional dynamic inference: semantic stability (intermediate outputs approximating final results) and monotonic locality (smooth representation evolution across layers), which renders existing dynamic inference methods ineffective for VAR models. To address this challenge, we propose FreqExit, a unified training framework that enables dynamic inference in VAR without altering its architecture or compromising output quality. FreqExit is based on a key insight: high-frequency details are crucial for perceptual quality and tend to emerge only in later decoding stages. Leveraging this insight, we design targeted mechanisms that guide the model to learn more effectively through frequency-aware supervision. The proposed framework consists of three components: (1) a curriculum-based supervision strategy with progressive layer dropout and early exit loss; (2) a wavelet-domain high-frequency consistency loss that aligns spectral content across different generation steps; and (3) a lightweight self-supervised frequency-gated module that guides adaptive learning of both structural and detailed spectral components. On ImageNet 256×256, FreqExit achieves up to 2× speedup with only minor degradation, and delivers 1.3× acceleration without perceptible quality loss. This enables runtime-adaptive acceleration within a unified model, offering a favorable trade-off between efficiency and fidelity for for practical and flexible deployment.

---

Record id: `title:f4d76f842234cebc`
