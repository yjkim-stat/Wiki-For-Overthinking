<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning

- **Authors**: Haoyu Zheng, Yun Zhu, Qing Wang, Wenqiao Zhang
- **Venue**: cs.LG
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07371>
- **PDF**: <https://arxiv.org/pdf/2608.07371v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

---

Record id: `arxiv:2608.07371`
