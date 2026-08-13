<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training

- **Authors**: Xucong Wang, Zhe Zhao, Liheng Yu, Di Wu, Xiaofeng Cao, Pengkun Wang
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07147>
- **PDF**: <https://arxiv.org/pdf/2608.07147v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

---

Record id: `arxiv:2608.07147`
