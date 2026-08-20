<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions

- **Authors**: Maisha Maliha, Dean F. Hougen
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.1265>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.1265
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Traces how individual prompt tokens ground into image regions during diffusion denoising, using fixed-seed single-word removal for causal faithfulness and a head-resolved spike score for attribution.

## Problem

Text-to-image diffusion models generate well but their internal mechanisms for grounding prompt semantics into visual structure are poorly understood.

## Contributions

- A mechanistic interpretability framework for Stable Diffusion probing per-token representation and use during denoising
- Token-level spatial grounding maps derived from cross-attention activations across UNet denoising
- Fixed-seed single-word removal interventions establishing causal faithfulness through counterfactual generations
- A head-resolved spike score based on divergence between per-head token contribution distributions
- Findings on token grounding, semantic drift and head specialization across denoising timesteps

## Method

Cross-attention activations are recorded throughout UNet denoising and converted into token-level spatial grounding maps showing where each token contributes signal. Causal faithfulness is established by controlled prompt interventions that remove one word at a time while holding the sampling seed fixed, producing counterfactual generations — fixing the seed is what makes the two images comparable, so the difference is attributable to the removed word. A head-resolved spike score based on divergence between per-head token contribution distributions before and after intervention quantifies mechanistic sensitivity, enabling module- and head-wise attribution.

## Results

Experiments on compositional prompts and challenging relational descriptions reveal systematic patterns of token grounding, semantic drift and head specialization across denoising timesteps. No numbers are given in the abstract.

## Limitations

No quantitative results in the abstract. Scope is Stable Diffusion, so architecture generality is untested. Single-word removal changes the prompt distribution as well as the target semantics, so the counterfactual is not perfectly isolated. Diffusion models, not language reasoning models, so nothing here bears on reasoning traces.

## Why it matters here

- **reasoning-interpretability**: Off-target as content — diffusion image generation, no reasoning model — and it reached this topic on interpretability vocabulary. The transferable element is the experimental discipline: holding the sampling seed fixed while ablating one word converts a generative comparison into a controlled counterfactual, and the head-resolved divergence score then attributes the change. The archive's reasoning-trace interventions face the same nuisance-variation problem, since resampling a trace changes everything at once, and seed-fixing is the analogue that trace-level counterfactual studies here do not consistently apply.

## Entities

- **Concepts**: [mechanistic interpretability](../../../../wiki/concepts/mechanistic-interpretability.md), cross-attention, causal faithfulness, attribution, head specialization, counterfactual intervention, [localization](../../../../wiki/concepts/localization.md)
- **Methods**: cross-attention intervention, [activation patching](../../../../wiki/methods/activation-patching.md), counterfactual prompt ablation, head-resolved attribution
- **Datasets**: _none recorded_

Tags: `diffusion`, `cross-attention`, `interpretability`, `counterfactual`, `off-topic-candidate`

## Abstract

Text-to-image diffusion models achieve remarkable generation quality, yet their internal mechanisms for grounding prompt semantics into visual structure remain poorly understood. We present a novel mechanistic interpretability framework for Stable Diffusion that probes how individual prompt tokens are represented and utilized during the denoising process. Given a prompt, we record cross-attention activations throughout UNet denoising and convert them into token-level spatial grounding maps that indicate where each token contributes signal during image synthesis. To establish causal faithfulness, we perform controlled prompt interventions by removing a single word at a time while keeping the sampling seed fixed, producing counterfactual generations. To quantify mechanistic sensitivity, we introduce a head-resolved spike score based on divergence between per-head token contribution distributions before and after intervention, enabling module-wise and head-wise attribution of semantic changes. Experiments on compositional prompts and challenging relational descriptions reveal systematic patterns of token grounding, semantic drift, and head specialization across denoising timesteps. Our results provide a practical and reproducible toolkit for analyzing how diffusion models encode and apply semantic information, supporting deeper transparency in text-to-image generation.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1265`
