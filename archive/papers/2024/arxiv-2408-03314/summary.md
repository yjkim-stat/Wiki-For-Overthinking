<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

- **Authors**: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- **Venue**: cs.LG
- **Published**: 2024-08-06
- **Source**: seed
- **Link**: <https://arxiv.org/abs/2408.03314>
- **PDF**: <https://arxiv.org/pdf/2408.03314v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.62

## In one line

Studies how far a fixed model improves when given more inference compute, and shows that allocating that compute adaptively per prompt by difficulty beats a uniform best-of-N budget by more than 4x.

## Problem

Whether and how much extra inference compute helps a fixed model was largely unanswered, with prior work reporting mostly negative results for individual strategies. The question matters beyond inference, since it sets the trade-off between spending compute at pretraining and spending it at test time.

## Contributions

- An analysis of two distinct mechanisms for scaling test-time computation: search against dense, process-based verifier reward models, and adaptively updating the model's distribution over a response given the prompt.
- The finding that which mechanism works depends critically on prompt difficulty, which is why single-strategy studies produce mixed results.
- A 'compute-optimal' strategy that allocates test-time compute adaptively per prompt.
- A FLOPs-matched comparison against pretraining a larger model.

## Method

Two families are compared. The first searches against a process-based verifier reward model that scores intermediate steps densely. The second revises the model's own distribution over a response at test time given the prompt. Both are evaluated across prompt difficulty levels, and the compute-optimal strategy selects the allocation per prompt on that basis. The abstract does not state the model, benchmark or difficulty estimator.

## Results

The compute-optimal strategy improves the efficiency of test-time compute scaling by more than 4x compared with a best-of-N baseline. In a FLOPs-matched evaluation, on problems where a smaller base model already attains somewhat non-trivial success rates, test-time compute lets it outperform a 14x larger model. The abstract gives no benchmark-level accuracies. Summarized from the abstract alone, so the figures below are only those the abstract states; the paper's full evaluation is not represented here.

## Limitations

Not discussed in the abstract, though one boundary is stated inside the headline result and is easy to miss: the 14x claim holds on problems where the smaller model already has non-trivial success rates. Test-time compute is shown to amplify existing competence, not to supply competence the base model lacks, which bounds how far this topic's central strategy can go.

## Why it matters here

- **test-time-scaling**: The paper that named this topic's central question and gave it a unit of measurement. Two results are load-bearing. First, difficulty-conditioned allocation: the right way to spend inference compute depends on the prompt, so a single fixed strategy is leaving most of the gain unclaimed and the mixed prior results were an artefact of not conditioning. Every archived method that scores or filters trajectories is implicitly doing a version of this, and none of them condition on difficulty explicitly — an open gap this paper identifies but the archive has not closed. Second, the FLOPs-matched comparison makes the pretraining-versus-inference trade-off concrete, which is the framing that turned test-time scaling from a decoding trick into a compute-allocation question. The stated caveat, that the advantage holds where the smaller model already has non-trivial success, is the honest boundary and should travel with the claim.

## Entities

- **Concepts**: [test-time compute](../../../../wiki/concepts/test-time-compute.md), compute-optimal scaling, [prompt difficulty](../../../../wiki/concepts/prompt-difficulty.md), process reward model, best-of-n, pretraining vs inference trade-off, FLOPs-matched comparison
- **Methods**: verifier-guided search, adaptive distribution update, [best-of-N](../../../../wiki/methods/best-of-n.md), process-based verifier reward model
- **Datasets**: _none recorded_

Tags: `test-time scaling`, `inference compute`, `compute-optimal`, `verifier`, `scaling`

## Abstract

Enabling LLMs to improve their outputs by using more test-time computation is a critical step towards building generally self-improving agents that can operate on open-ended natural language. In this paper, we study the scaling of inference-time computation in LLMs, with a focus on answering the question: if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt? Answering this question has implications not only on the achievable performance of LLMs, but also on the future of LLM pretraining and how one should tradeoff inference-time and pre-training compute. Despite its importance, little research attempted to understand the scaling behaviors of various test-time inference methods. Moreover, current work largely provides negative results for a number of these strategies. In this work, we analyze two primary mechanisms to scale test-time computation: (1) searching against dense, process-based verifier reward models; and (2) updating the model's distribution over a response adaptively, given the prompt at test time. We find that in both cases, the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt. This observation motivates applying a "compute-optimal" scaling strategy, which acts to most effectively allocate test-time compute adaptively per prompt. Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.

---

Record id: `arxiv:2408.03314`
