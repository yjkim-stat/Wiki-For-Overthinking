<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning

- **Authors**: Jaeeun Jang, Hansle Lee, Sangmin Kim
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.641/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.641.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.641
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Derives an exact, non-asymptotic decomposition of GRPO's token-level policy update showing entropy collapse in reasoning RL is driven by a small subset (~5%) of structurally critical 'branch-defining' tokens rather than uniform decay across the sequence, and proposes SCOPE, which applies KL regularization only to that top-5% (ranked by a computable redistribution score), consistently improving both Pass@1 and Pass@k under both RLVR and RLIF across model scales.

## Problem

Reinforcement Learning with Verifiable Rewards (RLVR) and Reinforcement Learning from Internal Feedback (RLIF) often fail to benefit fully from test-time compute because RL post-training systematically sharpens the policy -- improving single-sample accuracy (Pass@1) but collapsing the diversity of reasoning paths (eroding Pass@k) -- and existing entropy-regularization methods apply uniformly across the decoding sequence or rely on heuristic proxies (raw entropy thresholds) that are disconnected from the actual optimization dynamics driving this collapse.

## Contributions

- an exact, non-asymptotic token-level decomposition of GRPO policy updates, separating a smooth leading geometry term from a token-outcome coupling residual that identifies which token positions are structurally critical (branch-defining) versus ordinary continuations
- a mathematically grounded, computable redistribution score identifying the small subset (~5%) of tokens whose repeated reinforcement drives global entropy collapse
- SCOPE, a plug-in KL-regularization method applying selective (not uniform) entropy control to only this top-5% of tokens, consistently improving both Pass@1 and Pass@k under both RLVR and RLIF across model scales and as an add-on to five existing entropy-control methods
- demonstration that which updates are regularized matters far more than how much entropy is preserved overall, and that targeted regularization can improve Pass@1 without the usual exploration-exploitation trade-off cost to Pass@k at larger sampling budgets

## Method

Performs a fixed-context, token-level analysis of GRPO-style policy updates in logit coordinates, deriving an exact (non-asymptotic, no small-step approximation) decomposition of the expected redistribution magnitude S_v at each token position into a smooth leading geometry term L_v = 2*eta*A_scale*p_v(1-p_v) (depending only on current policy probability and global advantage scale) and a token-outcome coupling residual R_v (which is near-zero for ordinary continuation tokens but grows specifically at 'branch-defining' positions where sampling that token meaningfully alters downstream trajectory outcome). This shows entropy collapse is driven by tokens that (i) receive positive-advantage reinforcement, (ii) have intermediate (not extreme) policy probability enabling repeated sampling, and (iii) exhibit non-negligible expected update magnitude under the p_v(1-p_v) scaling -- a small subset of the action space whose repeated reinforcement induces global entropy decay. Proposes SCOPE (Structural Collapse-aware Optimization via Partial Entropy control): computes an online, per-sampled-token-instance Redistribution score s_{k,t} = p_{k,t}(1-p_{k,t})*[A_{k,t}]_+ (restricted to positive-advantage events), then applies KL regularization only to the top-q% of tokens in a minibatch ranked by this score (q=5% found optimal via ablation), leaving all other tokens' updates unregularized. Evaluated on Qwen2.5-Base models (1.5B/3B/7B) trained on MATH (7,500 problems) under both RLVR (verifiable-reward GRPO) and RLIF (self-certainty as intrinsic reward, INTUITOR), tested on GSM8K, MATH500, AMC, AIME24, AIME25, and against five entropy-control baselines (Forking RL, Div/DA-PO, KL-Cov, Self-Certainty, Tok-Entropy, Traj-Entropy) and five token-selection ablations (Uniform, Positive-Adv, Forking, Fork+Adv, Non-Forking, KL-Cov).

## Results

A redistribution-ablation sweep (varying the top-q% regularized from 0-100%) shows a consistent non-monotonic accuracy curve peaking around q~=5% across all benchmarks and model scales, confirming collapse-inducing tokens are highly sparse and selective regularization on the redistribution score alone captures the dominant drivers of collapse. SCOPE achieves the highest accuracy and lowest entropy-collapse metric (d_collapse) across all model scales and benchmarks under both RLVR and RLIF, outperforming all five token-selection-strategy baselines at the same 5% regularization budget -- Non-Forking selection (avoiding structurally critical positions) often underperforms even Uniform random selection, and Fork+Adv/KL-Cov attain comparable d_collapse to SCOPE but with lower accuracy, indicating indiscriminate entropy preservation retains uninformative rather than reasoning-relevant diversity. As a plug-in enhancement (+SCOPE) added to five existing RLVR/RLIF methods (Forking RL, Div, KL-Cov, Self-Certainty, Tok-Entropy, Traj-Entropy), SCOPE yields consistent gains across every base method, model scale, and paradigm, with the largest improvements on harder benchmarks (AMC, AIME24/25) -- e.g. Self-Certainty+SCOPE improves AIME24 from 0.054 to 0.115 at the 7B scale under RLIF, where confidence-based intrinsic objectives impose stronger entropy-reducing pressure and targeted regularization is proportionally more impactful than under RLVR. Multi-seed evaluation (N=10) shows SCOPE improves every individual seed's Acc@16 rather than relying on outlier runs, with stabilization more pronounced under RLIF (tighter seed distributions) than RLVR. Pass@k curves at the 7B scale show SCOPE's largest absolute gains occur at small k (improved sampling efficiency, concentrating probability mass on solution-relevant trajectories), and critically this Pass@1 improvement does not come at the expense of Pass@k at larger k -- a departure from the exploration-exploitation trade-off typically exhibited by standard RL post-training, where single-sample accuracy and sampling coverage are normally sacrificed against each other. On harder benchmarks SCOPE's advantage grows with k, while under RLIF the base (untrained) model surpasses both SCOPE and the INTUITOR baseline at large k on AIME24/25, confirming confidence-based intrinsic rewards reduce diversity beyond the point of net utility even with SCOPE mitigating it. Cross-architecture tests on Qwen2.5-Math-7B (already math-specialized) and LLaMA3.1-8B-Instruct show SCOPE's benefit is broadly applicable but depends on the base policy's structural properties: gains are smaller on Qwen2.5-Math-7B because its math-focused continued pretraining already leaves less headroom for diversity preservation, and gains on LLaMA3.1-8B-Instruct are modest on easier benchmarks with no meaningful benefit on harder ones (AIME24/25) where the baseline already scores near zero, consistent with LLaMA-family models exhibiting weaker search-like reasoning structure than Qwen-family models -- SCOPE can only rescue trajectories already within the base policy's support, not create new reasoning capability.

## Limitations

SCOPE's effectiveness is bounded by the base model's own policy support: on LLaMA3.1-8B-Instruct at the hardest benchmarks (AIME24/25) where the baseline already achieves near-zero accuracy, SCOPE (and entropy-control methods generally) provide no meaningful benefit, since the required reasoning trajectories evidently lie outside what the base policy can already generate. The redistribution score s_{k,t} is an instance-level modeling choice (using the leading geometry term as a surrogate for the not-directly-accessible exact quantities alpha_v, beta_v, and their covariance), not a proven-optimal approximation, and its justification is described as a rationale rather than a formal approximation theorem.

## Why it matters here

- **overthinking**: Directly relevant to the RL training dynamics that produce today's reasoning models and to test-time scaling more broadly: it provides a mathematically rigorous, mechanistic account of why RL post-training narrows a reasoning model's exploration (entropy collapse) at a small number of critical decision tokens, which bears on the archive's broader concern with when and why reasoning models fail to productively use additional test-time compute (Pass@k) even as they improve single-attempt accuracy. Its central finding -- that a vanishingly small subset of tokens governs a global reasoning-diversity property -- parallels this archive's recurring theme (also seen in Step Pruner and other papers this session) that reasoning quality and quantity are governed by a small set of structurally important positions rather than distributed uniformly across a trace, though this paper addresses training-time RL dynamics rather than inference-time trace length directly.

## Entities

- **Concepts**: entropy collapse (test-time scaling), branch-defining token, redistribution score, structural collapse-aware optimization, exploration-exploitation dilemma at the token level
- **Methods**: SCOPE (Structural Collapse-aware Optimization via Partial Entropy control), [GRPO](../../../../wiki/methods/grpo.md), INTUITOR (RLIF baseline), Forking RL (baseline), Div / DA-PO (baseline), KL-Cov (baseline), Self-Certainty (RLIF baseline), Tok-Entropy (baseline), Traj-Entropy (baseline)
- **Datasets**: MATH (training, 7,500 problems), [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AMC](../../../../wiki/datasets/amc.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md)

Tags: `entropy-collapse`, `test-time-scaling`, `reinforcement-learning`, `reasoning-diversity`, `GRPO`

## Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) and Reinforcement Learning from Internal Feedback (RLIF) often fail to benefit from test-time compute due to entropy collapse and the resulting loss of reasoning diversity. We show that this collapse is driven not by uniform entropy decay, but by premature overconfidence at a small number of structurally critical decision points. Based on a token-level analysis of GRPO-style policy optimization, we propose SCOPE (Structural Collapse-aware Optimization via Partial Entropy control), which assigns each generated token a redistribution score and applies selective KL regularization to only the top ∼ 5% of tokens under this score. Across model scales and architectures on math reasoning benchmarks, SCOPE consistently improves performance under both RLVR and RLIF settings, demonstrating that targeted entropy control at a vanishingly small subset of tokens is sufficient to sustain reasoning diversity and effective test-time scaling.

---

Record id: `doi:10.18653/v1/2026.findings-acl.641`
