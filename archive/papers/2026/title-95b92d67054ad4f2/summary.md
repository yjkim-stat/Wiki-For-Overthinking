<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10010734>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

DC-CoT is a benchmark that isolates the effect of data augmentation, data selection and data mixing on chain-of-thought distillation into smaller student models, across teacher models, student models and reasoning domains.

## Problem

Data-centric distillation - augmenting, filtering and mixing the CoT traces a teacher produces - is a route to small students that keep reasoning ability, but the individual manipulations had never been compared under one protocol, so it was not known which augmentation helps generalization, which filter trades quality against coverage, or when mixing several teachers pays off.

## Contributions

- DC-CoT, a benchmark that varies data-centric distillation choices along method, model and data axes under one evaluation protocol
- A comparison of four augmentation operators, three selection filters and two mixing strategies on the same teacher-student pairs
- Evidence that augmentation dominates selection and mixing, with reverse thinking the strongest single operator at 24.64% over vanilla CoT distillation
- Evidence that smaller students are better served by moderately sized teachers than by the largest available ones

## Method

The benchmark varies three axes independently. Method: four augmentation operators (question rephrasing, question augmentation, answer augmentation, reverse thinking), three selection filters (teacher-correctness filtering, student-error filtering, LLM-as-a-judge) and two mixing strategies (length-based, teacher-based). Model: five teachers (Gemini-1.5-Pro, GPT-4, Claude-3.5 Sonnet, GPT-4o-mini, o4-mini) distilled into five students (LLaMA-3.1-8B, LLaMA-3.1-8B-R1, Mistral-7B, Gemma-7B, Qwen-2.5-7B), roughly 3B and 7B scale. Data: textual, agentic and visual reasoning tasks, scored in-distribution, out-of-distribution and across domains.

## Results

Reverse-thinking augmentation gave the largest reported gain, 24.64% over a vanilla-CoT distillation baseline. Answer augmentation was strongest on commonsense tasks (57.58% average). Augmentation outperformed both selection and mixing overall. Smaller students gained more from moderately sized teachers than from the largest ones. Gains from added data were non-linear, with diminishing returns as volume grew, and OOD transfer varied widely by task pairing.

## Limitations

The authors cite budget limits that excluded broader teacher coverage, hardware and time limits on the choice of student models, and API cost as the reason WebArena is the only agentic benchmark. A reader should also note that the benchmark measures student accuracy, not the length or cost of the student's reasoning: 'efficient reasoning' in the title means a smaller model, not a shorter chain of thought, so nothing here says whether the distilled students think for the right length of time.

## Why it matters here

- **overthinking**: Partially relevant, and worth reading with the distinction in mind. The paper's notion of efficiency is parameter count, not reasoning length: it asks how to distil a teacher's chain of thought into a 3B or 7B student that still answers correctly, and never measures how many tokens the student spends. It touches the topic through the training data rather than the inference budget - the choice of which CoT traces to keep is the choice of what reasoning behaviour a small model inherits, and the finding that a moderately sized teacher beats the largest one for a small student is the same capacity-matching intuition that motivates length adaptation. But it offers no stopping criterion, no length/accuracy curve and no test-time compute result, so it is background for how efficient reasoners get built, not evidence about when a model thinks too much.

## Entities

- **Concepts**: Chain-of-Thought Distillation, Data-Centric Benchmarking, Teacher-Student Capacity Gap, [Out-of-Distribution Generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), Rationale Augmentation
- **Methods**: DC-CoT, [chain-of-thought distillation](../../../../wiki/methods/chain-of-thought-distillation.md), reverse thinking, answer augmentation, question rephrasing, teacher-correctness filtering, student-error filtering, LLM-as-a-judge selection, length-based mixing, teacher-based mixing
- **Datasets**: [StrategyQA](../../../../wiki/datasets/strategyqa.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), [ARC-Challenge](../../../../wiki/datasets/arc-challenge.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), ANLI, Date Understanding, WebArena, Visual-CoT, OK-VQA, CLEVR

Tags: `cot-distillation`, `benchmark`, `data-centric`, `knowledge-distillation`, `small-models`, `ood-generalization`

---

Record id: `title:95b92d67054ad4f2`
