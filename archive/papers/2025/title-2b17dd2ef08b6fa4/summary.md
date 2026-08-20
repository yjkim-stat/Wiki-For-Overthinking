<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Let LRMs Break Free from Overthinking via Self-Braking Tuning

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115532>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

Introduces Self-Braking Tuning, which trains a large reasoning model to detect and stop its own redundant reasoning steps, cutting token usage by up to 60% with comparable accuracy on math benchmarks.

## Problem

Large reasoning models generate longer chains of thought to improve accuracy, but this produces substantial redundant reasoning (overthinking) and high computational overhead; existing fixes typically rely on external interventions rather than letting the model regulate itself.

## Contributions

- Proposes Self-Braking Tuning (SBT), a framework that lets a reasoning model regulate its own reasoning length internally, without external control mechanisms (e.g. external length budgets or separate stopping controllers).
- Constructs overthinking identification metrics based on standard (gold) answers to systematically detect redundant reasoning steps in a chain of thought.
- Builds training data with adaptive reasoning lengths and an accompanying 'braking prompt' mechanism so the model learns when to stop reasoning at an appropriate point.
- Shows the method reduces token consumption by up to 60% while keeping accuracy comparable to unconstrained models, across AIME, AMC, MATH500 and GSM8K.

## Method

SBT first defines metrics, based on comparison to standard/gold answers, that identify which steps in a reasoning trajectory are redundant (i.e. overthinking). It uses these metrics to construct training data with variable, adaptively-lengthed reasoning traces and to derive a 'braking prompt' signal. The model is then tuned on this data so it learns, during its own generation, to detect when further reasoning is unnecessary and to terminate at that point, rather than relying on an external controller or fixed length budget.

## Results

Reduces token consumption by up to 60% while maintaining accuracy comparable to unconstrained models, evaluated on AIME, AMC, MATH500 and GSM8K.

## Limitations

Only the abstract was available for this task (no PDF attachment); the paper's own stated limitations (e.g. generalization beyond math benchmarks, robustness of the overthinking-identification metric, behavior on harder or non-math tasks) are not given in the abstract and so are left unstated here.

## Why it matters here

- **overthinking**: This is a direct, central treatment of the topic: it defines metrics for detecting overthinking, builds training data and a mechanism (braking prompts) that teach a model to stop reasoning at the right point on its own, and reports a concrete accuracy/efficiency tradeoff (up to 60% token reduction at comparable accuracy across AIME, AMC, MATH500, GSM8K).

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), redundant reasoning steps, self-regulated reasoning termination, adaptive reasoning length, braking prompt mechanism
- **Methods**: Self-Braking Tuning (SBT), overthinking identification metrics, braking prompt mechanism
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md), [AMC](../../../../wiki/datasets/amc.md), MATH500, [GSM8K](../../../../wiki/datasets/gsm8k.md)

Tags: `overthinking`, `self-braking-tuning`, `reasoning-length`, `efficiency`, `chain-of-thought`, `math-reasoning`

## Abstract

Abstract Large reasoning models (LRMs), such as OpenAI o1 and DeepSeek-R1, have significantly enhanced their reasoning capabilities by generating longer chains of thought, demonstrating outstanding performance across a variety of tasks. However, this performance gain comes at the cost of a substantial increase in redundant reasoning during the generation process, leading to high computational overhead and exacerbating the issue of overthinking. Although numerous existing approaches aim to address the problem of overthinking, they often rely on external interventions. In this paper, we propose a novel framework, Self-Braking Tuning (SBT), which tackles overthinking from the perspective of allowing the model to regulate its own reasoning process, thus eliminating the reliance on external control mechanisms. We construct a set of overthinking identification metrics based on standard answers and design a systematic method to detect redundant reasoning. This method accurately identifies unnecessary steps within the reasoning trajectory and generates training signals for learning self-regulation behaviors. Building on this foundation, we develop a complete strategy for constructing data with adaptive reasoning lengths and introduce an innovative braking prompt mechanism that enables the model to naturally learn when to terminate reasoning at an appropriate point. Experiments across mathematical benchmarks (AIME, AMC, MATH500, GSM8K) demonstrate that our method reduces token consumption by up to 60\% while maintaining comparable accuracy to unconstrained models.

---

Record id: `title:2b17dd2ef08b6fa4`
