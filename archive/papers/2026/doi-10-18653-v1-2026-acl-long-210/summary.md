<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Language Models

- **Authors**: Yang Liu, Hongming Li, Melissa Xiaohui Qin, Chao Huang, Qiankun Liu
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.210>
- **DOI**: 10.18653/V1/2026.ACL-LONG.210
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Consolidates multiword-expression resources into one evaluation suite covering idioms, noun compounds and verbal constructions across extraction, classification and interpretation tasks.

## Problem

Semantic phrase processing is scattered across separate multiword-expression resources with no unified testbed, so how language models handle non-trivial semantic phrases cannot be assessed consistently.

## Contributions

- SemanticQA, a unified evaluation suite consolidating existing multiword-expression resources
- Coverage of lexical collocations plus idiomatic expressions, noun compounds and verbal constructions
- Assessment across extraction, classification and interpretation tasks and their sequential compositions
- A released evaluation harness and data

## Method

SemanticQA consolidates existing MwE resources and reorganizes them into a unified testbed. It covers general lexical phenomena such as lexical collocations plus three fine-grained categories — idiomatic expressions, noun compounds, verbal constructions. Models of diverse architectures and scales are assessed on extraction, classification and interpretation, and on sequential compositions of those tasks; the compositions are what test whether ability on the parts predicts ability on the chain.

## Results

Substantial performance variation is found, particularly on tasks requiring semantic reasoning, highlighting differences in reasoning efficacy and semantic understanding across models. No numbers or model names are given in the abstract.

## Limitations

No quantitative results and no named models in the abstract. Built by consolidating existing resources, so it inherits their annotation conventions and any contamination in them, and no contamination check is mentioned. 'Semantic reasoning' is not distinguished from lexical knowledge, which is the distinction the benchmark would need to make to support claims about reasoning.

## Why it matters here

- **reasoning-evaluation**: A thin fit: it measures lexical-semantic competence and calls the harder parts semantic reasoning, without separating the two. Its one methodologically interesting feature for this topic is the sequential task composition, which tests whether performance on extraction and classification predicts performance on their chain — the same compositional-drop question AgentCoMa answers with a measured ~30% gap, but here without a reported number. Read alongside arxiv:2608.04670 on Italian proverbs it belongs to a small cluster on figurative and culturally embedded language, where the archive currently has no reasoning-specific finding.

## Entities

- **Concepts**: multiword expression, semantic understanding, [compositional generalization](../../../../wiki/concepts/compositional-generalization.md), [figurative language](../../../../wiki/concepts/figurative-language.md), [construct validity](../../../../wiki/concepts/construct-validity.md)
- **Methods**: SemanticQA, sequential task composition, benchmark consolidation
- **Datasets**: SemanticQA

Tags: `benchmark`, `multiword expressions`, `semantics`, `evaluation suite`, `thin-evidence`

## Abstract

We present SemanticQA, an evaluation suite designed to assess language models (LMs) in semantic phrase processing tasks. The benchmark consolidates existing multiword expression (MwE) resources and reorganizes them into a unified testbed. It covers both general lexical phenomena, such as lexical collocations, and three fine-grained categories: idiomatic expressions, noun compounds, and verbal constructions. Through SemanticQA, we assess LMs of diverse architectures and scales in extraction, classification, and interpretation tasks, as well as sequential task compositions. We reveal substantial performance variation, particularly on tasks requiring semantic reasoning, highlighting differences in reasoning efficacy and semantic understanding of LMs, providing insights for pushing LMs with stronger comprehension on non-trivial semantic phrases. The evaluation harness and data of SemanticQA are available at https://github.com/jacklanda/SemanticQA.

---

Record id: `doi:10.18653/v1/2026.acl-long.210`
