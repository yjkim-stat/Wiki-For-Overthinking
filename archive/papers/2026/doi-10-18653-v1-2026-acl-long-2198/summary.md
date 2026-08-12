<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?

- **Authors**: Yuandong Wang 0002, Yao Cui, Yuxin Zhao, Zhen Yang 0034, Yangfu Zhu, Zhenzhou Shao
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.2198>
- **DOI**: 10.18653/V1/2026.ACL-LONG.2198
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

A university-level multimodal math benchmark with original, hand-drawn, photographed and text-only variants of each problem, on which a model with no image beats its own multimodal variants and GPT-5.

## Problem

Multimodal math benchmarks report strong overall performance but seldom isolate the role of the image, so whether vision-language models genuinely use visual understanding or lean on linguistic priors is unresolved.

## Contributions

- MathSight, a university-level multimodal math benchmark with per-problem original, hand-drawn, photo-captured and text-only variants
- A controlled design that quantifies the marginal contribution of visual input
- The finding that visual contribution diminishes with increasing problem difficulty
- The result that Qwen3-VL without image input surpasses its multimodal variants and GPT-5

## Method

MathSight is a university-level multimodal mathematical reasoning benchmark built to disentangle and quantify the effect of visual input. Each problem carries multiple visual variants — original, hand-drawn, photo-captured — plus a text-only condition for controlled comparison. The text-only arm is the decisive control: if a model scores as well without the image, the image was not contributing.

## Results

The contribution of visual information diminishes as problem difficulty increases. Qwen3-VL with no image input surpasses both its own multimodal variants and GPT-5.

## Limitations

No aggregate numbers in the abstract beyond the ordering of that one comparison, and the full model list is not given. A text-only arm that matches the multimodal arm shows the image is unnecessary for these items, which may indicate the problems are under-specified visually rather than that models cannot see — the benchmark's own construction is implicated in its headline result. That a model beats itself without the image also raises the possibility that image tokens actively interfere, which is a different claim from failing to use them.

## Why it matters here

- **reasoning-evaluation**: Supplies the control that multimodal reasoning benchmarks generally omit — run the same problem with no image — and the result is that the image is often unnecessary and sometimes harmful. That makes multimodal math scores partly a text benchmark, which parallels doi:10.18653/v1/2026.acl-long.826's finding that ARC scores are largely a perception benchmark: in both cases the reported quantity is not the intended one, in opposite directions. With VisAidMath and ErrorRadar this drain now holds four multimodal reasoning benchmarks whose common conclusion is that the modality split is mismeasured, and the text-only ablation is the cheapest of the four controls to adopt.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), linguistic prior, modality ablation, [perception bottleneck](../../../../wiki/concepts/perception-bottleneck.md), [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md)
- **Methods**: MathSight, modality ablation, visual variant perturbation
- **Datasets**: MathSight

Tags: `benchmark`, `multimodal`, `math reasoning`, `modality ablation`, `construct validity`

## Abstract

Recent advances in Vision-Language Models (VLMs) have achieved impressive progress in multimodal mathematical reasoning. Yet, howmuch visual information truly contributes to reasoning remains unclear. Existing benchmarks report strong overall performance but seldom isolate the role of the image modality, leaving open whether VLMs genuinely leverage visual understanding or merely depend on linguistic priors. To address this, we present MathSight, a university-level multimodal mathematical reasoning benchmark designed to disentangle and quantify the effect of visual input. Each problem includes multiple visual variants—original, hand-drawn, photocaptured—and a text-only condition for controlled comparison. Experiments on state-of-the-art VLMs reveal a consistent trend: the contribution of visual information diminishes with increasing problem difficulty. Remarkably, Qwen3-VL without any image input surpasses both its multimodal variants and GPT-5, underscoring the need for benchmarks like MathSight to advance genuine vision-grounded reasoning in future models. The project page is available at https://cnu-bot-group.github.io/MathSight/.

---

Record id: `doi:10.18653/v1/2026.acl-long.2198`
