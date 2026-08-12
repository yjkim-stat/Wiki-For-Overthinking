<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

- **Authors**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
- **Venue**: cs.AI
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05987>
- **PDF**: <https://arxiv.org/pdf/2608.05987v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

Turns token-level teacher-student log-probability gaps into turn-level credit for agentic RL by recursively updating a Bayesian belief in log-odds space, identifying pivotal turns without a critic.

## Problem

RLVR builds trajectory-level advantage estimates, which fail to credit the few pivotal decisions that determine outcomes in long-horizon multi-turn agentic tasks. Privileged self-distillation gives denser supervision, but how those local signals should represent sequential credit is unresolved.

## Contributions

- AgentOPSD, a critic-free recursive method for turn-level credit assignment in agentic RL
- Aggregation of token-level teacher-student log-probability gaps into turn-level evidence
- A recursive Bayesian belief update in log-odds space producing history-dependent credit weights
- Pivotal-turn identification via marginal belief revision between consecutive states
- 89.1% success on ALFWorld with Qwen2.5-7B, above GRPO and self-distillation baselines

## Method

AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence, then recursively updates a Bayesian belief state in log-odds space. Log-odds is what makes the aggregation additive, so per-token evidence composes into a turn-level posterior. This yields a reweighting scheme converting sparse outcome supervision into turn-level credit, and identifies pivotal turns as the marginal belief revision between consecutive states. It is critic-free, needs no extra rollouts, and composes with standard policy optimization.

## Results

On ALFWorld, WebShop and Search-QA with Qwen2.5 at 3B and 7B, AgentOPSD outperforms GRPO and strong self-distillation baselines, reaching 89.1% success on ALFWorld with Qwen2.5-7B. Ablations attribute the gains to turn-level aggregation and to history-dependent recursive belief updates.

## Limitations

Only 89.1% on ALFWorld is quantified; margins over GRPO and the self-distillation baselines are not given in the abstract. Requires a privileged teacher, so it is not applicable where none exists. Evaluated on three agentic environments at two scales, all Qwen2.5, so model-family generality is untested. Pivotal-turn identification is validated by downstream reward rather than against any ground truth of which turns mattered.

## Why it matters here

- **reasoning-training**: A direct entry in this topic's central dispute — how to get dense credit without a process reward model. It answers with a teacher's log-probabilities as the density source and a recursive belief update as the aggregator, so the supervision is derived rather than learned, which sidesteps reward-model calibration entirely. The identification of pivotal turns by marginal belief revision is the same shape of claim as the token-selection literature in this archive, moved up from tokens to turns, and it makes the archive's four-way token-selection dispute a five-way one at a different granularity. It is one of three OPSD-family papers in this batch, with arxiv:2608.06243 varying the temporal weighting and arxiv:2608.06347 the multilingual pivot.

## Entities

- **Concepts**: [credit assignment](../../../../wiki/concepts/credit-assignment.md), [process supervision](../../../../wiki/concepts/process-supervision.md), [privileged information](../../../../wiki/concepts/privileged-information.md), [belief state](../../../../wiki/concepts/belief-state.md), [long-horizon reasoning](../../../../wiki/concepts/long-horizon-reasoning.md), pivotal decision, log-odds aggregation
- **Methods**: AgentOPSD, [on-policy self-distillation](../../../../wiki/methods/on-policy-self-distillation.md), [GRPO](../../../../wiki/methods/grpo.md), [RLVR](../../../../wiki/methods/rlvr.md), recursive Bayesian update, [token-level distillation](../../../../wiki/methods/token-level-distillation.md)
- **Datasets**: ALFWorld, WebShop, Search-QA

Tags: `credit assignment`, `agentic rl`, `self-distillation`, `grpo`, `turn-level`

## Abstract

Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in agentic reinforcement learning. AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space. This yields a principled reweighting scheme that converts sparse outcome supervision into turn-level credit signals and identifies pivotal turns through the marginal belief revision between consecutive states. The method is fully compatible with standard policy optimization and requires neither an additional critic nor extra rollouts. We evaluate AgentOPSD on ALFWorld, WebShop, and Search-QA using Qwen2.5 models at two scales (3B and 7B). AgentOPSD outperforms GRPO and strong self-distillation baselines, achieving 89.1% success on ALFWorld with Qwen2.5-7B. Ablation studies attribute the gains to turn-level aggregation and history-dependent recursive belief updates.

---

Record id: `arxiv:2608.05987`
