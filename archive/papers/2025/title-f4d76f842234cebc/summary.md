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

A training framework that adds early-exit inference to Visual AutoRegressive image generation by supervising the model with frequency-aware losses, so a single model can trade decoding cost against image fidelity at runtime.

## Problem

Visual AutoRegressive (VAR) modelling decodes an image scale by scale, from coarse structure to fine detail. Existing dynamic-inference methods assume semantic stability (an intermediate output already approximates the final one) and monotonic locality (representations change smoothly across layers); the paper argues next-scale decoding violates both, so those methods do not work on VAR. The framing observation is that high-frequency detail, which is what perceptual quality depends on, only appears in the late decoding stages, so exiting early costs exactly the component that matters most.

## Contributions

- An argument that next-scale VAR decoding violates the semantic-stability and monotonic-locality assumptions that existing dynamic-inference methods rely on.
- FreqExit, a training framework enabling dynamic inference in VAR without architectural change.
- A curriculum-based supervision strategy combining progressive layer dropout with an early-exit loss.
- A wavelet-domain high-frequency consistency loss aligning spectral content across generation steps.
- A lightweight self-supervised frequency-gated module for adaptive learning of structural and detail spectral components.
- Up to 2x speedup with minor degradation and 1.3x with no perceptible quality loss on ImageNet 256x256, within a single runtime-adaptive model.

## Method

FreqExit trains a VAR model to support exiting early without changing its architecture, using three components. First, a curriculum-based supervision strategy with progressive layer dropout and an early-exit loss, so the model learns to produce usable output at intermediate depths. Second, a wavelet-domain high-frequency consistency loss that aligns the spectral content produced at different generation steps, targeting the high-frequency detail that early exits would otherwise lose. Third, a lightweight self-supervised frequency-gated module that steers the model to learn structural (low-frequency) and detail (high-frequency) spectral components adaptively. The result is one model whose inference cost can be set at runtime rather than a family of separately trained models.

## Results

On ImageNet 256x256, up to 2x speedup with what the paper calls minor degradation, and 1.3x acceleration with no perceptible quality loss. The abstract states no image-quality metric values (no FID, IS or precision/recall numbers) and no baseline comparison figures, so the size of the 'minor degradation' at 2x cannot be established from the available material.

## Limitations

The two speedup figures are reported against qualitative quality descriptions rather than metric values, so the tradeoff curve is not quantified in the material available; 'minor degradation' and 'no perceptible quality loss' are the paper's own characterisations. Only one dataset and resolution (ImageNet 256x256) is named. The method requires a training framework, not a drop-in inference change, so it cannot be applied to an already-trained VAR checkpoint without retraining. The frequency-based insight is specific to image generation and carries no claim beyond it.

## Why it matters here

- **overthinking**: Not relevant. This is a false positive: the task matched on the keyword 'early exit', but the paper is about image generation with Visual AutoRegressive models, and 'early exit' means stopping the decoding of an image at an intermediate scale or layer to save FLOPs. There is no language model, no reasoning chain, no notion of a problem needing more or fewer thinking steps, and the quantity being traded away is high-frequency image detail rather than solution correctness. The topic is about how long a reasoning model should think; nothing here bears on that. The only shared vocabulary is 'early exit' and the generic shape of a compute/quality tradeoff, which is not a connection worth recording. It should not be treated as evidence for any overthinking concept.

## Entities

- **Concepts**: early exit, dynamic inference, semantic stability, monotonic locality, next-scale decoding, frequency-aware supervision, runtime-adaptive acceleration, efficiency-fidelity tradeoff
- **Methods**: FreqExit, Visual AutoRegressive (VAR) modelling, next-scale decoding, progressive layer dropout, early exit loss, wavelet-domain high-frequency consistency loss, frequency-gated module
- **Datasets**: ImageNet 256x256

Tags: `image generation`, `visual autoregressive`, `early exit`, `dynamic inference`, `wavelet`, `imagenet`, `inference efficiency`, `false positive`

## Abstract

Abstract Visual AutoRegressive (VAR) modeling employs a next-scale decoding paradigm that progresses from coarse structures to fine details. While enhancing fidelity and scalability, this approach challenges two fundamental assumptions of conventional dynamic inference: semantic stability (intermediate outputs approximating final results) and monotonic locality (smooth representation evolution across layers), which renders existing dynamic inference methods ineffective for VAR models. To address this challenge, we propose FreqExit, a unified training framework that enables dynamic inference in VAR without altering its architecture or compromising output quality. FreqExit is based on a key insight: high-frequency details are crucial for perceptual quality and tend to emerge only in later decoding stages. Leveraging this insight, we design targeted mechanisms that guide the model to learn more effectively through frequency-aware supervision. The proposed framework consists of three components: (1) a curriculum-based supervision strategy with progressive layer dropout and early exit loss; (2) a wavelet-domain high-frequency consistency loss that aligns spectral content across different generation steps; and (3) a lightweight self-supervised frequency-gated module that guides adaptive learning of both structural and detailed spectral components. On ImageNet 256×256, FreqExit achieves up to 2× speedup with only minor degradation, and delivers 1.3× acceleration without perceptible quality loss. This enables runtime-adaptive acceleration within a unified model, offering a favorable trade-off between efficiency and fidelity for for practical and flexible deployment.

---

Record id: `title:f4d76f842234cebc`
