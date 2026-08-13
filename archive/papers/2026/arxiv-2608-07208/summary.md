<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes

- **Authors**: Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand
- **Venue**: cs.CL
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07208>
- **PDF**: <https://arxiv.org/pdf/2608.07208v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similarities. They score the words a text uses, not the judgment a reader forms about it. Recent work has shown that a gap exists in what Large Language Models (LLMs) know internally versus what they express in their response. This paper asks whether that internal knowledge, read by monitoring the activations of frozen, out-of-the-box LLMs, can stand in for task-specific fine-tuning when measuring concept content, and which extraction method reads it best. We extract such measures via the Recursive Feature Machine (RFM) algorithm and via linear probing, and compare these against an embedding baseline, surface baselines, and the same model's own answer to the question. We demonstrate the approach on financial text, a domain studied extensively and served by established annotated resources, using a human-annotated Environmental, Social and Governance (ESG) dataset. The best linear probe comes within 0.6 percentage points of a fine-tuned domain classifier's accuracy without any task-specific fine-tuning, and outscores the same model's own answer to the question in eleven of twelve comparisons, so the activations carry concept content the response does not report. The simple probe consistently beats the RFM concept vectors, which in turn provide what classification alone does not: a continuous score intended to reflect how strongly a concept is present in a text, whose validation awaits graded labels.

---

Record id: `arxiv:2608.07208`
