<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VTO: Visual Tool Orchestration for Video Anomaly Detection

- **Authors**: Rui Wang, Yeteng Wu, Xianling Zhang, Mengshi Qi
- **Venue**: cs.CV
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08219>
- **PDF**: <https://arxiv.org/pdf/2608.08219v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-training 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Video anomaly detection (VAD) is a critical yet challenging task due to the complex and diverse nature of real-world scenarios. Traditional deep learning approaches are fundamentally limited by poor generalization across diverse scenarios. While multimodal agents offer a promising tool-learning paradigm for VAD, current systems relying on supervised fine-tuning struggle with complex orchestration, and standard reinforcement learning often causes premature termination due to coarse-grained outcome rewards. To address these challenges, we propose VTO, a process-supervised reinforcement learning framework. Moving beyond static tool usage, VTO enables the agent to dynamically explore and interact with the environment. Specifically, we introduce a foundation model-driven cognitive evaluator to provide context-aware semantic feedback, which is seamlessly integrated into a Process-Supervised Cognitive Alignment that delivers fine-grained, step-wise supervision. By explicitly penalizing logical truncation and rewarding complete causal chains, the agent optimizes its multi-step reasoning policy for interrelated tool orchestration. To support our proposed framework, we meticulously crafted VAD-Tool, a hierarchical visual tool set comprising 12 specialized vision tools spanning from entity tracking to high-stakes hazard detection, and established the corresponding benchmark for rigorous multi-step reasoning evaluation. Extensive experiments on VAD-Tool demonstrate that VTO significantly outperforms baselines, achieving up to a 10.2\% absolute accuracy improvement in tool scheduling. Code and data are available at https://github.com/MICLAB-BUPT/VTO.

---

Record id: `arxiv:2608.08219`
