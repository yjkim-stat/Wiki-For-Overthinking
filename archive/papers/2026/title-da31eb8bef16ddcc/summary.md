<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10011128>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

## Problem

Existing process reward models are trained to verify domain-specific knowledge, which limits how well test-time-scaling techniques such as weighted voting generalize beyond mathematical reasoning to other domains.

## Contributions

- A domain-agnostic process reward model (PRM) annotation and training framework based on contextual coherence between CoT steps rather than domain-specific knowledge checking
- Demonstrates test-time-scaling gains via weighted voting that generalize beyond mathematics to non-mathematical MMLU-Pro domains

## Method

ContextPRM is a process reward model trained with a new annotation and training scheme that scores the contextual coherence, i.e. the domain-agnostic logical flow, between successive chain-of-thought steps, instead of verifying domain-specific facts as prior PRMs do. At test time, ContextPRM scores are used to weight votes among multiple sampled reasoning chains (weighted voting), a form of test-time compute scaling.

## Results

6.5% average accuracy improvement over majority voting via weighted voting across nine non-mathematical MMLU-Pro domains; outperforms VersaPRM (2.2% improvement) and mathematics-focused PRMs (0.5% improvement); comparable performance is reported across both mathematical and non-mathematical domains.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Addresses the test-time-compute-scaling strand of the topic: a process reward model used to weight votes among sampled reasoning chains, generalized across domains (6.5% average accuracy gain over majority voting on nine non-mathematical MMLU-Pro domains, versus 2.2% for VersaPRM and 0.5% for math-focused PRMs). It targets the verification/selection side of scaling test-time compute, not reasoning length, stopping criteria, or the overthinking/underthinking tradeoff directly.

## Entities

- **Concepts**: contextual coherence between chain-of-thought steps, domain-agnostic process reward modeling, test-time scaling via verifier-weighted voting
- **Methods**: ContextPRM, process reward model, weighted voting
- **Datasets**: MMLU-Pro (nine non-mathematical domains, including law, history, philosophy)

Tags: `process-reward-model`, `test-time-scaling`, `best-of-n`, `weighted-voting`

---

Record id: `title:da31eb8bef16ddcc`
