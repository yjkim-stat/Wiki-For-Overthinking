<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MTR-Bench: A Comprehensive Benchmark for Multi-Turn Reasoning Evaluation

- **Authors**: Xiaoyuan Li 0001, Keqin Bao, Yubo Ma, Moxin Li, Wenjie Wang 0007, Rui Men, Yichang Zhang, Fuli Feng, Dayiheng Liu
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.984>
- **DOI**: 10.18653/V1/2026.ACL-LONG.984
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50

## In one line

A fully automated multi-turn reasoning benchmark of 40 tasks and 3600 instances requiring interaction with an environment, on which frontier reasoning models fall short.

## Problem

Reasoning evaluation focuses predominantly on single-turn scenarios, leaving interactive tasks largely unexplored. The paper attributes the gap to two missing pieces: comprehensive datasets and scalable automatic evaluation protocols.

## Contributions

- MTR-Bench, a multi-turn interactive reasoning benchmark with 4 classes, 40 tasks and 3600 instances
- Fine-grained difficulty granularity and required interaction with environments
- A fully automated framework covering both dataset construction and evaluation
- Evidence that cutting-edge reasoning models fall short on multi-turn interactive reasoning

## Method

MTR-Bench comprises 4 classes, 40 tasks and 3600 instances, covering diverse reasoning capabilities with fine-grained difficulty granularity and requiring multi-turn interaction with environments. The framework is fully automated across both dataset construction and model evaluation, which is what makes the benchmark scalable without human intervention — the same property that lets it be regenerated rather than saturated.

## Results

Even cutting-edge reasoning models fall short on multi-turn interactive reasoning tasks. No numbers or model names are given in the abstract.

## Limitations

No quantitative results and no named models in the abstract. Fully automated construction bounds task realism to what can be generated and checked programmatically. Multi-turn evaluation confounds several abilities — state tracking, instruction adherence across turns, recovery from earlier mistakes — and the abstract does not indicate whether these are separated.

## Why it matters here

- **reasoning-evaluation**: Fills a real gap in this archive, which is dominated by single-turn math and QA: nearly every evaluation here scores one prompt and one answer, so nothing measures whether reasoning survives interaction. The automated-regeneration property also addresses contamination structurally rather than by checking for it, which the archive has found is almost never done. Without numbers the finding is directional, but the design is the contribution, and it pairs with the drain's agentic entries (AgentCoMa, AgentOPSD) as the evaluation side of the same shift toward multi-turn settings.

## Entities

- **Concepts**: multi-turn reasoning, interactive evaluation, [state tracking](../../../../wiki/concepts/state-tracking.md), difficulty granularity, automated benchmark construction, [construct validity](../../../../wiki/concepts/construct-validity.md)
- **Methods**: MTR-Bench, automated dataset construction, environment interaction
- **Datasets**: MTR-Bench

Tags: `benchmark`, `multi-turn`, `interactive`, `automated evaluation`, `state tracking`

## Abstract

Recent advances in Large Language Models (LLMs) have shown promising results in complex reasoning tasks. However, current evaluations predominantly focus on single-turn reasoning scenarios, leaving interactive tasks largely unexplored. We attribute it to the absence of comprehensive datasets and scalable automatic evaluation protocols. To fill these gaps, we present MTR-Bench for LLMs’ Multi-Turn Reasoning evaluation. Comprising 4 classes, 40 tasks and 3600 instances, MTR-Bench covers diverse reasoning capabilities, fine-grained difficulty granularity, and necessitates multi-turn interactions with the environments. Moreover, MTR-Bench features fully-automated framework spanning both dataset constructions and model evaluations, which enables scalable assessment without human interventions. Extensive experiments reveal that even the cutting-edge reasoning models fall short of multi-turn, interactive reasoning tasks. And the further analysis upon these results brings valuable insights for future research in interactive AI systems.

---

Record id: `doi:10.18653/v1/2026.acl-long.984`
