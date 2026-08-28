<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic

- **Authors**: Yichuan Ma, Linyang Li, Yongkang Chen, Peiji Li, Xiaozhe Li, Qipeng Guo, Dahua Lin, Kai Chen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.211/>
- **PDF**: <https://aclanthology.org/2026.acl-long.211.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.211
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Timely Machine redefines test-time scaling in agentic settings as wall-clock time rather than token/generation length (since unpredictable tool-call latency decouples the two), introduces Timely-Eval to benchmark this, and trains Timely-RL (SFT cold-start + a sinusoidal time-utilization RL reward) so an 8B model learns to query elapsed time and dynamically size its reasoning to a time budget, beating much larger models' on-time completion rates and outperforming Qwen3-8B on all three general-reasoning benchmarks.

## Problem

Test-time scaling is traditionally defined by generation length because token count and inference time are proportional in pure-generation tasks, but in agentic tasks with tool calls, tool-execution latency is unpredictable and can dominate total time -- a concise trajectory using slow tools can take longer than a long trajectory using fast tools -- so token-based budget control is insufficient, and models lack any intrinsic awareness of, or ability to plan around, actual wall-clock time budgets.

## Contributions

- a reformulation of test-time scaling for agentic tasks as wall-clock time rather than token/generation length, motivated by a formal decomposition of when tool latency dominates, is dominated by, or roughly matches generation time
- Timely-Eval, a benchmark spanning interactive text games, machine-learning tasks, and general reasoning under configurable time budgets and tool latencies, revealing that model-size scaling advantage flips direction depending on tool latency and that existing models lack time-budget-adaptive reasoning
- Timely-RL, a time-aware cold-start-plus-RL training recipe with a sinusoidal time-utilization reward (ablated against linear and step-function alternatives) that gives an 8B model measurable, budget-responsive reasoning-length adaptation and on-time completion rates exceeding much larger untrained models
- empirical evidence that Timely-RL training, not scale or generic RLVR alone, produces genuine time awareness, validated via ablation against SFT-only and standard-RLVR-only baselines

## Method

Formalizes total agentic task time as generation time plus tool-execution time summed over interaction rounds, and derives three regimes via the per-step latency ratio (tool time / generation time): tool-dominated, generation-dominated (collapses to standard token-length control), and mixed. Introduces Timely-Eval, a benchmark spanning Interactive Games (four Jericho text adventures with controllable per-action latency), Machine Learning tasks (adapted from MLEBench-Lite, execution-time-dominated), and General Reasoning tasks (AIME, MATH, GPQA-Diamond, with a timer tool and a hard timeout). Builds Timely-RL: cold-start SFT distilling time-budget-varying solutions from a teacher equipped with a timer tool, plus interaction traces from DeepSeek-V3.2 on interactive games, followed by a GRPO variant whose reward combines correctness/formatting with a sinusoidal time-utilization bonus that grows and saturates as elapsed time approaches the budget, designed to reward appropriately-paced full budget use without over-penalizing minor timing variation near the deadline.

## Results

Scaling experiments across four interactive games and Qwen3 models (0.6B-32B) show tool latency flips which model size wins: at low/no latency smaller models can outperform larger ones by completing more interaction rounds, but as latency increases the task becomes tool-dominated and larger models pull ahead via higher per-round interaction quality. TimelyLM-8B (Qwen3-8B cold-started then Timely-RL-trained) outperforms untrained Qwen3-8B on all three general-reasoning benchmarks (MATH 78.0 vs. 71.2, AIME 42.5 vs. 40.0, GPQA-Diamond 49.5 vs. 37.5) and achieves the best or near-best Machine Learning task scores among all evaluated models including much larger ones, while remaining competitive with substantially larger general models on interactive games despite being cold-started on only the first 50 steps of each game. Under a reduced (0.75x) time budget, TimelyLM-8B achieves the highest on-time completion rate across AIME/GPQA/MATH (53.3%/52.0%/56.0%) versus Qwen3-8B/14B/32B (18-46%) and even versus larger closed models, while matching or exceeding their accuracy -- Qwen3-series models cannot adapt reasoning length to shrunken budgets and frequently fail to finish in time. TimelyLM's average token count clearly increases as the time budget scales from 0.75x to 3.0x, while Qwen3-series models show comparatively flat length changes across budgets; an ablation shows Timely-RL achieves markedly higher on-time completion than SFT alone, and standard RLVR (no time-aware reward) on the same SFT checkpoint fails to produce comparable adaptation. Reward-design ablation confirms the sinusoidal utilization bonus outperforms both a linear-reward variant (under-incentivizes full budget use) and a step-function reward (coarse intervals fail to distinguish trajectories within the same bin), across standard and reduced-budget settings.

## Limitations

Evaluation is currently conducted only on text-based tasks; multimodal interactive tasks with image or video streams introduce more complex and variable latencies not addressed here. The framework does not fully address multi-agent deployment where latency arises from another LLM's own generation time; training for effective time-aware collaboration in such contexts remains open. Accuracy improvements from Timely-RL training vary by benchmark difficulty in ways not yet fully characterized.

## Why it matters here

- **overthinking**: Directly relevant, and a useful complication of the topic's usual token-count framing: it argues that in tool-using agentic settings, token length is not even the right unit for measuring 'how much a model thinks,' since tool latency can decouple wall-clock cost from generation length entirely -- a concise trajectory can be slow, and a long one can be fast. This reframes the overthinking mitigation problem (train models to use their budget well, not just to generate fewer tokens) and its finding that model-size scaling advantage flips with tool latency is a caution for any efficiency comparison in this archive that assumes token count is a reliable proxy for inference cost in agentic or tool-augmented settings.

## Entities

- **Concepts**: Timely Machine (wall-clock-time test-time scaling), tool-dominated / generation-dominated / mixed latency regimes, sinusoidal time-utilization reward, time-budget-aware cold start
- **Methods**: Timely-RL (time-aware GRPO with sinusoidal reward), Timely cold-start SFT, timer-tool-augmented reasoning
- **Datasets**: [AIME](../../../../wiki/datasets/aime.md), [MATH](../../../../wiki/datasets/math.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), MLEBench-Lite (Leaf Classification, Spaceship Titanic, Random Acts of Pizza, Detecting Insults), Jericho interactive fiction games (Zork1, Advent, Enchanter, Detective), AM-DeepSeek-R1-Distilled-1.4M (distillation source), DataScience-Instruct-500K

Tags: `test-time-scaling`, `agentic-reasoning`, `time-budget-awareness`, `reinforcement-learning`, `tool-use`

## Abstract

As large language models (LLMs) increasingly tackle complex reasoning tasks, test-time scaling has become critical for enhancing capabilities. However, in agentic scenarios with frequent tool calls, the traditional generation-length-based definition breaks down: tool latency decouples inference time from generation length. We propose Timely Machine, redefining test-time as wall-clock time, where models dynamically adjust strategies based on time budgets. We introduce Timely-Eval, a benchmark spanning high-frequency tool calls, low-frequency tool calls, and time-constrained reasoning. By varying tool latency, we find smaller models excel with fast feedback through more interactions, while larger models dominate high-latency settings via superior interaction quality. Moreover, existing models fail to adapt reasoning to time budgets. We propose Timely-RL to address this gap. After cold-start supervised fine-tuning, we use reinforcement learning to enhance temporal planning. Timely-RL improves time budget awareness and consistently boosts performance across Timely-Eval. We hope our work offers a new perspective on test-time scaling for the agentic era.

---

Record id: `doi:10.18653/v1/2026.acl-long.211`
