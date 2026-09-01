<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CodeChemist: Test-Time Scaling for Low-Resource Code Generation via Functional Knowledge Transfer

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/63512>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

CodeChemist is a training-free test-time-scaling framework that improves code generation for low-resource programming languages by transferring functional knowledge from well-supported languages: it samples multiple candidate implementations at varied temperatures, generates synthetic test inputs, and either uses within-language consensus voting (when confident) or executes cross-language reference implementations to build test benchmarks and select the best candidate (when less confident).

## Problem

Code LLMs perform unevenly across programming languages, struggling on less common ones due to insufficient training data, and existing test-time methods do not transfer functional correctness knowledge from well-supported languages to underrepresented ones.

## Contributions

- CodeChemist, a training-free test-time-scaling framework transferring functional correctness knowledge from well-supported to low-resource programming languages
- a confidence-gated selection mechanism switching between within-language consensus voting and cross-language reference-implementation test synthesis
- substantial code-generation improvements for underrepresented (Lua) and syntactically complex (C++, Java) languages

## Method

At test time and without retraining, CodeChemist generates multiple candidate implementations for a target (low-resource) language via varied-temperature sampling, creates synthetic test inputs, and assesses confidence in the candidates; when confidence is high, it selects via within-language consensus voting among candidates; when confidence is lower, it executes reference implementations of the same problem in stronger (well-supported) languages to build cross-language test benchmarks, then selects the target-language candidate that performs best against those cross-language-derived tests.

## Results

Testing shows substantial improvements for underrepresented languages like Lua as well as for syntactically complex ones such as C++ and Java (no specific numeric deltas given in the fetched abstract).

## Limitations

Not stated in the fetched abstract beyond the languages named as tested (Lua, C++, Java) and the training-free scope of the method.

## Why it matters here

- **overthinking**: Indirectly relevant: a test-time-scaling method (sampling multiple candidates, then selecting via consensus or synthesized tests) for a different problem (cross-lingual code-generation transfer) rather than reasoning-length control, but another example of spending test-time compute on structured candidate generation and verification rather than a single longer trace.

## Entities

- **Concepts**: functional knowledge transfer across programming languages, confidence-gated consensus vs. cross-language test synthesis, test-time scaling for code generation
- **Methods**: CodeChemist (test-time functional knowledge transfer), varied-temperature sampling, cross-language test synthesis
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `code-generation`, `low-resource-languages`, `training-free`

---

Record id: `title:84ca66661062ae22`
