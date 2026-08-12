<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation

- **Authors**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
- **Venue**: cs.CL
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03077>
- **PDF**: <https://arxiv.org/pdf/2608.03077v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in terminology-intensive and stylistically constrained settings. We trace this failure to a credit-assignment bottleneck: existing methods optimize final outputs or coarse trajectories, but cannot identify which translation steps actually help the final translation. To address this, we propose PAMT, a process-aligned training framework that combines cold-start domain-aware Long-CoT supervision with reinforcement learning. PAMT uses sequence-level format and outcome rewards for the final translation, together with a step-level process reward that measures how much each explicit translation step increases the likelihood of the reference translation. Across two backbones, PAMT improves over base models, outperforms MT-specialized baselines on average, and remains competitive with strong LLMs/LRMs across in-domain, OOD, and multilingual settings.

---

Record id: `arxiv:2608.03077`
