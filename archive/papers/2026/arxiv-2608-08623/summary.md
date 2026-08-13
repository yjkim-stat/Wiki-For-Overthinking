<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# MedCalc-R1: Knowledge-Guided Reward Framework for Medical Mathematical Reasoning

- **Authors**: Haotian Wang, Lian Yan, Xingzhi Yao, Fanshu Meng, Ye He, Jingchi Jiang, Yi Guan
- **Venue**: cs.AI
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08623>
- **PDF**: <https://arxiv.org/pdf/2608.08623v1>
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50, reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

In Reinforcement Learning with Verifiable Rewards (RLVR) frameworks for mathematical reasoning tasks, floating-point results are typically evaluated using a tolerance-based reward. However, this strategy suffers from challenges such as difficulty in threshold calibration, unstable training dynamics, and limited accuracy, especially in clinical scenarios. To address these limitations, we propose a knowledge-guided hybrid reward framework (\textsc{MedCalc-R1}). Specifically, we introduce a knowledge verification reward mechanism that enforces explicit generation of computational formulas, which are further validated by an external verifier to enhance interpretability and reasoning reliability. Furthermore, we design a hybrid soft-hard reward scheme combining a hard constraint based on clinical safety thresholds with a soft, precision-sensitive reward that progressively guides learning within the acceptable range. Experimental results demonstrate that our method significantly outperforms existing baselines in both reasoning accuracy and generalization capability, validating the effectiveness and applicability in safety-critical domains.

---

Record id: `arxiv:2608.08623`
