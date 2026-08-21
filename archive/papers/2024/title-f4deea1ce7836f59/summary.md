<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph

- **Authors**: _unknown_
- **Venue**: NeurIPS 2024
- **Published**: 2024-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2024/poster/96593>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A benchmark-construction framework that extracts the reasoning graph behind each item in an existing benchmark and perturbs it to generate new test items at controlled complexity levels, then measures how 15 LLMs degrade as complexity rises.

## Problem

Static benchmarks are vulnerable to data contamination — items may have been seen in training — and they cannot adapt as model capability improves, so a saturated benchmark stops distinguishing models. What is needed is a way to produce fresh evaluation data whose difficulty can be dialled up deliberately, while staying close enough to the original benchmark that scores remain interpretable.

## Contributions

- DARG, a framework that dynamically extends existing benchmarks by extracting and perturbing per-item reasoning graphs.
- A mechanism for generating test items at controlled complexity levels while retaining linguistic diversity similar to the source benchmark.
- Use of a code-augmented LLM to verify label correctness of the generated items.
- An evaluation across reasoning tasks in four domains with 15 state-of-the-art LLMs, showing near-universal accuracy decline as complexity rises.
- The finding that LLMs display more bias on higher-complexity generated data.

## Method

For each data point in an existing benchmark, DARG extracts a reasoning graph: an explicit structure representing the reasoning required to solve that item. The graph is then perturbed to produce new test items — the perturbations change graph properties such as depth or width, which is what 'controlled complexity' means here — while the surface language stays similar in diversity to the original benchmark, so the new items are not obviously out of distribution. Because a perturbed graph implies a different answer, label correctness is verified by a code-augmented LLM rather than assumed. The framework is applied to reasoning tasks in four domains and used to evaluate 15 state-of-the-art LLMs across complexity levels.

## Results

Applied to reasoning tasks across four domains with 15 state-of-the-art LLMs. Almost all models lose accuracy as generated complexity increases, and some drop sharply. Models also exhibit more bias when evaluated on higher-complexity DARG-generated data than on the original benchmarks. The abstract states no per-model accuracy figures, no per-domain numbers and no bias metric values, so the size of the drops cannot be given from the available material.

## Limitations

The reported degradations are stated qualitatively in the available material ('almost all', 'certain LLMs exhibit significant drops') without per-model numbers, so the effect size is not established here. Correctness of generated labels rests on a code-augmented LLM, which makes the evaluation's ground truth partly model-generated. The method presupposes that an item's reasoning can be extracted as a graph, which restricts it to tasks with recoverable structure and not to open-ended reasoning. Complexity is defined by graph perturbation, which is a proxy for difficulty rather than difficulty itself, and the claim that linguistic diversity is preserved is asserted rather than quantified in the abstract.

## Why it matters here

- **overthinking**: Tangential. The task matched on 'adaptive reasoning', but in this paper that phrase describes how test items are constructed — a reasoning graph is adaptively perturbed to make a harder question — not how a model adapts its reasoning effort. The paper measures accuracy against item complexity; it does not measure reasoning length, token budget, or when a model should stop or continue thinking, and it proposes no inference-time mechanism. The one indirect bearing on the topic is that DARG supplies a way to vary problem difficulty on a controlled axis while holding the surface form roughly fixed, which is the independent variable an overthinking study needs if it wants to ask whether a model's spending tracks what a problem actually requires — but the paper itself never asks that question, and reports no length or compute measurements to support it. Useful as possible evaluation machinery, not as a finding about overthinking.

## Entities

- **Concepts**: dynamic evaluation, data contamination, controlled complexity, [reasoning graph](../../../../wiki/concepts/reasoning-graph.md), benchmark saturation, linguistic diversity, label verification, model bias under complexity
- **Methods**: DARG, [reasoning graph extraction](../../../../wiki/methods/reasoning-graph-extraction.md), reasoning graph perturbation, code-augmented LLM label verification
- **Datasets**: existing reasoning benchmarks across four domains, extended by DARG (individual benchmark names not given in the supplied material)

Tags: `benchmark generation`, `dynamic evaluation`, `data contamination`, `reasoning graph`, `task complexity`, `llm evaluation`, `bias`, `tangential`

## Abstract

Abstract The current paradigm of evaluating Large Language Models (LLMs) through static benchmarks comes with significant limitations, such as vulnerability to data contamination and a lack of adaptability to the evolving capabilities of LLMs. Therefore, evaluation methods that can adapt and generate evaluation data with controlled complexity are urgently needed. In this work, we introduce Dynamic Evaluation of LLMs via Adaptive Reasoning Graph Evolvement (DARG) to dynamically extend current benchmarks with controlled complexity and diversity. Specifically, we first extract the reasoning graphs of data points in current benchmarks and then perturb the reasoning graphs to generate novel testing data. Such newly generated test samples can have different levels of complexity while maintaining linguistic diversity similar to the original benchmarks. We further use a code-augmented LLM to ensure the label correctness of newly generated data. We apply our DARG framework to diverse reasoning tasks in four domains with 15 state-of-the-art LLMs. Experimental results show that almost all LLMs experience a performance decrease with increased complexity and certain LLMs exhibit significant drops. Additionally, we find that LLMs exhibit more biases when being evaluated via the data generated by DARG with higher complexity levels. These observations provide useful insights into how to dynamically and adaptively evaluate LLMs.

---

Record id: `title:f4deea1ce7836f59`
