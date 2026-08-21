<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119334>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Proposes an LLM-agent framework, AgentTTS, that searches for the compute-optimal choice of model and inference budget per subtask in multi-stage complex tasks.

## Problem

Existing test-time scaling research targets single-stage tasks, but many real tasks are multi-stage pipelines of heterogeneous subtasks each needing a different model and budget; searching the combinatorial, interdependent space of model/budget allocations per subtask is impractical by brute force.

## Contributions

- Defines the problem of test-time compute-optimal scaling for multi-stage complex tasks: selecting a suitable model and compute budget per subtask
- Reports three empirical insights on LLM behavior in multi-stage tasks from pilot experiments across four tasks and six datasets
- Proposes AgentTTS, an LLM-agent framework that iteratively searches for compute-optimal model/budget allocations via feedback from the execution environment

## Method

Studies test-time scaling (TTS) in multi-stage complex tasks composed of heterogeneous subtasks, each needing a model of specific capability. Because brute-force search over the combinatorial space of model and budget allocations is impractical and optimal choices across subtasks are interdependent, the paper runs pilot experiments to derive empirical insights, then builds AgentTTS: an LLM-agent-based framework that autonomously searches for compute-optimal model and budget allocations through iterative feedback-driven interaction with the task execution environment.

## Results

AgentTTS is reported to significantly outperform traditional and other LLM-based baselines in search efficiency, with improved robustness to varying training set sizes and enhanced interpretability; no specific accuracy or cost numbers are given in the abstract.

## Limitations

Abstract does not name the specific datasets, tasks, or quantitative results (accuracy/cost numbers); scope is restricted to multi-stage pipelines with heterogeneous subtasks rather than single-model reasoning length.

## Why it matters here

- **overthinking**: Uses the phrase 'test-time scaling' but addresses a different problem: allocating which model and how much inference budget to assign to each subtask in a multi-stage pipeline, not the accuracy/efficiency tradeoff of a single model's reasoning length or when it should stop thinking. Only tangentially related to overthinking as tracked here.

## Entities

- **Concepts**: [compute-optimal scaling](../../../../wiki/concepts/compute-optimal-scaling.md), multi-stage task decomposition, model and budget allocation
- **Methods**: AgentTTS (LLM-agent search framework)
- **Datasets**: six datasets across four tasks (not individually named in abstract)

Tags: `test-time-scaling`, `multi-stage-tasks`, `agent-orchestration`, `compute-allocation`

## Abstract

Abstract Test-time scaling (TTS) enhances the performance of large language models (LLMs) by allocating additional compute resources during inference. However, existing research primarily investigates TTS in single-stage tasks; while many real-world problems are multi-stage complex tasks, composed of a sequence of heterogeneous subtasks with each subtask requires LLM of specific capability. Therefore, we study a novel problem: the test-time compute-optimal scaling in multi-stage complex tasks, aiming to select suitable models and allocate budgets per subtask to maximize overall performance. TTS in multi-stage tasks introduces two fundamental challenges: (i) The combinatorial search space of model and budget allocations, combined with the high cost of inference, makes brute-force search impractical. (ii) The optimal model and budget allocations across subtasks are interdependent, increasing the complexity of the compute-optimal search. To address this gap, we conduct extensive pilot experiments on four tasks across six datasets, deriving three empirical insights characterizing the behavior of LLMs in multi-stage complex tasks. Informed by these insights, we propose AgentTTS, an LLM-agent-based framework that autonomously searches for compute-optimal allocations through iterative feedback-driven interactions with the execution environment. Experimental results demonstrate that AgentTTS significantly outperforms traditional and other LLM-based baselines in search efficiency, and shows improved robustness to varying training set sizes and enhanced interpretability.

---

Record id: `title:f3f44348f8094543`
