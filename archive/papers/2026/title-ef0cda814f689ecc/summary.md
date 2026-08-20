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

Amplifies the weight-space direction between a base model and its reasoning-distilled variant to make the model leak concealed information during safety auditing.

## Problem

Black-box auditing of language models needs better ways to surface information a model has been trained or instructed to conceal; the paper addresses how to increase the chance that such concealed information becomes visible during pre-deployment auditing.

## Contributions

- Introduces 'overthinking': a black-box auditing technique that amplifies the reasoning-direction weight difference between a base instruct model and a reasoning-distilled model
- Defines the amplified model as O_alpha = M + alpha(R - M), where M is the base instruct model, R is the reasoning-distilled model, and alpha > 1
- Develops layer-wise attenuation strategies to selectively boost reasoning while keeping output quality usable
- Shows the technique surfaces concealed information roughly 10x more often than the unamplified reasoning model, tested on models from 2B to 32B parameters across four experimental configurations

## Method

Given a base instruct model M and a reasoning-distilled version R of the same model, the method constructs an amplified model O_alpha = M + alpha(R - M) with alpha > 1, extrapolating past R along the reasoning direction in weight space. Layer-wise attenuation is used to control how much of this amplification is applied per layer, trading off amplification strength against output coherence, with the goal of making a model reveal information it would otherwise conceal.

## Results

Amplified ('overthinking') models exposed concealed information approximately 10x more frequently than the original (unamplified) reasoning model, across models ranging from 2B to 32B parameters in four experimental configurations.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential despite the shared title word. This paper's 'overthinking' is a weight-space amplification technique (O_alpha = M + alpha(R - M)) for extracting concealed information during model auditing, a safety/interpretability method unrelated to reasoning length, stopping criteria, or the accuracy/efficiency tradeoff of test-time reasoning that the tracked topic concerns. No content here addresses reasoning length or test-time compute scaling in the topic's sense.

## Entities

- **Concepts**: reasoning task vectors, model weight amplification for auditing, layer-wise attenuation
- **Methods**: reasoning task vector amplification (O_alpha = M + alpha(R - M)), layer-wise attenuation
- **Datasets**: _none recorded_

Tags: `model-auditing`, `weight-amplification`, `extraction-attack`, `ai-safety`, `tangential`

---

Record id: `title:ef0cda814f689ecc`
