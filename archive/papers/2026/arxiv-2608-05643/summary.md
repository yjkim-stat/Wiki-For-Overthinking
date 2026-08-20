<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning

- **Authors**: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, Dean F. Hougen
- **Venue**: cs.AI
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05643>
- **PDF**: <https://arxiv.org/pdf/2608.05643v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

A training-free, verifier-free test-time scaling method that refines each of N sampled reasoning rollouts through D rounds of self-critique and self-correction before majority-voting the answers, instead of only sampling more candidates or relying on an external verifier.

## Problem

Width-only test-time scaling (sampling more candidates and majority-voting or verifier-selecting among them) suffers diminishing returns because additional samples increasingly repeat existing answer patterns rather than adding new reasoning evidence, and because every i.i.d. rollout remains exposed to the same per-trace hallucination mechanism, which the paper shows analytically underestimates the model's latent accuracy; verifier-based selection is an alternative but depends on reward-model calibration.

## Contributions

- Identifies two limitations of width-only test-time scaling: diversity saturation (larger sample budgets increasingly revisit the same semantic reasoning clusters instead of adding new reasoning directions) and per-trace hallucination (each i.i.d. rollout is exposed to the same perturbation mechanism, creating a systematic accuracy floor below the model's latent accuracy).
- Proposes a training-free, verifier-free breadth-depth refinement framework: breadth samples N independent rollouts, depth applies D rounds of self-critique and self-correction to each rollout, and terminal traces are aggregated by majority voting, requiring no external verifier, reward model, or learned stopping policy.
- Evaluates across five math benchmarks and four open-weight models, showing consistent gains over greedy decoding, majority voting, verifier-based best-of-N, beam search, and lookahead decoding, plus compute-normalized analysis and refinement-dynamics diagnostics (recovery, regression, diversity, agreement).

## Method

Given a problem, the framework allocates test-time compute along two axes using the same base model in three role-conditioned prompts (generator, critic, corrector). Breadth: N independent reasoning rollouts are sampled i.i.d. at temperature tau>0 to preserve diverse initial reasoning directions. Depth: each rollout is refined over D iterative cycles, where at each depth d the generator continues/rewrites the previous corrected trace, a self-critic identifies possible logical, arithmetic or structural errors in that continuation, and a self-corrector revises the trace conditioned on both the reasoning and the critique (confirming the trace if no error is found). After D refinement steps, each rollout's terminal corrected trace is passed through a deterministic answer extractor, and the final prediction is obtained by plurality (majority) voting over the N per-rollout candidate answers -- no reward model, verifier score, or learned stopping policy is used at any point.

## Results

On Qwen2.5-Math-7B (N=8, D=4), the method reaches 16.67% on AIME25 (vs. 13.33% for the strongest verifier baseline RM@8), 67.5% on AMC (vs. 65.0% Maj@8/RM@8), 47.2% on OlympiadBench (vs. 41.0% RM@8) and 81.6% on MATH (vs. 81.0% RM@8). On the weaker Qwen2.5-1.5B, accuracy on MATH500 rises from 29.6% (RM@8) to 58.0%, and on AMC from 25.0% to 32.5%; AIME25 rises from 0.0-6.67% (baselines) to 6.67%. Ministral-8B and LLaMA-3.1-8B show similar but smaller gains (e.g. Ministral-8B AMC 42.5% vs. 30.0% RM@8; MATH 65.78% vs 61.4% RM@8). The self-critique ablation (Table 2, N=8, D=4) shows explicit critique helps most for Qwen2.5-1.5B (AIME25 0.0%->6.67%, AMC 27.5%->32.5%, MATH 55.6%->58.0%) and gives smaller but consistent gains for Qwen2.5-Math-7B (AMC 65.0%->67.5%, OlyBench 44.9%->47.2%). Compute-normalized gain (eta) is largest for Qwen2.5-1.5B (eta=17.10 vs Maj@8, 17.01 vs RM@8, average accuracy 13.21%/14.95% -> 25.67%) and smallest for the strongest model Qwen2.5-Math-7B (+2.36 avg accuracy points vs RM@8, eta=1.16), indicating gains shrink as base model strength increases. All results use N=8, D=4, temperature 0.7 on a single H100 GPU unless stated otherwise; Table 3 shows accuracy on AMC23 is not monotonic in N or D across models.

## Limitations

Stated limitations: (1) higher inference cost, since each rollout goes through reasoning, critique, and correction steps requiring more forward passes than greedy decoding, majority voting, or standard best-of-N; (2) the method depends on the base model's own ability to critique and revise its reasoning -- an inaccurate critique or an over-correction of a valid solution can introduce rollout-level regressions, though majority voting helps suppress isolated ones; (3) evaluation is limited to mathematical reasoning benchmarks where answers are well-defined and extraction is reliable, so effectiveness of verifier-free self-refinement in domains with more open-ended outputs or ambiguous evaluation criteria is untested. Table 3 also shows accuracy is not monotonic in breadth N or depth D (e.g. Qwen2.5-1.5B on AMC23 peaks at moderate settings rather than the largest N or D).

## Why it matters here

- **overthinking**: Directly on topic: this is a test-time compute allocation method for LLM reasoning that trades sampling breadth against per-trajectory refinement depth, explicitly targeting the accuracy/efficiency behavior of additional inference compute (Table 4 and Figure 5 report compute-normalized gains in TFLOPs, and the paper analyzes when extra depth helps vs. produces harmful over-corrections/regressions).

## Entities

- **Concepts**: diversity saturation under fixed sample budget, per-trace hallucination as a systematic accuracy floor, breadth-depth test-time refinement, verifier-free self-critique and self-correction, compute-normalized gain
- **Methods**: breadth-depth refinement framework, self-critique and self-correction (iterative), majority voting / plurality aggregation, compute-normalized gain metric (accuracy improvement per additional TFLOP)
- **Datasets**: AIME24, AIME25, [AMC](../../../../wiki/datasets/amc.md), OlympiadBench, MATH500

Tags: `test-time-scaling`, `self-correction`, `self-critique`, `majority-voting`, `reasoning-refinement`, `mathematical-reasoning`, `compute-allocation`

## Abstract

Test-time scaling improves LLM reasoning by using additional inference compute, but wider sampling alone can suffer from diminishing returns: new rollouts often repeat existing answer patterns instead of adding useful reasoning diversity. Verifier-based selection offers an alternative, but its performance depends on the calibration of an external reward model. We propose a verifier-free breadth--depth refinement framework that uses test-time compute to both explore and improve candidate solutions. The method samples multiple independent reasoning rollouts, refines each rollout through iterative self-critique and self-correction, and aggregates the refined answers by majority voting. Breadth preserves diverse initial attempts, while depth repairs local reasoning errors before aggregation. Across AIME24, AIME25, AMC, OlympiadBench, and MATH500, our method consistently improves over greedy decoding, majority voting, verifier-based best-of-$N$, beam search, and lookahead decoding across multiple open-weight models. For instance, with Qwen2.5-1.5B, accuracy increases from the strongest verifier-based baseline to $58.0\%$ on MATH500, and from $25.0\%$ to $32.5\%$ on AMC. These results show that test-time compute can be more effective when used to refine sampled trajectories rather than only to sample more candidates or rely on verifier-guided selection.

---

Record id: `arxiv:2608.05643`
