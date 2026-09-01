<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63085>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A model-auditing/extraction paper that repurposes the word 'overthinking' for an unrelated technique: amplifying a reasoning-distilled model's task vector relative to its base instruct model (O_alpha = M + alpha(R - M), alpha > 1) to boost chain-of-thought faithfulness, revealing hidden/concealed information a black-box audit is trying to elicit up to 10x more often than standard reasoning models, across 2B-32B-parameter models.

## Problem

Black-box auditing of language models -- eliciting concealed information a model has been trained to hide -- is limited by the model's chain-of-thought not always faithfully reflecting information it actually possesses, and existing techniques do not have a reliable way to amplify a model's tendency to reveal such information through its reasoning.

## Contributions

- an 'overthinking' model construction (O_alpha = M + alpha(R-M), alpha > 1) that amplifies a reasoning-distilled model's task vector to boost chain-of-thought faithfulness for black-box auditing purposes
- layer-wise attenuation strategies selectively boosting reasoning while preserving output coherence
- empirical demonstration that amplified-weight models reveal concealed information up to 10x more often than standard reasoning models across 2B-32B parameter scales, with secret-type-dependent sensitivity to the amplification direction

## Method

Defines an 'overthinking' model as a weight-space extrapolation beyond the reasoning-distilled model: O_alpha = M + alpha(R - M), where M is a base instruct model, R is the same model after reasoning distillation, and alpha > 1 extrapolates past R along the reasoning-induction task-vector direction, amplifying reasoning behavior beyond what standard distillation produces. Also proposes layer-wise attenuation strategies that selectively boost reasoning in some layers while preserving output quality and coherence, avoiding wholesale degradation from uniform amplification.

## Results

Across models ranging from 2B to 32B parameters, 'overthinking' (amplified-weight) models reveal hidden/concealed information substantially more often than standard reasoning models -- up to tenfold more frequently. Effectiveness varies by secret type: some concealed information is revealed specifically through perturbation along the reasoning task-vector direction, while other secrets are revealed by any sufficiently strong weight adjustment regardless of direction, suggesting different secrets are encoded differently in the model's weights.

## Limitations

Not stated in the fetched abstract beyond the 2B-32B parameter range tested and the qualitative distinction between secret types (reasoning-direction-sensitive vs. any-sufficiently-strong-perturbation).

## Why it matters here

- **overthinking**: IMPORTANT NAMING COLLISION, not the topic's usual meaning: this paper uses the word 'overthinking' as its own coined term for a weight-amplification model-auditing technique (extrapolating a reasoning task vector to boost chain-of-thought faithfulness for security/interpretability auditing), entirely unrelated to the reasoning-trace-length overthinking this archive tracks -- it does not address the accuracy/efficiency tradeoff of reasoning length, test-time compute scaling, or when a model should stop reasoning. Flagged here so the coincidental keyword match is not mistaken for topical relevance in future reads.

## Entities

- **Concepts**: task-vector weight amplification (extrapolation beyond distillation), chain-of-thought faithfulness for auditing, layer-wise attenuation
- **Methods**: task-vector weight amplification (O_alpha = M + alpha(R-M)), layer-wise attenuation
- **Datasets**: _none recorded_

Tags: `model-auditing`, `chain-of-thought-faithfulness`, `task-vectors`, `weight-extrapolation`

---

Record id: `title:ef0cda814f689ecc`
