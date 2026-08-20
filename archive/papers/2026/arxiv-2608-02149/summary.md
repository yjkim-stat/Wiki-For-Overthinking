<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning

- **Authors**: Yijun Zhang, Yule Xie, Jiaxin Ding, Xin Ding, Fan Xu, Haoxiang Zhang, Luoyi Fu
- **Venue**: cs.AI
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02149>
- **PDF**: <https://arxiv.org/pdf/2608.02149v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-training 0.25

## In one line

Treats a policy's per-problem failure probability as a random variable over the problem distribution and shows that REINFORCE, pass@K training and MaxRL each optimize a single moment of it, then proposes minimizing the first T moments jointly — which is exactly minimizing the expected truncated number of rollouts needed to reach a first success.

## Problem

RLVR objectives are usually compared by their motivations rather than by what they optimize. Written in terms of the failure-probability distribution across problems, they turn out to be doing the same kind of thing at different coordinates, and none of them characterizes the distribution's shape. That matters because a policy can lower its average failure probability by getting better at problems it already solves, leaving the hard tail where it was — and the objective gives no way to say so.

## Contributions

- A moment-based reformulation placing existing objectives on one axis: REINFORCE-style methods minimize the first raw moment of the failure-probability variable, pass@K training minimizes the K-th, and MaxRL minimizes a harmonically weighted sum of moments of a *transformed* variable rather than of the original one
- MMPO, which minimizes the first T moments with uniform coefficients, and the observation that this sum is precisely the truncated expected first-success stopping time under a finite rollout budget
- Two advantage estimators for it — a plug-in one used in the experiments and an unbiased leave-one-out construction, with a closed form when the truncation order equals the group size
- A proof that this whole family is strictly Schur-convex in the vector of per-problem failure probabilities, so it explicitly prefers success spread evenly across problems over the same mean concentrated on easy ones
- A bound showing the induced reweighting toward hard problems is strictly milder than pass@T's, which is offered as the reason it does not pay for tail gains with pass@1

## Method

For each problem the success probability of one rollout defines a failure probability, and drawing a problem at random makes that a random variable on the unit interval; by the Hausdorff moment theorem its complete moment sequence determines it. The objective is the sum of its first T raw moments. Because the first-success time is geometric, that sum equals the expected first-success time truncated at T+1, which is the operational reading. Differentiating gives a problem-level weight equal to a sum of k times the failure probability to the k-1, so implementation is GRPO with one extra per-problem reweighting: within a group of G rollouts the success rate is estimated empirically, the weight is formed from it, and the advantage is the weight times the centred reward, optimized under the usual clipped surrogate. Training uses Qwen3-1.7B-Base and Qwen3-4B-Base under verl on the MATH7.5K training set, batch of 16 problems, 8 rollouts each, learning rate 1e-6 without warmup, clipping at 0.2, sampling temperature and top-p 1.0, on two H20 GPUs, with Math-Verify as the rule-based verifier. Truncation order is 4 and the plug-in estimator is used. Evaluation is avg@1 on MATH500 and OlymMATH and avg@16 on AMC23, AIME24 and AIME25, checkpointed every 20 steps with the best average reported, at temperature 0.6 and top-p 0.95.

## Results

Average accuracy across the five benchmarks is 34.7 at 1.7B and 47.6 at 4B, against 33.9 and 45.0 for GRPO, 34.1 and 45.9 for pass@K training, 32.5 and 45.5 for DMPO, and 33.8 and 43.5 for MaxRL — margins over GRPO of 0.8 and 2.6 points. The average conceals per-benchmark losses: at 1.7B pass@K takes AIME24 (12.1 against 10.6) and AIME25 (7.5 against 5.4), GRPO takes MATH at 4B (84.0 against 84.2 — MMPO's is the underlined runner-up there by the paper's own marking), and MaxRL takes AMC23 at 4B. The distributional evidence is the more interesting part and matches the Schur-convexity theorem: on difficulty-controlled subsets the Gini coefficient of per-problem success rates is 0.3301 for MMPO against 0.3642 for GRPO, with the Lorenz curve closer to equality at every threshold. The first-success-time histogram localizes where the gain comes from — the two methods solve within five problems of each other on the first rollout, but more than thirty fewer problems remain unsolved after sixteen rollouts under MMPO. Pass@K measured after training moves in the same direction and widens with K: 47.6, 59.4, 63.4, 66.2 at K = 1, 4, 8, 16 against GRPO's 45.0, 56.2, 59.8, 62.2. The truncation-order ablation shows a real bias-variance trade-off rather than a monotone benefit: T = 4 is best, T = 3 second, and larger T degrades substantially because higher moments cannot be estimated reliably from eight rollouts. Among transformation variables, the degenerate choice that recovers plain MMPO beats the Beta-distributed ones that recover MaxRL-style harmonic weighting.

## Limitations

The paper states none. What a reader should weigh: the margins are 0.8 and 2.6 average points from single runs with no seeds or variance anywhere, and the reported figure is the best average across checkpoints evaluated every twenty steps — applied equally to all methods, but still a best-checkpoint protocol selected on the evaluation benchmarks rather than a held-out criterion. The truncation order T = 4 is likewise chosen by an ablation on the same model and benchmarks the headline table reports. The main results use the plug-in advantage estimator, which the authors say is generally biased; the unbiased leave-one-out estimator is derived in full and then not what produced the numbers. Scale is small — two base checkpoints under 4B, one training set, mathematics only, two GPUs — and the Schur-convexity result is a value judgement made explicit rather than a free improvement: the objective is designed to prefer evenly distributed success, and the bound on reweighting limits but does not eliminate the risk that buying tail coverage costs first-attempt accuracy, which is visible in the AIME columns at 1.7B.

## Why it matters here

- **reasoning-evaluation**: It supplies a vocabulary for something this archive keeps running into without a name: two RLVR methods can report the same mean accuracy while distributing it differently across problems, and mean accuracy cannot tell them apart. Writing each objective as a moment of the failure-probability distribution says exactly which coordinate a method optimizes, and the Gini coefficient and Lorenz curve over per-problem success rates give a measurement to go with it — 0.3301 against GRPO's 0.3642 on matched difficulty subsets. The first-success-time histogram is the cleaner diagnostic still: it separates 'solves more on the first try' from 'leaves fewer problems unsolved after sixteen', which are different capabilities that a single pass@1 number merges. It also gives a principled reading of the pass@k disagreement recorded elsewhere in this archive — pass@K training is not a different kind of objective from REINFORCE, it is the same objective evaluated at a higher moment, which is why the two can order methods differently.

## Entities

- **Concepts**: failure-probability distribution, moment-based objective, [reasoning boundary](../../../../wiki/concepts/reasoning-boundary.md), [advantage estimation](../../../../wiki/concepts/advantage-estimation.md), [exploration](../../../../wiki/concepts/exploration.md), Schur convexity, [problem difficulty](../../../../wiki/concepts/prompt-difficulty.md), first-success time, Gini coefficient
- **Methods**: MMPO, [GRPO](../../../../wiki/methods/grpo.md), pass@K training, [MaxRL](../../../../wiki/methods/maxrl.md), DMPO, [REINFORCE](../../../../wiki/methods/reinforce.md), [PPO](../../../../wiki/methods/ppo.md), leave-one-out advantage estimation
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [MATH-500](../../../../wiki/datasets/math500.md), OlymMATH, [AMC23](../../../../wiki/datasets/amc23.md), [AIME 2024](../../../../wiki/datasets/aime-2024.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), MATH7.5K

Tags: `reinforcement learning`, `policy optimization`, `moments`, `pass@k`, `difficulty distribution`

## Abstract

Reinforcement learning has become a central paradigm for improving the reasoning capabilities of large language models. Existing methods generally aim to reduce the failure probabilities induced across problems. In this paper, we introduce a moment-based perspective on policy optimization for LLM reasoning by treating the failure probability of a randomly sampled problem as a random variable and characterizing optimization objectives through its moments. Under this perspective, many existing methods optimize only a single moment of the failure-probability distribution, leaving its broader distributional structure largely uncharacterized. We propose \textbf{M}ulti-\textbf{M}oment \textbf{P}olicy \textbf{O}ptimization (MMPO), a novel policy optimization framework that jointly minimizes multiple moments of the failure-probability distribution. MMPO admits a direct operational interpretation as minimizing the expected truncated time required to obtain the first successful response. Beyond MMPO, we further develop a general moment-transformation framework that systematically induces different moment profiles and provides a unified view of a broader family of policy optimization objectives. Experiments across five mathematical reasoning benchmarks and models of different scales demonstrate that MMPO consistently outperforms strong baselines. We hope this moment-based perspective offers new insights into the design of policy optimization objectives for LLM reasoning.

---

Record id: `arxiv:2608.02149`
