<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Provable Scaling Laws for the Test-Time Compute of Large Language Models

- **Authors**: Yanxi Chen, Xuchen Pan, Yaliang Li, Bolin Ding, Jingren Zhou
- **Venue**: NeurIPS
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: test-time-scaling, reasoning-evaluation
- **Relevance score**: test-time-scaling 0.50

## In one line

Gives two aggregation algorithms whose failure probability provably decays to zero as inference compute grows, assuming only that the model can sometimes be right and can compare two solutions better than chance.

## Problem

High-stakes and agentic uses need success probabilities like 99.9% rather than 90%, because one error in a multi-step workflow ruins the output. Spending more inference compute is the obvious lever, but the standard aggregation methods carry no guarantee and can get worse with scale — best-of-N with an imperfect verifier can decay as adversarial solutions that fool the verifier become more likely to be found, and majority voting converges to zero whenever some incorrect answer is individually more probable than the correct one.

## Contributions

- A definition of a provable inference scaling law for LLM algorithms
- A two-stage knockout algorithm with exponential decay of failure probability in the number of candidates and comparisons
- A power-law guarantee for scaling candidates alone with the comparison budget held fixed
- A two-stage league algorithm scoring candidates by average win rate, with exponential decay under weaker and more robust assumptions
- Both algorithms needing only a black-box LLM, with no verifier or reward model
- The observation that majority voting's success probability converges to zero when an incorrect answer is individually more likely than the correct one

## Method

A provable inference scaling law is defined as an algorithm whose success probability can be pushed arbitrarily close to 100% as test-time compute grows under stated assumptions. The knockout algorithm generates N candidates in parallel, then runs a knockout tournament in which each encountered pair is compared K times and the majority decides; only pairwise comparison is used, so no verifier or reward model is needed. Assumption 2.1 is the whole content: for this input there is p_gen > 0 that a sampled solution is correct, and p_comp > 0.5 that a comparison of a correct against an incorrect solution picks the right winner. The paper notes that requiring p_comp > 0.5 for every such pair is restrictive and non-robust, and for that reason introduces the league algorithm, which scores each candidate by average win rate against many opponents rather than eliminating it on a single loss, so one bad pairing cannot remove a correct solution.

## Results

For the knockout algorithm, failure probability is bounded by (1 - p_gen)^N + ceil(log2 N) * exp(-2K (p_comp - 0.5)^2), decaying exponentially in both N and K; reaching failure delta needs N of order (1/p_gen) log(2/delta) and K of order (p_comp - 0.5)^-2 log(2 ceil(log2 N)/delta), so both are logarithmic in 1/delta. Scaling N alone with K held fixed still works, yielding a power-law relationship between failure probability and the number of candidates. The league algorithm's failure probability also decays exponentially, under the weaker assumption that some correct solution has a higher average win rate against a distribution of opponents than any incorrect one. Experiments span Llama3.1, Qwen2.5, GPT-4o and QwQ-32B on GPQA, MMLU-Pro and MATH-500.

## Limitations

The guarantees are per input problem, not per benchmark: p_gen and p_comp are defined for a specific question, so a problem the model never solves has p_gen = 0 and no amount of compute helps. The knockout assumption that comparison beats chance on every correct-versus-incorrect pair is acknowledged by the authors as strong and non-robust, and the league variant weakens rather than removes that requirement. The theory bounds failure probability but says nothing about the constants that decide affordability, and the cost is N generations plus K comparisons per tournament pair. Nothing here identifies when the assumptions hold for a given model and task, so the laws are conditional rather than predictive.

## Why it matters here

- **reasoning-evaluation**: Reduces the whole guarantee to one measurable quantity about a judge — p_comp, the probability that a pairwise comparison of a correct against an incorrect solution goes the right way. That is a sharper and more useful target than the absolute judge-accuracy numbers this archive holds, because the theorem says only the margin above 0.5 matters and it enters as (p_comp - 0.5)^-2. It gives a reason to measure pairwise discrimination rather than scoring calibration, and it connects to the archive's finding that a diffusion model can be badly calibrated yet rank correct above incorrect well: ranking is what these algorithms need.
- **test-time-scaling**: The first result in this archive that turns test-time scaling from an observed curve into a theorem, and it changes what the curve means: with the right aggregation the failure probability goes to zero, so a flattening curve is evidence about the aggregation rather than about a ceiling on the model. It also explains two failures the archive has only recorded empirically. Majority voting converging to zero when a wrong answer holds 46% against a right answer's 45% is the precise reason self-consistency saturates and then degrades. And best-of-N decaying with N under an imperfect verifier is why the archive's verifier-free methods keep beating verifier-based ones. The constructive part matters as much: pairwise comparison needs no reward model, so the guarantee survives exactly where the archive has repeatedly found reward models to be miscalibrated.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), test-time scaling, provable scaling law, failure probability, [verification](../../../../wiki/concepts/verification.md), pass-k, aggregation, self-consistency, [reward hacking](../../../../wiki/concepts/reward-hacking.md)
- **Methods**: knockout tournament, league-style aggregation, [best-of-n](../../../../wiki/methods/best-of-n.md), [majority voting](../../../../wiki/methods/majority-voting.md), pairwise comparison, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md)
- **Datasets**: [GPQA](../../../../wiki/datasets/gpqa.md), [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [MATH-500](../../../../wiki/datasets/math-500.md)

Tags: `test-time compute`, `provable scaling law`, `knockout tournament`, `aggregation`, `theory`

## Abstract

We propose two simple, principled and practical algorithms that enjoy provable scaling laws for the test-time compute of large language models (LLMs). The first one is a two-stage knockout-style algorithm: given an input problem, it first generates multiple candidate solutions, and then aggregate them via a knockout tournament for the final output. Assuming that the LLM can generate a correct solution with non-zero probability and do better than a random guess in comparing a pair of correct and incorrect solutions, we prove theoretically that the failure probability of this algorithm decays to zero exponentially or by a power law (depending on the specific way of scaling) as its test-time compute grows. The second one is a two-stage league-style algorithm, where each candidate is evaluated by its average win rate against multiple opponents, rather than eliminated upon loss to a single opponent. Under analogous but more robust assumptions, we prove that its failure probability also decays to zero exponentially with more test-time compute. Both algorithms require a black-box LLM and nothing else (e.g., no verifier or reward model) for a minimalistic implementation, which makes them appealing for practical applications and easy to adapt for different tasks. Through extensive experiments with diverse models and datasets, we validate the proposed theories and demonstrate the outstanding scaling properties of both algorithms.

---

Record id: `local:e5ae26db2daac1d7`
