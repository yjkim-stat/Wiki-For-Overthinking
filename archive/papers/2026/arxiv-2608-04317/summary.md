<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Trident : How to Break Deep Reinforcement Learning Cyber Defenses (Agentic)

- **Authors**: Ryozo Masukawa, Ian Bryant, Armita Kazeminajafabadi, Sanggeon Yun, Hyunwoo Oh, SungHeon Jeong, Nathaniel D. Bastian, Mahdi Imani, Mohsen Imani
- **Venue**: cs.CR
- **Published**: 2026-08-05
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.04317>
- **PDF**: <https://arxiv.org/pdf/2608.04317v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

An agentic RLVR red-teaming framework that trains an LLM planner to attack deep-RL cyber-defence agents, showing those defences were only ever evaluated against static attackers.

## Problem

Deep-RL autonomous cyber defences are evaluated almost exclusively against static heuristic red agents, so their robustness against an adaptive attacker is unmeasured. Separately, RLVR has improved LLM reasoning but has no benchmark environment or interaction dataset in cybersecurity.

## Contributions

- A dynamic red-teaming benchmark with isolated sandbox servers over CybORG CAGE 4 and CyberWheel
- A dataset of over 13,000 red-blue interaction trajectories intended for RLVR training
- The Trident Agentic Code-as-Policy architecture, which casts red-agent training as a contextual bandit over a Summarizer/Planner/Coder decomposition
- An empirical demonstration that existing DRL cyber defences are brittle against an adaptive LLM attacker

## Method

Three components. A dynamic benchmark of isolated sandbox servers spanning CybORG CAGE 4 and CyberWheel; a dataset of over 13,000 red-blue interaction trajectories for RLVR; and a 'Code-as-Policy' architecture that reformulates red-agent training as a contextual bandit through a Log Summarizer / Planner / Coder split. The trainable Planner reads compressed execution logs and emits a complete attack strategy; a frozen Coder translates it into executable Python deployed against a live DRL defender. Only the Planner is trained, which is what makes the single-step bandit formulation possible.

## Results

With a single trainable 7B planner, blue-agent defensive performance falls by an average of 522% relative to static red-agent baselines. The trained attacker discovers decoy avoidance and adaptive state prioritization, behaviours static heuristics never produce.

## Limitations

Evaluated only in two simulators, so transfer to real networks is unestablished. The 522% average degradation is reported without a per-environment breakdown or variance, and a percentage change above 100% implies a signed reward whose scale is not given. The Coder is frozen, so the search is over strategies expressible in its code vocabulary. No accuracy or reasoning-benchmark evaluation of the planner is reported, so the effect of RLVR on the planner's general reasoning is unknown.

## Why it matters here

- **reasoning-training**: Peripheral. It uses RLVR as an off-the-shelf training signal for a security task rather than studying what that signal does to reasoning, and reports no reasoning-benchmark result. Its one transferable point for this topic is the architectural choice of training only a planner over compressed state while freezing the executor, which turns a long-horizon credit-assignment problem into a single-step bandit — the opposite bet from AgentOPSD (arxiv:2608.05987), which keeps the horizon and works on turn-level credit instead.

## Entities

- **Concepts**: reinforcement learning with verifiable rewards, contextual bandit, [credit assignment](../../../../wiki/concepts/credit-assignment.md), adaptive adversary, [emergent behaviour](../../../../wiki/concepts/emergent-behaviour.md)
- **Methods**: [RLVR](../../../../wiki/methods/rlvr.md), Code-as-Policy, contextual bandit formulation, log summarization
- **Datasets**: CybORG CAGE 4, CyberWheel, Trident red-blue interaction dataset (13,000+ trajectories)

Tags: `rlvr`, `cybersecurity`, `red teaming`, `agentic`, `off-topic-candidate`

## Abstract

Autonomous cyber defense systems based on Deep Reinforcement Learning (DRL) have attracted significant research attention, yet remain evaluated almost exclusively against static, heuristic red agents, leaving their robustness against adaptive threats critically understudied. Meanwhile, recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) have improved LLM reasoning, but their integration into cybersecurity remains elusive due to the absence of suitable benchmark environments and interaction datasets. To bridge this gap, we introduce Trident, an agentic LLM red teaming framework comprising three components: a dynamic benchmark with isolated sandbox servers spanning CybORG CAGE 4 and CyberWheel, a dataset comprises over 13,000 high-fidelity red-blue interaction trajectories for RLVR, and a ``Code-as-Policy'' RLVR agentic architecture Trident Agentic). The latter reformulates red agent training as a contextual bandit via a tripartite Log Summarizer--Planner--Coder design, where a trainable Planner generates complete attack strategies from compressed execution logs, which a frozen Coder translates into executable Python policies deployed against live DRL defenders. Empirical evaluations reveal a fundamental brittleness in existing defenses: with a single trainable 7B planner, Trident reduces blue agent defensive performance by an average of 522% compared to static red agent baselines while autonomously discovering emergent behaviors such as decoy avoidance and adaptive state prioritization that static heuristics entirely fail to uncover.

---

Record id: `arxiv:2608.04317`
