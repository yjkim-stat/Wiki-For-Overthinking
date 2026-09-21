<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models

- **Authors**: Polina Tsvilodub, Max Höth, Michael Franke, Björn Deiseroth, Carina Kauf
- **Venue**: cs.CL
- **Published**: 2026-09-21
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2609.20846>
- **PDF**: <https://arxiv.org/pdf/2609.20846>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While modern large reasoning models (LRMs) excel at providing correct answers in many tasks, we provide additional evidence for the observation that they often struggle with a critical capability: knowing when to abstain from answering. We analyze this gap by comparing LRM behavior to results from a human study, revealing that human reasoning effort on unanswerable tasks is upper-bounded by answerable tasks, whereas LRMs waste computational resources by generating longer Chains of Thought (CoTs) on unanswerable than on answerable prompts. To overcome this inefficiency, we take inspiration from a resource-rational perspective on human cognition and introduce a novel GRPO reward that encourages efficient reasoning about whether the task contains all the information needed to solve it. Fine-tuning several 4B LRMs with this reward leads to human-like abstention performance gains (+12.8% on average) while retaining answering capabilities and boosting the models' efficiency (44% shorter CoTs on average).

---

Record id: `arxiv:2609.20846`
