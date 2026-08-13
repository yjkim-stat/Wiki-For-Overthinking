<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning

- **Authors**: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, Dean F. Hougen
- **Venue**: cs.AI
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05643>
- **PDF**: <https://arxiv.org/pdf/2608.05643v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.62

## In one line

Spends test-time compute on iteratively refining each sampled rollout rather than on drawing more of them, then majority-votes the refined answers, with no verifier.

## Problem

Wider sampling at test time has diminishing returns because new rollouts tend to repeat existing answer patterns instead of adding reasoning diversity. Verifier-based selection is the alternative, but its performance depends on the calibration of an external reward model.

## Contributions

- A verifier-free breadth-depth test-time framework combining independent sampling with per-rollout iterative refinement
- Majority voting over refined rather than raw rollouts
- Comparisons against greedy decoding, majority voting, verifier-based best-of-N, beam search and lookahead decoding
- Results on AIME24, AIME25, AMC, OlympiadBench and MATH500

## Method

A verifier-free breadth-depth framework. Breadth: sample multiple independent reasoning rollouts, preserving diverse initial attempts. Depth: refine each rollout through iterative self-critique and self-correction, repairing local reasoning errors. Then aggregate the refined answers by majority voting. The design uses compute for both exploration and improvement, and needs no external reward model to be calibrated.

## Results

Across AIME24, AIME25, AMC, OlympiadBench and MATH500, it improves over greedy decoding, majority voting, verifier-based best-of-N, beam search and lookahead decoding on multiple open-weight models. With Qwen2.5-1.5B, accuracy reaches 58.0% on MATH500, above the strongest verifier-based baseline, and rises from 25.0% to 32.5% on AMC.

## Limitations

The reported gains are concentrated on small open-weight models, and the headline example is a 1.5B model; whether refinement still beats resampling when the base model is strong enough to have little to repair is not established here. Compute is not obviously matched — refining each of N rollouts costs more than generating N, so a compute-matched comparison against a larger N is the control the abstract does not report. It also depends on self-critique being informative, which arxiv:2608.04355 argues is largely a format effect at small-to-mid scale.

## Why it matters here

- **test-time-scaling**: A direct claim on this topic's central question — what to buy with extra inference compute. It argues depth beats breadth and that neither needs a verifier, which cuts against the best-of-N and process-reward-selection line the archive tracks. The result sits in tension with arxiv:2608.04355 in this same batch, which finds that at small-to-mid scale the content margin of self-revision is near zero and the measured gain is format repair; this paper's strongest numbers come from a 1.5B model on parseable-answer math benchmarks, exactly the regime that argument targets. The two should be read together, and the missing control is compute-matched breadth.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), test-time scaling, [self-correction](../../../../wiki/concepts/self-correction.md), [answer stabilization](../../../../wiki/concepts/answer-stabilization.md), reasoning diversity, diminishing returns, verifier-free selection
- **Methods**: [majority voting](../../../../wiki/methods/majority-voting.md), [self-consistency](../../../../wiki/methods/self-consistency.md), [best-of-n](../../../../wiki/methods/best-of-n.md), [beam search](../../../../wiki/methods/beam-search.md), lookahead decoding, iterative self-critique, [greedy decoding](../../../../wiki/methods/greedy-decoding.md)
- **Datasets**: [AIME24](../../../../wiki/datasets/aime-2024.md), [AIME25](../../../../wiki/datasets/aime-2025.md), [AMC](../../../../wiki/datasets/amc.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [MATH500](../../../../wiki/datasets/math500.md)

Tags: `test-time scaling`, `self-correction`, `majority voting`, `verifier-free`, `math reasoning`

## Abstract

Test-time scaling improves LLM reasoning by using additional inference compute, but wider sampling alone can suffer from diminishing returns: new rollouts often repeat existing answer patterns instead of adding useful reasoning diversity. Verifier-based selection offers an alternative, but its performance depends on the calibration of an external reward model. We propose a verifier-free breadth--depth refinement framework that uses test-time compute to both explore and improve candidate solutions. The method samples multiple independent reasoning rollouts, refines each rollout through iterative self-critique and self-correction, and aggregates the refined answers by majority voting. Breadth preserves diverse initial attempts, while depth repairs local reasoning errors before aggregation. Across AIME24, AIME25, AMC, OlympiadBench, and MATH500, our method consistently improves over greedy decoding, majority voting, verifier-based best-of-$N$, beam search, and lookahead decoding across multiple open-weight models. For instance, with Qwen2.5-1.5B, accuracy increases from the strongest verifier-based baseline to $58.0\%$ on MATH500, and from $25.0\%$ to $32.5\%$ on AMC. These results show that test-time compute can be more effective when used to refine sampled trajectories rather than only to sample more candidates or rely on verifier-guided selection.

---

Record id: `arxiv:2608.05643`
