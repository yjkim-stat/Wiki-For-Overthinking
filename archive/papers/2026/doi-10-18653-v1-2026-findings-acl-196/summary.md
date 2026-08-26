<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models

- **Authors**: Yuxuan Jiang, Dawei Li, Francis Ferraro
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.196/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.196.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.196
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While Large Reasoning Models (LRMs) excel at complex tasks via long Chain-of-Thought (CoT) reasoning, their outputs are often excessively verbose, leading to inefficiency. This problem is amplified when the student’s long-form reasoning mismatches the concise outputs of smaller teacher models—common in LLM distillation to avoid using costly large teachers. To address this issue, we propose Distilled Reasoning Pruning (DRP), a hybrid framework that combines inference-time pruning with tuning-based distillation. DRP leverages a teacher model to perform mathematical problem-solving skill-aware step decomposition and pruning, then distills the refined reasoning paths into a student model, enabling efficient and accurate reasoning. Across challenging math datasets, DRP significantly reduces token usage without sacrificing accuracy—for instance, cutting tokens on GSM8K from 917 to 328 while improving accuracy from 91.7% to 94.1%, and reducing AIME tokens by 43% with no performance drop. Further analysis shows that aligning training CoT structure with the student’s capacity is key to effective knowledge transfer.

---

Record id: `doi:10.18653/v1/2026.findings-acl.196`
