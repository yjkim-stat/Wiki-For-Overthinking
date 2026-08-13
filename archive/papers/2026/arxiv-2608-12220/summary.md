<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward

- **Authors**: Zile Zhou, Huining Yuan, Weichen Zhang, Xinlei Chen, Xiao-ping Zhang
- **Venue**: cs.CV
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.12220>
- **PDF**: <https://arxiv.org/pdf/2608.12220v1>
- **Topics**: reasoning-training, test-time-scaling
- **Relevance score**: reasoning-training 0.50, test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Existing Vision-Language Models (VLMs) exhibits a critical bottleneck in robust spatial reasoning. Recent reinforcement learning (RL) methods aim to close this gap with verifiable outcomes, yet they suffer from poor credit assignment across intermediate reasoning steps. Concurrently, structured reasoning approaches overlook the critical depth perception necessary for comprehensive 3D understanding. To address these challenges, we propose SCOUT (Structured Chain-Of-Thought Utilizing Process-Supervised RL Training). Specifically, we design a structured Chain-of-Thought (CoT) framework that explicitly models 3D environmental perception to ensure robust spatial understanding and reasoning. Furthermore, we introduce a novel RL algorithm featuring multi-objective process rewards and a tailored advantage estimation method, facilitating fine-grained credit assignment across distinct segments of the reasoning trajectory. To support our framework, we develop SCOUT-24k, a structured spatial reasoning CoT dataset synthesized through a customized pipeline. Extensive evaluations demonstrate that SCOUT-3B improves upon baseline models by 16.85% and 6.3% on general spatial benchmarks and complex spatial reasoning tasks respectively. Notably, our larger SCOUT-7B even outperforms GPT-4o by a margin of 4.28%. Moreover, despite being trained exclusively on single image, SCOUT-7B exhibits robust out-of-domain generalization to multi-image and video scenarios. These empirical results render SCOUT as a critical step towards next generation of spatially-aware VLMs.

---

Record id: `arxiv:2608.12220`
