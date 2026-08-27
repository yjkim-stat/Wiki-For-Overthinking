<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008007>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Studies sequential and parallel test-time compute scaling for deep-search LLM agents and shows that allocating modest compute to a cheap verifier outperforms pushing sequential generation length further.

## Problem

How to scale test-time compute for deep-search agents efficiently, given that naive sequential scaling (longer generation via budget forcing) helps initially but eventually degrades performance.

## Contributions

- Shows sequential test-time scaling (budget forcing) improves deep-search agent performance initially but degrades it if pushed further.
- Introduces the use of asymmetric verification (verification cheaper than generation) to get substantial gains from a modest amount of verifier compute rather than more generation.
- Builds 'Heavy' variants of flagship open-source deep-research agents via test-time scaling that match or exceed proprietary systems on BrowseComp and GAIA.

## Method

The paper studies two test-time compute scaling axes for deep-search agents built on LLMs: sequential scaling (lengthening generation, e.g. via budget forcing) and parallel scaling (verifying and selecting among multiple candidate outputs). It exploits domains where verifying a candidate answer is much cheaper than generating it (asymmetric verification), allocating a modest amount of compute to a verifier to select among parallel rollouts instead of relying purely on longer sequential generation.

## Results

Deep-research 'Heavy' agents built with this approach gain up to 27 absolute points on BrowseComp over their base versions; GLM-4.5 Heavy reaches 54.0% on BrowseComp and 66.0% on GAIA, and 68.0% on xbench-DeepSearch, comparable to proprietary systems such as OpenAI Deep Research; Tongyi-DeepResearch Heavy reaches 69.0% on BrowseComp.

## Limitations

The abstract does not report where or by how much extended sequential scaling starts to hurt performance, nor does it detail cost/latency overhead of the verifier, or test domains lacking the asymmetric-verification property.

## Why it matters here

- **overthinking**: Directly documents a stopping-point problem for sequential test-time scaling: budget forcing (making the model 'think'/search longer) helps up to a point and then degrades results, and the paper's fix is to redirect added test-time compute into verification rather than more generation -- a concrete instance of choosing where to spend compute instead of just extending reasoning length.

## Entities

- **Concepts**: asymmetric verification, sequential vs. parallel test-time scaling, budget forcing
- **Methods**: [budget forcing](../../../../wiki/methods/budget-forcing.md), asymmetric verification, parallel test-time scaling (verify-and-select)
- **Datasets**: [BrowseComp](../../../../wiki/datasets/browsecomp.md), [GAIA](../../../../wiki/datasets/gaia.md), xbench-DeepSearch

Tags: `test-time-scaling`, `verification`, `deep-search-agents`, `budget-forcing`, `parallel-scaling`

---

Record id: `title:711c479b500244c5`
