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

Improves code generation in low-resource programming languages at inference time by sampling many candidate solutions and validating them against test oracles built by executing equivalent high-resource-language reference programs.

## Problem

Code language models perform inconsistently across programming languages, doing poorly on less common ones because of limited training data, and there is usually no labeled test suite in the target low-resource language to validate generated candidates.

## Contributions

- CodeChemist, a test-time framework for low-resource programming-language code generation that requires no retraining.
- Multi-temperature hedged sampling to generate a diverse pool of candidate solutions in the low-resource target language.
- Construction of cross-lingual I/O test oracles by executing high-resource reference programs, used to select among candidates without ground-truth tests in the target language.

## Method

For a coding problem in a low-resource programming language, the model samples a pool of candidate solutions at multiple temperatures (hedged sampling). It then builds test oracles by executing reference programs written in a high-resource language on generated inputs, using their outputs as a cross-lingual ground truth to check and select among the low-resource candidates functionally, without needing labeled tests in the target language.

## Results

No specific benchmark numbers were available in the retrieved material (no PDF or numeric results found on the paper's ICML page); the paper reports qualitative improvements over baselines for both less common and syntactically complex low-resource languages.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Tangential. This uses 'test-time scaling' only in the generic sense of spending more inference compute by sampling a wider pool of candidate solutions (best-of-N style) for code generation; it is about cross-lingual functional validation of code, not about a large reasoning model's chain-of-thought length, and it does not address the accuracy/efficiency tradeoff of reasoning duration or when a model should stop reasoning.

## Entities

- **Concepts**: cross-lingual knowledge transfer for code generation, functional (I/O) test oracles, hedged sampling
- **Methods**: CodeChemist, multi-temperature hedged sampling, cross-lingual test oracle construction
- **Datasets**: _none recorded_

Tags: `code-generation`, `low-resource`, `test-time-sampling`, `cross-lingual`

---

Record id: `title:84ca66661062ae22`
