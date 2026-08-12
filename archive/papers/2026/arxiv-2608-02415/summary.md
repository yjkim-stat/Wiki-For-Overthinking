<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes

- **Authors**: Nan Chen, Zhouhao Yang, Soufiane Hayou
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02415>
- **PDF**: <https://arxiv.org/pdf/2608.02415v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approaches for intent classification. For this purpose, we consider two lightweight, training-free methods based on statistics of internal representations and compare them against MLP classifiers and linear probes. Our comprehensive empirical evaluation reveals that 1) Both training-free and training-based methods saturate easy benchmarks (mathematics vs. coding vs. natural language), 2) Training-based classifiers have an advantage on harder classification tasks (e.g. Java vs Python), and 3) Training-free methods are generally more robust to mixed-intent and adversarial prompts.

---

Record id: `arxiv:2608.02415`
