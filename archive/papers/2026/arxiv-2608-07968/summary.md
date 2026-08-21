<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions

- **Authors**: Chenrui Fan, Yize Cheng, Ming Li, Yongyuan Liang, Tianyi Zhou, Soheil Feizi
- **Venue**: cs.CL
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07968>
- **PDF**: <https://arxiv.org/pdf/2608.07968v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces an exam-style evaluation where reasoning models must divide one shared token budget across multiple questions of different difficulty and value, and finds they allocate it by presentation order rather than by difficulty or value.

## Problem

Existing test-time compute evaluations study one question at a time, concealing whether a reasoning model can strategically divide a fixed, shared inference budget across several competing problems of different difficulty and worth.

## Contributions

- Introduces an exam-style evaluation framework where a model must divide one shared token budget across N questions of varying difficulty and point value.
- Shows models allocate compute largely by presentation order rather than difficulty or stated value ('greedy sequential solvers').
- Shows budget pressure magnifies the failure: as exam length N grows, position-effort correlation strengthens and coverage of attempted questions shrinks.
- Shows explicit planning prompts spread compute more evenly across questions but do not induce value- or difficulty-aware prioritization.
- Extends the same behavioral pattern from mathematical reasoning (Omni-MATH) to code reasoning (CRUXEval-O).

## Method

Constructs 'exams' of N questions (from Omni-MATH, difficulty <=5) with visible point values, presented together under one shared reasoning-token budget B; the model produces a single free-form reasoning trace for the whole exam, then answers are extracted in a separate turn. Reasoning tokens are attributed to individual questions using the Qn markers in the trace, giving a token effort t_i and a token-weighted-centroid solving order for each question (restricted to a 'work set' of substantively attempted questions). Partial Spearman correlations relate token effort and solving order to presentation position, difficulty, and point value, controlling for confounds between position and difficulty. Four scoring schemes (fixed, random, aligned, reversed) and three orderings (random, ascending, descending difficulty) are crossed with five open-weight models (DeepSeek-R1-Distill-Qwen-7B/14B, Qwen3-8B/14B/32B) and two DeepSeek-V4 API models, and with a baseline vs. explicit-planning prompt.

## Results

Averaged over models, the position-effort correlation is -0.17 at N=5, -0.38 at N=10, and -0.48 at N=20 (increasingly negative = later questions get fewer tokens), while solving order tracks presentation position strongly (overall rho=+0.68, ranging +0.55 to +0.91 by model). Effort- and order-value correlations stay near zero across N (effort-value: 0.00, +0.04, +0.11; order-value: -0.03, -0.09, -0.07). Coverage of the exam (work-set size / N) falls from 55-90% at N=5 to 23-46% at N=20 for locally hosted models, and even more for API models (DSV4-F: 80% to 23%); zero-token rate rises to 51% (open-model average), 69% (DSV4-F) and 61% (DSV4-P) at N=20. The reached work set overlaps with model-adaptive value-density ranking only at chance level (0.59) while overlapping with early-position ranking at 0.76. Explicit planning improves coverage by +0.09 to +0.14 as N grows from 5 to 20 but leaves solving-order correlation with position essentially unchanged (open models: 0.64 to 0.60; DSV4-P: 0.68 to 0.83, i.e. more sequential). The same position-driven, value-insensitive pattern reproduces on CRUXEval-O code reasoning.

## Limitations

The full factorial design (varying length, order, and point values) is run only on Omni-MATH; CRUXEval-O experiments cover just two exam lengths, four models and two scoring schemes, with no native difficulty axis and no ordering/repricing manipulations, so absolute score rates and effect magnitudes should not be compared across the two domains. Per-question token attribution is recovered from Q1/Q2 marker segmentation, which the authors call reliable for the large majority of traces but only an approximation; a fully rigorous notion of effort (detecting where a question is actually being solved, not merely referenced) remains open.

## Why it matters here

- **overthinking**: Directly establishes a distinct overthinking/underthinking-adjacent failure mode: under a fixed shared compute budget, reasoning models overspend effort on early or low-value questions (a form of overthinking relative to their worth) while leaving harder or more valuable questions underexplored, and this failure worsens as the budget becomes more contested. It frames cross-question compute allocation as a capability separate from, and not solved by, per-question length-control methods.

## Entities

- **Concepts**: shared-budget metareasoning across questions, budget allocation as a knapsack problem, position bias vs. difficulty/value sensitivity in reasoning, per-question reasoning attribution from a shared trace
- **Methods**: exam-style shared-budget evaluation framework, partial Spearman correlation analysis, marker-based reasoning attribution (token effort, token-weighted centroid solving order), explicit planning prompt condition, knapsack-style value-density analysis using an independent high-budget reference
- **Datasets**: [Omni-MATH](../../../../wiki/datasets/omni-math.md), CRUXEval-O

Tags: `test-time-compute`, `budget-allocation`, `reasoning-models`, `position-bias`, `overthinking`, `evaluation`

## Abstract

Reasoning language models increasingly use test-time compute to improve performance, but existing evaluations typically study this compute one question at a time. Yet when multiple problems share an end-to-end cost or latency constraint, models must decide how to divide limited inference compute among them. We introduce an exam-style evaluation framework for studying this setting, in which a model must distribute one shared token budget across questions with different difficulty and point values to maximize its total score. Across several open and frontier reasoning models, we find that models fail to allocate a shared budget strategically across questions of varying difficulties and values. Models behave largely as greedy sequential solvers: they prioritize questions by presentation order, front-load effort on early questions, and remain insensitive to value, with these tendencies becoming more pronounced as the number of questions grows. Explicit planning prompts spread compute more evenly but do not produce value- or difficulty-aware prioritization. The same behavioral pattern extends from mathematical to code reasoning. These findings establish global budget allocation as a distinct capability that is not captured by conventional per-question evaluation and remains a challenge for current reasoning models.

---

Record id: `arxiv:2608.07968`
