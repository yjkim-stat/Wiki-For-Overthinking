<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning

- **Authors**: Sangkwon Park, Donghun Kang, Jisoo Mok, Sungroh Yoon
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1712/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1712.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1712
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

Verbal-R3 shows that rewriting retrieved documents into 'Verbal Annotations' -- analytic narratives that explicitly state the logical connection between a query and a document, distilled from GPT-OSS-120B into a lightweight 1.5B/3B Verbal Reranker -- substantially improves RAG accuracy over both raw context injection and stylistic paraphrasing, and pairs this with a relevance-guided test-time-scaling method that allocates search-trajectory budget toward high-relevance-scored queries, beating Search-R1 by up to 18% F1 while cutting reranker calls ~45-54%.

## Problem

Standard Retrieval-Augmented Generation injects raw retrieved text directly into an LLM's context, which is suboptimal due to exposure bias and the frequent inclusion of irrelevant, distracting information, and it was unclear what kind of intermediate transformation of retrieved documents would actually help an LLM integrate retrieval results correctly.

## Contributions

- identification and validation of Verbal Annotations as a distinct and more effective way to bridge retrieval and LLM reasoning than raw context injection or paraphrasing
- Context Utilization Efficacy (CUE), isolating whether an LLM correctly uses accurately-retrieved evidence
- Verbal-R3, a two-agent agentic RAG framework achieving state-of-the-art results across seven QA benchmarks, with larger gains on multi-hop tasks
- relevance-guided test-time scaling that allocates trajectory budget toward the most promising search paths, matching or exceeding naive majority voting while cutting reranker calls 45-54%

## Method

Defines Verbal Annotations as analytic narratives that explicitly articulate the logical alignment between a query and a retrieved document, distinct from mere paraphrasing. A preliminary study finds Verbal Annotations substantially outperform naive context injection and paraphrasing, improving a new Context Utilization Efficacy (CUE) metric. Builds Verbal-R3, a two-agent framework: a Generator performs iterative retrieval and reasoning, and a Verbal Reranker (distilled via SFT from GPT-OSS-120B into a lightweight 1.5B/3B model) scores each document's relevance and rewrites it into a Verbal Annotation appended back into the Generator's context; the Generator is aligned to the Reranker via GRPO. At inference, relevance-guided test-time scaling allocates a fixed trajectory budget across active reasoning branches in proportion to each query's relevance score, selectively expanding promising search trajectories rather than exploring all branches equally.

## Results

Paraphrased context underperforms raw-context injection, while Verbal Annotations improve average EM to 41.92% from 38.75% (Search-R1 3B baseline) and increase CUE substantially more than raw retrieval accuracy or EM/F1, confirming the mechanism is better use of correctly-retrieved evidence. The distilled Verbal Reranker matches or outperforms larger 3B/7B reranking baselines. Verbal-R3 3B (~6B total parameters) surpasses Search-R1 3B by 17.1% EM/18.0% F1 and even surpasses the larger Search-R1 7B; Verbal-R3 7B improves over Search-R1 7B by 15.3% EM/14.3% F1. Gains are markedly larger on multi-hop tasks (+26.91% F1) than single-hop tasks (+9.67%). Relevance-guided test-time scaling matches or exceeds naive majority voting's accuracy while cutting reranker calls by 45.2%/53.8% and saving substantial tokens per query. An ablation replacing Verbal Annotations with full-document observations confirms the annotation mechanism itself (not just reranking) drives the gains.

## Limitations

The framework employs two LLM modules, introducing computational overhead depending on deployment setting; remaining errors in Verbal Annotations can accumulate during iterative retrieval and reasoning. Experiments use an offline retriever; live web-search integration is left for future work. The paper notes the approach cannot fully eliminate hallucination and flags the need for complementary safeguards (confidence scoring, human oversight).

## Why it matters here

- **overthinking**: Indirectly relevant: a RAG/reranking paper, not a direct study of reasoning-trace length, but its relevance-guided test-time scaling is a concrete instance of the topic's broader concern -- allocating parallel test-time compute (search trajectories rather than reasoning tokens) toward the most promising candidates instead of exploring uniformly, achieving comparable-or-better accuracy at lower query/token cost. A useful cross-application example of adaptive, signal-guided test-time budget allocation outside the pure chain-of-thought setting.

## Entities

- **Concepts**: Verbal Annotation (analytic query-document relevance narrative), Context Utilization Efficacy (CUE), Verbal Reranker (distilled relevance-scoring + rewriting module), relevance-guided test-time scaling
- **Methods**: Verbal-R3 (Generator + Verbal Reranker, GRPO alignment), relevance-guided test-time scaling, Search-R1 (baseline), IRCoT, ITER-RETGEN, RAG (baselines), MonoT5, RankLLaMA, Rank1 (reranker baselines)
- **Datasets**: 2WikiMultiHopQA, Bamboogle, [HotpotQA](../../../../wiki/datasets/hotpotqa.md), [MuSiQue](../../../../wiki/datasets/musique.md), Natural Questions (NQ), PopQA, [TriviaQA](../../../../wiki/datasets/triviaqa.md), BEIR

Tags: `retrieval-augmented-generation`, `reranking`, `test-time-scaling`, `agentic-reasoning`, `multi-hop-qa`

## Abstract

The conventional Retrieval-Augmented Generation (RAG) paradigm of injecting raw retrieved texts into the Large Language Model (LLM)’s context often results in suboptimal integration of retrieved information. This paper proposes to bridge retrieval results and the LLM’s reasoning ability through Verbal Annotations, analytic narratives that explicitly articulate the logical connection between a search query and retrieved contexts. Our empirical investigation reveals the potential of Verbal Annotations to substantially enhance the LLM’s ability to generate accurate, contextually-grounded responses. Motivated by this finding, we introduce Verbal-R3, a novel agentic RAG framework that consists of a Generator and a Verbal Reranker. The Generator performs iterative retrieval and reasoning, while the Verbal Reranker returns relevance scores and Verbal Annotations to guide the reasoning and answering process of the Generator. The inference process of Verbal-R3 is further refined through relevance-guided test-time scaling, which efficiently allocates test-time compute for effective trajectory expansion. Verbal-R3 achieves state-of-the-art performance on complex Question Answering benchmarks, validating the effectiveness of the proposed framework.

---

Record id: `doi:10.18653/v1/2026.acl-long.1712`
