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

TaTToo trains a table-grounded, tool-verified process reward model that supervises test-time-scaling search for large reasoning models on tabular reasoning tasks.

## Problem

Process reward models used to guide test-time scaling of large reasoning models are built for text-only reasoning steps and perform poorly on table-specific operations such as sub-table retrieval and schema interaction, creating a performance bottleneck for tabular reasoning.

## Contributions

- Identifies that text-only PRMs struggle with table-specific operations (sub-table retrieval, schema interaction), bottlenecking tabular reasoning
- Builds a data curation pipeline producing over 60k step-level annotations combining table-verification rationales with tool-based executions
- Trains TaTToo with cold-start SFT followed by RL with tool-grounded reward shaping
- Improves downstream policy LRMs by 30.9% at inference across 5 tabular reasoning benchmarks, surpassing a 72B baseline PRM with only 8B parameters

## Method

TaTToo is a table-grounded process reward model trained in two stages: cold-start supervised fine-tuning on step-level annotations (over 60k, built by combining table-verification rationales with tool-based executions) to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping to align the PRM's judgments with actual table verification. At inference it scores intermediate reasoning steps of a policy LRM to guide test-time-scaling search strategies over tabular reasoning tasks.

## Results

Improves downstream policy LRMs by 30.9% at inference across 5 tabular reasoning benchmarks (numerical reasoning, fact-checking, data analysis); surpasses Qwen-2.5-Math-PRM-72B while using only 8B parameters; generalizes across diverse test-time-scaling strategies.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential: this paper improves the reward model that guides test-time-scaling search (which reasoning steps to keep/expand) in a specific domain, tabular reasoning, but it does not address the reasoning-length tradeoff, overthinking/underthinking, or stopping criteria that the topic tracks. Its connection is limited to sharing the 'test time scaling' framing and applying to large reasoning models.

## Entities

- **Concepts**: process reward model, tool-grounded verification, test-time scaling for search
- **Methods**: TaTToo, process reward model (PRM), tool-grounded reward shaping, cold-start SFT + RL
- **Datasets**: 5 tabular reasoning benchmarks covering numerical reasoning, fact-checking and data analysis

Tags: `process-reward-model`, `tabular-reasoning`, `test-time-scaling`, `tool-use`

## Abstract

Abstract Process Reward Models (PRMs) have recently emerged as a powerful framework for enhancing the reasoning capabilities of large reasoning models (LRMs), particularly in the context of test-time scaling (TTS). However, their potential for supervising LRMs on tabular reasoning domains remains underexplored. Through detailed empirical analyses, we identify that existing PRMs, though widely adopted for supervising text-only reasoning steps, struggle with table-specific operations such as sub-table retrieval and schema interaction, leading to critical performance bottlenecks. To address this limitation, we propose TaTToo, a novel table-grounded PRM framework that (i) reasons explicitly over tabular reasoning steps and (ii) integrates tool-based verification to provide precise reward supervision. Concretely, we first design a scalable data curation pipeline that constructs over 60k high-quality step-level annotations by integrating table verification rationales with tool-based executions. Building on the collected data, we train TaTToo with a dual-stage paradigm: cold-start supervised fine-tuning to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping to align our model with table-based verification. We provide a comprehensive evaluation of the policy improvement induced by our newly designed PRM. Across 5 challenging tabular reasoning benchmarks covering numerical reasoning, fact-checking, and data analysis, TaTToo improves downstream policy LRMs by 30.9\% at inference, surpasses strong PRM baselines such as Qwen-2.5-Math-PRM-72B with only 8B parameters, and demonstrates strong generalizability across diverse TTS strategies.

---

Record id: `title:983af40bdcebe387`
