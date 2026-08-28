<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Ranking Reasoning LLMs under Test-Time Scaling

- **Authors**: Mohsen Hariri, Michael Hinczewski, Jing Ma, Vipin Chaudhary
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1544/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1544.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1544
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Formalizes ranking reasoning LLMs under test-time scaling as inference over a dense response tensor of repeated stochastic trials, compares 72 ranking methods (paired-comparison, IRT, voting, graph/spectral) across 20 models and four Olympiad math benchmarks, and finds Bayes_R0@N (Bayesian mean with an empirical greedy-decoding prior) is the most stable low-budget ranking method -- though its greedy prior can introduce systematic bias when greedy and stochastic sampling disagree.

## Problem

Test-time scaling evaluates reasoning LLMs by sampling multiple outputs per prompt, but which statistical ranking method to use for the resulting repeated-trial benchmark data -- especially with a small number of trials (low budget) -- remains underexplored, and different ranking-method families can produce noticeably different model orderings whose agreement varies with benchmark difficulty.

## Contributions

- a formalization of dense benchmark ranking under test-time scaling via the response tensor R, unifying pointwise, pairwise and listwise/setwise ranking-method families as different transformations of the same underlying data
- a low-budget-stability and convergence evaluation protocol comparing 72 ranking methods across 20 reasoning models and four Olympiad math benchmarks, up to N=80 trials
- identification of Bayes_R0@N (an empirical greedy-decoding prior incorporated into a Bayesian estimator) as generally the most stable low-budget ranking method, with an explicit account of when its variance reduction can become a bias (when greedy and stochastic sampling disagree)
- Scorio, an open-source library implementing the studied ranking methods with Bayesian options, plus an extension of the framework to categorical (non-binary) outcome ranking

## Method

Formalizes the dense benchmark-ranking problem via a response tensor R in {0,1}^(L models x M questions x N trials), and connects common ranking-method families (pointwise/IRT models operating on per-question solve rates; pairwise win/tie models like Bradley-Terry and graph/spectral methods like PageRank/HodgeRank operating on pairwise comparison counts; listwise/setwise models like Plackett-Luce operating on winning/losing sets) as different transformations of R. Defines an empirical gold-standard ranking, Bayes_U@80 (Bayesian posterior-mean under a uniform prior using all 80 trials, order-equivalent to mean accuracy avg@80), and evaluates 72 ranking methods' low-budget stability (agreement between a ranking computed from N=1 subsampled trial and either the gold standard or the method's own full-trial ranking) and their convergence as N grows from 1 to 80, using Kendall's tau_b. Also studies Bayes_R0@N, which incorporates a single greedy-decoding output per question as an empirical prior into the Bayesian estimate, versus the uniform-prior Bayes_U@N, and extends the framework to categorical (non-binary) outcomes using auxiliary signals (answer format, confidence, token efficiency, verifier judgments) via a Dirichlet-multinomial model. Experiments cover 20 reasoning LLMs on AIME'24, AIME'25, HMMT'25 and BrUMO'25 (30 questions each, N=80 trials via top-p sampling, plus one greedy decode per question), releasing the methods as an open-source library, Scorio.

## Results

At full budget (N=80), most of the 72 ranking methods agree closely with the Bayes_U@80 gold standard (mean Kendall's tau_b 0.93-0.95 across benchmarks, median 0.95-0.99), and 19-34 methods recover exactly the same ordering (tau_b=1); the largest deviations (tau_b 0.68-0.79) come from a small set of voting rules (minimax, Nanson variants) and difficulty-weighted baselines. In the low-budget (N=1) regime, Bayes_R0@1 is the best-agreeing method with the gold standard on AIME'24/25 and BrUMO'25 (tau_b=0.779-0.858), while on the hardest benchmark (HMMT'25) a 21-method equivalence class (including Bayes_U@1 and several graph/voting-based methods) ties for best at tau_b=0.790; Rasch MML with LCB scoring is the most self-consistent method (best agreement with its own full-trial ranking) on three of four benchmarks (tau_b=0.804-0.834), while Nanson's rule with tie averaging is most self-consistent when benchmarks are pooled (tau_b=0.892). Using the empirical greedy-decoding prior (Bayes_R0@N vs. Bayes_U@N) reduces variance at N=1 by 16-52% depending on benchmark, but this variance reduction does not guarantee improved gold-standard agreement: the prior helps (increases tau_b) on AIME'24/25/BrUMO'25 but hurts on HMMT'25, and the direction of this effect tracks 'greedy-sampling alignment' (tau_G-S, the Kendall's tau_b between greedy-decoding rankings and full-trial stochastic-sampling rankings at N=80) -- higher tau_G-S predicts the prior helping more. Bootstrapped model-pool robustness analysis (pools of 5, 10, 15 models) shows the qualitative best-method recommendation is stable, with cross-subset ranking variance shrinking substantially (e.g. standard deviation of tau_b on Combined falling from 0.084 at pool size 5 to 0.023 at pool size 15) as pool size grows. In the categorical-ranking extension, signal-rich schemes (verifier-only, OOD-robust) achieve the highest self-consistency (tau_Self=0.892-0.897) but the lowest gold-standard agreement (tau_GS=0.824-0.840), and this self-consistency/gold-standard trade-off widens further on harder benchmarks.

## Limitations

Experiments focus exclusively on mathematical reasoning benchmarks with binary correctness outcomes; partial credit or open-ended outputs, where category boundaries are less clear and annotation/verification noise is larger, are not evaluated. When informative priors are used (especially those derived from auxiliary signals other than greedy decoding), the paper argues the prior source and specification should always be reported explicitly, since a misaligned prior can introduce systematic bias relative to the stochastic evaluation regime being approximated -- a caution the paper raises about its own Bayes_R0@N method rather than only about alternatives.

## Why it matters here

- **overthinking**: Methodological infrastructure rather than a direct contribution to the topic: it does not study reasoning length or the accuracy/efficiency tradeoff, but it addresses a problem every other paper in the archive that reports test-time-scaling results implicitly relies on -- how many stochastic trials are needed, and which ranking/aggregation method, to reliably compare reasoning models under repeated sampling. Its finding that low-budget rankings can be unstable, and that a naive prior can introduce systematic bias, is a caution relevant to any efficiency claim in this archive derived from a small number of sampled reasoning trajectories.

## Entities

- **Concepts**: dense benchmark ranking under test-time scaling, low-budget ranking stability vs. convergence, empirical greedy-decoding prior (Bayes_R0@N), greedy-sampling alignment (tau_G-S)
- **Methods**: Bayes_U@N / Bayes_R0@N (Bayesian posterior-mean ranking), Bradley-Terry / Rao-Kupper (pairwise paired-comparison models), Rasch / IRT models, PageRank, Rank Centrality, HodgeRank (graph/spectral ranking), Borda, Copeland, Nanson (voting rules), Plackett-Luce / Davidson-Luce (listwise/setwise models)
- **Datasets**: [AIME'24](../../../../wiki/datasets/aime-2024.md), [AIME'25](../../../../wiki/datasets/aime-2025.md), [HMMT'25](../../../../wiki/datasets/hmmt25.md), BrUMO'25

Tags: `evaluation-methodology`, `statistical-ranking`, `test-time-scaling`, `benchmarking`, `bayesian-inference`

## Abstract

Test-time scaling evaluates reasoning LLMs by sampling multiple outputs per prompt, but ranking models in this regime remains underexplored. We formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library that implements statistical ranking methods such as paired-comparison models, item response theory (IRT) models, voting rules, and graph- and spectral-based methods. Across 20 reasoning models on four Olympiad-style math benchmarks (AIME’24, AIME’25, HMMT’25, and BrUMO’25; up to N = 80 trials), most full-trial rankings agree closely with the Bayesian gold standard Bayes_𝒰@80 (mean Kendall’s τ_b = 0.93–0.95), and 19–34 methods recover exactly the same ordering. In the single-trial regime, the best methods reach τ_b ≈ 0.86.Using greedy decoding as an empirical prior (Bayes_R₀@N) reduces variance at N = 1 by 16–52%, but can bias rankings when greedy and stochastic sampling disagree. These results identify reliable ranking methods for both high- and low-budget test-time scaling. We release Scorio as an open-source library at https://github.com/mohsenhariri/scorio.

---

Record id: `doi:10.18653/v1/2026.acl-long.1544`
