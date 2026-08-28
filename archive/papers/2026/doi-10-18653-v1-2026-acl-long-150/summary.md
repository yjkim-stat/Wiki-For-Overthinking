<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics

- **Authors**: Jinu Lee, Kyoung-Woon On, Sophia Simeng Han, Arman Cohan, Julia Hockenmaier
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.150/>
- **PDF**: <https://aclanthology.org/2026.acl-long.150.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.150
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

LEGIT is a 24K-instance Korean legal-judgment-prediction benchmark that converts real court judgments into hierarchical legal issue trees, using them as fine-grained rubrics (issue coverage and issue correctness, alongside final-order correctness) to evaluate LLM reasoning traces with human-lawyer-level reliability, and shows retrieval-augmented generation and RL-with-rubrics have complementary effects on legal reasoning quality.

## Problem

Evaluating LLM-generated reasoning traces in expert domains like law requires domain expertise current automatic evaluators lack, and existing legal-judgment-prediction benchmarks only score final-order accuracy while ignoring whether the reasoning trace actually and correctly covers the legal issues a case turns on -- so two reasoning traces predicting the same correct outcome cannot be distinguished on reasoning quality.

## Contributions

- LEGIT, a 24K-instance Korean legal-judgment-prediction dataset with hierarchical legal-issue-tree rubrics extracted automatically from real court judgments
- empirical validation that LEGIT rubrics achieve human-lawyer-level (alpha=0.87) inter-rater reliability and substantially higher LLM-judge consistency than a coarse Likert-scale baseline
- a taxonomy of decomposition and deduction errors in legal reasoning traces, with a quantitative analysis of how these errors propagate up the issue hierarchy and degrade parent-issue correctness
- an empirical demonstration that retrieval-augmented generation and rubric-based RL have complementary effects on legal reasoning quality (RAG broadens coverage, RL sharpens correctness at coverage's expense)

## Method

Constructs legal issue trees from 24,406 Korean court judgments (civil/administrative law, filtered to cases with legally deterministic outcomes) by extracting atomic facts and issue structure via a two-pass LLM pipeline (Gemini-2.0-Flash, with human-inspected 300-example test split), representing each case as a hierarchical tree of opposing arguments and conclusions rooted at the purpose of claim. Converts each non-root issue node into an LLM-as-judge rubric item assessing issue coverage (was the issue addressed) and issue correctness (was the conclusion about it correct), combined with final-order correctness into a 10-point LEGIT score (5 for final order, 2 for coverage, 3 for correctness). Validates rubric reliability via Krippendorff's alpha inter-rater agreement between two independent groups of licensed Korean lawyers and between lawyers and 10 LLM judges, and compares against a coarser Likert-scale (0-10) baseline rubric. Evaluates 12 frontier/open-weight LLMs as reasoning-trace generators, characterizes two error types (decomposition error: failing to identify relevant sub-issues; deduction error: failing to reason correctly about facts), and tests retrieval-augmented generation (BM25/Contriever citation retrieval) and GRPO-based reinforcement learning with LEGIT-score rewards (on Gemma-3-4B) as ways to improve legal reasoning.

## Results

Lawyer-lawyer inter-rater agreement on LEGIT scores is very high (Krippendorff's alpha=0.87, above the recommended 0.67 threshold), confirming the rubrics are objective and reliable. Closed-source LLM judges (GPT-4.1, GPT-4.1-mini, Gemini-2.5-Pro/Flash, Gemini-2.0-Flash) achieve alpha=0.62-0.74 agreement with lawyers, while smaller open-weight judges perform worse (Gemma-3-12B alpha=0.53, Gemma-3-4B alpha=0.20), and LLM judges systematically overestimate both issue coverage and correctness relative to lawyers' stricter standards. LEGIT-style modular rubrics show substantially higher LLM-LLM pairwise agreement than a coarse Likert-scale baseline evaluating the whole trace at once. No generator LLM saturates the task: the best (GPT-4.1) reaches only 5.71/10 average LEGIT score; error-propagation analysis shows failing to cover a child issue drops parent-issue correctness from ~0.9 (all children correct) to ~0.3-0.6 (no children covered), i.e. decomposition/deduction errors compound up the issue hierarchy. Retrieval-augmented generation (prepending BM25- or Contriever-retrieved citations) improves all three LEGIT score components by roughly +0.4 points on average for Gemma-3-4B. GRPO-based RL trained directly on the LEGIT score significantly increases final-order correctness and issue correctness but reduces issue coverage, because the reward more heavily penalizes incorrect reasoning than omitted issues, causing the policy to favor only covering issues it is confident about -- making RAG and RL complementary (RAG broadens coverage/exploration, RL sharpens correctness).

## Limitations

LEGIT is limited to the Korean legal system and language; the authors believe the approach generalizes to other jurisdictions and languages but leave this as future work. The benchmark deliberately does not evaluate citation accuracy (whether a cited legal source actually exists and is relevant) because Korean court judgments are not freely disclosed to the public, making verification infeasible at the time of writing, despite documented cases of ambiguous or overloaded case-law citations in the dataset. Rubric-based LLM-as-judge evaluation requires substantially more compute than Likert-scale or final-order-only evaluation, a deliberate computation-for-reliability tradeoff the paper accepts rather than resolves.

## Why it matters here

- **overthinking**: Not relevant to the topic: this is a benchmark and evaluation methodology for the *correctness and completeness* of legal reasoning traces, with no engagement with reasoning length, token cost, or the accuracy/efficiency tradeoff. It appears to have matched the topic's collection keywords only via generic terms like 'reasoning trace' or 'large reasoning model.'

## Entities

- **Concepts**: legal issue tree, issue coverage vs. issue correctness, decomposition error vs. deduction error, rubric-based LLM-as-judge
- **Methods**: LLM-as-judge with structured rubrics, retrieval-augmented generation (BM25, Contriever), GRPO-based reinforcement learning with rubric rewards
- **Datasets**: LEGIT (new, 24,406 Korean court judgments)

Tags: `legal-reasoning`, `reasoning-trace-evaluation`, `llm-as-judge`, `benchmark`, `retrieval-augmented-generation`

## Abstract

Evaluating the quality of LLM-generated reasoning traces in expert domains (e.g., law) is essential for ensuring credibility and explainability, yet remains challenging due to the inherent complexity of such reasoning tasks. We introduce LEGIT (LEGal Issue Trees), a novel large-scale (24K instances) expert-level legal reasoning dataset with an emphasis on reasoning trace evaluation. We convert court judgments into hierarchical trees of opposing parties’ arguments and the court’s conclusions, which serve as rubrics for evaluating the issue coverage and correctness of the reasoning traces. We verify the reliability of these rubrics via human expert annotations and comparison with coarse, less informative rubrics. Using the LEGIT dataset, we show that (1) LLMs’ legal reasoning ability is seriously affected by both legal issue coverage and correctness, and that (2) retrieval-augmented generation (RAG) and RL with rubrics bring complementary benefits for legal reasoning abilities, where RAG improves overall reasoning capability, whereas RL improves correctness albeit with reduced coverage.

---

Record id: `doi:10.18653/v1/2026.acl-long.150`
