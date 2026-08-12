<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning

- **Authors**: Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xiong-Hui Chen, Jianxin Yang, Zhenru Zhang, Yuqiong Liu, An Yang, Andrew Zhao, Yang Yue, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-training

## In one line

Shows that the roughly 20% of CoT tokens with the highest entropy act as decision forks, and that restricting RLVR policy-gradient updates to only those tokens matches or beats full-gradient training, with the advantage growing with model size.

## Problem

RLVR is the technique behind recent reasoning models, but implementations train over all tokens with no account of what different tokens do in a reasoning trace. Tokens play heterogeneous functional roles — some choose between reasoning branches, most merely complete a phrase already determined — and treating them uniformly may waste or actively misdirect gradient. The mechanism by which RLVR improves reasoning was not characterized at the token level.

## Contributions

- An empirical characterization of token entropy in CoT: over half of tokens have entropy below 0.01 and only 20% exceed 0.672, and the highest-entropy tokens are logical connectors ('wait', 'however', 'thus', 'suppose', 'since') that bridge reasoning steps, while the lowest are word suffixes, code fragments and parts of mathematical expressions.
- A controlled decoding experiment establishing the causal role of these 'forking tokens': raising their sampling temperature improves accuracy while raising the temperature of the rest degrades or destroys output.
- Evidence that RLVR largely preserves rather than reshapes the base model's entropy pattern — over 86% of the top-20% high-entropy token positions still overlap with the base model at convergence — and that it primarily adjusts the entropy of already-high-entropy tokens.
- An RLVR variant that masks the policy gradient of the bottom 80% of tokens by entropy, evaluated on three Qwen3 base models against vanilla DAPO, with an ablation over the retained fraction (10%, 20%, 50%, 80%-lowest, 100%).

## Method

Token entropy H_t is the entropy of the generation distribution at position t (a property of the distribution, not of the sampled token). Analysis: over 10^6 response tokens from Qwen3-8B on AIME'24/'25 at T=1.0, the entropy distribution is measured and the 100 highest- and lowest-average-entropy frequent tokens are inspected. To test whether high-entropy tokens are causally special rather than incidentally uncertain, decoding is modified to use two temperatures — T_high for tokens whose entropy exceeds the 80th-percentile threshold h=0.672, T_low for the rest — and each is swept independently. Training: starting from DAPO (GRPO without a value network, with clip-higher, dynamic sampling, token-level policy-gradient loss and overlong reward shaping), the objective is modified in exactly two places: the advantage term is multiplied by an indicator that the token's entropy is at or above the batch threshold tau_rho, and the normalization denominator counts only those tokens. rho = 0.2 selects the top 20% of tokens within each batch, so the threshold is recomputed per batch rather than fixed. Nothing else changes — same hyperparameters as DAPO (clip_high 0.28, clip_low 0.2, max response 20480, batch 512, mini-batch 32, lr 1e-6, no KL loss, no entropy loss), trained on DAPO-Math-17K with verl.

## Results

Entropy structure: about 50.64% of tokens have entropy below 0.01; the 80th percentile is 0.672. Decoding intervention on Qwen3-8B (average of AIME'24 and AIME'25): raising T_high from 1.0 to 2.0 lifts the score from 71.67 to 72.22 and lowering it to 0 drops it to 68.33, while the same sweep on T_low peaks at 71.67 and collapses to 20.14 at T=3.0 and 0.14 at T=5.0 — so forking tokens benefit from more entropy and the majority tokens tolerate almost none. Entropy-pattern persistence: overlap of top-20% high-entropy positions with the base model falls only from 100% to 86.67% over 1360 RLVR steps. Main RLVR results (Acc@16, forking-token gradients vs all tokens): Qwen3-32B average 70.69 vs 66.59 (+4.10), with AIME'25 56.67 vs 45.63 (+11.04) and AIME'24 63.54 vs 55.83 (+7.71); Qwen3-14B average 64.39 vs 61.40 (+2.99), AIME'24 +5.21 and AIME'25 +4.79; Qwen3-8B average 54.23 vs 53.71 (+0.53), with AMC'23 regressing 77.19 vs 77.81. The 32B model reaches 63.5 on AIME'24 and 56.7 on AIME'25, reported as state of the art for RLVR from base models under 600B parameters, rising to 68.1 on AIME'24 when the response-length cap is raised from 20k to 29k. Response length grows in every configuration, by roughly 1378 (32B), 2876 (14B) and 1486 (8B) tokens on average. Ablation: 20% is the best retained fraction; 10% removes useful tokens and weakens exploration, 50% and 100% dilute it, and training on the bottom 80% lowest-entropy tokens degrades performance markedly.

## Limitations

The paper's own limitations: experiments cover only the Qwen family — LLaMA models were attempted but could not reach meaningful AIME performance — the data is mathematics only, with programming and ARC-AGI named as untested, and the conclusions are tied to the specific experimental setting, with the effective 20% proportion likely needing retuning in a different RLVR setup. What a reader should add: the headline scaling trend rests on three points (8B +0.53, 14B +2.99, 32B +4.10) and the 8B result is close to a wash with one benchmark regressing, so 'scales with model size' is an extrapolation from a short line. The accuracy gains are also bought with substantially longer responses — roughly 25-70% more tokens — which is a real inference cost the comparison does not price in, and rho = 0.2 was selected by ablation on the same benchmarks used to report the main results.

## Why it matters here

- **reasoning-training**: The clearest available answer to what RLVR is actually optimizing, and it is a claim about credit assignment: nearly all the gain comes from a fifth of the tokens, and the other four fifths contribute little or interfere. That reframes the training signal from a sequence-level to a token-role question, and it does so with a one-line change to DAPO rather than a new algorithm, which makes the result easy to check and to adopt. The finding that RLVR preserves over 86% of the base model's high-entropy positions is equally load-bearing for this topic: it argues RLVR sharpens a structure the base model already has rather than installing a new one, which bears directly on what training signal can and cannot produce. The paper's own discussion connects this to why SFT memorizes while RL generalizes, and argues clip-higher is preferable to an entropy bonus because the bonus raises entropy on exactly the low-entropy tokens that should stay deterministic.

## Entities

- **Concepts**: [token-level entropy](../../../../wiki/concepts/token-level-entropy.md), forking tokens, high-entropy minority tokens, entropy patterns in chain of thought, exploration in RLVR, [credit assignment](../../../../wiki/concepts/credit-assignment.md), [entropy bonus](../../../../wiki/concepts/entropy-bonus.md), clip-higher, policy gradient masking
- **Methods**: [RLVR](../../../../wiki/methods/rlvr.md), [DAPO](../../../../wiki/methods/dapo.md), [GRPO](../../../../wiki/methods/grpo.md), [PPO](../../../../wiki/methods/ppo.md), high-entropy token gradient masking, dual-temperature decoding, [verl](../../../../wiki/methods/verl.md)
- **Datasets**: [DAPO-Math-17K](../../../../wiki/datasets/dapo-math-17k.md), [AIME'24](../../../../wiki/datasets/aime-24.md), [AIME'25](../../../../wiki/datasets/aime-25.md), AMC'23, [MATH500](../../../../wiki/datasets/math500.md), [Minerva](../../../../wiki/datasets/minerva.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md)

Tags: `rlvr`, `entropy`, `forking tokens`, `dapo`, `grpo`, `exploration`, `credit assignment`, `mathematical reasoning`

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful approach to enhancing the reasoning capabilities of Large Language Models (LLMs), while its mechanisms are not yet well understood. In this work, we undertake a pioneering exploration of RLVR through the novel perspective of token entropy patterns, comprehensively analyzing how different tokens influence reasoning performance. By examining token entropy patterns in Chain-of-Thought (CoT) reasoning, we observe that only a small fraction of tokens exhibit high entropy, and these tokens act as critical forks that steer the model toward diverse reasoning pathways. Furthermore, studying how entropy patterns evolve during RLVR training reveals that RLVR largely adheres to the base model's entropy patterns, primarily adjusting the entropy of high-entropy tokens. These findings highlight the significance of high-entropy tokens (i.e., forking tokens) to RLVR. We ultimately improve RLVR by restricting policy gradient updates to forking tokens and uncover a finding even beyond the 80/20 rule: utilizing only 20% of the tokens while maintaining performance comparable to full-gradient updates on the Qwen3-8B base model and significantly surpassing full-gradient updates on the Qwen3-32B (+11.04 on AIME'25 and +7.71 on AIME'24) and Qwen3-14B (+4.79 on AIME'25 and +5.21 on AIME'24) base models, highlighting a strong scaling trend. In contrast, training exclusively on the 80% lowest-entropy tokens leads to a marked decline in performance. These findings indicate that the efficacy of RLVR primarily arises from optimizing the high-entropy tokens that decide reasoning directions. Collectively, our results highlight the potential to understand RLVR through a token-entropy perspective and optimize RLVR by leveraging high-entropy minority tokens to further improve LLM reasoning.

---

Record id: `local:7d5e3edea2d46b92`
