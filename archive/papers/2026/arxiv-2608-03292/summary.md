<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning

- **Authors**: Le Xiang, Zhicheng Guan, Hong Chen, Xiaocong Lin, Zhenghua Lei, Teng Hu, Bolei He, Long Zeng
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03292>
- **PDF**: <https://arxiv.org/pdf/2608.03292v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.40

## In one line

Recasts long-document visual question answering as building an explicit evidence graph whose nodes are grounded document blocks and whose edges are reasoning dependencies, and verifies the graph causally — masking the evidence it cites flips 82.8% of correct answers while masking uncited evidence changes 9.6%.

## Problem

Answering a question over a hundred-page document requires composing evidence scattered across pages, and every existing approach leaves that composition implicit. End-to-end models aggregate evidence inside hidden states; retrieval pipelines hand the model an unordered set of pages; agentic methods produce an interaction trajectory rather than a dependency structure. So even when the answer is right there is no way to inspect how it was derived, which is disqualifying in auditing or medical settings where a standalone prediction is insufficient. The obstacle to fixing it is that the benchmarks supply only final answers, with no annotation of which evidence was used or how it combined.

## Contributions

- Treating evidence composition as an explicit object — a directed graph whose nodes are grounded document blocks or intermediate conclusions and whose edges are reasoning dependencies — rather than as something to be inferred from a trace
- A coarse-to-fine pipeline that localizes candidate pages on downsampled images before parsing only those at native resolution, so the search space shrinks before the expensive step
- Automatically constructed supervision for the missing intermediate labels: one frontier model generates evidence pages and graphs, a second independently validates evidence sufficiency and logical consistency, and only verified samples are kept
- Task-specific reinforcement rewards per stage — a distance-aware soft score for page localization because the target is ordinal rather than binary, and a graph-faithfulness term decomposing into grounding, completeness, structural validity and topology
- A counterfactual traceability evaluation that tests whether the produced graph is load-bearing rather than decorative

## Method

Stage one predicts evidence page indices from low-resolution images of all pages. Stage two parses only those pages at native resolution with a document-parsing model into typed layout elements with bounding boxes and extracted content, forming an evidence pool. Stage three constructs a graph over that pool and derives the answer conditioned on it, factorized so the graph is generated first and the answer conditioned on it, which is what makes every reasoning step attributable to a document block. Training is joint supervised finetuning on the automatically constructed corpus followed by stage-specific group-relative policy optimization: localization is rewarded by a soft F-score that gives partial credit to near-miss pages and favours recall, while the final stage weights a graph-faithfulness term against answer correctness, the latter combining exact match with a model verifier for flexible surface forms. Unanswerable questions are supervised to abstain when supporting evidence is absent. The backbone is an 8B vision-language model finetuned on 16 GPUs, evaluated on three long-document benchmarks with documents up to 150 pages, reporting page localization F1 and coverage alongside accuracy split by single-page, multi-page and unanswerable questions.

## Results

The method reaches 52.9, 56.4 and 85.1 on the three benchmarks, improving its own backbone by 14.4, 11.3 and 11.7 points and exceeding both the strongest open baseline (49.7 on the hardest set) and proprietary reference points (45.6). The staged analysis separates what each optimization does: supervised finetuning carries most of the gain (38.5 to 50.3 on the hardest benchmark), reinforcement on the localization stage raises page coverage from 62.4 to 65.5 and helps single- and multi-page questions while *lowering* unanswerable accuracy from 68.0 to 66.0 — better recall makes the model answer more aggressively when it should abstain — and reinforcement on the reasoning stage slightly reduces retrieval metrics while lifting every question type, recovering unanswerable accuracy to 70.5. The traceability evaluation is the part worth carrying beyond this domain. Masking the evidence the graph cites flips 82.8% of originally correct predictions, while masking evidence it does not cite changes only 9.6% — a counterfactual test that the cited structure is what the answer actually depends on, rather than a plausible annotation printed alongside it. Evidence grounding and graph integrity are near-saturated at 99.5 and 99.6 by rule-based checks, and evidence localization F1 against ground truth is 72.5. Scaling to longer documents isolates the remaining bottleneck: retrieval coverage falls from 70.6 to 50.2 as documents lengthen while accuracy conditioned on successful localization stays roughly flat, so the reasoning holds and the retrieval does not. The ablations are reported honestly against the paper's own thesis — removing structured parsing or graph reasoning both *raise* unanswerable accuracy (to 74.2 and 74.5 from 68.0) by making the model more conservative, at the cost of answerable questions, and a vanilla chain-of-thought variant beats the full method on single-page questions (53.2 against 51.7) while losing on multi-page and unanswerable.

## Limitations

The paper has no limitations section. What a reader should weigh: the intermediate supervision that makes the whole approach possible is generated by two proprietary frontier models and filtered by one of them, so the training signal's quality and its licensing both depend on systems the authors neither control nor release, and the graph structures the model learns are those the generator produces. The counterfactual traceability numbers are computed by the model re-evaluating its own masked inputs, which tests dependence rather than correctness — a graph could be load-bearing and still cite the wrong evidence, and the separate localization F1 of 72.5 suggests roughly a quarter of it is wrong. One backbone at 8B, no seeds or variance, and the reinforcement stages are evaluated on the same benchmark whose fine-grained splits are used to attribute their effects. Finally, the unanswerable result cuts against the framing: two ablations that remove the paper's central mechanisms do better on abstention, so the mechanism trades calibrated refusal for answerable accuracy rather than improving both.

## Why it matters here

- **reasoning-training**: Its transferable contribution is a way of testing whether a reasoning structure is doing work, which this archive has needed and rarely seen: mask what the structure cites and see whether the answer changes, then mask what it does not cite as the control. The 82.8% against 9.6% gap is the shape of evidence the archive's faithfulness thread asks for and usually cannot get, because most reasoning traces have no explicit citation to mask. It also supplies a clean instance of two training signals pulling in opposite directions — optimizing evidence recall raised answerable accuracy and lowered abstention, and only a second reward stage restored it — which is the same tension the archive records between coverage and calibrated refusal. And the scalability decomposition is a diagnostic worth borrowing: reporting accuracy conditioned on successful retrieval separates a reasoning failure from an evidence-acquisition failure, and here it shows the reasoning was never the thing degrading with document length.

## Entities

- **Concepts**: evidence graph, traceability, provenance, counterfactual intervention, [multi-hop reasoning](../../../../wiki/concepts/multi-hop-reasoning.md), [abstention](../../../../wiki/concepts/abstention.md), grounding, long-context reasoning, [process reward](../../../../wiki/concepts/process-reward.md), synthetic data generation
- **Methods**: DocTrace, [GRPO](../../../../wiki/methods/grpo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), [retrieval-augmented generation](../../../../wiki/methods/retrieval-augmented-generation.md), [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), document layout parsing
- **Datasets**: MMLongBench-Doc, LongDocURL, SlideVQA

Tags: `long document`, `evidence graph`, `traceability`, `multimodal`, `counterfactual evaluation`

## Abstract

Long Document Visual Question Answering (LongDocVQA) requires Multimodal Large Language Models (MLLMs) to locate, integrate, and reason over heterogeneous document elements distributed across multiple pages. Existing approaches, including end-to-end MLLMs, retrieval-augmented generation (RAG) pipelines, and document agents, often lack explicit mechanisms to represent and verify how grounded evidence is progressively composed during reasoning, limiting both answer accuracy and traceability. In this paper, we cast LongDocVQA as an explicit evidence graph reasoning problem rather than implicit answer prediction. To this end, we propose DocTrace, a hierarchical framework that progressively performs evidence localization, structured document parsing, and evidence graph reasoning to enable explicit evidence provenance. To effectively learn these capabilities, we develop a two-stage training framework: joint Supervised Fine-Tuning (SFT) first initializes evidence localization and graph reasoning abilities, followed by task-specific Group Relative Policy Optimization (GRPO) with dedicated rewards to further optimize these capabilities. Extensive experiments on MMLongBench-Doc, LongDocURL, and SlideVQA demonstrate that DocTrace consistently outperforms both existing open-source baselines and proprietary MLLMs. Compared with the Qwen3-VL-8B-Instruct backbone, DocTrace achieves absolute improvements of 14.4, 11.3, and 11.7 points on the three benchmarks, respectively. Beyond competitive performance, DocTrace constructs traceable evidence graphs with explicit node-level provenance, enabling transparent and verifiable reasoning for long document understanding.

---

Record id: `arxiv:2608.03292`
