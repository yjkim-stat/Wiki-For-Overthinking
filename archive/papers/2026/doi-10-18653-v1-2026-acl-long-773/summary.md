<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking

- **Authors**: Xinliang Frederick Zhang, Anhad Mohananey, Alexandra Chronopoulou, Pinelopi Papalampidi, Somit Gupta, Tsendsuren Munkhdalai, Lu Wang, Shyam Upadhyay
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.773/>
- **PDF**: <https://aclanthology.org/2026.acl-long.773.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.773
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.

## Problem

Existing overthinking analyses are confined to superficial, length-based profiling (e.g. token-distance to the first correct answer) that never examines the internal structure or evolution of a model's thought process, leaving the underlying causes of overthinking -- and a principled, non-length-based way to detect it -- unknown; prior work is also largely confined to STEM/math domains and complex queries, leaving simple queries across diverse domains underexplored.

## Contributions

- the first large-scale benchmark of LLM overthinking on simple queries across both horizontal (6 domains) and vertical (systematically varied difficulty) axes, spanning 14 thinking models from 0.6B to 235B parameters
- TRACE, a four-stage analyzer that decomposes reasoning traces into labeled sub-thoughts and constructs thought-progression graphs, validated at 93% agreement with human labeling
- identification of two generalizable thought-progression patterns (Explorer, Late Landing) that manifest overthinking differently (over-exploration vs. over-verification) and are properties of models rather than individual prompts
- a utility-based, structure-grounded redefinition of overthinking as continuation of thought past the point where marginal return drops below a threshold, replacing purely length-based definitions and generalizing them as a special case
- two ground-truth-free inference-time heuristics (self-looping, backtrack-detection) derived from the identified patterns that manage overthinking in practice, with model-specific tuning recovering most accuracy at substantially reduced cost

## Method

First runs a horizontal analysis (6 domains: SQuAD 2.0, NIAH, SimpleQA, ASDiv, date arithmetic, Zebra Logic grid puzzles) and vertical analysis (systematically increasing difficulty within math and temporal reasoning) across 14 thinking LLMs (Qwen3 0.6B-235B, DeepSeek-R1-distilled models) comparing thinking vs. non-thinking mode with greedy decoding, to benchmark overthinking magnitude. It then introduces TRACE (Thought-process Reconstruction and Automated Clustering Engine), a four-stage analyzer: (1) Response Sampling from 4 large thinking models (Qwen3-30B-A3B, Qwen3-32B, R1-Distill-Llama-70B, Qwen3-235B-A22B); (2) Thought Decomposition & Label Inference, using gemini-2.5-pro to segment each trace into self-contained, complete, answer-bearing 'sub-thoughts' and label the discourse relationship between consecutive sub-thoughts (Initial, Final, Verification, Correction, Backtrack, Branching Out, Sidetrack) -- validated at 93% agreement against 200 human-labeled sub-thoughts; (3) Progression Graph Construction, representing each trace as a directed graph with distinct proposed answers as nodes, projected onto a 2D coordinate system encoding search depth (branching) and progression; (4) Thought Pattern Induction, clustering progression graphs across topically-similar queries (grouped by query type/difficulty, not identical prompts) via group-based aggregation, thresholded pruning, and ground-truth linkage to surface dominant, generalizable reasoning patterns. Utility tracing then measures both correctness (does this sub-thought contain the right answer) and helpfulness (does it lead to a correct final answer) as a function of sub-thought index, to find each pattern's point of diminishing returns.

## Results

Horizontal analysis: thinking models spend 5-20x more inference cost than non-thinking mode on simple queries with little-to-no accuracy improvement; the performance gap between thinking/non-thinking modes vanishes once model scale exceeds ~4-8B parameters, and for knowledge-recall tasks (minimal reasoning workload) thinking provides negligible benefit regardless of difficulty. Vertical analysis on Qwen3-235B-A22B: on math (ASDiv-1 through GSM8K), thinking's accuracy edge over non-thinking grows from negligible at ASDiv-1/2 to +15 points at GSM8K, but GSM8K requires >10x more thought tokens for that gain, so 80% of the extra compute produces no measurable benefit even where thinking does help; on temporal reasoning, thinking helps up to ~50% accuracy improvement through L1-L2 but then saturates and effectively collapses beyond L3 (where day-level counting over centuries and leap-year/calendar handling exceed the model's representational capacity), so additional reasoning becomes 'pure overthinking' that cannot bridge the capability gap. TRACE's structural analysis reveals two dominant thought-progression patterns among cases with >=3 distinct intermediate answers: Explorer (correctness probability spread across nearly all proposed answers, frequent branching/backtracking, exhibited by the largest model Qwen3-235B-A22B) and Late Landing (a convergent, sequential-correction trajectory where correctness concentrates at the final node, exhibited by most open-weight models including R1-Distill-Llama-70B, Qwen3-30B-A3B, Qwen3-32B). Utility tracing shows Explorer's performance is volatile and peaks early (further reasoning yields diminishing/negative returns from over-exploration), while Late Landing rises steadily to a plateau, with overthinking manifesting as redundant post-plateau steps, predominantly excessive self-verification (over-verification). Applying the structure-based convergence-point definition to a Temporal-L3 case study: for Qwen3-235B-A22B (Explorer-type), a self-looping-plus-backtrack heuristic preserves accuracy (63.44%, above the 52.87% standard-thinking baseline) while cutting length to 1,100 words (~60% efficiency saving vs. 2,722 words); for Qwen3-32B (Late Landing-type), k=3 self-looping slightly encourages verification, raising accuracy to 80.18% (vs. 83.84% standard thinking, only 3 points lower) while cutting inference cost 40% (4,000->2,463 words) -- demonstrating the redefinition detects a convergence point beyond which added thinking measurably hurts or does not help, and can drive practical, ground-truth-free inference-time management heuristics.

## Limitations

The largest evaluated model (235B parameters) is substantially more time- and resource-intensive to run than smaller prior-generation models, incurring a significantly higher carbon footprint, and required 8 NVIDIA H100s with evaluation time up to 1 day per configuration. The study covers six evaluation domains chosen to span diverse task/input-output mappings but does not claim exhaustive domain coverage; 4 samples were excluded from one analysis due to gemini-2.5-pro parsing errors, causing minor discrepancies between tables.

## Why it matters here

- **overthinking**: Directly and centrally relevant -- this is a foundational structural study of overthinking itself, not a mitigation applied on top of an assumed definition. It empirically pins down where thinking helps (a narrow middle ground bounded below by trivial-task waste and above by tasks that exceed a model's representational capacity), gives a mechanistic, non-length-based account of overthinking via two distinct thought-progression patterns (Explorer's over-exploration vs. Late Landing's over-verification), and proposes a utility-based convergence-point definition of overthinking that several length-penalty or budget-based methods elsewhere in this archive implicitly approximate without stating explicitly.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), sub-thought decomposition, thought progression graph, Explorer pattern, Late Landing pattern, over-verification, over-exploration, convergence point, utility-based (structure-based) overthinking definition
- **Methods**: TRACE (Thought-process Reconstruction and Automated Clustering Engine), LLM-as-rater sub-thought labeling (gemini-2.5-pro), self-looping heuristic, backtrack-detection heuristic, greedy decoding
- **Datasets**: SQuAD 2.0, NIAH (Needle in a Haystack), SimpleQA, ASDiv, [GSM8K](../../../../wiki/datasets/gsm8k.md), date arithmetic (extended from Tan et al.), Zebra Logic (grid puzzles)

Tags: `overthinking`, `thought-structure-analysis`, `mechanistic-interpretability`, `over-verification`, `over-exploration`, `evaluation-methodology`

## Abstract

Models employing long chain-of-thought (CoT) reasoning have shown superior performance on complex reasoning tasks. Yet, this capability introduces a critical and often overlooked inefficiency—overthinking—models often engage in unnecessarily extensive reasoning even for simple queries, incurring significant computations without accuracy improvements. While prior work has explored solutions to mitigate overthinking, a fundamental gap remains in our understanding of its underlying causes. Most existing analyses are limited to superficial, profiling-based observations, failing to delve into LLMs’ inner workings. This study introduces a systematic, fine-grained analyzer of LLMs’ thought process to bridge the gap, TRACE. We first benchmark the overthinking issue, confirming that long-thinking models are five to twenty times slower on simple tasks with no substantial gains. We then use TRACE to first decompose the thought process into minimally complete sub-thoughts. Next, by inferring discourse relationships among sub-thoughts, we construct granular thought progression graphs and subsequently identify common thinking patterns for topically similar queries. Our analysis reveals two major patterns for open-weight thinking models—Explorer and Late Landing. This finding provides evidence that over-verification and over-exploration are the primary drivers of overthinking in LLMs. Grounded in thought structures, we propose a utility-based definition of overthinking, which moves beyond length-based metrics. This revised definition offers a more insightful understanding of LLMs’ thought progression, as well as practical guidelines for principled overthinking management.

---

Record id: `doi:10.18653/v1/2026.acl-long.773`
