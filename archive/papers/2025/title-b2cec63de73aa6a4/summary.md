<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Provable Scaling Laws for the Test-Time Compute of Large Language Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/118984>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Proposes and proves scaling laws for two black-box test-time-compute algorithms for LLMs, a knockout tournament and a league-style aggregation, showing failure probability decays exponentially or by a power law as compute grows.

## Problem

Establishing provable scaling laws for test-time compute of LLMs, i.e. formal guarantees on how the failure probability of an LLM decreases as more compute is spent generating and comparing candidate solutions at inference time, without a verifier or reward model.

## Contributions

- A two-stage knockout-style algorithm (generate candidates, then single-elimination tournament) with proven exponential or power-law decay of failure probability as test-time compute grows
- A two-stage league-style algorithm (candidates ranked by average win rate against multiple opponents rather than single elimination) with proven exponential decay of failure probability under more robust assumptions
- Both algorithms need only a black-box LLM, with no verifier or reward model, making them simple to implement and adapt

## Method

The knockout-style algorithm first generates multiple candidate solutions to a problem, then runs a knockout tournament where candidates are compared pairwise and eliminated until one final output remains. The league-style algorithm instead evaluates each candidate by its average win rate across comparisons against multiple opponents, rather than eliminating it after a single loss. Both rely only on a black-box LLM to generate candidates and to judge pairwise comparisons; no separate verifier or reward model is used.

## Results

Theoretical proofs that failure probability decays to zero exponentially (or by a power law, depending on the scaling regime) as test-time compute grows for both algorithms; the theory is validated experimentally with diverse models and datasets, but no specific numeric results are given in the abstract.

## Limitations

The theoretical guarantees rely on two assumptions: the LLM can generate a correct solution with non-zero probability, and it does better than random guessing when comparing a correct against an incorrect solution. The abstract does not name the specific models or datasets used to validate the theory, nor give numeric results.

## Why it matters here

- **overthinking**: Directly addresses test-time-compute scaling for LLMs: proposes and theoretically proves scaling laws for two black-box strategies (knockout tournament, league aggregation) that trade additional test-time compute for a provably lower failure probability, which is the accuracy/compute tradeoff this topic tracks, though the focus is on parallel sample aggregation rather than reasoning-chain length or stopping criteria.

## Entities

- **Concepts**: test-time compute scaling laws, pairwise candidate comparison, black-box LLM aggregation
- **Methods**: knockout-style tournament algorithm, league-style algorithm
- **Datasets**: _none recorded_

Tags: `test-time-compute`, `scaling-laws`, `tournament-aggregation`, `black-box-llm`

## Abstract

Abstract We propose two simple, principled and practical algorithms that enjoy provable scaling laws for the test-time compute of large language models (LLMs). The first one is a two-stage knockout-style algorithm: given an input problem, it first generates multiple candidate solutions, and then aggregate them via a knockout tournament for the final output. Assuming that the LLM can generate a correct solution with non-zero probability and do better than a random guess in comparing a pair of correct and incorrect solutions, we prove theoretically that the failure probability of this algorithm decays to zero exponentially or by a power law (depending on the specific way of scaling) as its test-time compute grows. The second one is a two-stage league-style algorithm, where each candidate is evaluated by its average win rate against multiple opponents, rather than eliminated upon loss to a single opponent. Under analogous but more robust assumptions, we prove that its failure probability also decays to zero exponentially with more test-time compute. Both algorithms require a black-box LLM and nothing else (e.g., no verifier or reward model) for a minimalistic implementation, which makes them appealing for practical applications and easy to adapt for different tasks. Through extensive experiments with diverse models and datasets, we validate the proposed theories and demonstrate the outstanding scaling properties of both algorithms.

---

Record id: `title:b2cec63de73aa6a4`
