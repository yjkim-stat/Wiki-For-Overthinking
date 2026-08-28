<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience

- **Authors**: Zhixiao Qi, Feng Huang, Yunqi Zhang, Shijie Zhang, Qingqing Sun, Yongfeng Huang, Minghu Jiang, Shuai Chen, Tianyi Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1572/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1572.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1572
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Thought-Action Graph (TAG) distills past successful LLM-knowledge-graph interaction trajectories into a structured, reusable repository of fine-grained reasoning operators (a thought layer of abstract query patterns plus an action layer of concrete entity/relation parameters), letting TAG-Reasoning (TAGR) retrieve and assemble a query-specific reasoning blueprint offline instead of exploring the KG online -- outperforming 15 baselines on three KGQA benchmarks while using far fewer LLM calls (3, vs. up to 11.6) and generated tokens (65-71, vs. hundreds).

## Problem

LLMs hallucinate on knowledge-intensive question answering due to gaps in factual knowledge; integrating knowledge graphs (KGs) helps, but existing KG-augmented approaches either retrieve KG context into the prompt (poor generalization to unseen questions/concepts, dependent on retriever quality) or treat the LLM as an agent that iteratively explores the KG (many LLM calls, low efficiency) -- and critically, neither class of method learns or reuses reasoning paths from past successfully-solved questions, so each new query is solved from scratch with no accumulation of solution patterns over time.

## Contributions

- the Thought-Action Graph (TAG), a structured, two-layer (thought/action) repository distilling reusable, fine-grained reasoning operators from past successful LLM-KG interaction trajectories, addressing the lack of experience reuse in prior retrieval- and agent-based KGQA methods
- TAG-Reasoning (TAGR), a KGQA paradigm that retrieves and assembles a query-specific reasoning blueprint (Meta-Action-Chain) from TAG offline, then executes it on a filtered KG subgraph, replacing costly online trial-and-error exploration
- a three-step KG filtering procedure that substantially reduces irrelevant triples the LLM must navigate during execution, shown via ablation to be the single largest contributor to accuracy
- state-of-the-art results across three KGQA benchmarks and three LLM backbones with dramatically fewer LLM calls (3) and generated tokens (65-71) than compared agent-based baselines, plus demonstrated cross-dataset generalization and continued improvement as the TAG repository scales

## Method

Constructs the Thought-Action Graph (TAG) from training-set SPARQL queries: a GPT-4o-mini-based parser converts each SPARQL query into a Meta-Action-Chain (MAC), a sequence of atomic operations (SELECT, WHERE_TRI_PATTERN, UNION, WHERE_FILTER, etc.) from a topic entity to an answer; these MACs are then decomposed and organized into TAG's two-layer structure -- a thought layer (upper layer, storing abstract operation patterns as a graph of Ontology and Option nodes, e.g. a path Country->SELECT->WHERE_TRI_PATTERN->UNION->WHERE_FILTER->Country represents an abstract query template independent of specific entities) and an action layer (lower layer, storing concrete Entity and Action nodes linked to their corresponding thought-layer nodes via instance_of/has_parameter relationships, providing the specific parameters needed to instantiate a thought-layer template for a given query). At inference (TAGR), given a new question: (1) Thought Layer Retrieval locates the relevant ontology-node paths and prunes them to those ending at the LLM-predicted target answer ontology; (2) Action Layer Retrieval maps the pruned abstract paths to their corresponding action-layer nodes and filters by embedding-based semantic similarity between the query and candidate source questions, retaining the top-k most similar; (3) Composition combines the pruned thought-layer paths and filtered action-layer paths into a complete thought-action subgraph, which the LLM (Navigator phase) turns into a query-specific Meta-Action-Chain M*; (4) the LLM (Executor phase) then executes M* on the KG to derive the final answer, with KG Filtering (a three-step process using Fasttext embedding similarity per MAC step) removing irrelevant triples from a >1K-triple original subgraph down to a small, action-relevant filtered subgraph before execution, reducing noise the LLM would otherwise have to navigate.

## Results

Across three KGQA benchmarks (WebQSP, CWQ, GrailQA, all built on Freebase) and three LLM backbones (GPT-4o-mini, Qwen2.5-7B, Llama-3.1-8B, each fine-tuned on 6K samples), TAGR outperforms all 15 compared baselines (LLM/graph-reasoning-only methods like ReaRev/UniKGQA, and KG-enhanced LLM-reasoning methods like ToG, RoG, EffiQA, GNN-RAG, KG-Agent, DoG, GCR, KBQA-o1, EoG_SFT) on Hits@1 across all three datasets, with relative improvements of 0.5%, 1.6%, and 4.7% respectively over the best prior method (GrailQA specifically: 96.1% Hits@1 for TAGR/Llama-3.1-8B vs. 91.4% for the next-best EoG_SFT). Efficiency gains are substantial: TAGR requires only 3 LLM calls across all configurations, versus up to 11.6 for ToG and 7.3 for GNN-RAG among compared methods that report this metric, and only 65-71 generated tokens versus 7,069 for ToG and 521 for GNN-RAG -- because TAGR transforms the costly online trial-and-error exploration of agent-based methods into an offline TAG retrieval-and-assembly process, requiring far less generation at inference time. Ablations (WebQSP/CWQ) show all three components matter: removing KG Filtering drops WebQSP Hits@1 from 93.2% to 72.4% (F1 65.7%->61.7%), confirming that filtering the KG down to action-relevant triples before execution is critical to avoid the LLM getting lost in a noisy, >1K-triple subgraph; replacing the complete TAG with an incomplete (reduced) version drops Hits@1 to 86.6% (still substantially above most baselines, but below the full system), showing TAG's completeness matters though the framework degrades gracefully; skipping fine-tuning of the LLM component drops Hits@1 to 82.2%, confirming the reasoning task is specialized enough that fine-tuning meaningfully helps even with TAG's structured guidance. Retrieval-breadth analysis (varying the number of MACs retrieved per query) shows Hits@1 rises continuously with more MACs (more comprehensive candidate reasoning blueprints), while F1 can decline at higher MAC counts on some datasets due to increased hallucination risk during KG execution -- a precision/recall tradeoff in how much candidate reasoning breadth to expose to the LLM. A three-stage TAG-scale experiment (progressively adding WebQSP -> WebQSP+CWQ -> WebQSP+CWQ+GrailQA training data to build TAG) shows performance on WebQSP continues to improve as TAG scale grows, evidence the repository genuinely accumulates useful reusable reasoning experience rather than saturating quickly. Cross-dataset (out-of-distribution) evaluation, constructing TAG solely from each individual dataset's training set and testing on all three, shows no significant 'diagonal advantage' (a TAG built from dataset X performs comparably whether tested on X or a different dataset Y), demonstrating TAGR's generalization capability rather than narrow overfitting to its construction dataset's specific query distribution.

## Limitations

TAG construction currently relies on SPARQL-based training data (converted to MACs via an LLM parser) to build the reusable reasoning repository, so applicability to KGQA settings lacking structured query annotations for training is not directly addressed. Retrieval breadth (number of MACs retrieved) presents an explicit precision/recall tradeoff: larger breadth improves Hits@1 but can reduce F1 due to increased hallucination risk during KG execution, requiring a tuning choice rather than a strictly dominant setting. All evaluation is conducted on Freebase-based benchmarks (WebQSP, CWQ, GrailQA); the paper does not report generalization to other knowledge-graph schemas within its own experiments.

## Why it matters here

- **overthinking**: Only tangentially relevant: this targets KGQA efficiency by replacing costly agent-style online KG exploration (many LLM calls, many tokens) with an offline-retrieved reasoning blueprint, which shares this archive's general concern with reducing wasted LLM inference compute, but the object being optimized is the number of LLM-KG interaction rounds and generated action tokens in a structured-query setting, not the length or productiveness of a single free-form chain-of-thought reasoning trace that overthinking-mitigation methods elsewhere in this archive address.

## Entities

- **Concepts**: Thought-Action Graph (TAG), Meta-Action-Chain (MAC), reasoning-experience reuse, thought layer / action layer, KG filtering (noise reduction)
- **Methods**: Thought-Action Graph (TAG) construction and retrieval, TAG-Reasoning (TAGR), KG Filtering, ToG / RoG / EffiQA / GNN-RAG / KG-Agent / DoG / GCR / KBQA-o1 / EoG_SFT (baselines)
- **Datasets**: WebQSP, CWQ (ComplexWebQuestions), GrailQA, Freebase (underlying KG)

Tags: `knowledge-graph-question-answering`, `reasoning-efficiency`, `experience-reuse`, `retrieval`, `agentic-reasoning`

## Abstract

Large language models (LLMs) often hallucinate in question answering (QA) tasks due to a lack of factual knowledge. While integrating knowledge graphs (KGs) with LLMs has alleviated this issue, existing methods suffer from poor generalization or low reasoning efficiency, and critically, they overlook the learning and reuse of reasoning paths from past experiences. To address these challenges, we introduce Thought-Action Graph (TAG), a structured repository of reasoning experiences. TAG decomposes successful LLM-KG interaction trajectories into fine-grained semantic operators, which are stored in TAG constructed by the thought layer and action layer. Building upon TAG, we propose a novel KGQA paradigm — TAG-Reasoning (TAGR). TAGR first retrieves and assembles reasoning blueprints from TAG, and then guides LLM to efficiently execute on KG according to them. Through this approach, TAGR transforms the computationally expensive online exploration process of LLMs into an offline process of TAG retrieval and assembly. Experimental results on multiple KGQA benchmarks demonstrate that TAGR significantly outperforms state-of-the-art methods across key metrics, while drastically reducing the number of LLM calls and generated tokens. This work opens new avenues for building continual learning, efficient, and faithful KGQA systems.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1572`
