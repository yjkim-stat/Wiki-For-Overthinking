<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasonAny: Incorporating Reasoning Capability to Any Model via Simple and Effective Model Merging

- **Authors**: Junyao Yang, Chen Qian 0010, Wen Shen, Yong Liu 0007, Jing Shao, Dongrui Liu
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.2201>
- **DOI**: 10.18653/V1/2026.ACL-LONG.2201
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

Merges a reasoning model into a domain-specialized one after finding that reasoning ability resides in low-gradient-sensitivity parameter regions rather than high-magnitude ones.

## Problem

Equipping domain-specialized models with long chain-of-thought reasoning — 'Reasoning + X' — is difficult. Model merging is a promising training-free route, but existing methods suffer a destructive performance collapse that both weakens reasoning depth and compromises domain utility.

## Contributions

- The finding that reasoning ability predominantly resides in low-gradient-sensitivity parameter regions rather than high-magnitude parameters
- ReasonAny, a model-merging framework for combining reasoning with domain specialization without performance collapse

## Method

The paper identifies a counter-intuitive phenomenon underlying the collapse: reasoning ability predominantly resides in parameter regions with low gradient sensitivity, contrary to the common assumption that capabilities correspond to high-magnitude parameters. ReasonAny is a merging framework motivated by that insight. The abstract available from the ACL Anthology is truncated mid-sentence, so the mechanism by which ReasonAny resolves the collapse is not recorded here.

## Results

_not recorded_

## Limitations

The published abstract is truncated, so no method detail beyond the motivating insight and no results are available. The claim that reasoning lives in low-gradient-sensitivity regions is the substantive finding and the evidence for it is not in the retrievable text. This record needs the full paper before anything is built on it.

## Why it matters here

- **reasoning-training**: If the localization claim holds, it bears directly on this topic's modularity thread: reasoning would sit in parameter regions that magnitude-based and sensitivity-based methods systematically overlook, which would explain why merging and pruning damage it disproportionately. It also offers a parameter-space account of the capability interference that findings-acl.1717 documents behaviourally as general-capability forgetting under RLVR. The evidence is unavailable from the truncated abstract, so this is a claim to verify rather than one to rely on.

## Entities

- **Concepts**: model merging, [localization](../../../../wiki/concepts/localization.md), [modularity](../../../../wiki/concepts/modularity.md), gradient sensitivity, capability interference, [catastrophic forgetting](../../../../wiki/concepts/catastrophic-forgetting.md)
- **Methods**: [model merging](../../../../wiki/methods/model-merging.md), ReasonAny
- **Datasets**: _none recorded_

Tags: `model merging`, `localization`, `reasoning transfer`, `truncated-abstract`

## Abstract

Large Reasoning Models (LRMs) with long chain-of-thought reasoning have recently achieved remarkable success. Yet, equipping domain-specialized models with such reasoning capabilities, referred to as “Reasoning + X”, remains a significant challenge. While model merging offers a promising training-free solution, existing methods often suffer from a destructive performance collapse: existing methods tend to both weaken reasoning depth and compromise domain-specific utility. Interestingly, we identify a counter-intuitive phenomenon underlying this failure: reasoning ability predominantly resides in parameter regions with low gradient sensitivity, contrary to the common assumption that domain capabilities correspond to high-magnitude parameters. Motivated by this insight, we propose ReasonAny, a novel merging framework that resolves the reasoning–domain performance collapse

---

Record id: `doi:10.18653/v1/2026.acl-long.2201`
