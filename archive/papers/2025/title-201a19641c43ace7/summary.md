<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/120231>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces a counterfactual intervention framework to test whether large reasoning models' intermediate thinking-draft steps and final answers are causally faithful to each other, finding they often are not.

## Problem

Large reasoning models produce a thinking draft before their final answer, but it is unclear whether that draft causally determines the steps and answer that follow it or is post-hoc rationalization; this bears on whether the draft can be trusted for monitoring, interpretation and control.

## Contributions

- A counterfactual intervention framework to measure faithfulness of LRM thinking drafts along two dimensions: intra-draft (whether steps causally influence later steps and the conclusion) and draft-to-answer (whether the final answer depends on the draft's stated conclusion).
- An empirical evaluation across six state-of-the-art LRMs showing selective faithfulness to intermediate steps and frequent failure of final answers to align with the draft's own conclusion.

## Method

The paper defines two evaluation axes and probes them with counterfactual step insertions and perturbations to the draft's concluding logic: (1) Intra-Draft Faithfulness inserts counterfactual content into individual reasoning steps and checks whether it causally changes subsequent steps and the final draft conclusion; (2) Draft-to-Answer Faithfulness perturbs the draft's concluding logic and checks whether the final answer changes accordingly, testing logical dependence of the answer on the draft.

## Results

Across six state-of-the-art LRMs, the paper reports selective faithfulness to intermediate reasoning steps and frequent failure of final answers to be faithfully aligned with the draft's stated conclusions; no specific numeric faithfulness scores are given in the abstract.

## Limitations

The abstract does not report which six LRMs were tested, on what tasks/benchmarks, or specific faithfulness rates; no discussion of reasoning length, compute budget, or efficiency is present in the material available.

## Why it matters here

- **overthinking**: This paper is about whether a reasoning model's thinking draft is causally faithful to its own conclusion, not about how long that draft is or whether its length is well matched to the problem. It shares only the generic term 'large reasoning model' with the overthinking topic and does not address reasoning-length/accuracy tradeoffs, test-time compute scaling, or stopping criteria.

## Entities

- **Concepts**: thinking draft faithfulness, counterfactual intervention, intra-draft faithfulness, draft-to-answer faithfulness
- **Methods**: counterfactual step insertion, counterfactual intervention framework
- **Datasets**: _none recorded_

Tags: `faithfulness`, `interpretability`, `chain-of-thought`, `counterfactual-evaluation`, `large-reasoning-models`

## Abstract

Abstract Large Reasoning Models (LRMs) have significantly enhanced their capabilities in complex problem-solving by introducing a thinking draft that enables multi-path Chain-of-Thought explorations before producing final answers. Ensuring the faithfulness of these intermediate reasoning processes is crucial for reliable monitoring, interpretation, and effective control. In this paper, we propose a systematic counterfactual intervention framework to rigorously evaluate thinking draft faithfulness . Our approach focuses on two complementary dimensions: (1) Intra-Draft Faithfulness , which assesses whether individual reasoning steps causally influence subsequent steps and the final draft conclusion through counterfactual step insertions; and (2) Draft-to-Answer Faithfulness , which evaluates whether final answers are logically consistent with and dependent on the thinking draft, by perturbing the draft’s concluding logic. We conduct extensive experiments across six state-of-the-art LRMs. Our findings show that current LRMs demonstrate selective faithfulness to intermediate reasoning steps and frequently fail to faithfully align with the draft conclusions. These results underscore the need for more faithful and interpretable reasoning in advanced LRMs.

---

Record id: `title:201a19641c43ace7`
