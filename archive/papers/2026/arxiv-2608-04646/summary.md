<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning

- **Authors**: Ian B. de Haan, Peter van der Putten, Max van Duijn
- **Venue**: cs.CL
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04646>
- **PDF**: <https://arxiv.org/pdf/2608.04646v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.73

## In one line

Tests reasoning models on Theory of Mind tasks and argues their gains are increased robustness to prompt and task perturbation rather than a new ToM-specific ability.

## Problem

LLMs score well on Theory of Mind tests, and it is disputed whether this reflects a genuine ToM capability. Reasoning models trained with RLVR improve on many benchmarks, so the question becomes whether their ToM gains are a ToM ability or something more general.

## Contributions

- Adaptations of machine-psychology ToM experiments for reasoning models
- Evidence that reasoning models are more robust to prompt and task perturbation on ToM tasks
- A robustness-based account of reasoning-model ToM gains, offered against a ToM-specific-ability account

## Method

Reasoning models are examined on ToM tasks using novel adaptations of machine-psychology experiments together with results from established ToM benchmarks. The analysis compares behaviour under prompt variations and task perturbations rather than only at a single canonical prompt, which separates 'gets the right answer' from 'keeps getting the right answer as the surface changes'.

## Results

Reasoning models consistently show increased robustness to prompt variations and task perturbations. The analysis attributes the gains at least partly to models being more robust at reaching the correct answer under variation, which the authors read as evidence for a robustness-based account rather than a ToM-specific ability.

## Limitations

The claim is a reading of the evidence, and the paper states the gains come 'at least partly' from robustness, so it does not exclude a ToM-specific component. Robustness and capability are not fully separated: a model with a genuine ToM mechanism would also be expected to be robust. No numbers are given in the abstract for the size of the robustness gain or the set of models tested.

## Why it matters here

- **reasoning-training**: Offers a deflationary account of what RLVR buys: not a new capability but reduced sensitivity to surface variation. That reframes benchmark gains as variance reduction, and it is testable — a robustness account predicts the gain shrinks when the baseline is evaluated over a prompt distribution rather than one prompt. It lines up with the archive's evaluation-noise thread, where the same failure of single-prompt measurement recurs.

## Entities

- **Concepts**: [theory of mind](../../../../wiki/concepts/theory-of-mind.md), [robustness](../../../../wiki/concepts/robustness.md), [prompt sensitivity](../../../../wiki/concepts/prompt-sensitivity.md), [construct validity](../../../../wiki/concepts/construct-validity.md), capability attribution
- **Methods**: [RLVR](../../../../wiki/methods/rlvr.md), prompt perturbation, machine psychology experiments
- **Datasets**: _none recorded_

Tags: `theory of mind`, `robustness`, `rlvr`, `construct validity`

## Abstract

Large language models (LLMs) have recently shown strong performance on Theory of Mind (ToM) tests, prompting debate about the nature and validity of the underlying capabilities. At the same time, reasoning-oriented LLMs trained via reinforcement learning with verifiable rewards have demonstrated notable improvements across a range of benchmarks. In this work, we examine the behavior of such reasoning models in ToM tasks using novel adaptations of machine psychological experiments together with results from established benchmarks. We observe that reasoning models consistently exhibit increased robustness to prompt variations and task perturbations. Our analysis suggests these gains come at least partly from models being more robust at reaching the correct answer under prompt and task variation. We read this as evidence for a robustness-based account rather than for a new ToM-specific ability.

---

Record id: `arxiv:2608.04646`
