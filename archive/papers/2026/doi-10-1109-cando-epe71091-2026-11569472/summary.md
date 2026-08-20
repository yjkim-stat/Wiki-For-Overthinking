<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning models, test-time compute, self refinement

- **Authors**: Juhász Levente Zsolt
- **Venue**: 2026 IEEE 8th International Conference and Workshop Óbuda on Electrical and Power Engineering (CANDO-EPE)
- **Published**: 2026-05-26
- **Source**: semanticscholar
- **Link**: <https://www.semanticscholar.org/paper/0249f6192c6a7cb170fd1b45c5d3e5607f5b9f92>
- **DOI**: 10.1109/CANDO-EPE71091.2026.11569472
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A short empirical study applying self-refinement test-time compute scaling to a small parameter-efficient reasoning model (Qwen 0.6B) to examine gains in mathematical-logical performance.

## Problem

How to enhance the mathematical-logical performance of reasoning-model LLMs, examined here specifically for a small, parameter-efficient model where full test-time scaling budgets may be less affordable.

## Contributions

- Examines the fundamental characteristics of reasoning models and the methodologies used to enhance their mathematical-logical performance.
- Presents an empirical study applying the self-refinement test-time compute scaling technique to a parameter-efficient model (Qwen 0.6B).

## Method

Not stated beyond the abstract: the paper applies a self-refinement test-time compute scaling technique to a parameter-efficient reasoning model (Qwen 0.6B), presumably having the model iteratively critique and revise its own output to improve mathematical-logical performance, but the mechanism, prompts, and iteration budget are not described in the available material.

## Results

Not stated in the available abstract; no numbers, benchmarks, or comparisons are given, and the full text could not be retrieved.

## Limitations

The payload provides only the abstract (no attached PDF, no reachable full text found); no numerical results, benchmark names, or stated limitations are available from the accessible material. The paper appears to be a short workshop-style contribution (IEEE CANDO-EPE 2026) and its full text could not be retrieved.

## Why it matters here

- **overthinking**: On-topic by subject matter: it directly studies a test-time compute scaling method (self-refinement) applied to a reasoning model, which is squarely within the topic's scope of test-time compute scaling and the accuracy/efficiency tradeoff of reasoning. However, the only available material is a brief abstract with no numerical results, benchmarks, or discussion of when self-refinement helps versus wastes compute (i.e. no explicit overthinking/underthinking analysis), so its actual contribution to the topic cannot be assessed beyond the fact that it evaluates one scaling technique on one small model.

## Entities

- **Concepts**: self-refinement, [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), parameter-efficient reasoning models
- **Methods**: Self-refinement, Test-time compute scaling, Qwen 0.6B
- **Datasets**: _none recorded_

Tags: `self-refinement`, `test-time-compute`, `reasoning-models`, `qwen`, `parameter-efficient`

## Abstract

Reasoning models represent a specialized class of Large Language Models (LLMs) that are significantly advancing the field of artificial intelligence. This paper examines the fundamental characteristics of reasoning models and explores the methodologies employed to enhance their mathematical-logical performance. The empirical study evaluates the application of the self-refinement test-time compute scaling technique on a parameter-efficient model (Qwen 0.6B). Keywords—large language models, reasoning models, inference-time computing, self refinement

---

Record id: `doi:10.1109/cando-epe71091.2026.11569472`
