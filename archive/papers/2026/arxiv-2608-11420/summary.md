<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology

- **Authors**: Del Coburn, Scott Sanner, Dan Silver
- **Venue**: cs.AI
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11420>
- **PDF**: <https://arxiv.org/pdf/2608.11420v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Medical diagnostic reasoning is a high-impact use case for LLMs that carries significant implications for the health and wellbeing of users. When OpenAI (2026) reports that more than 5% of ChatGPT messages globally are healthcare-related, the transparency of these systems becomes a serious design concern. This is especially true for complex cases, where differential diagnosis often requires integrating multiple forms of specialist reasoning. Existing work has proposed multi-agent approaches to medical diagnosis, but it remains unclear when such systems are needed, why they help, and where they outperform monolithic inference. We introduce Social Chain of Thought (SCoT),a multi-round pipeline for medical differential diagnosis that structures multi-agent interaction as a deliberative framework for collabora. tive LLM reasoning. Evaluating SCoT against single-agent baselines, one-agent pipeline ablations, and best-of-n scaling, we show that its recall advantage is not reproduced by monolithic inference alone. SCoT is most successful in the hardest diagnostic cases, where multiple rounds of specialist conversation help recover ground-truth diagnoses and converge on a higher-recall differential.

---

Record id: `arxiv:2608.11420`
