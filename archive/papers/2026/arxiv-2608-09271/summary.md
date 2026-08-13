<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SoftmaxGRPO: Learning to Reason using Softmax Advantage Group Estimation

- **Authors**: Jefferson Hernandez, Jaywon Koo, Zilin Xiao, Chen Wei, Vicente Ordonez
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09271>
- **PDF**: <https://arxiv.org/pdf/2608.09271v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Group-based reinforcement learning objectives such as GRPO can allocate learning signal poorly across prompt difficulty: under binary rewards, group normalization induces a divergent weighting on easy prompts. We introduce Softmax Advantage Group Estimation (SoftmaxGRPO), a drop-in alternative that replaces z-score-normalized group advantages with temperature-scaled softmax advantages, keeping weights bounded regardless of prompt difficulty. For binary rewards, we derive the exact finite-group population objective and identify MaxRL as its low-temperature limit. For bounded scalar rewards, we show that the large-group update exactly optimizes a log-moment-generating-function objective, while a universal finite-group scalar objective cannot exist without additional assumptions on the reward distribution. Empirically, SoftmaxGRPO reallocates measured gradient budget away from near-solved prompts and consistently improves over GRPO under identical rewards. It reaches 51.8% on DeepMath with verifiable rewards and improves a 1.5B instruction-tuned model from 35.0% to 68.0% on Poetry using only lightweight text-similarity rewards.

---

Record id: `arxiv:2608.09271`
