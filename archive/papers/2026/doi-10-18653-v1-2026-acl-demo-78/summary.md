<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Spectra: A Mechanistic Interpretability Library for Vision-Language Models

- **Authors**: Clement Neo, Yongsen Zheng, Kwok-Yan Lam, Luke Ong
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-demo.78>
- **DOI**: 10.18653/V1/2026.ACL-DEMO.78
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

An open library giving vision-language models the mechanistic-interpretability tooling that text-only models already have: activation patching, attention analysis and meta-functions behind one interface.

## Problem

Interpretability tooling for VLMs lags behind text-only models. TransformerLens enabled progress on language models, but existing VLM tools are limited to basic activation probing and saving, so experiments that are routine on LLMs are cumbersome on VLMs.

## Contributions

- Spectra, a mechanistic interpretability library for VLMs with unified activation-patching and attention-analysis abstractions
- Per-checkpoint configuration handling of architecture-specific differences behind one high-level interface
- Support for Qwen2.5-VL, Qwen3-VL, LLaVA 1.5 and SmolVLM with an extensible design
- A demonstration on a counting task

## Method

Spectra provides unified abstractions for activation patching, attention pattern analysis and meta-functions across diverse VLM architectures. It is built on HuggingFace Transformers and handles architecture-specific differences through per-checkpoint configurations, keeping a single high-level interface. Per-checkpoint configuration is the design choice that lets one API span architectures without a common internal structure.

## Results

Capabilities are demonstrated with interpretability experiments on a counting task, presented as experiments that were previously cumbersome. Supported checkpoints are Qwen2.5-VL, Qwen3-VL, LLaVA 1.5 and SmolVLM.

## Limitations

A tooling contribution, so there are no empirical findings about models beyond the counting-task demonstration. Four supported checkpoints at release, and per-checkpoint configuration means each new architecture needs manual work rather than being handled generically. No performance or fidelity comparison against TransformerLens or other libraries is reported.

## Why it matters here

- **reasoning-interpretability**: Infrastructure, not a finding, and multimodal rather than reasoning-specific. It matters to this topic for one reason: the archive already holds a case where two interpretability papers reached opposite conclusions about the same behaviour with no shared model or tooling, and shared instrumentation is the precondition for that class of disagreement to be resolvable at all. Spectra is the multimodal instance of that argument, and it pairs directly with doi:10.18653/v1/2026.acl-long.159 in this same batch, which argues the field needs auditable protocols.

## Entities

- **Concepts**: [mechanistic interpretability](../../../../wiki/concepts/mechanistic-interpretability.md), activation patching, [attention pattern](../../../../wiki/concepts/attention-pattern.md), tooling, [reproducibility](../../../../wiki/concepts/reproducibility.md)
- **Methods**: [activation patching](../../../../wiki/methods/activation-patching.md), attention pattern analysis, TransformerLens
- **Datasets**: _none recorded_

Tags: `interpretability`, `tooling`, `vision-language models`, `activation patching`, `library`

## Abstract

,

---

Record id: `doi:10.18653/v1/2026.acl-demo.78`
