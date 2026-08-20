<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Sample Complexity and Representation Ability of Test-time Scaling Paradigms

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10009511>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

A theoretical paper deriving sample-complexity bounds for self-consistency versus best-of-n, and an expressiveness result showing self-correction lets a Transformer simulate online learning over multiple tasks at test time.

## Problem

Test-time scaling paradigms (self-consistency, best-of-n, self-correction) have shown strong empirical results, but there is limited theoretical understanding of their sample efficiency and representational power.

## Contributions

- Proves a separation result: self-consistency requires Theta(1/Delta^2) samples to produce the correct answer, while best-of-n requires only Theta(1/Delta), where Delta is the probability gap between the correct and second most likely answer.
- Proves an expressiveness result showing self-correction with verifier feedback lets a Transformer simulate online learning over a pool of experts at test time, so a single Transformer can solve multiple tasks without prior knowledge of which task a query belongs to.
- Empirically validates the theoretical results, showing self-correction methods are practically effective.

## Method

The paper analyzes three test-time scaling paradigms theoretically. For repeated sampling, it derives sample-complexity bounds for self-consistency (majority voting over samples) versus best-of-n (selecting via a verifier/reward), showing best-of-n needs quadratically fewer samples in terms of the probability gap Delta. For self-correction, it shows that a Transformer receiving verifier feedback at test time can simulate an online-learning algorithm over a pool of experts, giving it the representational capacity to handle multiple tasks with a single fixed architecture.

## Results

States a separation result (self-consistency: Theta(1/Delta^2) samples; best-of-n: Theta(1/Delta) samples) and an expressiveness result for self-correction, plus an unspecified empirical validation of these results. No concrete benchmark accuracy numbers are given in the abstract.

## Limitations

Only the abstract was available for this task (no PDF attachment and no full text retrieved); no specific benchmarks, models, or numeric results beyond the sample-complexity exponents are stated. The empirical validation is described only as confirming the theory, with no numbers given.

## Why it matters here

- **overthinking**: Gives theoretical grounding for one branch of test-time compute scaling: it quantifies how many repeated samples different test-time strategies need to reach a correct answer (self-consistency vs. best-of-n), which bears on how much test-time compute is worth spending for a given accuracy gain. It does not address sequential reasoning length or when a model should stop generating within a single chain of thought, so it speaks to the parallel-sampling side of test-time scaling rather than to overthinking/underthinking of reasoning length directly.

## Entities

- **Concepts**: self-consistency, best-of-n sampling, self-correction with verifier feedback, sample complexity, Transformer expressiveness, online learning over a pool of experts
- **Methods**: [self-consistency](../../../../wiki/methods/self-consistency.md), [best-of-n](../../../../wiki/methods/best-of-n.md), self-correction with verifier feedback
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `sample-complexity`, `self-consistency`, `best-of-n`, `self-correction`, `theory`, `transformer-expressiveness`

## Abstract

Abstract Test-time scaling paradigms have significantly advanced the capabilities of large language models (LLMs) on complex tasks. Despite their empirical success, theoretical understanding of the sample efficiency of various test-time strategies---such as self-consistency, best-of-$n$, and self-correction---remains limited. In this work, we first establish a separation result between two repeated sampling strategies: self-consistency requires $\Theta(1/\Delta^2)$ samples to produce the correct answer, while best-of-$n$ only needs $\Theta(1/\Delta)$, where $\Delta < 1$ denotes the probability gap between the correct and second most likely answers. Next, we present an expressiveness result for the self-correction approach with verifier feedback: it enables Transformers to simulate online learning over a pool of experts at test time. Therefore, a single Transformer architecture can provably solve multiple tasks without prior knowledge of the specific task associated with a user query, extending the representation theory of Transformers from single-task to multi-task settings. Finally, we empirically validate our theoretical results, demonstrating the practical effectiveness of self-correction methods.

---

Record id: `title:27bc5c2aff7ebdab`
