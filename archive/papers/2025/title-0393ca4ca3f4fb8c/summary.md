<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Atom of Thoughts for Markov LLM Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115860>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Atom of Thoughts reframes multi-step LLM reasoning as a Markov process of decomposing a question into independent atomic subquestions and contracting them into an answer-equivalent simplified question, removing the need to carry accumulated historical context and serving as a plug-in for existing test-time scaling methods.

## Problem

As test-time scaling increases the amount of reasoning an LLM performs, existing methods accumulate historical context across steps, which wastes computational resources and can interfere with effective reasoning; the paper addresses how to scale reasoning without this accumulation cost.

## Contributions

- Identifies that existing test-time scaling methods suffer from accumulated historical information as reasoning scale increases, wasting computation and interfering with effective reasoning.
- Proposes Atom of Thoughts (AoT), where each reasoning state transition decomposes the current question into a dependency-based DAG of subquestions and contracts them into a simplified, answer-equivalent question, forming a memoryless (Markov) reasoning process.
- Shows AoT can be integrated as a plug-in into existing test-time scaling methods (e.g. tree search, reflective refinement) to improve reasoning capability.
- Reports that AoT consistently outperforms existing baselines as computational budget increases, across math, multiple-choice, and multi-hop QA tasks.

## Method

Atom of Thoughts models multi-step reasoning as a Markov process: at each state, the current (sub)question is decomposed into a dependency-based directed acyclic graph of atomic subquestions, which are then contracted back into a single simplified question that preserves the answer to the original problem. Because each new state is self-contained and does not depend on the full history of prior reasoning steps, this removes the need to carry accumulated context forward, and the resulting atomic states can be plugged into existing test-time scaling methods (such as tree search or iterative refinement) as an enhancement.

## Results

The retrievable material (arXiv abstract and project summary) states qualitatively that AoT 'consistently outperforms existing baselines as computational budgets increase' across math, multiple-choice (BBH, MMLU), and multi-hop QA (HotpotQA) tasks, and integrates with long-context settings (LongBench); no specific numerical scores, tables, or effect sizes were available from the accessible sources.

## Limitations

Not stated in the retrievable abstract/summary material; no specific numerical results, ablations, or explicit limitations were available from the accessible sources (arXiv abstract page and project README) -- the full paper (NeurIPS 2025 / arXiv:2502.12018) would need to be read directly for quantitative comparisons and stated limitations.

## Why it matters here

- **overthinking**: On-topic: the paper's core motivation is that longer reasoning under existing test-time scaling methods wastes computation via accumulated historical context that interferes with reasoning quality -- a direct instance of the overthinking/inefficiency problem this topic tracks. Its proposed fix (decomposing reasoning into memoryless atomic subquestions) is a concrete method for keeping test-time compute effective as it scales, rather than letting reasoning bloat with irrelevant history, and it is explicitly designed to plug into other test-time scaling methods to improve their compute efficiency.

## Entities

- **Concepts**: atomic questions / Markov property in reasoning, decomposition-contraction reasoning process, answer-preserving question simplification, dependency-based directed acyclic graph over subquestions
- **Methods**: Atom of Thoughts (AoT), Markov reasoning process, Decomposition-contraction
- **Datasets**: Math reasoning benchmarks (including GSM8K), [BBH (BIG-Bench Hard)](../../../../wiki/datasets/bbh-big-bench-hard.md), [MMLU](../../../../wiki/datasets/mmlu.md), [HotpotQA](../../../../wiki/datasets/hotpotqa.md), LongBench

Tags: `test-time-scaling`, `markov-reasoning`, `question-decomposition`, `context-accumulation`, `overthinking`, `plug-in-method`

## Abstract

Abstract Large Language Models (LLMs) achieve superior performance through training-time scaling, and test-time scaling further enhances their capabilities by conducting effective reasoning during inference. However, as the scale of reasoning increases, existing test-time scaling methods suffer from accumulated historical information, which not only wastes computational resources but also interferes with effective reasoning. To address this issue, we observe that complex reasoning can be achieved by solving a series of independent and self-contained subquestions. These subquestions are essentially \textit{atomic questions}, exhibiting the memoryless property similar to Markov processes. Based on this observation, we propose Atom of Thoughts (\our), where each state transition consists of decomposing the current question into a dependency-based directed acyclic graph and contracting its subquestions, forming a simplified question that maintains answer equivalence with the original problem. This answer preservation enables the iterative \textit{decomposition-contraction} process to naturally form a meaningful Markov reasoning process. Furthermore, these atomic states can be seamlessly integrated into existing test-time scaling methods, enabling \our to serve as a plug-in enhancement for improving reasoning capabilities.

---

Record id: `title:0393ca4ca3f4fb8c`
