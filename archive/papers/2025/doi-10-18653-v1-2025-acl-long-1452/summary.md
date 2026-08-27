<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling

- **Authors**: Bingxuan Li, Yiwei Wang, Jiuxiang Gu, Kai-Wei Chang, Nanyun Peng
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-long.1452/>
- **PDF**: <https://aclanthology.org/2025.acl-long.1452.pdf>
- **DOI**: 10.18653/v1/2025.acl-long.1452
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

METAL decomposes chart-to-code generation into four specialized VLM agents (Generation, Visual Critique, Code Critique, Revision) that iteratively refine the code until a multi-criteria verifier passes, beating direct prompting, hint-enhanced prompting, and Best-of-N by 5.2-11.3 F1 points, with performance rising near-linearly in the log of test-time compute budget from 2^9 to 2^13 tokens.

## Problem

Generating chart-reproducing code from a reference chart image requires jointly strong visual design understanding and precise coding ability; direct VLM prompting (even with GPT-4o) frequently fails to accurately reproduce structure, color, and text properties, and existing test-time approaches (Best-of-N, hint-enhanced prompting) do not substantially improve on direct prompting for this visually-grounded code generation task.

## Contributions

- METAL, a four-agent (Generation/Visual Critique/Code Critique/Revision) test-time-scaling framework for chart-to-code generation, outperforming direct prompting, hint-enhanced prompting, and Best-of-N
- empirical evidence of test-time scaling in a multi-agent, cross-modal (visually-grounded code generation) setting, with F1 improving near-linearly in the log of compute budget from 2^9 to 2^13 tokens
- an ablation showing that separating visual and code critique into distinct specialized agents (rather than one unified critique agent) is necessary for effective self-correction, avoiding context dilution and mismatched per-modality feedback requirements

## Method

METAL splits chart-to-code generation across four specialized agents: a Generation Agent produces initial Python code from the reference chart; a Visual Critique Agent renders the generated code and compares the rendered chart against the reference to identify visual discrepancies; a Code Critique Agent reviews the generated code itself and suggests specific line-level improvements; a Revision Agent integrates both critiques to update the code. These run in an iterative loop, re-rendering and re-critiquing after each revision, until a heuristic multi-criteria verifier (three metrics: color, text, overall structure) confirms the rendered chart meets quality thresholds or a maximum iteration count T_max is reached. Evaluated on ChartMIMIC (1,000 human-curated figure/instruction/code triplets across 18 regular + 4 advanced chart types, 191 subcategories) with GPT-4o and LLaMA 3.2-11B as base VLMs, against Direct Prompting, Hint-Enhanced Prompting, and Best-of-N (n=5) baselines, measuring F1 on text/type/color/layout chart elements.

## Results

METAL (n=5 iterations) achieves 51.78% average F1 with LLaMA 3.2-11B (vs. 40.45% direct prompting, 41.33% hint-enhanced, 43.13% Best-of-N -- an 11.33% improvement over direct prompting) and 86.46% average F1 with GPT-4o (vs. 81.26% direct, 81.12% hint-enhanced, 82.32% Best-of-N -- a 5.2% improvement over direct prompting and the current best result). Gains are largest on Text and Layout metrics for both base models. Test-time scaling: F1 rises near-monotonically and near-linearly in the log of the compute budget as it grows from 2^9 to 2^13 tokens, for both base models across all four metrics (Figure 3), attributed to the iterative multi-agent refinement compounding error corrections across rounds. Ablations (GPT-4o base) show both critique agents are necessary: using only the visual critique agent (METAL_V) reaches 84.31% average F1, only the code critique agent (METAL_C) reaches 82.96%, and merging both critiques into a single unified agent (METAL_S) reaches only 80.86% -- below either single-modality ablation -- versus 86.46% for the full separate-critique design, a 5.6% improvement attributed to modality-tailored (rather than merged) critique avoiding information dilution from an overloaded context and addressing visual (spatial/color) and code (syntax/logic) critique's differing requirements separately. A modular-system ablation removing self-decision-making and code-execution ability (replacing the agentic loop with a fixed one-shot self-revision pipeline) causes a 4.51% average performance drop versus full METAL, isolating the agentic (not just iterative) design as contributing meaningfully. Performance gains from 5 compute recurrences are largest on easy-difficulty charts (13.99% GPT-4o / 5.3% LLaMA) and shrink on hard charts (4.62% GPT-4o / 5.0% LLaMA), though gains remain positive across all difficulty levels for both models.

## Limitations

METAL is built on VLMs and requires extensive prompt engineering; even the best-performing prompts identified may not be optimal, and further prompt refinement could improve results further. Automatic evaluation metrics (adopted from prior work for fairness) have inherent imperfections and may not capture every detail of chart-visual fidelity. METAL has higher computational cost than direct prompting due to its multi-agent iterative refinement loop, and the paper explicitly leaves optimizing this cost to future work; due to limited resources the test-time-scaling experiments were not extended beyond a 2^13-token budget, so whether the near-linear log-compute scaling trend continues at larger budgets is untested.

## Why it matters here

- **overthinking**: Relevant as a positive test-time-scaling case study outside single-model text reasoning: it demonstrates the same log-linear compute-vs-performance scaling pattern the overthinking literature examines, but in a multi-agent, cross-modal (chart-to-code) setting, and explicitly names higher inference cost as an acknowledged, unaddressed limitation. Its ablation isolating which architectural choice (separate vs. merged critique) drives the scaling benefit is methodologically relevant to understanding when 'more test-time compute' translates into real accuracy gains versus wasted iteration, a central question for overthinking mitigation.

## Entities

- **Concepts**: multi-agent test-time refinement, modality-tailored critique (visual vs. code), multi-criteria verifier with dynamic threshold, log-linear test-time scaling
- **Methods**: multi-agent iterative refinement, Direct Prompting / Hint-Enhanced Prompting / Best-of-N (baselines), multi-criteria heuristic verifier
- **Datasets**: ChartMIMIC (1,000 figure/instruction/code triplets, 18 regular + 4 advanced chart types)

Tags: `test-time-scaling`, `multi-agent`, `chart-generation`, `self-correction`, `vision-language-model`

## Abstract

Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and healthcare. In this work, we build a vision-language model (VLM) based multi-agent framework for effective automatic chart generation. Generating high-quality charts requires both strong visual design skills and precise coding capabilities that embed the desired visual properties into code. Such a complex multi-modal reasoning process is difficult for direct prompting of VLMs. To resolve these challenges, we propose METAL, a multi-agent framework that decomposes the task of chart generation into the iterative collaboration among specialized agents. METAL achieves a 5.2% improvement in the F1 score over the current best result in the chart generation task. Additionally, METAL improves chart generation performance by 11.33% over Direct Prompting with LLaMA-3.2-11B.Furthermore, the METAL framework exhibits the phenomenon of test-time scaling: its performance increases monotonically as the logarithm of computational budget grows from 512 to 8192 tokens.

---

Record id: `doi:10.18653/v1/2025.acl-long.1452`
