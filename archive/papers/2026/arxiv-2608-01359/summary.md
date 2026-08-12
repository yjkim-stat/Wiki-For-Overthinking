<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents

- **Authors**: Jianan Xie, Xin Sun, Zhongqi Chen, Xing Zheng, Shu Wu, Bowen Song, Liang Wang
- **Venue**: cs.CL
- **Published**: 2026-08-02
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01359>
- **PDF**: <https://arxiv.org/pdf/2608.01359v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Outcome-based reinforcement learning enables search-augmented language agents to learn from verifiable final answers, but its trajectory-level credit cannot distinguish the contributions of individual actions in a multi-turn search process. We propose EviSD, an evidence-conditioned self-distillation framework that uses instance-level supporting evidence as privileged information for search actions and golden answers as complementary privilege for answer actions. During training, the student samples actions from the original context, while the same model re-scores them as a privileged teacher under an action-aligned context. EviSD converts the detached teacher--student gap into a bounded correction to the outcome-derived GRPO advantage and applies it only to generated action spans. This design localizes privileged guidance while preserving the update direction determined by the outcome reward, without an auxiliary distillation objective or any change at inference time. Across seven question-answering benchmarks and three backbones spanning model scales and generations, EviSD achieves the highest macro-average Exact Match in all evaluated settings, outperforming the strongest compared methods by 1.3--2.3 points while modulating only 6.7%--15.1% of response tokens. Code is available at https://github.com/JiananXie/EviSD.

---

Record id: `arxiv:2608.01359`
