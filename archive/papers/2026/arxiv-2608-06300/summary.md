<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors

- **Authors**: Arya Labroo, Mengjie Qian, Kate Knill
- **Venue**: cs.AI
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06300>
- **PDF**: <https://arxiv.org/pdf/2608.06300v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.57

## In one line

Extends Concept Activation Vector bias analysis to neural L2 speaking graders, and finds concept recoverability and concept influence come apart, with SAEs improving the first while attenuating the second.

## Problem

Automatic speaking assessment systems mark second-language speaking tests in high-stakes settings, so their scores must depend on proficiency rather than on irrelevant speaker attributes such as first language or age. Transformer foundation models improved accuracy but their black-box representations make fairness and interpretability analysis harder.

## Contributions

- Extension of CAV-based bias analysis to a BERT text grader and a Whisper-based multimodal speaking grader
- An explicit separation of concept recoverability from concept influence, the latter via a gradient-based sensitivity metric
- Learning CAVs in an SAE latent space and mapping them back to activation space
- The finding that SAEs improve linear recoverability while attenuating activation-space sensitivity, especially in low-dimensional layers

## Method

CAV-based analysis is extended from feature-based graders to two neural systems: a text-based BERT grader and a speech-and-text multimodal grader based on Whisper. CAVs represent human-interpretable concepts as directions in activation space, which lets the analysis separate whether a concept is encoded in the representation from whether it influences the predicted score, the latter quantified with a gradient-based sensitivity metric. Because CAVs assume linear separability, which is less likely in complex neural embeddings, the paper also learns CAVs in a sparse autoencoder latent space and maps them back to activation space.

## Results

Concept recoverability depends strongly on the representation and architecture being probed rather than on the concept alone. Sensitivity to concepts is also architecture-dependent. SAEs make concepts more linearly recoverable but attenuate the original activation-space sensitivity, especially in low-dimensional layers.

## Limitations

No numeric results in the abstract. Two systems and one task domain, so the architecture-dependence conclusion rests on a small sample of architectures. The gradient-based sensitivity metric is a local measure and need not capture influence realized through nonlinear paths. The SAE finding is a trade-off without a resolution: the sparse space gives cleaner directions but a distorted influence estimate, and which to trust is left open.

## Why it matters here

- **reasoning-interpretability**: Not a reasoning paper — the task is L2 speaking assessment and no reasoning model appears. It earns its place in this topic on one methodological result the archive should hold: probing shows a concept is encoded, which is not the same as showing it is used, and SAEs improve the first measurement while degrading the second. Every SAE result in this archive that reads a feature and infers a role inherits that gap, and this paper is the cleanest statement of it, on an application where the distinction has legal consequences. The finding that attenuation is worst in low-dimensional layers is a concrete caution for layer selection.

## Entities

- **Concepts**: concept activation vector, sparse autoencoder, [monosemanticity](../../../../wiki/concepts/monosemanticity.md), [localization](../../../../wiki/concepts/localization.md), linear separability, fairness auditing, recoverability versus influence
- **Methods**: Concept Activation Vectors, [sparse autoencoder](../../../../wiki/methods/sparse-autoencoder.md), gradient-based sensitivity analysis, [linear probe](../../../../wiki/methods/linear-probe.md)
- **Datasets**: _none recorded_

Tags: `concept activation vectors`, `sparse autoencoder`, `fairness`, `speech assessment`, `off-topic-candidate`

## Abstract

Automatic speaking assessment systems are increasingly deployed in high-stakes settings to mark second language (L2) learners' speaking tests, making it critical to show that their scores depend on speaking proficiency rather than irrelevant speaker attributes such as first language (L1) or age. Transformer-based foundation models have improved the accuracy of these L2 speaking graders, but their black-box representations make fairness and interpretability analysis more difficult. Building on prior work that used Concept Activation Vectors (CAVs) to detect bias towards unwanted attributes (`concepts') in feature-based graders, we extend CAV-based analysis to two neural speaking assessment systems: a text-based BERT grader and a speech-and-text multimodal grader based on Whisper. CAVs represent human-interpretable concepts as directions in a model's activation space, allowing us to distinguish between whether a concept is encoded in a model's internal representations and whether it influences the predicted score, the latter quantified using a gradient-based sensitivity metric. Since CAVs rely on linear separability, which is less likely in complex neural embedding spaces, we also investigate whether sparse autoencoders (SAEs) provide cleaner concept directions by learning CAVs in a sparse latent space and mapping them back to activation space. Our analysis shows that concept recoverability depends strongly on the representation and architecture being probed, rather than on the concept alone. Sensitivity to concepts is also architecture-dependent. SAEs make concepts more linearly recoverable, but attenuate the original activation-space sensitivity, especially in low-dimensional layers. These findings highlight the need to distinguish concept recoverability from concept influence when auditing bias in speaking assessment systems.

---

Record id: `arxiv:2608.06300`
