<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models

- **Authors**: Jiawei Li, Yang Gao, Huashan Sun, Chong Feng
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1386/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1386.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1386
- **Topics**: overthinking
- **Relevance score**: overthinking 0.73

## In one line

Introduces token-level marginal utility -- the per-token log-probability gain toward the ground-truth answer -- and MUTO, a training framework that penalizes trajectories and individual tokens that reduce this probability, cutting DeepSeek-R1-Distill-Qwen token usage by 87.1% (1.5B) / 80.2% (7B) with comparable or better accuracy.

## Problem

Large reasoning models frequently overthink, generating unnecessarily long inference trajectories with diminishing accuracy returns, but existing efficiency methods rely on coarse trajectory-level signals (length, external control) rather than knowing which individual tokens actually help or hurt the final answer.

## Contributions

- token-level marginal utility, a dense per-token supervision signal quantifying each reasoning token's log-probability contribution to the ground-truth answer, requiring no labeled CoT
- MUTO, an RLVR training framework that penalizes trajectories and tokens with negative marginal utility on top of a dual-mode Think/No-Think scaffold
- an efficiency-accuracy Pareto improvement across model scales (1.5B/7B) and six benchmarks, generalizing beyond math to GPQA/TheoremQA
- an analysis linking overthinking failures to accumulated negative-utility tokens causing the model to drift away from an answer it had transiently locked onto, rather than a pure capability deficit

## Method

Defines token-level marginal utility Delta_t = log p(y*|x,z<=t) - log p(y*|x,z<t-1), the change in the ground-truth answer's probability caused by each generated token, estimated by probing the model's answer likelihood after each token without altering the prefix. Builds MUTO (Marginal Utility Guided Thinking Optimization) on top of AutoThink's dual-mode (Think/No-Think) adaptive reasoning scaffold: at the trajectory level, a marginal-utility penalty discourages Think-mode trajectories whose final answer probability is lower than the No-Think baseline; at the token level, a redundancy penalty (based on the fraction of tokens with non-positive Delta_t, i.e. the Negative Utility Ratio) suppresses non-helpful tokens; both are combined with a length-shaping prior into a scalar reward optimized via GRPO-based RLVR. Marginal utility is computed sparsely (once every 20 tokens, sign propagated to a local window) for training efficiency.

## Results

On six math benchmarks with DeepSeek-R1-Distill-Qwen backbones: at 1.5B, MUTO cuts average token usage 87.1% (10,633->1,374 tokens) while improving accuracy +2.3%, including +5.8% on AIME24 (27.5%->33.3%); at 7B, it cuts tokens 80.2% (7,815->1,544) with only -0.1% accuracy change (64.4%->64.3%). Under the Length-normalized Accuracy metric (L-Acc), MUTO scores 47.5 (1.5B) and 57.6 (7B), beating baselines Concise-RL (40.9), ShorterBetter, ThinkPrune and AutoThink (37.3 at 1.5B; AutoThink needs ~3x more tokens for comparable accuracy at 7B). Generalizes beyond math: on GPQA and TheoremQA, MUTO improves accuracy 33.45->34.00 while cutting tokens 75.32% (1.5B), and 34.35->35.20 while cutting tokens 69.21% (7B). Even on an already-concise math-specialized backbone (Qwen2.5-Math-1.5B-Instruct), MUTO still improves accuracy +2.0 points while cutting tokens 12.9%, though the efficiency gain is smaller than on the long-CoT DeepSeek-R1-Distill backbones. Failure analysis on MATH finds incorrect trajectories have a higher Negative Utility Ratio than correct ones (45.8% vs 34.9%), and that in all incorrect trajectories the model transiently reaches high confidence in the correct answer before drifting away as negative-utility tokens accumulate -- evidence the paper reads as 'reasoning drift' rather than pure capability deficit.

## Limitations

Marginal utility is computed using ground-truth labels, making it most suitable for training/offline analysis and limiting direct use at inference time for open-ended queries without labels; the paper notes training a lightweight 'utility reward model' predicting token utility from the prefix as a direction to enable inference-time pruning. Validation is primarily on mathematical and scientific reasoning tasks with well-defined correctness; extending token-level utility optimization to creative writing or long-context summarization is called challenging because 'utility' becomes more subjective and multi-criteria. The paper flags a primary risk that encouraging shorter reasoning could remove useful intermediate steps in some cases, mitigated by defining utility directly against ground-truth log-probability and jointly training the think/no-think routing policy.

## Why it matters here

- **overthinking**: Central to the topic: proposes a fine-grained, causally-motivated (probability-gain) diagnostic for exactly which tokens in a reasoning trace are wasteful, and uses it to train models that cut tokens 80-87% with comparable or improved accuracy -- among the strongest length-reduction results in the archive -- plus a mechanistic account (transient correct-answer confidence followed by negative-utility-token-driven drift) for why overthinking happens at all.

## Entities

- **Concepts**: token-level marginal utility, Negative Utility Ratio (NUR), reasoning drift vs. capability deficit, dual-mode (Think/No-Think) adaptive reasoning
- **Methods**: MUTO (Marginal Utility Guided Thinking Optimization), GRPO / RLVR, AutoThink dual-mode scaffold, Length-normalized Accuracy (L-Acc)
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [Minerva](../../../../wiki/datasets/minerva.md), OlympiadBench (Olym.), [AIME24](../../../../wiki/datasets/aime-2024.md), [AMC23](../../../../wiki/datasets/amc23.md), [GPQA](../../../../wiki/datasets/gpqa.md), TheoremQA, DeepScaleR (training corpus, 40K problems)

Tags: `overthinking`, `efficient-reasoning`, `token-level-supervision`, `reward-shaping`, `reasoning-drift`

## Abstract

While Large Reasoning Models (LRMs) have demonstrated remarkable capabilities through explicit Chain-of-Thought (CoT) generation, they frequently suffer from “overthinking”. In this work, we bridge this gap by introducing Token-level Marginal Utility, which quantifies the per-token log-probability gain of the ground-truth answer. Leveraging this dense supervision signal, we propose MUTO (Marginal Utility Guided Thinking Optimization), a unified training framework designed to synthesize concise reasoning chains. Rather than relying only on coarse trajectory-level length control, MUTO identifies tokens that reduce the model’s likelihood of the correct answer and penalizes such negative-utility reasoning, yielding concise yet effective CoT trajectories. Experiments on DeepSeek-R1-Distill-Qwen backbones (1.5B and 7B) across six math reasoning benchmarks show that MUTO yields a markedly better efficiency-accuracy Pareto frontier. It reduces average token usage by 87.1% at 1.5B while improving accuracy by 2.3%, and cuts tokens by 80.2% at 7B with only -0.1% accuracy change, achieving the best length-normalized accuracy among baselines.

---

Record id: `doi:10.18653/v1/2026.acl-long.1386`
