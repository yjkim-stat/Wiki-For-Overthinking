<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics

- **Authors**: Atharva Naik, Prakam, Yash Mathur, Darsh Agrawal, Manav Nitin Kapadnis, Yuwei An, Clayton Marr, Carolyn P. Rosé, David R. Mortensen
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.432>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.432
- **Topics**: reasoning-evaluation, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.50

## In one line

An inductive-reasoning benchmark from historical linguistics that requires inducing cascades of string-rewrite programs, with automated contamination-resistant generation and controllable difficulty.

## Problem

Many benchmarks evaluate reasoning, but few isolate reasoning as a capability independent of domain knowledge — a model can score well by knowing the domain rather than by reasoning about it.

## Contributions

- A formulation of Sound Law Induction as multi-step Programming by Example, isolating inductive reasoning from domain knowledge
- PBEBench, with fully automated generation, controllable difficulty and ordering constraints for contamination-resistant evaluation
- Three constructed datasets showing a large gap between models using test-time compute or long CoT and those that do not
- The finding that solve rates remain below 5% on hard long-cascade instances even under expensive scaling, including for GPT-5 and gpt-oss-120b
- Evidence that PBEBench scores predict real Sound Law Induction performance better than other inductive reasoning benchmarks

## Method

Sound Law Induction from historical linguistics is formulated as a multi-step Programming by Example task: induce a cascade of string rewrite programs transforming inputs into target outputs. PBEBench generates such problems fully automatically with controllable difficulty and ordering constraints, which makes evaluation scalable and contamination-resistant — the problems are synthesized rather than collected, so they cannot be in pretraining data. Three datasets are constructed, and scores are checked against performance on real Sound Law Induction.

## Results

A large gap appears between models that use test-time compute or long chain-of-thought reasoning and those that do not. Recent models including GPT-5 and gpt-oss-120b show promise, but solve rates stay below 5% on hard PBEBench instances with long program cascades even under computationally expensive scaling strategies. PBEBench scores are more predictive of real Sound Law Induction performance than other inductive reasoning benchmarks are.

## Limitations

String-rewrite induction is a narrow formalism, so 'reasoning independent of domain knowledge' means independent of knowledge this formalism does not require, not domain-free in general. Below-5% solve rates on hard instances leave little dynamic range for comparing models at the top. Predictive validity is established against real Sound Law Induction, one downstream task.

## Why it matters here

- **reasoning-evaluation**: One of the stronger evaluation designs in this drain on two counts the archive has repeatedly found missing. Contamination is handled structurally by generating problems rather than by testing for leakage, and predictive validity is actually checked against a real downstream task instead of assumed — almost no benchmark here does the second. The below-5% hard-instance result also gives a rare unsaturated headroom measurement, and that it survives expensive test-time scaling is a limit on scaling rather than on any one model, which is directly relevant to the archive's test-time-compute thread.

## Entities

- **Concepts**: inductive reasoning, programming by examples, [benchmark contamination](../../../../wiki/concepts/benchmark-contamination.md), [construct validity](../../../../wiki/concepts/construct-validity.md), [test-time compute](../../../../wiki/concepts/test-time-compute.md), predictive validity, difficulty control, [compositional generalization](../../../../wiki/concepts/compositional-generalization.md)
- **Methods**: PBEBench, automated problem generation, programming by examples, sound law induction
- **Datasets**: PBEBench

Tags: `benchmark`, `inductive reasoning`, `contamination-resistant`, `programming by examples`, `predictive validity`

## Abstract

While many benchmarks evaluate the reasoning abilities of Large Language Models (LLMs), few isolate reasoning as a capability independent of domain knowledge. We introduce a new benchmark for inductive reasoning inspired by Sound Law Induction (SLI) in historical linguistics and formulated in a simple multi-step Programming by Example (PBE) framework. The task requires inducing a cascade of string rewrite programs that transform inputs into target outputs. We present PBEBench, a fully automated evaluation approach that generates such problems with controllable difficulty and ordering constraints, enabling scalable and contamination-resistant evaluation of sequential inductive reasoning. Using this approach, we construct three datasets that show a large gap between models that leverage test-time compute or long chain-of-thought reasoning and those that do not. Although recent models such as GPT-5 and gpt-oss-120b show promise, solve rates remain below 5% on hard PBEBench instances with long program cascades, even under computationally expensive scaling strategies. Finally, we show that PBEBench scores are more predictive of performance on real SLI than are other inductive reasoning benchmarks. We will release code and data to support further research.

---

Record id: `doi:10.18653/v1/2026.findings-acl.432`
