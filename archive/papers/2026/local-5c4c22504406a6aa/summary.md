<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers

- **Authors**: Jingkai Huang, Will Ma, Zhengyuan Zhou
- **Venue**: ICML
- **Published**: 2026-01-01
- **Source**: local
- **Topics**: test-time-scaling

## In one line

Stops self-consistency sampling by Bayesian posterior over which answer is the mode, and proves that tracking only the top two answer counts plus an aggregate is enough for asymptotic optimality.

## Problem

Self-consistency samples a fixed number of reasoning paths per query regardless of difficulty, which wastes compute on easy questions. Adaptive self-consistency methods stop early once a dominant answer emerges, but they use uninformative priors and so ignore what is known in advance about the answer distribution's shape — whether probability mass is peaked, meaning an easy query, or flat, meaning a hard one — which can be estimated from previous attempts by the same model on similar problems.

## Contributions

- A Bayesian formulation of adaptive self-consistency with an informative prior, as sequential hypothesis testing for mode identification
- The observation that the exact posterior costs O(K!) and is intractable for open-ended reasoning
- The L-aggregated posterior approximation, tracking the L-1 most frequent counts at cost O(K^L)
- A proof that L >= 3 achieves asymptotic optimality identical to the exact posterior, and that even L = 2 beats prior-free baselines under known priors
- Empirical confirmation that L = 3 matches the full posterior's sample efficiency without its computation cost
- The framing of optimal Bayesian stopping for mode identification without knowing the candidate answers as a new sequential-testing problem

## Method

Stopping is posed as sequential hypothesis testing for mode identification: sample until the posterior probability that the most-frequently-observed answer is the true mode exceeds 1 - delta. Because the answer set is unknown, the only information available after n samples is the partition of samples into groups of identical answers, compressed to a count-of-counts. The exact posterior requires enumerating injective mappings between observed and latent answers and costs O(K!) in the number of distinct answers, which is intractable for open-ended reasoning. The L-aggregated approximation tracks only the L-1 most frequent counts and lumps the remainder, reducing the cost to O(K^L). At L = 3 the state is the count of the most frequent answer, the count of the second most frequent, and everything else combined.

## Results

The approximated posterior remains unbiased and achieves asymptotic optimality for any L >= 3 — the rate of the asymptotic stopping time is identical to that under the exact posterior as the confidence level 1 - delta tends to 1. For known priors even L = 2 gives a smaller asymptotic stopping time than prior-free adaptive self-consistency baselines. Where the prior is uncertain, belonging to one of several candidates, L = 2 may lose efficiency but L >= 3 still beats the prior-free baselines. Non-asymptotically, L = 3 replicates the sample efficiency of the full L = K posterior from confidence level 0.8 upward without its computation time. For K = 2 the problem reduces to a sequential test between two Bernoullis with a closed-form rule.

## Limitations

The gains depend on having an informative prior over the answer distribution's shape, which must be estimated from historical attempts on similar problems — so the method is not drop-in for a new task or model without that data, and the uncertain-prior analysis covers a prior known to lie among several candidates rather than an arbitrarily wrong one. Only consistency is optimized, not correctness: the target is the mode of the model's answer distribution, so where the mode is wrong, stopping sooner reaches the wrong answer faster. Ties among equally frequent answers are broken at random. Asymptotic optimality is stated as the confidence level approaches 1.

## Why it matters here

- **test-time-scaling**: Gives the archive's answer-stabilization thread an optimality result rather than another heuristic. The concrete finding is unusually actionable: the whole decision needs just two numbers — how often the leading answer appeared and by how much it leads the runner-up — and the paper proves that a third statistic adds nothing asymptotically. That is a sharp bound on how complicated a stopping rule needs to be, and it retrospectively justifies the first-versus-second-margin heuristics the field already uses. It also separates cleanly from the archive's other stopping work: DEER and CUSUM read the model's internal state or entropy, while this reads only the answer counts, so the two families are estimating different things and could be combined. The standing caveat is that it targets the mode, and where the mode is wrong it only arrives at the wrong answer sooner — which is the same limit self-consistency itself has and the provable-scaling-law paper in this archive addresses from the other direction.

## Entities

- **Concepts**: self-consistency, [answer stabilization](../../../../wiki/concepts/answer-stabilization.md), [optimal stopping](../../../../wiki/concepts/optimal-stopping.md), sequential hypothesis testing, mode identification, [test-time compute](../../../../wiki/concepts/test-time-compute.md), adaptive compute allocation, [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), Bayesian prior
- **Methods**: adaptive self-consistency, L-aggregated posterior approximation, [majority voting](../../../../wiki/methods/majority-voting.md), sequential hypothesis testing, Beta-posterior updating
- **Datasets**: _none recorded_

Tags: `optimal stopping`, `self-consistency`, `bayesian`, `adaptive sampling`, `theory`

## Abstract

A simple strategy for improving LLM accuracy, especially in math and reasoning problems, is to sample multiple responses and submit the answer most consistently reached. In this paper we leverage Bayesian prior information to save on sampling costs, stopping once sufficient consistency is reached. Although the exact posterior is computationally intractable, we further introduce an efficient "L-aggregated" stopping policy that tracks only the L-1 most frequent answer counts. Theoretically, we prove that L = 3 is all you need: this coarse approximation is sufficient to achieve asymptotic optimality, and strictly dominates prior-free baselines, while having a fast posterior computation. Empirically, this identifies the most consistent (i.e., mode) LLM answer and achieves similar answer accuracy using fewer samples.

---

Record id: `local:5c4c22504406a6aa`
