<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Consilience for Verifier-Free Test-Time Scaling

- **Authors**: Lecheng Kong, Like Hui, Haitao Mao, Jun Huan
- **Venue**: cs.CL
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09898>
- **PDF**: <https://arxiv.org/pdf/2608.09898v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces consilience, a verifier-free test-time-scaling selection metric that picks the sampled reasoning rollout whose confidence starts low (exploratory) and ends high (convergent), fixing a failure mode where naive confidence maximization favors confidently wrong answers on hard problems.

## Problem

Confidence-based verifier-free test-time scaling ranks and selects sampled rollouts solely by average confidence, but this catastrophically breaks down on complex tasks, where uniformly high confidence often signals a failure to explore rather than correctness, causing confidence maximization to favor confidently wrong answers.

## Contributions

- Shows that on hard problems (low Pass@1), confidence-based verifier-free test-time scaling inverts: incorrect completions have higher mean confidence than correct ones, so naive confidence maximization selects 'confidently wrong' answers.
- Introduces the consilience score, a combinatorial metric (final-window confidence minus alpha times initial-window confidence) that explicitly rewards a rising confidence trajectory instead of uniformly high confidence.
- Introduces reasoning-phase isolation, restricting the confidence computation to the reasoning trace (e.g., before </think>) rather than the answer-restating tokens.
- Demonstrates consilience outperforms Pass@1 and existing confidence-based baselines (self-certainty, DeepConf) across math (HMMT), graduate-level QA (GPQA), free-form code generation (LiveCodeBench), and an agentic coding benchmark (SWE-bench Verified).

## Method

Defines token-level confidence as the negative mean log-probability of the top-K candidate tokens at each decoding step. Observes that across a full dataset, higher average confidence correlates with correctness, but on the subset of hard problems (Pass@1 < 20%) this relationship inverts, with incorrect completions forming a heavy-tailed high-confidence group. Proposes the consilience score S = C_final - alpha*C_initial, where C_initial and C_final are average token confidences over boundary windows of size W near the start and end of the (reasoning-phase-isolated) generated sequence, alpha>=0 penalizing high initial confidence while rewarding high final confidence. During test-time scaling, n completions are sampled per prompt and the one maximizing S is selected (best-of-n, training-free, no external verifier). Reasoning-phase isolation splits the sequence at a model-specific delimiter (e.g., </think>) so the score is computed only over the active reasoning trace, excluding the more deterministic answer-summarization tokens. The method is also integrated into an agentic coding loop (mini-SWE-agent), applying consilience to select among n=32 sampled actions at large edit steps.

## Results

With n=64 sampled completions: on LiveCodeBench, the reasoning-isolated variant (Cns-think) raises GPT-OSS-120B to 69.7% accuracy versus Pass@1's 65.7% and versus self-certainty's degraded 64.5%, and raises Qwen to 60.4-60.9% versus Pass@1's 55.3%. On HMMT 2025, self-certainty degrades GPT-OSS-20B from Pass@1's 76.5% down to 68.0%, while consilience reaches 78.0-80.7%. On GPQA-Diamond, consilience reaches 72.0-73.8% versus Pass@1's 71.8% (OSS-20B) and 60.5% (Qwen). Difficulty-stratified results on LiveCodeBench show consilience is neutral on easy problems (near-ceiling Pass@1, e.g. 99.9-100.0%) but improves medium-difficulty accuracy by up to +13.7 points and improves hard-tier accuracy (e.g. GPT-OSS-120B hard tier 17.2% vs. mean-confidence baseline's 13.4%). On the agentic SWE-bench Verified benchmark (n=32), mini-SWE-agent + consilience raises the issue-resolve rate from 23.0% to 26.9% for GPT-OSS-120B and from 65.3% to 67.3% for Qwen3-Coder-Next. On hard problems, consilience separates correct from incorrect completions with AUROC 0.61-0.62 versus chance-level 0.47-0.50 for mean confidence, and the within-problem rise in confidence (final minus initial) is statistically significant on LiveCodeBench (p=0.011, 0.018) and GPQA (Wilcoxon p=0.042).

## Limitations

The suggested frozen hyperparameters (alpha=3, window k=20%) capture only 72-78% of the per-dataset grid-search optimum under 5-fold cross-validation, so some gain is left on the table without per-task tuning; performance degrades if the penalty multiplier alpha is set too large, over-penalizing early exploration. Applying consilience with n=32 samples at every step of an agentic workflow incurs roughly 32x the compute of a single rollout; in the authors' implementation this took about 18 hours versus 8 hours for the plain agent on their hardware, though only a subset of high-value steps were targeted. The method requires access to top-K token log-probabilities (K=5 used), so it needs at least partial logit access and is not purely black-box. On easy problems (near-ceiling Pass@1), consilience is neutral since all candidates already show similarly high initial confidence, leaving no discriminative signal to exploit.

## Why it matters here

- **overthinking**: Directly relevant: addresses test-time compute scaling for LLM reasoning by showing that naive confidence-based selection among sampled reasoning rollouts rewards 'premature convergence' -- a model collapsing onto a single line of thought too early instead of exploring diverse paths -- and proposes a verifier-free criterion (consilience) that instead favors trajectories that explored before converging. This is a selection method for the accuracy/efficiency tradeoff among parallel test-time-compute samples, targeting when reasoning has converged too soon rather than directly controlling the length of a single chain-of-thought.

## Entities

- **Concepts**: temporal confidence asymmetry (low initial, high final confidence), premature convergence vs. exploratory branching in reasoning trajectories, reasoning-phase isolation (separating chain-of-thought from final-answer tokens), the long-tail trap of confidence maximization on hard problems
- **Methods**: consilience score, self-certainty (baseline), DeepConf / DeepConf-20% (baseline), Pass@1, [best-of-n selection](../../../../wiki/methods/best-of-n-selection.md), reasoning-phase isolation, mini-SWE-agent integration
- **Datasets**: [LiveCodeBench-v6](../../../../wiki/datasets/livecodebench-v6.md), [HMMT 2025](../../../../wiki/datasets/hmmt-2025.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md), [SWE-bench Verified](../../../../wiki/datasets/swe-bench-verified.md)

Tags: `test-time-scaling`, `verifier-free`, `confidence-calibration`, `reasoning-selection`, `premature-convergence`

## Abstract

Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts. Verifier-free test-time scaling (or VF-TTS) is gaining extensive attention as a mechanism to enhance Large Language Model (LLM) reasoning, primarily because we do not have access to such high-quality verifiers in many real-world applications. Among existing VF-TTS methods, confidence-based VF-TTS methods, which compute and rank rollouts solely by confidence, are particularly promising. Such methods introduce near-zero overhead for sample evaluation and require minimal access to internal model states, making the methods highly flexible across models and tasks. In this paper, we demonstrate a critical limitation of existing confidence-based VF-TTS methods by showing that such methods catastrophically break down on complex tasks. We observe a very interesting phenomenon: uniformly high confidence frequently indicates a failure to explore, favoring confidently wrong answers. To address this, our core insight is that robust cognitive search requires a specific confidence trajectory pattern: such methods perform exploratory branching at the beginning, as manifested by low initial confidence, and converge to a high final confidence solution. To implement this insight, we introduce consilience, a novel selection framework that explicitly evaluates the temporal asymmetry of confidence in reasoning. We operationalize this via a combinatorial metric that actively penalizes high initial confidence while strictly demanding final certainty. Extensive experiments covering both graduate-level mathematics problems and free-form code generation demonstrate that consilience effectively outperforms existing baselines, validating our novel perspective on completion confidence.

---

Record id: `arxiv:2608.09898`
