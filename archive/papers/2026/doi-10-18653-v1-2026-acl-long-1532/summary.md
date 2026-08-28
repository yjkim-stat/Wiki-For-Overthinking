<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Scaling Test-Time Compute to Achieve IOI Gold Medal with Open-Weight Models

- **Authors**: Mehrzad Samadi, Aleksander Ficek, Sean Narenthiran, Siddhartha Jain, Wasi Uddin Ahmad, Somshubra Majumdar, Vahid Noroozi, Boris Ginsburg
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1532/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1532.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1532
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

GENCLUSTER is a scalable test-time-compute pipeline (parallel generation, behavioral clustering by execution output, LLM-tournament ranking, round-robin submission) that lets an open-weight model (gpt-oss-120b) achieve gold-medal-level performance at the International Olympiad in Informatics 2025 for the first time, by generating up to 5,000 candidate solutions per subtask.

## Problem

Proprietary systems (OpenAI's o1-ioi/o3, later systems) have claimed gold-medal performance at IOI and ICPC using undisclosed test-time-compute methods, but no open, reproducible pipeline had achieved comparable competitive-programming results with open-weight models, and prior large-scale test-time-compute systems (AlphaCode, AlphaCode 2) used proprietary models and did not address selecting strong representatives from a huge candidate pool under strict submission-count budgets.

## Contributions

- GENCLUSTER, a fully specified, reproducible test-time-compute pipeline (generation, behavioral clustering, tournament ranking, budget-aware submission) for competitive programming under strict submission constraints
- the first demonstration of IOI gold-medal-level performance using only open-weight models, narrowing (but not closing) the gap to undisclosed proprietary systems
- systematic scaling analyses showing score improves consistently with candidate-pool size and with maximum generation length, and ablations isolating the contribution of clustering, representative selection, and ranking
- an honest limitations analysis flagging the pipeline's own reliance on reasoning length as a correctness proxy as unreliable in some cases, alongside its high compute cost and synthetic-test blind spots

## Method

For each IOI subtask, GENCLUSTER (1) generates K candidate solutions in parallel (up to 5,000 per subtask), filtering out non-compiling code; (2) performs behavioral clustering by having the LLM generate randomized test-input generators and independent validators (keeping a test input only if >=75% of validators approve it), executing all candidate solutions on these tests, and grouping solutions with identical outputs into the same cluster (empty-output clusters removed); (3) ranks clusters via an LLM-judged partial round-robin tournament between cluster representatives (the solution in each cluster with the longest reasoning trace, used as a proxy for correctness likelihood), each cluster playing G_n=10 randomly-paired matches, ranked by number of tournament wins; (4) submits under the official IOI budget (max 50 submissions per problem) via a round-robin strategy that starts with the hardest (final) subtask of each problem, submits the top-ranked cluster's representative from each cluster in ranked order, skips a subtask's remaining clusters once it is solved, and moves to the next subtask.

## Results

Across 4 open-weight models (gpt-oss-120b, gpt-oss-20b, DeepSeek-R1-0528, Qwen3-235B-A22B-Thinking) on the IOI-2025 benchmark, gpt-oss-120b achieves the highest unconstrained Score@K by a significant margin (499.51 at K=5000, exceeding the gold threshold of 438.3) and is the only model whose score under the real 50-submission constraint reaches gold level: 446.75 (vs. silver 338.01, bronze 252), narrowing but not closing the gap to OpenAI's reported 533.29. Scores scale consistently with compute: submitted score rises from 332.27 (K=50) to 446.75 (K=5000), while the gap between constrained and unconstrained scores widens as K grows, showing selection among a larger candidate pool becomes harder even as the pool's ceiling improves. Ablations against six alternative selection strategies show the full GENCLUSTER pipeline (longest-trace representative + tournament-wins ranking) scores 446.75, beating GENCLUSTER (Score-Based) at 441.11, GENCLUSTER (Random-Rep) at 406.49, Cluster-Majority at 314.22, Random at 300.10, Cluster-Size at 299.87, and Longest-only (no clustering) at 277.36 -- clustering plus tournament ranking is necessary, not just the length heuristic alone. Increasing tournament rounds per cluster improves score but saturates after ~10 rounds; the correct solution is found within the top-50 ranked clusters in 35 of 39 subtasks. Different models scale differently with maximum generation-length token budget: gpt-oss models keep improving up to their 120K-token limit and eventually surpass DeepSeek-R1-0528/Qwen3-235B-A22B (which saturate around 48-64K tokens), despite the latter performing better at shorter reasoning lengths.

## Limitations

The full pipeline is extremely compute-intensive: generating 5,000 candidates per subtask consumes approximately 7.3 billion tokens, with the ranking tournament consuming another 7.3 billion tokens, making the approach impractical for real-time applications or low-resource settings. Behavioral clustering depends on model-generated synthetic tests and validators, which can have blind spots on rare corner cases, letting incorrect and correct solutions cluster together as problem complexity grows. The LLM-as-judge tournament ranking can be noisy and swayed by superficial features (code style, length, explanation quality) rather than actual correctness, despite randomizing match presentation order to reduce position bias, contributing to the gap between unconstrained and submission-constrained scores. Using reasoning-trace length to select cluster representatives and order within-cluster candidates is explicitly flagged as an unreliable heuristic in some cases: longer traces can also reflect confusion, verbosity, or unproductive exploration rather than higher correctness, potentially over-prioritizing verbose but incorrect solutions.

## Why it matters here

- **overthinking**: An important counterexample within the topic: rather than treating a long reasoning trace as waste to prune, GENCLUSTER pushes test-time compute to an extreme (up to 5,000 candidates and ~120K-token traces per subtask, ~14.6B tokens total per subtask across generation and ranking) and gets a real, gold-medal-level payoff on a genuinely hard task -- and it uses reasoning-trace length positively, as a within-cluster proxy for correctness, which the paper itself flags as an unreliable heuristic that can favor verbose-but-wrong solutions. Reading this against the archive's skeptical/efficiency-focused papers (e.g. that correct solutions are often shorter than incorrect ones, or that self-consistency degenerates without grounding) suggests the payoff from spending more test-time compute depends heavily on task difficulty and on the quality of the selection mechanism, not on trace length alone -- naive parallel exploration can fail for the same underlying reason naive self-revision does elsewhere in the archive, and it is the clustering/tournament selection machinery, not raw scale, that GENCLUSTER's own ablations show is doing the real work.

## Entities

- **Concepts**: behavioral clustering (by execution output), LLM-tournament ranking, round-robin submission strategy, reasoning length as a correctness proxy
- **Methods**: GENCLUSTER (parallel generation + behavioral clustering + tournament ranking + round-robin submission), behavioral clustering, LLM-as-judge pairwise tournament
- **Datasets**: IOI-2025 (new, subtask-level benchmark derived from IOI 2025 competition problems)

Tags: `test-time-scaling`, `competitive-programming`, `best-of-N`, `clustering`, `large-scale-generation`

## Abstract

Competitive programming has become a rigorous benchmark for evaluating the reasoning and problem-solving capabilities of large language models (LLMs). The International Olympiad in Informatics (IOI) stands out as one of the most prestigious annual competitions in competitive programming and has become a key benchmark for comparing human and AI-level programming ability. While several proprietary models have been claimed to achieve gold medal-level performance at the IOI, often with undisclosed methods, achieving comparable results with open-weight models remains a significant challenge. In this paper, we present GenCluster, a scalable and reproducible test-time compute framework that attains IOI gold-level performance using open-weight models. It combines large-scale generation, behavioral clustering, ranking, and a round-robin submission strategy to efficiently explore diverse solution spaces under limited validation budgets. Our experiments show that the performance of our proposed approach scales consistently with available compute, narrowing the gap between open and closed systems. Notably, we will show that GenCluster can achieve a gold medal at IOI 2025 for the first time with an open-weight model gpt-oss-120b, setting a new benchmark for transparent and reproducible evaluation of reasoning in LLMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1532`
