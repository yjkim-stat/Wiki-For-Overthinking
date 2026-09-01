<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation

- **Authors**: Pratyay Banerjee, Ankit Chadha
- **Venue**: cs.CL
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.25277>
- **PDF**: <https://arxiv.org/pdf/2608.25277v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Routed Graph Handoff (RGH) uses a lightweight LLM router to pick, per delegation, between a typed dependency-graph message and natural-language prose for multi-agent LLM handoffs, matching or beating NL-only on every one of four benchmarks while cutting token cost 2-3x.

## Problem

Multi-agent LLM systems coordinate via natural-language messages that consume 40-60% of total token budget; replacing NL with structured graphs cuts cost but regresses badly on tasks requiring adaptive reasoning, and no prior work treats handoff format itself as a first-class, per-task design decision.

## Contributions

- a typed graph schema for multi-agent handoffs that compresses delegations 2-3x while improving task success on dependency-chain benchmarks
- empirical identification of a structure-flexibility tradeoff across four benchmarks: neither graph nor NL format dominates, and a graph-aware executor prompt is necessary for the schema to help
- a near-zero-cost LLM router achieving Pareto improvement on quality and cost, with oracle analysis quantifying 8.6pp of headroom achievable only through execution-time adaptive routing

## Method

Designs a typed DAG schema (8 node types, 7 edge relations) for delegations, emitted via constrained decoding at ~350 tokens vs. NL's ~730-770. A single lightweight LLM router (~155 tokens, 0.15% overhead, temperature 0, one abstract instruction with no benchmark-specific examples) classifies each delegation as needing GRAPH (deterministic, ordered sub-tasks) or NL (iteration, conditionals, free-text interpretation) before the orchestrator emits it; the receiving executor is given a graph-aware prompt so it can traverse the typed dependency edges. Evaluated across four multi-agent benchmarks (BrowseComp, tau-retail, BFCL v3, AppWorld; 1,052 trajectories total) with Claude Sonnet 4.5 as orchestrator (cross-checked with GPT-5 mini and Nova Pro), against NL-only, graph-only (NGH), and an oracle per-task-best upper bound; also compares against 7 alternative schema-unaware and trained-compressor handoff protocols on tau-retail.

## Results

The routed system matches or exceeds NL on every one of four benchmarks: +12.7pp task success on tau-retail (p<0.01, 3.2x compression) and +8.7pp on BrowseComp (p<0.05, 2.2x compression), with parity on BFCL and AppWorld. Graph-only alone regresses -14.6pp on AppWorld (CI [-22.8,-6.4]) because rigid dependency edges prevent adaptive backtracking when the environment deviates from the encoded plan; the router eliminates this regression at near-zero cost by defaulting 89% of AppWorld tasks to NL. Average handoff compression across all trials is 2.1x. An oracle per-task-best format reaches 60.3% on AppWorld vs. the router's 51.7%, identifying 8.6pp of headroom attributable only to execution-time (not task-content) signals the current router cannot see. On tau-retail, the routed graph (+12.7pp, zero-training) beats all seven other schema-aware/unaware compression protocols tested, including a GRPO-fine-tuned 1.5B-param router and a trained T5 autoencoder compressor. Effects replicate in direction with GPT-5 mini as orchestrator (BrowseComp 65->68%, BFCL 82->85%, AppWorld 50->52%). Error-taxonomy analysis of 345 trajectories finds 76% of multi-agent failures stem from inter-agent misalignment (misinterpreted ordering, dropped prerequisites, ambiguity-induced retry loops) -- absent by construction in single-agent systems -- which the typed dependency edges directly address.

## Limitations

The router performs per-task-type (not fine-grained per-instance) routing and is blind to benchmark identity, so decisions cluster coarsely (100% graph on dependency-chain benchmarks, 89% NL on AppWorld); the 8.6pp oracle headroom would require execution-time signals and is left to future work. The typed schema was designed on 47 tau-bench trajectories disjoint from all evaluation data; the paper notes the schema may not generalize to domains with fundamentally different coordination patterns (e.g. open-ended creative tasks), and automating schema generation beyond hand-design is left as future work. Main results use one orchestrator backbone (Claude Sonnet 4.5) with only partial cross-vendor/cross-model replication reported. The graph-aware executor prompt is a required complement to the schema -- omitting it yields no gain -- so adoption requires updating the receiving agent, not just the message format.

## Why it matters here

- **overthinking**: Indirectly relevant: the core structure-flexibility tradeoff -- explicit structure prevents waste on predictable tasks but over-constrains tasks needing adaptive reasoning -- is explicitly drawn by the authors as a parallel to intra-agent chain-of-thought (structure helps arithmetic but over-constrains creative generation, motivating adaptive prompting). It is evidence for the same design principle overthinking mitigation targets (match the amount/kind of structure to task difficulty) applied one level up, at the inter-agent message-format layer rather than within a single reasoning trace.

## Entities

- **Concepts**: structure-flexibility tradeoff, handoff format selection, typed dependency graph for multi-agent delegation, inter-agent misalignment
- **Methods**: typed dependency-graph (DAG) message schema, LLM-based per-task format router, constrained decoding
- **Datasets**: [BrowseComp](../../../../wiki/datasets/browsecomp.md), tau-bench (tau-retail, tau-airline), [BFCL v3](../../../../wiki/datasets/bfcl-v3.md), AppWorld

Tags: `multi-agent`, `token-efficiency`, `adaptive-routing`, `structured-communication`

## Abstract

Multi-agent LLM systems coordinate through natural-language messages that consume 40--60\% of their token budget. Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning. We propose \textbf{Routed Graph Handoff}, where a lightweight LLM router (155 tokens, 0.15\% overhead) selects between a typed dependency graph and natural language for each delegation. On four benchmarks (1,050+ trajectories), the routed system matches or exceeds NL-only on every task: \textbf{+12.7\,pp} on $τ$-retail at 3.2$\times$ compression ($p{<}0.01$), \textbf{+8.7\,pp} on BrowseComp at 2.2$\times$ compression ($p{<}0.05$), and parity on BFCL and AppWorld. Without the router, graph-only delegation regresses 14.6\,pp on AppWorld; the router eliminates this at near-zero cost. A graph-aware executor prompt is required: the same schema without interpretation guidance yields no gain. An oracle analysis reveals 8.6\,pp of additional headroom, motivating execution-time adaptive routing as future work.

---

Record id: `arxiv:2608.25277`
