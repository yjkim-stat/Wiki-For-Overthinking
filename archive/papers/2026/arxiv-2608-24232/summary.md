<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

- **Authors**: Zhenyu Wu, Siyuan Chen, Changchun Yang, Jiaqi Dong, Min Zhou, Ali Almadan, Talal Hammad, Faisal Wahbo, Aminullah Tora, Mona Alshahrani, Xin Gao
- **Venue**: cs.AI
- **Published**: 2026-08-25
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.24232>
- **PDF**: <https://arxiv.org/pdf/2608.24232v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

---

Record id: `arxiv:2608.24232`
