<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# HalluGuard: Evidence-Grounded Small Reasoning Models to Mitigate Hallucinations in Retrieval-Augmented Generation

- **Authors**: Loris Bergeron, Ioana Buhnila, Jérôme François, Radu State
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.835>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.835
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.67

## In one line

A 4B small reasoning model that classifies document-claim pairs as grounded or hallucinated for RAG pipelines and produces evidence-grounded justifications.

## Problem

Large language models remain prone to hallucination, which limits trust in deployment. Retrieval-augmented generation grounds answers in documents but does not guarantee the answer follows from them, so a separate guardrail is needed to judge whether a claim is supported by the retrieved evidence.

## Contributions

- HalluGuard, a 4B small reasoning model acting as a grounded-versus-hallucinated classifier for RAG with evidence-grounded justifications
- A domain-agnostic synthetic training set derived from FineWeb through multi-stage curation and data reformation
- Synthetic generation of paired grounded and hallucinated claims as the supervision signal
- Distillation of large-model reasoning into a small backbone via Odds Ratio Preference Optimization
- 84.4% balanced accuracy on the RAGTruth subset of LLM-AggreFact at roughly half the parameters of MiniCheck and Granite Guardian, and 77.1% overall against GPT-4o's 75.9%

## Method

HalluGuard is a 4B-parameter Small Reasoning Model used as a guardrail in RAG pipelines, classifying document-claim pairs as grounded or hallucinated in closed-book, document-grounded settings and emitting an evidence-grounded justification rather than a bare label. Three ingredients: a domain-agnostic synthetic dataset derived from FineWeb and refined by multi-stage curation and data reformation; synthetic grounded and hallucinated claims; and preference-based fine-tuning with Odds Ratio Preference Optimization to distil large-model reasoning into the smaller backbone. Building the training signal from synthesized claim pairs rather than annotated ones is what makes it domain-agnostic.

## Results

On the RAGTruth subset of LLM-AggreFact, 84.4% balanced accuracy, above MiniCheck (7B, 84.0%) and Granite Guardian 3.3 (8B, 82.2%) at roughly half their parameters. Across the full benchmark, 77.1% balanced accuracy, above GPT-4o at 75.9%.

## Limitations

The RAGTruth margin over MiniCheck is 0.4 points, within the range that evaluation noise can produce, and no variance or seed information is reported. Training claims are synthetic, so the grounded/hallucinated distinction learned is the one the generator produced rather than one observed in real RAG failures. Scope is closed-book document-grounded verification, so it does not cover claims requiring outside knowledge. Model and datasets were to be released on acceptance.

## Why it matters here

- **reasoning-training**: A distillation result where the target is verification rather than problem-solving: a 4B model trained to judge groundedness beats 7B and 8B specialists and GPT-4o. That matters to this topic because verification quality bounds every RLVR and process-supervision method tracked here, and it suggests the verifier need not be large — the archive's verifier line has largely assumed capability scales with the judge. It also pairs with doi:10.18653/v1/2026.findings-acl.2102 in this drain, which finds evaluator accuracy rises with reasoning tokens spent: one buys verification with parameters, the other with inference compute, and neither is compared against the other.

## Entities

- **Concepts**: [hallucination](../../../../wiki/concepts/hallucination.md), retrieval-augmented generation, groundedness, [verification](../../../../wiki/concepts/verification.md), reasoning distillation, synthetic data generation, guardrail, balanced accuracy
- **Methods**: Odds Ratio Preference Optimization, preference-based fine-tuning, [reasoning distillation](../../../../wiki/methods/reasoning-distillation.md), synthetic claim generation
- **Datasets**: RAGTruth, LLM-AggreFact, FineWeb

Tags: `hallucination`, `rag`, `verification`, `distillation`, `small reasoning model`, `orpo`

## Abstract

Large Language Models excel at NLP tasks but remain prone to hallucinations, limiting trust in real-world applications. We present HalluGuard, a 4B-parameter Small Reasoning Model (SRM) designed as a guardrail for Retrieval-Augmented Generation (RAG) pipelines, which classify document-claim pairs as grounded or hallucinated in closed-book, document-grounded settings and produces evidence-grounded justifications. Our approach combines (i) a domain-agnostic synthetic dataset derived from FineWeb and refined through multi-stage curation and data reformation, (ii) synthetic grounded and hallucinated claims, and (iii) preference-based fine-tuning with Odds Ratio Preference Optimization (ORPO) to distill large-model reasoning into a smaller backbone. On the RAGTruth subset of the LLM-AggreFact benchmark, HalluGuard achieves 84.4% balanced accuracy (BAcc), surpassing specialized models, MiniCheck (7B; 84.0%) and Granite Guardian 3.3 (8B; 82.2%) while using roughly half their parameters. Across the benchmark, it reaches 77.1% BAcc, surpassing larger general-purpose LLMs such as GPT-4o (75.9%). HalluGuard and datasets will be released upon acceptance.

---

Record id: `doi:10.18653/v1/2026.findings-acl.835`
