<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SLPO: Scaling Latent Reasoning via a Surrogate Policy

- **Authors**: Runyang You, Zhiyuan Liu, Yongqi Li, Wenjie Li
- **Venue**: cs.CL
- **Published**: 2026-07-22
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2607.19691>
- **PDF**: <https://arxiv.org/pdf/2607.19691v2>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

SLPO adds outcome-reward RL to autoregressive latent (continuous-vector) reasoners by scoring latent transitions with a Gaussian surrogate density built from MC-dropout forwards, and by training a stopping head that turns a fixed latent thinking budget into a learned per-instance horizon.

## Problem

Explicit chain-of-thought reasoners can be optimized with outcome-reward RL because every step is a sampled token with a tractable log-probability, and because rollout length is free to vary. Latent reasoners, which carry intermediate computation as continuous hidden vectors, have neither: the vocabulary distribution is bypassed so there is no per-step action likelihood for credit assignment, and existing latent reasoners (COCONUT, CODI) prescribe a fixed number of latent steps at training and inference, so nothing about the compute horizon is optimizable. Prior latent-policy methods (LEPO, Latent-GRPO, CoLaR) route back through the vocabulary or through architecture-specific latent heads, so they do not apply to a reasoner that propagates plain hidden states.

## Contributions

- Identifies the two missing interfaces that block outcome-reward RL for latent reasoning: no tractable likelihood over continuous latent transitions, and a fixed thinking budget that freezes the compute horizon.
- Introduces a surrogate policy density over latent transitions, estimated from K MC-dropout forwards as an isotropic Gaussian, that gives trajectory-level credit assignment without routing through the vocabulary or an architecture-specific latent head.
- Adds a correctness-supervised stopping head whose stopping-time likelihood enters the RL objective, so outcome rewards refine a fixed budget into a variable-horizon policy.
- Reports Pass@8 and Pass@16 improvements in all 12 backbone-dataset settings for two latent reasoners (COCONUT, CODI), under both RLOO and GRPO, with transfer to soft-token latent inference.
- Measures the resulting compute allocation: gate-selected latent length correlates with problem difficulty, and inter-step cosine distance rises while prefix effective rank falls.

## Method

Two stages on top of a released latent-reasoning checkpoint (the imitation stage is not retrained). (1) Stopping-gate cold start: a head g_theta over each latent state emits a stop probability s_theta(h) = sigma(g_theta(h)). For each training problem the backbone samples N=4 stochastic latent trajectories (MC-dropout, p=0.1) up to T_max=12; at each candidate stopping length t in [T_min=3, T_max] the answer is decoded from the truncated latent prefix and checked against the reference, giving an answer-valid stopping set V. The gate is trained to put probability mass on stopping times inside V, where P(tau=t) = rho_t * prod_{k<t}(1 - rho_k). (2) Surrogate latent policy optimization: for each prefix, K=4 independent dropout forwards give samples z^(k); their empirical mean mu and floored isotropic variance sigma^2 define a Gaussian surrogate under which the realized latent state h is scored, log pi~(h) = -(d/2) log(2 pi sigma^2) - ||h-mu||^2 / (2 sigma^2). The realized states are stop-gradient targets; gradients flow through the recomputed moments, so a positive advantage pulls mu toward the sampled state. The rollout score sums the surrogate latent-transition term, the answer-token log-likelihood, and the stopping-time log-probability, and is weighted by an RLOO or GRPO advantage from a binary correctness reward (beta=0, no KL term, no PPO clipping). At inference, latent steps run sequentially and stop at the first step where the gate exceeds a threshold chosen by validation sweep, so no candidate-prefix enumeration is needed.

## Results

Training on GSM8K-Aug; held-out GSM8K-Test, GSM-Hard, MultiArith. Table 1: +SLPO raises Pass@8 and Pass@16 in all 12 backbone-dataset-reasoner cells, with Pass@k averaged over three MC-dropout seeds at p=0.1 rather than temperature sampling. Largest gain is +12.07 points (26.8% relative) on Pass@8, MultiArith, Llama-3.2-1B COCONUT (45.00 -> 57.07). Deterministic accuracy gains are usually much smaller: CODI+SLPO on GSM8K goes 55.22 -> 55.27 (Llama-1B) and 42.30 -> 42.76 (GPT-2). Note the budget is not held fixed: ungated COCONUT/CODI run at T_max=6 while +SLPO is allowed T_max=12, so part of the parallel-sampling gain comes with a doubled maximum horizon. Table 2 (length): Llama-3.2-1B CODI+SLPO reaches 54.95 average accuracy at 5.79 mean latent steps, +1.05 points over Latent-SFT with 50.3% fewer latent steps, and on GSM8K beats explicit CoT-SFT by 1.17 points (55.27 vs 54.1) with 75.2% fewer reasoning steps; COCONUT+SLPO on Llama-1B stays weak in absolute terms (25.01 average). Soft-token transfer (Table 3, Llama-3.2-1B): SLPO best deterministic accuracy on GSM8K 46.70 and MATH500 27.20, but its sequence length grows to 256.65/642.32 tokens versus CoT's 200.18/599.02 and LEPO's 197.43/572.27, and its GSM8K Pass@32 (82.03) is below GRPO's 87.57. At 3B (Table 4) AIME 2025 Pass@1 rises 0.96 -> 3.33 and AMC23 Pass@1 27.03 -> 32.50. Fig. 5 shows SLPO expanding rollout length during soft-token training while GRPO and LEPO stay flat or contract. Fig. 7: gate-selected latent length correlates with problem difficulty (1 - acc@32) at Pearson r=0.30 validation, r=0.26 test, both p<0.001. Fig. 3: group size G is the dominant rollout axis; sensitivity to K is small. Fig. 6: after SLPO, inter-step cosine distance rises (+3.8% to +17.9%) and prefix effective rank falls in every backbone-dataset pair. Cost (Table 5 / App. A.4): 1.130 s per optimizer step at (K,G)=(4,8) on 4x RTX 5880 Ada, of which surrogate construction is 0.274 s (24%); G=4 drops this to 0.676 s, K=8 raises it to 2.021 s. All numbers are from GPU runs, none from simulation.

## Limitations

The paper states no limitations section; the conclusion only names larger backbones, open-ended reasoning and multimodal latent architectures as future work. Limits a reader should notice: (a) backbones are GPT-2 124M and Llama-3.2-1B/3B only, and tasks are grade-school arithmetic plus MATH500/AIME/AMC, so nothing tests a frontier-scale reasoner; (b) +SLPO is given T_max=12 against baselines fixed at 6, so the headline Pass@k comparison confounds the method with a larger compute ceiling; (c) Pass@k is measured under MC-dropout at p=0.1 rather than the usual temperature sampling, so the numbers are not directly comparable to standard Pass@k tables; (d) deterministic-accuracy gains are frequently under one point and no variance is reported for Acc; (e) the difficulty-length correlation that supports the adaptive-computation claim is weak (r=0.26-0.30) and is shown on GSM8K only; (f) on soft-token inference the method lengthens generations rather than shortening them, and loses to GRPO on GSM8K Pass@32; (g) AIME 2025 Pass@1 of 3.33 on 30 problems is one problem, so the 3.47x framing rests on a very small count; (h) the surrogate is an empirical Gaussian fitted from K=4 dropout samples, and App. A.5 gives only a sufficient condition for local improvement, not an unbiasedness guarantee.

## Why it matters here

- **overthinking**: Substantively on topic, from the 'keep going when it helps' side rather than the 'stop earlier' side. The archive's overthinking material is mostly about explicit token chains; this paper argues the whole accuracy/length tradeoff can be moved into hidden space, where a step costs no decoded token, and it supplies the missing machinery: a learned stopping head whose stopping-time likelihood is optimized by the same outcome reward that shapes the reasoning itself. Two results bear directly on the topic. First, a fixed thinking budget can be converted into a per-instance one after the fact, without retraining the imitation stage: Fig. 7 shows gate-selected latent length rising with empirical failure rate (r=0.30 validation, r=0.26 test, p<0.001), which is the adaptive-allocation behaviour the topic asks for, though the correlation is weak enough that it is a tendency and not a controller. Second, it is a counterexample to reading length reduction as the goal: on hidden-state recurrence the gate shortens (54.95 average accuracy at 5.79 latent steps, 50.3% fewer than Latent-SFT, and 75.2% fewer steps than explicit CoT-SFT at higher accuracy), but on soft-token inference the same objective lengthens generations (256.65 vs CoT 200.18 tokens on GSM8K, 642.32 vs 599.02 on MATH500) and Fig. 5 shows length growing over training where GRPO and LEPO contract. The comparison is also a caution for the topic's evidence standards, since +SLPO is evaluated at T_max=12 against baselines pinned at 6, so its parallel-sampling gains are not measured at matched budget.

## Entities

- **Concepts**: Latent reasoning, [Test-Time Scaling](../../../../wiki/concepts/test-time-scaling.md), [Thinking Budget](../../../../wiki/concepts/thinking-budget.md), Adaptive Stopping, Difficulty-Adaptive Compute Allocation, Outcome-Reward RL / RLVR, Trajectory-Level Credit Assignment, Pass@k under Parallel Sampling, MC-Dropout Stochastic Rollouts, Prefix Effective Rank
- **Methods**: SLPO (Surrogate Latent Policy Optimization), surrogate Gaussian latent-transition likelihood from MC-dropout, correctness-supervised stopping gate / first-stop objective, [RLOO](../../../../wiki/methods/rloo.md), [GRPO](../../../../wiki/methods/grpo.md), [COCONUT](../../../../wiki/methods/coconut.md), [CODI](../../../../wiki/methods/codi.md), LEPO, Latent-GRPO, [CoLaR](../../../../wiki/methods/colar.md), ReGuLaR, DART, Latent-SFT, soft-token / Soft Thinking inference, iCoT, CoT-SFT
- **Datasets**: GSM8K-Aug (training), GSM8K-Test, [GSM-Hard](../../../../wiki/datasets/gsm-hard.md), MultiArith, MATH500, [AIME 2025](../../../../wiki/datasets/aime-2025.md), [AMC23](../../../../wiki/datasets/amc23.md), SVAMP (latent-geometry probe only)

Tags: `latent-reasoning`, `continuous-cot`, `rlvr`, `test-time-scaling`, `adaptive-computation`, `stopping-policy`, `gsm8k`, `grpo`, `rloo`

## Abstract

Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners. Yet this scaling path remains computationally costly, since every intermediate step must be decoded as a language token. Latent reasoning instead carries intermediate computation as continuous vectors and already matches or surpasses explicit CoT at far shorter horizons. Despite this promise, latent reasoners remain largely imitation-bound, while explicit CoT has already moved past imitation via outcome-reward RL. Latent trajectories lack a tractable per-step likelihood and an adaptive stopping interface under fixed thinking budgets, so outcome rewards cannot elicit latent test-time scaling. We introduce Surrogate Latent Policy Optimization (SLPO) to bring outcome-reward RL to autoregressive latent reasoners: an empirical surrogate policy density over latent transitions for trajectory-level credit assignment, and a correctness-supervised stopping head that outcome-reward optimization refines into a variable-horizon policy. Across continuous and soft thinking settings, SLPO improves Pass@$k$ under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.

---

Record id: `arxiv:2607.19691`
