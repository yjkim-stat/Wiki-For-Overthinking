<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Multi-component Causal Tracing in Large Language Models

- **Authors**: Zirui Yan, Dennis Wei, Dmitriy A. Katz, Prasanna Sattigeri, Ali Tajer
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.154>
- **DOI**: 10.18653/V1/2026.ACL-LONG.154
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Generalizes causal tracing from one component or layer at a time to selecting subsets of components jointly, by relaxing the combinatorial search into a continuous one over soft interventions.

## Problem

Causal tracing intervenes on internal representations to quantify the pathways linking inputs or computations to a metric of interest. Prior work traces a single component or a single layer, which cannot identify subsets that matter jointly, and the multi-component problem is combinatorial.

## Contributions

- A unified framework for causally tracing multiple components simultaneously against a target metric
- Support for flexible interventions over a range of metrics including accuracy and fairness
- An efficient algorithm using soft interventions and a metric transformation that relaxes the combinatorial subset search into a continuous one while yielding binary selections
- Reported gains over existing causal-tracing baselines

## Method

A unified framework traces multiple components simultaneously, identifying the subsets — attention heads, MLP neurons — most critical to a target metric such as accuracy or fairness, with flexible interventions applicable to a range of metrics. The combinatorial complexity is handled by an algorithm using soft interventions plus a carefully designed metric transformation, converting the discrete subset search into a continuous problem solvable efficiently under suitable constraints while still yielding proper binary selection decisions. The continuous relaxation is the whole enabling step.

## Results

The method efficiently identifies subsets of components with high impact on the target metric, outperforming existing baselines. No numbers, models or baselines are named in the abstract.

## Limitations

No quantitative results, models or baselines in the abstract. Soft interventions are a relaxation, so a subset selected in the continuous problem is not guaranteed optimal for the discrete one; the constraints under which the relaxation is tight are unstated. The metric transformation is described as carefully designed, which suggests it must be constructed per metric. Selection is relative to a chosen target metric, so 'critical' is metric-relative rather than a property of the component.

## Why it matters here

- **reasoning-interpretability**: Addresses a limitation that undercuts much of the archive's circuit work directly: single-component tracing can miss components that only matter together, and redundant components can each look unimportant in isolation. A joint-subset method is what the archive's modularity dispute needs, since claims that a capability is or is not localized depend on whether the search could see distributed sets at all. The catch is that criticality remains defined relative to a chosen target metric, so this makes the search tractable without making 'important' model-intrinsic. No reasoning-specific result is reported, so the application to reasoning circuits is open.

## Entities

- **Concepts**: causal tracing, [localization](../../../../wiki/concepts/localization.md), [modularity](../../../../wiki/concepts/modularity.md), [attention head](../../../../wiki/concepts/attention-head.md), [superposition](../../../../wiki/concepts/superposition.md), combinatorial search, soft intervention, continuous relaxation
- **Methods**: [causal tracing](../../../../wiki/methods/causal-tracing.md), [causal mediation analysis](../../../../wiki/methods/causal-mediation-analysis.md), [activation patching](../../../../wiki/methods/activation-patching.md), soft intervention, continuous relaxation
- **Datasets**: _none recorded_

Tags: `causal tracing`, `multi-component`, `localization`, `interpretability`, `optimization`

## Abstract

Causal tracing systematically intervenes on a large language model's (LLM's) internal representations to uncover and quantify the causal pathways linking specific inputs or computations to specific metrics of interest, quantifying the LLM's behavior. Building on previous single-component or single-layer studies, this paper presents a unified framework for causally tracing multiple components simultaneously. This framework systematically identifies the subsets of components (e.g., attention heads and multi-layer perceptron neurons) most critical to a desired target performance metric (e.g., accuracy and fairness). This is achieved by incorporating flexible interventions applied to a wide range of desired metrics. To address the combinatorial complexity of the multi-component problem, an efficient algorithm is designed that leverages soft interventions and a carefully designed metric transformation, converting the combinatorial search problem into a continuous one that can be solved efficiently under proper constraints, thereby generating proper binary decisions for selecting components. Experimental results demonstrate that the proposed method efficiently identifies subsets of the model's components that have a high impact on the target metric, outperforming existing baseline approaches. Our code is available at https://github.com/ZiruiYan/multi-component-causal-tracing.

---

Record id: `doi:10.18653/v1/2026.acl-long.154`
