<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR

- **Authors**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03119>
- **PDF**: <https://arxiv.org/pdf/2608.03119v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) improves LLM reasoning but typically relies on ground-truth (GT) answers, limiting scalability. Voting-based label-free RLVR replace gold supervision with answer-level consensus from model samples. However, collapse arises when the same answer-level signal is used both to estimate rewards and to drive token-level policy optimization, encouraging the model to directly reinforce answer tokens rather than improve reasoning. We propose OM-GRPO, a label-free RLVR framework that decouples reward estimation from policy optimization. OM-GRPO masks gradients on the answer span while retaining answer-level rewards through a soft consensus signal, shifting optimization pressure away from answer tokens. We further introduce Contrast-Augmented Reward, which refines reward estimation via low-cost pairwise comparisons over existing trajectories without additional rollouts. Across diverse reasoning benchmarks and three LLM backbones, OM-GRPO consistently outperforms existing label-free RLVR methods and matches supervised GT-reward training with stable optimization. This stability is particularly beneficial in the Test-Time Training setting, where OM-GRPO surpasses majority voting by 4.24 points.

---

Record id: `arxiv:2608.03119`
