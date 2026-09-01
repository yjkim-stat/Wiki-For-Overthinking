<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Follow the Path: Reasoning over Knowledge Graph Paths to Improve Large Language Model Factuality

- **Authors**: Mike Zhang, Johannes Bjerva, Russa Biswas
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.561/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.561.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.561
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

fs1 fine-tunes LLMs on reasoning traces grounded in knowledge-graph paths (rather than raw distilled reasoning traces), improving factual accuracy on complex multi-hop QA by 6-14 pass@16 points while also producing shorter reasoning traces than the ungrounded baseline.

## Problem

It is unclear whether LLM 'thinking'/reasoning traces, which improve performance on math and puzzle tasks via test-time compute, actually improve factual accuracy on complex multi-hop open-domain QA, since reasoning traces distilled from large reasoning models carry no guarantee of being factually correct along the way.

## Contributions

- fs1, a method for grounding distilled LLM reasoning traces in minimum-hop knowledge-graph paths before fine-tuning, rather than fine-tuning on raw distilled traces
- a demonstration that fs1-tuned models improve factual accuracy 6-14 pass@16 points over instruction-tuned baselines across six multi-hop QA benchmarks, with gains concentrated on harder (3+-hop) questions
- two ablations isolating the source of the gain: near-zero train/test overlap rules out leakage, and near-identical performance across two different teacher models (QwQ-32B vs. DeepSeek-R1) shows KG grounding, not teacher strength, drives the improvement
- release of 3.4K raw and 3.9K KG-enhanced reasoning traces and eight fine-tuned models spanning 0.36B-32B parameters

## Method

Distills reasoning traces from QwQ-32B and DeepSeek-R1 on ComplexWebQuestions (rt: 3.4K correct-only traces), then constructs fs1 by additionally conditioning the trace-generation prompt on minimum-hop knowledge-graph paths (extracted from Wikidata via SPARQL, subject-relation-object linearized graphs) connecting the question entities to the gold answer -- producing 3.9K KG-grounded reasoning traces. Fine-tunes eight Qwen2.5-Instruct/SmolLM2 models (0.36B-32B) via standard SFT on rt or fs1, then evaluates zero-shot on six multi-hop QA benchmarks (23.9K questions total: CWQ, ExaQT, GrailQA, SimpleQA, Mintaka, WebQSP) using pass@k (k up to 16) as an upper-bound test-time-scaling metric, judged by Llama-3.3-70B-as-a-judge.

## Results

With parallel sampling (pass@16), fs1-tuned Qwen2.5-32B consistently outperforms its instruction-tuned counterpart by 6-14 absolute accuracy points across the six benchmarks, and outperforms the rt (KG-ungrounded reasoning trace) variant too. fs1's advantage grows with question difficulty: on questions requiring 3+ hops, fs1 shows the largest relative improvement, while on 1-2 hop questions fs1's improvement is smaller than the baselines'. At single-pass (pass@1) accuracy, fine-tuning benefits are far more pronounced for smaller models (e.g. Qwen2.5-0.5B improves relative WebQSP accuracy by +74.6% with fs1) than larger ones (32B models show only modest single-digit-to-low-teens relative gains, and sometimes slight degradation on individual benchmarks). Two controlled ablations rule out confounds: (Finding 5.1) near-zero training/test data overlap (cosine similarity, exact match) shows the gain is not data leakage; (Finding 5.2) fine-tuning on fs1 traces sourced from QwQ-32B versus from DeepSeek-R1 (685B) yields almost identical downstream performance, showing the gain comes from KG grounding itself rather than from a stronger teacher model. Reasoning-trace-length statistics show fs1 traces are typically shorter than rt traces (e.g. median subwords 496 vs. 635 for DeepSeek-R1-sourced traces), despite being more factually accurate by exact-match/semantic-match/LLM-judge criteria (e.g. LLM-as-Judge factual accuracy 0.49 for rt vs. 0.65 for fs1, aggregated).

## Limitations

The paper explicitly notes it assumes conditioning on KG paths improves reasoning-trace accuracy but does not guarantee every intermediate step is correct. Entity-answer evaluation is inherently difficult (exact string match fails on paraphrases/units), mitigated but not fully solved by LLM-as-a-judge, which carries its own limitations. Some test benchmarks are relatively old and English-only, with no control over whether their content appeared in the base models' pretraining data. pass@k is explicitly an upper-bound metric requiring an additional selection mechanism (e.g. majority voting, a verifier) for practical deployment; the paper does not implement or evaluate one. At the sub-billion parameter scale, fine-tuning benefits do not generalize uniformly across model families (SmolLM2-360M shows a -15.9% degradation on GrailQA despite gains elsewhere).

## Why it matters here

- **overthinking**: Loosely relevant but instructive: this is a factuality paper, not an efficiency paper, yet it reports as an incidental finding that its factually-grounded reasoning traces (fs1) are consistently *shorter* than the ungrounded baseline (rt) while also being more accurate -- a concrete data point for the claim (made elsewhere in this archive) that longer reasoning is not the same as better-grounded reasoning, and that anchoring reasoning to external verifiable structure (here, a knowledge graph) can substitute for raw trace length as a route to correctness.

## Entities

- **Concepts**: knowledge-graph-grounded reasoning trace, minimum-hop path extraction, factual simple test-time scaling (fs1), pass@k as an upper-bound metric
- **Methods**: fs1 (KG-path-grounded reasoning-trace fine-tuning), rt (raw distilled reasoning traces, baseline), supervised fine-tuning, pass@k evaluation, LLM-as-a-judge (entity-alignment factuality scoring)
- **Datasets**: ComplexWebQuestions (CWQ), ExaQT, GrailQA, [SimpleQA](../../../../wiki/datasets/simpleqa.md), Mintaka, WebQSP

Tags: `factuality`, `knowledge-graph`, `reasoning-trace-grounding`, `test-time-scaling`, `multi-hop-QA`

## Abstract

We introduce fs1, a simple yet effective method that improves the factuality of reasoning traces by sourcing them from large reasoning models and grounding them by conditioning on knowledge graph (KG) paths. We fine-tune eight instruction-tuned Large Language Models (LLMs) on 3.9K factually grounded reasoning traces and rigorously evaluate them on six complex open-domain question-answering (QA) benchmarks encompassing 23.9K questions. Our results demonstrate that our fs1-tuned model consistently outperforms instruction-tuned counterparts with parallel sampling by 6-14 absolute points (pass@). Our detailed analysis shows that fs1 considerably improves model performance over more complex questions (requiring 3 or more hops on KG paths) and numerical answer types compared to the baselines. Furthermore, in single-pass inference, we notice that smaller LLMs show the most improvements. While prior works demonstrate the effectiveness of reasoning traces primarily in the STEM domains, our work shows strong evidence that anchoring reasoning to factual KG paths is a critical step in transforming LLMs for reliable knowledge-intensive tasks.

---

Record id: `doi:10.18653/v1/2026.findings-acl.561`
