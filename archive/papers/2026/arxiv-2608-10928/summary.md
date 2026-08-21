<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling

- **Authors**: Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat, Soumyabrata Pal, Ramasuri Narayanam, Dinesh Manocha
- **Venue**: cs.AI
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10928>
- **PDF**: <https://arxiv.org/pdf/2608.10928v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

ThinkRetrieve augments each step of a reasoning model's chain of thought with a dynamically retrieved, fully worked solved example (rather than just facts), consistently beating standard sequential test-time scaling on math and QA benchmarks.

## Problem

Sequential test-time scaling (letting large reasoning models 'think longer' via self-reflection prompts) often yields diminishing or negative returns as traces grow, because longer traces exhibit increased uncertainty, error compounding, and drift from the original problem; self-reflection alone does not reliably catch or correct earlier errors.

## Contributions

- ThinkRetrieve: a framework that retrieves solved exemplars and injects them into the reasoning trace at each reasoning step, rather than once before generation
- Analysis showing in-trace exemplar injection lowers predictive entropy and length-normalised negative log-likelihood of the final answer compared to sequential test-time scaling
- Experiments on five reasoning models (1.5B-8B) across GSM-8K, MATH-500, AIME 2025 and SciQ, with two additional retrieval baselines (static input-level ICL, random per-step retrieval), showing consistent gains over every (model, benchmark) cell

## Method

ThinkRetrieve turns sequential test-time scaling into a retrieval-guided loop. At each step boundary (triggered when the model emits </think> or a fixed token interval is reached before the token budget B is exhausted), the model is prompted to produce an intermediate 'Final Answer' reflecting its current belief. This intermediate answer, jointly encoded with the original query via a sentence encoder (E5-Large) and indexed with FAISS, is used as a dense nearest-neighbour search query against an external corpus of (question, step-by-step solution) pairs (~309,609 examples from a decontaminated, quality-filtered synthetic split of NuminaMath-1.5). The single most similar exemplar is retrieved, formatted as an in-context example (question + full solution), and appended to the reasoning trace along with a continuation prompt instructing the model to use it; the model then resumes reasoning conditioned on this trajectory. This repeats at every step boundary until the token budget is exhausted, after which the model produces the final answer. Decontamination against evaluation benchmarks uses exact-match removal plus a cosine-similarity filter (>0.90 similarity to any eval instance) on QA-pair embeddings.

## Results

Table 1 (best accuracy across thinking budgets, 3-seed average): ThinkRetrieve beats sequential TTS on every (model, benchmark) cell across 5 models x 4 benchmarks. Largest gains on AIME 2025: up to +13.4 absolute points (Qwen3-1.7B: 22.2% TTS vs 35.6% ThinkRetrieve). On GSM-8K, DeepSeek-R1-1.5B: 82.7% (TTS) vs 87.3% (ThinkRetrieve). On MATH-500 gains are smaller (e.g. Qwen3-8B: 94.0% vs 94.8%). At compute-matched budget B=8K on a MATH-500 subset with Qwen3-1.7B, single-pass ThinkRetrieve (47%... reported as 0.47) beats TTS self-consistency majority voting at k=2,4,8 by 16-27 absolute accuracy points. Per-problem McNemar test on Qwen3-4B/MATH-500 shows ThinkRetrieve helps far more often than it hurts (p<10^-3 across budgets 2K-22K; peak p=5.9x10^-12 at B=12K, 26.5% problems helped vs 2.0% hurt), with gains concentrated on hardest (level-5) problems (+27.6pp net help) and near-neutral on already-saturated subjects (Algebra, Number Theory). Answer-leakage controls (excluding exemplars whose boxed answer matches the test gold answer) preserve or slightly improve accuracy, and zero of a sampled top-1 retrieved-exemplar audit shared the test problem's boxed answer, indicating gains are structural rather than answer-copying. Overhead: ThinkRetrieve produces fewer generated model tokens than sequential TTS at matched budget (12,913 vs 15,847) because injected exemplar tokens count against the budget, adding only ~6% wall-clock overhead.

## Limitations

Stated in Section 7: (1) retrieval quality depends on corpus coverage - for problems distributionally distant from the corpus, retrieved exemplars can be irrelevant or actively misleading and degrade performance below the no-retrieval baseline; a structurally analogous but load-bearing-different exemplar can anchor the model on a confident wrong answer because of the method's low-entropy property. (2) QA-QA contamination filtering (cosine similarity <=0.90) cannot exhaustively rule out latent structural similarities where two problems share an identical solution procedure despite different surface forms. (3) Additional per-step latency from retrieval calls and expanding context; wall-clock inference time is higher than sequential TTS even though token-budget-matched comparisons hold (Table 5, Appendix B). (4) The SciQ train/test splits (as released by the dataset authors) contain substantial paraphrase-level overlap that was not filtered in this work. (5) Every benchmark is paired with a domain-matched corpus (NuminaMath for math, SciQ's own training split for SciQ); whether the method remains beneficial where building a high-coverage exemplar corpus is harder (e.g. code generation, open-ended logical reasoning) is left to future work.

## Why it matters here

- **overthinking**: Directly targets the overthinking/diminishing-returns problem: the paper documents that sequential test-time scaling degrades or plateaus at higher thinking budgets (e.g. AIME 2025 with Qwen3-1.7B plateaus at 22% by B=8K and never improves further; DeepSeek-R1-1.5B accuracy on GSM-8K collapses from 83% to 52% as budget grows to 22K tokens), and proposes retrieval-augmented in-trace exemplars as a way to make additional inference-time compute keep paying off (monotonically non-decreasing accuracy with budget) instead of drifting into errors, directly addressing 'when/why models think more without benefit' and how to make longer thinking productive.

## Entities

- **Concepts**: [sequential test-time scaling](../../../../wiki/concepts/sequential-test-time-scaling.md), diminishing/negative returns from longer reasoning traces, [retrieval-augmented reasoning](../../../../wiki/concepts/retrieval-augmented-reasoning.md), in-context exemplar injection at each reasoning step, predictive entropy of final answers as a proxy for reasoning quality
- **Methods**: ThinkRetrieve, sequential test-time scaling (budget forcing, Muennighoff et al. 2025), static input-level ICL (S-ICL) baseline, random per-step retrieval (Rand) baseline, E5-Large dense retrieval with FAISS indexing, self-consistency / majority voting (compute-matched comparison)
- **Datasets**: GSM-8K, [MATH-500](../../../../wiki/datasets/math-500.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [SciQ](../../../../wiki/datasets/sciq.md), NuminaMath-1.5 (synthetic split, used as external example corpus)

Tags: `test-time-scaling`, `retrieval-augmented-reasoning`, `overthinking`, `in-context-learning`, `large-reasoning-models`, `chain-of-thought`

## Abstract

Large Reasoning Models (LRMs) improve performance by allocating additional inference-time compute to generate extended chain-of-thought reasoning. However, recent studies reveal that sequential test-time scaling often yields diminishing or even negative returns, as longer traces exhibit increased uncertainty, error compounding, and drift from the original problem. We propose ThinkRetrieve, a test-time scaling framework that augments the reasoning traces of LRMs with dynamically retrieved solved examples at each reasoning step. Given an external corpus of problems paired with step-by-step solutions, ThinkRetrieve retrieves relevant exemplars at each intermediate step and injects them directly into the thinking trace, providing the model with guidance on how to reason rather than merely what facts are relevant. Experiments across five reasoning models (1.5B--8B parameters) on GSM-8K, MATH-500, AIME 2025, and SciQ demonstrate that ThinkRetrieve consistently improves accuracy over standard test-time scaling, with relative gains of up to $60\%$ on AIME 2025.

---

Record id: `arxiv:2608.10928`
