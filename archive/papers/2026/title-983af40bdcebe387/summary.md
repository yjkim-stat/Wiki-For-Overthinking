<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10006442>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

TaTToo is a table-grounded Process Reward Model that reasons explicitly over tabular operations and uses tool-based verification to supervise test-time scaling for tabular reasoning, improving downstream policy LRMs by 30.9% at inference.

## Problem

Process Reward Models used to supervise test-time scaling of large reasoning models are widely adopted for text-only reasoning steps but struggle with table-specific operations (sub-table retrieval, schema interaction), creating a performance bottleneck for tabular reasoning.

## Contributions

- a scalable data curation pipeline producing 60k+ step-level table-verification annotations
- TaTToo, an 8B table-grounded PRM trained via cold-start SFT then tool-grounded RL
- an evaluation showing TaTToo outperforms a 72B text-only PRM baseline on 5 tabular reasoning benchmarks

## Method

Builds a scalable data curation pipeline producing 60k+ step-level annotations combining table verification rationales with tool-based executions, then trains TaTToo in two stages: cold-start supervised fine-tuning to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping.

## Results

Across 5 tabular reasoning benchmarks (numerical reasoning, fact-checking, data analysis), TaTToo improves downstream policy LRMs by 30.9% at inference and surpasses strong PRM baselines such as Qwen-2.5-Math-PRM-72B while using only 8B parameters; the abstract reports generalization across diverse test-time-scaling strategies but gives no further breakdown.

## Limitations

Not stated in the abstract beyond the domain scope (tabular reasoning); no quantitative comparison numbers besides the 30.9% aggregate figure are given.

## Why it matters here

- **overthinking**: Tangential: it is about supervising *where* test-time compute goes in tabular reasoning via a domain-specialized reward model, not about reasoning length or the accuracy/efficiency tradeoff directly, but it is an example of test-time-scaling supervision infrastructure that a length- or budget-aware PRM could build on.

## Entities

- **Concepts**: Process Reward Model, tool-grounded reward shaping, table-grounded reasoning supervision
- **Methods**: Process Reward Model (PRM), cold-start supervised fine-tuning, tool-grounded reinforcement learning
- **Datasets**: _none recorded_

Tags: `process-reward-model`, `test-time-scaling`, `tabular-reasoning`, `tool-use`

## Abstract

Abstract Process Reward Models (PRMs) have recently emerged as a powerful framework for enhancing the reasoning capabilities of large reasoning models (LRMs), particularly in the context of test-time scaling (TTS). However, their potential for supervising LRMs on tabular reasoning domains remains underexplored. Through detailed empirical analyses, we identify that existing PRMs, though widely adopted for supervising text-only reasoning steps, struggle with table-specific operations such as sub-table retrieval and schema interaction, leading to critical performance bottlenecks. To address this limitation, we propose TaTToo, a novel table-grounded PRM framework that (i) reasons explicitly over tabular reasoning steps and (ii) integrates tool-based verification to provide precise reward supervision. Concretely, we first design a scalable data curation pipeline that constructs over 60k high-quality step-level annotations by integrating table verification rationales with tool-based executions. Building on the collected data, we train TaTToo with a dual-stage paradigm: cold-start supervised fine-tuning to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping to align our model with table-based verification. We provide a comprehensive evaluation of the policy improvement induced by our newly designed PRM. Across 5 challenging tabular reasoning benchmarks covering numerical reasoning, fact-checking, and data analysis, TaTToo improves downstream policy LRMs by 30.9\% at inference, surpasses strong PRM baselines such as Qwen-2.5-Math-PRM-72B with only 8B parameters, and demonstrates strong generalizability across diverse TTS strategies.

---

Record id: `title:983af40bdcebe387`
