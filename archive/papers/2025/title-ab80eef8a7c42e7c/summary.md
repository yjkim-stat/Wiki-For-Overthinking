<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators

- **Authors**: _unknown_
- **Venue**: ICML 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2025/poster/46046>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

JETTS is a benchmark evaluating how well LLM-as-judge models perform as evaluators guiding test-time-scaling methods -- response reranking, step-level beam search, and critique-based refinement -- across math, code and instruction-following.

## Problem

Scaling test-time computation typically relies on external non-generative evaluators (verifiers, reward models) to select or guide extra compute, but how well general-purpose LLM judges perform this evaluator role, compared to purpose-built reward models, had not been systematically tested.

## Contributions

- Introduces the JETTS benchmark spanning three domains (math, code, instruction-following) and three test-time-scaling settings (response reranking, step-level beam search, critique-based refinement)
- Compares ten judge models (7B-70B) against eight base generator models and against outcome/process reward models
- Finds that judges match outcome reward models in response selection but underperform process reward models in beam search
- Finds that judges' natural-language critiques are currently ineffective at guiding a generator toward better responses

## Method

Evaluates ten LLM judge models, ranging from 7B to 70B parameters, as evaluators guiding three test-time-scaling protocols -- response reranking, step-level beam search, and critique-based response refinement -- against eight base generator models, and compares judge performance to dedicated outcome and process reward models.

## Results

Judges matched outcome reward models in response reranking/selection but underperformed process reward models in step-level beam search; judges' natural-language critiques were found ineffective at guiding the generator toward better responses.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Evaluates the judges/verifiers that decide how test-time compute is allocated across candidates (reranking, beam search, refinement), rather than reasoning length itself. It is a real, direct contribution to the test-time-compute-scaling side of this topic -- showing judges are competitive at selection but weak at beam search and at critique-guided refinement -- though its focus is evaluator quality rather than the stop/continue decision within a single chain of thought.

## Entities

- **Concepts**: [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), llm-as-judge, outcome reward model, process reward model, best-of-n reranking, step-level beam search
- **Methods**: JETTS benchmark
- **Datasets**: JETTS benchmark (math, code, instruction-following domains)

Tags: `test-time-scaling`, `llm-as-judge`, `verification`, `benchmark`

---

Record id: `title:ab80eef8a7c42e7c`
