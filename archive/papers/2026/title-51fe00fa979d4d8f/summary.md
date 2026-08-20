<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The First Impression Problem: Internal Bias Triggers Overthinking in Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011746>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Identifies an implicit first-guess bias formed on reading a question as a causal driver of overthinking in reasoning models, verified through counterfactual interventions and attention analysis.

## Problem

Reasoning models often generate redundant reasoning steps (overthinking), and the paper investigates why: it proposes that models form an implicit preliminary guess about the answer immediately on encountering a problem, and that conflict between this guess and subsequent reasoning triggers excessive reflection.

## Contributions

- Identifies internal bias (an implicit preliminary guess formed on first reading the question) as a causal trigger of overthinking in reasoning models
- Demonstrates the causal link with two counterfactual interventions: removing the input question after the model has read it, and manually injecting bias
- Shows via interpretability experiments that excessive attention to the input question is the mechanism through which internal bias shapes the reasoning trajectory
- Evaluates existing overthinking-mitigation methods and shows the internal-bias effect persists under all of them

## Method

The authors first show internal bias (a preliminary, often implicit answer guess formed immediately on reading a problem) correlates with overthinking across multiple models and reasoning tasks. They then run two counterfactual interventions: (1) removing the input question from context after the model has processed it, which reduces redundant reasoning steps, and (2) manually injecting a bias, which increases overthinking proportionally. Interpretability experiments analyzing attention to the input question are used to argue that heightened attention to the question is the channel through which internal bias propagates into the reasoning trajectory.

## Results

Removing the input question after the model has processed it reduces redundant reasoning across multiple complex reasoning tasks; manually injecting bias increases overthinking proportionally; the internal-bias effect persists across all overthinking-mitigation methods tested. Specific accuracy or token-count numbers were not available in the material reviewed.

## Limitations

The paper's own evaluation found that existing overthinking-mitigation methods did not remove the influence of internal bias under any tested condition; specific benchmarks/datasets used for validation were not stated in the material available.

## Why it matters here

- **overthinking**: Gives a causal mechanism for overthinking rather than just describing it: an implicit first-guess bias that, when it conflicts with subsequent reasoning, triggers excessive reflection. Counterfactual removal of the input question reduces redundant reasoning and injecting bias increases it, and the effect is shown to persist through existing overthinking-mitigation methods, which is directly relevant to understanding why current stopping/length-calibration methods fall short.

## Entities

- **Concepts**: internal bias, first-impression guess, overthinking as bias-conflict, attention to the input question
- **Methods**: [counterfactual intervention](../../../../wiki/methods/counterfactual-intervention.md), attention-based interpretability analysis
- **Datasets**: _none recorded_

Tags: `overthinking`, `internal-bias`, `interpretability`, `reasoning-models`, `attention`

---

Record id: `title:51fe00fa979d4d8f`
