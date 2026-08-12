<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction

- **Authors**: Jun Gao, Yun Peng, Qian Qiao, Changhai Zhou, Yuhua Zhou, Shiyang Zhang, Shichao Weng, Zhenchang Xing, Xiaoxue Ren
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.460>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.460
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Evaluates code reasoning by implementation invariance and intermediate-state accuracy, finding models get final outputs right while reasoning incorrectly about execution.

## Problem

Strong code generation leaves unclear whether models genuinely reason about code execution. Existing code reasoning benchmarks evaluate final output correctness under a single canonical implementation, leaving two things untested: whether predictions are consistent across functionally equivalent implementations, and whether models can accurately reason about intermediate execution states.

## Contributions

- CoRE, a code reasoning benchmark built on implementation invariance and process transparency
- Evaluation across functionally equivalent implementations as a direct test of surface dependence
- Intermediate execution-state prediction as a process measure beyond final output
- Identification of a substantial robustness gap across equivalent implementations in eight frontier LLMs
- Identification of 'superficial execution': correct outputs without correct intermediate-state reasoning

## Method

CoRE evaluates code reasoning along two axes. Implementation invariance tests the same functional behaviour across equivalent implementations — a model that reasons about execution should give the same answer for all of them, so variance across equivalents is a direct measure of surface dependence. Process transparency tests whether intermediate execution states are predicted correctly, not only the final output. Eight frontier LLMs are evaluated.

## Results

Two limitations emerge. Models show a substantial robustness gap, with performance varying significantly across functionally equivalent implementations. Models also exhibit 'superficial execution', arriving at correct final outputs without correctly reasoning about intermediate states. The authors conclude output-only evaluation is insufficient for assessing code reasoning.

## Limitations

No numbers in the abstract, so neither the robustness gap nor the rate of superficial execution is quantified, and the eight models are not named. Equivalence between implementations must be established by construction, and how equivalence was verified is unstated. Intermediate-state evaluation requires a canonical trace, which may admit more than one valid order of reasoning about it.

## Why it matters here

- **reasoning-evaluation**: Code execution is the one reasoning domain with a ground-truth intermediate trace available for free — the interpreter produces it — which makes it the cheapest place to measure whether a model's stated reasoning matches the reasoning that actually determines the answer. 'Superficial execution' is that measurement, and it is the same dissociation the archive's faithfulness thread finds in math and QA, here established against an oracle rather than against a proxy. The implementation-invariance axis is also the code analogue of VAR-MATH's instance variation, so the archive now holds the same robustness critique in two domains with independent construction.

## Entities

- **Concepts**: [construct validity](../../../../wiki/concepts/construct-validity.md), implementation invariance, process transparency, superficial execution, [robustness](../../../../wiki/concepts/robustness.md), code reasoning, [chain of thought faithfulness](../../../../wiki/concepts/chain-of-thought-faithfulness.md)
- **Methods**: CoRE, equivalent-implementation perturbation, intermediate state probing
- **Datasets**: CoRE

Tags: `benchmark`, `code reasoning`, `faithfulness`, `robustness`, `process evaluation`

## Abstract

Despite strong performance on code generation tasks, it remains unclear whether large language models (LLMs) genuinely reason about code execution. Existing code reasoning benchmarks primarily evaluate final output correctness under a single canonical implementation, leaving two critical aspects underexplored: (1) whether LLMs predictions are consistent to functionally equivalent implementations, and (2) whether LLMs can accurately reason about intermediate execution states. We introduce CoRE, a Code Reasoning benchmark that evaluates code reasoning through implementation invariance and process transparency. Extensive evaluations on eight frontier LLMs reveal two fundamental limitations. First, models exhibit a substantial robustness gap, with performance varying significantly across equivalent implementations. Second, we observe superficial execution, where models arrive at correct final outputs without correctly reasoning about intermediate execution states. Together, these findings demonstrate that output-only evaluations are insufficient for assessing code reasoning and position CoRE as a necessary benchmark for evaluating robust and faithful code reasoning.

---

Record id: `doi:10.18653/v1/2026.findings-acl.460`
