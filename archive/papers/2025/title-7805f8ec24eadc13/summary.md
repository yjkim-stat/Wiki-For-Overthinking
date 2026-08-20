<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/45540>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

The first systematic study of overthinking in o1-like reasoning models, introducing outcome/process efficiency metrics and a self-training method that trims redundant reasoning on easy problems without hurting accuracy.

## Problem

Long chain-of-thought reasoning models allocate excessive computational resources (tokens, thinking rounds) to problems that are already simple or whose answer is already evident, wasting compute for no accuracy benefit; there was no established way to measure or mitigate this.

## Contributions

- First comprehensive study of overthinking in o1-like reasoning models: excessive computational resources spent on simple problems for minimal benefit.
- Introduces efficiency metrics from both outcome and process perspectives to evaluate how rationally o1-like models use compute.
- Proposes self-training-based strategies to mitigate overthinking that reduce computational overhead without compromising accuracy.

## Method

The authors define efficiency metrics that separately assess outcome efficiency (whether extra compute changes the final answer) and process efficiency (how much of the generated reasoning chain is redundant), applied to o1-like long chain-of-thought reasoning models across problems of varying difficulty. Using a self-training paradigm, they then train the model to produce shorter, less redundant reasoning without changing its accuracy.

## Results

Experimental results show the proposed self-training approach reduces computational overhead (token/reasoning-round usage) while preserving model accuracy across GSM8K, MATH500, GPQA and AIME; the abstract does not give specific percentage figures.

## Limitations

The abstract does not give specific numeric reductions in token usage or accuracy deltas; details of the self-training procedure and which model(s) it was applied to are not stated in the abstract.

## Why it matters here

- **overthinking**: This paper is the origin study of the overthinking phenomenon that the tracked topic is named after: it defines the problem, proposes metrics to measure wasted reasoning compute, and demonstrates a concrete mitigation (self-training) that reduces token usage while preserving accuracy across GSM8K, MATH500, GPQA and AIME.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), outcome and process efficiency metrics, self-training for reasoning-length reduction
- **Methods**: self-training (preference-based), outcome/process efficiency metrics
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), MATH500, [GPQA](../../../../wiki/datasets/gpqa.md), [AIME](../../../../wiki/datasets/aime.md)

Tags: `overthinking`, `reasoning-efficiency`, `chain-of-thought`, `self-training`, `o1-like-models`

---

Record id: `title:7805f8ec24eadc13`
