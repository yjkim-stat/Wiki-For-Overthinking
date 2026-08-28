<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS

- **Authors**: Shijia Xu, Zhou Wu, Xiaolong Jia, Yu Wang, Kai Liu, April Xiaowen Dong
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1052/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1052.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1052
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Self-Correcting RAG reformulates retrieval-augmented generation as constrained optimization: a Multi-dimensional Multiple-choice Knapsack Problem (MMKP) selects a diverse, non-redundant, token-budget-respecting document context (replacing greedy top-k), and an NLI-guided Monte Carlo Tree Search explores reasoning trajectories at inference time, penalizing branches whose generated claims contradict retrieved evidence -- improving average EM/F1 (37.1/45.8) and retrieval recall@5 (72.0%) over strong RAG baselines across six QA datasets while cutting the contradiction rate to 0.04.

## Problem

Retrieval-augmented generation still suffers from low context utilization (greedy top-k retrieval selects redundant, overlapping documents rather than diverse, complementary evidence) and frequent hallucination (generated claims that contradict or are unsupported by the retrieved context), and standard LLM decoding lacks the lookahead needed to guarantee faithful, well-supported reasoning trajectories.

## Contributions

- an MMKP-based context selector that formalizes RAG document selection as constrained combinatorial optimization (maximizing information density and diversity under a token budget) rather than greedy top-k ranking
- an NLI-guided MCTS generator that uses entailment/contradiction scoring against retrieved evidence as an MCTS reward to prune hallucinated reasoning branches at inference time
- state-of-the-art average EM/F1 and retrieval recall across six diverse QA benchmarks (simple, multi-hop, multi-doc), with the largest gains on complex multi-hop and noisy-context settings
- ablations isolating and quantifying the individual and combined contributions of the retrieval-optimization and generation-faithfulness components

## Method

Phase I (context selection): retrieved document chunks are grouped via semantic clustering (cosine similarity above a threshold) into mutually-near-duplicate groups; context selection is then formalized as a Multi-dimensional Multiple-choice Knapsack Problem (MMKP) -- selecting at most one representative document per semantic group to maximize a fused relevance/diversity utility subject to a token budget and a redundancy-cost constraint, solved via a dynamic-programming approach with Pareto pruning (with a proven FPTAS for the single-dimensional case). Phase II (inference-time reasoning): frames generation as a Markov Decision Process over (query, selected context, partial answer) states, where at each step the policy (the LLM) either generates a continuation or triggers an augmentative retrieval call when uncertain, solved via Monte Carlo Tree Search whose reward function uses a Natural Language Inference model (RoBERTa-large-mnli) to score entailment/neutrality/contradiction between each generated answer sentence and the retrieved evidence snippets, with a severe penalty weight on contradiction to prune hallucinated branches during search. Backbone generator is Qwen2.5-7B-Instruct; retrieval combines BGE-small-en-v1.5 dense and BM25 sparse retrieval via Reciprocal Rank Fusion. Evaluated on six datasets across three task types: Simple QA (NQ, PopQA), Multi-Hop QA (MuSiQue, 2WikiMultiHopQA, HotpotQA), and Multi-Doc QA (MultiHop-RAG, testing robustness to noisy/irrelevant distractor documents).

## Results

Self-Correcting RAG achieves the highest average performance among all evaluated methods (EM 37.1, F1 45.8), beating standard RAG baselines (Naive, HyDE, RRR), advanced selection/reranking baselines (RAG+MMR, Filco, RECOMP, LongLLMLingua), and iterative/agentic RAG baselines (IRCoT, Self-RAG, CRAG, DRAG). Gains are most pronounced on complex multi-hop reasoning: on MuSiQue it beats the prior best (CRAG, EM 18.2) by 4.5 absolute EM points (22.7); on the noise-robustness-focused MultiHop-RAG dataset it reaches EM 35.3 versus RAG+MMR's 32.1 and Filco's 29.8. Retrieval quality (Recall@5) reaches an average 72.0% across all six datasets, the highest of any compared method (versus RAG+MMR's 63.3%, an 8.7-point absolute improvement), and 93.6% on HotpotQA specifically, exceeding the strongest competitor CRAG's 91.5%. Ablations isolate each component's contribution: replacing standard top-k retrieval with MMKP-only context selection improves Recall@5 from 49.6% to 71.8% (confirming the diversity/redundancy-aware formulation is the main driver of retrieval gains) but leaves faithfulness metrics comparable to baseline (Attribution Precision 0.58), showing better retrieval alone does not prevent hallucination; adding NLI-guided MCTS alone substantially improves faithfulness (Contradiction Rate down to 0.06, Support up to 0.84) with more modest retrieval-quality gains; the full combined framework achieves the best results on both axes simultaneously (AP 0.85, CR 0.04, Sup 0.88). A fine-grained ablation of the MMKP's three redundancy mechanisms (hard grouping constraint, diversity utility reward, cost redundancy penalty) shows each contributes incrementally: hard constraint alone raises average Recall@5 from 49.6% to 64.2%; adding the diversity reward raises it to 67.8%; adding the cost penalty raises it to 69.5%; and the full combination reaches 72.0% -- with a specific finding that the hard grouping constraint (exactly one document per semantic cluster) raises HotpotQA's Complementary Evidence Recall to 93.6% versus 86.2% for a softer 'max 2 per group' constraint, showing strict deduplication specifically helps preserve the complementary document pairs multi-hop reasoning needs.

## Limitations

Solving the MMKP exactly is computationally prohibitive (O(m*2^|G_max|)), so the paper relies on an approximate dynamic-programming solver with Pareto pruning for the practical (2-dimensional) case, meaning solution optimality is not guaranteed in general; a fixed similarity threshold for semantic grouping can, in edge cases where a query retrieves an abnormally dense pool of highly similar documents, collapse too many candidates into too few groups (acknowledged as requiring adaptive thresholding, discussed as a system-mechanics consideration in the paper's discussion section).

## Why it matters here

- **overthinking**: Not directly about overthinking: this targets RAG context selection and answer faithfulness (hallucination reduction), not reasoning-trace length or the accuracy/efficiency tradeoff of a single reasoning model's thinking process. It is tangentially related only through its use of test-time compute (MCTS-guided exploration of reasoning trajectories) as a mechanism to trade inference compute for output quality, a pattern shared with test-time-scaling methods elsewhere in this archive, but applied to grounding generated claims in retrieved evidence rather than to controlling reasoning length.

## Entities

- **Concepts**: Multi-dimensional Multiple-choice Knapsack Problem (MMKP) for context selection, NLI-guided Monte Carlo Tree Search, faithfulness metrics (Attribution Precision, Contradiction Rate, Support), test-time compute for RAG, semantic redundancy grouping
- **Methods**: Self-Correcting RAG (MMKP context selection + NLI-guided MCTS), Naive RAG (baseline), HyDE (baseline), RRR (baseline), RAG+MMR / Filco / RECOMP / LongLLMLingua (selection/reranking baselines), IRCoT / Self-RAG / CRAG / DRAG (iterative/agentic baselines)
- **Datasets**: [Natural Questions (NQ)](../../../../wiki/datasets/natural-questions-nq.md), PopQA, [MuSiQue](../../../../wiki/datasets/musique.md), [2WikiMultiHopQA](../../../../wiki/datasets/2wikimultihopqa.md), HotpotQA (distractor setting), MultiHop-RAG

Tags: `retrieval-augmented-generation`, `hallucination`, `monte-carlo-tree-search`, `test-time-compute`, `combinatorial-optimization`

## Abstract

Retrieval-augmented generation (RAG) substantially extends the knowledge boundary of large language models. However, it still faces two major challenges when handling complex reasoning tasks: low context utilization and frequent hallucinations. To address these issues, we propose Self-Correcting RAG, a unified framework that reformulates retrieval and generation as constrained optimization and path planning. On the input side, we move beyond traditional greedy retrieval and, for the first time, formalize context selection as a multi-dimensional multiple-choice knapsack problem (MMKP), thereby maximizing information density and removing redundancy under a strict token budget. On the output side, we introduce a natural language inference (NLI)-guided Monte Carlo Tree Search (MCTS) mechanism, which leverages test-time compute to dynamically explore reasoning trajectories and validate the faithfulness of generated answers. Experiments on six open-domain and multi-hop QA datasets demonstrate that our method significantly improves reasoning accuracy on complex queries while effectively reducing hallucinations, outperforming strong existing baselines. Our code is available at https://github.com/xjiacs/Self-Correcting-RAG .

---

Record id: `doi:10.18653/v1/2026.findings-acl.1052`
