<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Parallel Test-Time Scaling for Latent Reasoning Models

- **Authors**: Runyang You, Yongqi Li, Meng Liu, Wenjie Wang, Liqiang Nie, Wenjie Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.2069/>
- **PDF**: <https://aclanthology.org/2026.acl-long.2069.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.2069
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Extends parallel test-time scaling to latent reasoning models (which reason in continuous hidden-state vectors rather than tokens) by introducing two stochastic sampling strategies (Monte Carlo Dropout, Additive Gaussian Noise) to generate diverse latent trajectories and a Latent Reward Model trained with a step-wise contrastive objective to score and aggregate them, showing consistent scaling gains with best-of-N and beam search across three arithmetic benchmarks and backbones up to 4B parameters.

## Problem

Parallel test-time scaling (sampling multiple reasoning paths and aggregating via voting/best-of-N/search) is a proven way to convert extra inference compute into better token-based LLM performance, but latent reasoning models -- which replace explicit chain-of-thought tokens with continuous hidden-state vectors for greater efficiency -- lack any inherent mechanism to stochastically sample multiple diverse trajectories (no token-level probability distribution to sample from) and lack a scoring mechanism to aggregate sampled latent trajectories (no log-likelihoods or interpretable text for existing process reward models to read).

## Contributions

- introduction of parallel test-time scaling as a capability for latent reasoning models, previously exclusive to token-based reasoning paradigms
- two complementary, theoretically-grounded stochastic sampling strategies for continuous latent space (Monte Carlo Dropout for epistemic uncertainty, Additive Gaussian Noise for aleatoric uncertainty) with contrasting geometric exploration signatures (directional drift vs. isotropic dispersion) suited to different problem difficulties
- the Latent Reward Model (LatentRM), a step-wise-contrastively-trained scorer that enables effective best-of-N and beam-search aggregation over latent trajectories with no access to token-level probabilities
- extensive empirical validation across three benchmarks and five backbones (up to 4B parameters) showing both sampling strategies scale effectively with compute and that LatentRM-based aggregation consistently beats majority voting

## Method

Formalizes latent reasoning as an autoregressive process over continuous hidden-state vectors h_1:T, terminated by an end-of-thinking token. Introduces two complementary stochastic sampling strategies grounded in uncertainty-estimation theory: Monte Carlo Dropout (MC-dropout), keeping dropout active at inference with rate p to capture epistemic uncertainty via different weight-configuration samples per pass; and Additive Gaussian Noise (AGN), injecting independent zero-mean Gaussian perturbations (std sigma) directly into each latent thought to simulate aleatoric uncertainty. For aggregation, proposes the Latent Reward Model (LatentRM), a scoring head extending the latent backbone that maps a prompt and partial latent trajectory to a scalar promise score at each step; trained with a step-wise contrastive (softmax-over-candidates, cross-entropy) objective rather than isolated binary cross-entropy, using thought-level quality labels estimated by rolling out M stochastic completions from each sampled thought and computing the empirical fraction reaching the ground-truth answer. At inference, LatentRM supports best-of-N selection (summing per-step logits as a trajectory score) and LatentRM-guided beam search, compared against non-parametric majority voting.

## Results

On GSM8K-Test, GSM8K-Hard and MultiArith across five latent reasoning backbones (COCONUT, CODI, CoLaR, Latent-SFT, and Render-of-Thought up to 4B parameters), both MC-dropout and AGN scale monotonically with sample count N (coverage/pass@k rises with N for all three benchmarks and three backbones tested in detail), with diminishing marginal returns as N grows and increased sampling narrowing the performance gap between weaker and stronger backbone models (e.g. COCONUT and CODI reach nearly equivalent coverage at N=64 despite CODI's clear superiority at N=1). MC-dropout consistently achieves higher coverage than AGN across nearly all N, but a diversity analysis reveals a tradeoff: coverage peaks at a moderate diversity 'sweet spot,' and at high diversity levels AGN maintains or even improves coverage while MC-dropout's coverage declines sharply -- t-SNE visualization shows MC-dropout produces a directional, contiguous 'drift' pattern while AGN produces an isotropic radial 'firework' dispersion, and dropout's larger displacement helps more on hard questions (where correct regions are farther from the deterministic latent) while it can drift away from correct regions on easy questions where AGN's tighter central mass is more robust. Generalization experiments on larger backbones (Latent-SFT/Llama-3.2-1B, Render-of-Thought-2B/4B on Qwen3-VL) confirm the framework scales: on the challenging MATH500 benchmark, RoT-4B's Cov@16 improves from a deterministic baseline of 20.3% to 22.0%. For aggregation, accuracy increases monotonically with N across all three datasets under all three strategies, and both LatentRM-guided Best-of-N and beam search consistently outperform majority voting, confirming LatentRM successfully distinguishes promising latent trajectories from unpromising ones without any token-level probability signal; beam search matches Best-of-N on GSM-Test/MultiArith but trails on GSM-Hard, attributed to early-step score noise causing premature pruning on harder problems. Ablations isolating LatentRM's design choices show removing the step-wise contrastive objective in favor of plain BCE causes a noticeable accuracy drop (35.4->33.5 on GSM-Test Best-of-8), removing stochastic-rollout-based thought labels (using only final trajectory correctness) causes a further decline (->30.7), and an untrained random scalar head performs even worse than majority voting (28.9 vs. 33.6), confirming the gains come from LatentRM's learned evaluation rather than architectural modification alone.

## Limitations

The framework is presented as a proof-of-concept and in-depth analysis of parallel test-time scaling for latent reasoning models; real-time deployment would require additional engineering optimization not addressed here. Optimal performance depends on tuning the dropout rate p and Gaussian noise scale sigma per backbone architecture family (though the paper reports the search is straightforward, requiring no extra model training, and provides heuristic hyperparameter ranges by backbone style to reduce per-dataset re-tuning). LatentRM's beam search variant is noted to suffer from early-step score noise causing premature pruning specifically on harder problems (GSM-Hard), an unresolved weakness relative to Best-of-N in that setting.

## Why it matters here

- **overthinking**: Indirectly relevant: this is not about reducing or measuring overthinking in token-based reasoning traces, but about enabling parallel test-time scaling for a fundamentally more efficient reasoning paradigm (continuous latent 'thoughts' instead of verbose token-by-token chain-of-thought) that several papers in this archive treat as a compression target in its own right. Its LatentRM aggregation mechanism and diversity/coverage analysis are relevant infrastructure for any future work asking whether the overthinking literature's usual levers (length penalties, early stopping, self-consistency) can transfer to latent reasoning models, where the notion of 'reasoning length' itself is defined differently (number of latent steps, not tokens).

## Entities

- **Concepts**: latent (continuous) chain-of-thought reasoning, Monte Carlo Dropout for epistemic-uncertainty sampling, Additive Gaussian Noise for aleatoric-uncertainty sampling, Latent Reward Model (LatentRM), sampling diversity vs. coverage tradeoff
- **Methods**: Monte Carlo Dropout (MC-dropout), Additive Gaussian Noise (AGN), Latent Reward Model (LatentRM), [best-of-N selection](../../../../wiki/methods/best-of-n-selection.md), [beam search](../../../../wiki/methods/beam-search.md), [majority voting (baseline)](../../../../wiki/methods/majority-voting-baseline.md)
- **Datasets**: [GSM8K-Test](../../../../wiki/datasets/gsm8k-test.md), [GSM8K-Hard](../../../../wiki/datasets/gsm8k-hard.md), [MultiArith](../../../../wiki/datasets/multiarith.md), [MATH500](../../../../wiki/datasets/math500.md)

Tags: `latent-reasoning`, `test-time-scaling`, `parallel-sampling`, `reward-model`, `continuous-chain-of-thought`

## Abstract

Parallel test-time scaling (TTS) is a pivotal approach for enhancing large language models (LLMs), typically by sampling multiple token-based chains-of-thought in parallel and aggregating outcomes through voting or search. Recent advances in latent reasoning, where intermediate reasoning unfolds in continuous vector spaces, offer a more efficient alternative to explicit Chain-of-Thought, yet whether such latent models can similarly benefit from parallel TTS remains open, mainly due to the absence of sampling mechanisms in continuous space, and the lack of probabilistic signals for advanced trajectory aggregation. This work enables parallel TTS for latent reasoning models by addressing the above issues. For sampling, we introduce two uncertainty-inspired stochastic strategies: Monte Carlo Dropout and Additive Gaussian Noise. For aggregation, we design a Latent Reward Model (LatentRM) trained with step-wise contrastive objective to score and guide latent reasoning. Extensive experiments and visualization analyses show that both sampling strategies scale effectively with compute and exhibit distinct exploration dynamics, while LatentRM enables effective trajectory selection. Together, our explorations open a new direction for scalable inference in continuous spaces. Code and checkpoint are included as supplementary materials.GitHub Project: https://github.com/ModalityDance/LatentTTS

---

Record id: `doi:10.18653/v1/2026.acl-long.2069`
