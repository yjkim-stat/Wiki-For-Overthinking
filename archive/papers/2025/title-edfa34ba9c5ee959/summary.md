<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/116423>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Shows cross-entropy fine-tuning can hurt pass@N test-time performance via overconfidence, and proposes a confidence-limiting training loss that better aligns training with pass@N search.

## Problem

How training-time objectives should be adapted to be compatible with a subsequent test-time compute strategy; specifically, standard CE training is shown to conflict with the pass@N search strategy used at test time.

## Contributions

- Shows that cross-entropy training can be misaligned with pass@N test-time scaling: pass@N accuracy decreases with longer CE training
- Attributes this misalignment to model overconfidence induced by CE training
- Proposes a modified training loss that limits model confidence and is better aligned with pass@N

## Method

Analyzes why standard cross-entropy fine-tuning becomes misaligned with pass@N test-time search as training progresses, tracing this to increasing model overconfidence. Introduces a modified training loss that constrains model confidence during training, intended to preserve or improve pass@N accuracy at test time. Evaluated on providing math answers with and without chain-of-thought traces, and on theorem proving by searching over proof trees.

## Results

Reports that pass@N accuracy decreases with longer CE training (degree not quantified in abstract); the proposed confidence-limiting loss improves mathematical reasoning on MATH and MiniF2F under CoT and non-CoT answer settings and for theorem proving via proof-tree search, though specific accuracy deltas are not given in the abstract.

## Limitations

Abstract does not report specific accuracy numbers or the exact form of the modified loss; scope is limited to pass@N as the test-time strategy, not other test-time compute strategies like sequential reasoning length or self-consistency.

## Why it matters here

- **overthinking**: Addresses test-time compute scaling, but via the parallel-sampling axis (pass@N over independent samples) and its interaction with training-time overconfidence, rather than sequential reasoning length or when a model should stop/continue thinking. It is a training-time/test-time co-design result for search budgets, not a study of overthinking or reasoning-length control.

## Entities

- **Concepts**: pass@N, model overconfidence, training-test co-design
- **Methods**: pass@N sampling, modified cross-entropy loss with confidence limiting
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), MiniF2F

Tags: `test-time-compute`, `pass-at-n`, `overconfidence`, `training-objective`, `math-reasoning`, `theorem-proving`

## Abstract

Abstract Recent progress in large language models (LLMs) highlights the power of scaling test-time compute to achieve strong performance on complex tasks, such as mathematical reasoning and code generation. This raises a critical question: how should model training be modified to optimize performance under a subsequent test-time compute strategy and budget? To explore this, we focus on pass@N, a simple test-time strategy that searches for a correct answer in N independent samples. We show, surprisingly, that training with cross-entropy (CE) can be misaligned with pass@N in that pass@N accuracy decreases with longer CE training. We explain the origins of this misalignment in terms of model overconfidence induced by CE, and experimentally verify our prediction of overconfidence as an impediment to scaling test-time compute via pass@N. Furthermore we suggest a principled, modified training loss that is better aligned to pass@N by limiting model confidence and rescuing pass@N test performance. Our algorithm demonstrates improved mathematical reasoning on MATH and MiniF2F benchmarks under several scenarios: (1) providing answers to math questions both with and without Chain-of-Thought reasoning traces; and (2) proving theorems by searching over proof trees of varying shapes. Overall our work underscores the importance of co-designing two traditionally separate phases of LLM development: training-time protocols and test-time search and reasoning strategies.

---

Record id: `title:edfa34ba9c5ee959`
