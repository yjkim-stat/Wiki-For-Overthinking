<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection

- **Authors**: James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1305/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1305.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1305
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

VecCISC reduces the cost of Confidence-Informed Self-Consistency (CISC) -- which needs a separate critic-LLM call on every sampled reasoning trace to weight majority voting -- by embedding traces, clustering them per candidate answer, and sending only cluster-representative (nearest-centroid) traces to the critic, cutting critic calls 30-35% and total pipeline token usage 47% while matching or exceeding CISC's accuracy across five models and five datasets.

## Problem

Confidence-Informed Self-Consistency (CISC), a 'think twice' method that weights majority voting over sampled reasoning traces by a critic LLM's confidence score for each trace, substantially increases inference cost because it requires an additional critic-LLM call for every one of the n sampled traces, and naive CISC makes no distinction between semantically redundant, degenerate, or hallucinated traces and higher-quality ones when deciding which to send to the (expensive) critic.

## Contributions

- VecCISC, a lightweight framework that filters semantically redundant, degenerate, or low-quality reasoning traces via per-answer embedding clustering before invoking an expensive critic LLM for confidence scoring, reducing the 'think-twice' overhead of CISC
- a min-centroid cluster-representative selection rule, shown via ablation against random-trace selection to be specifically responsible for preserving downstream accuracy while reducing token cost
- empirical validation across five models and five diverse reasoning/QA datasets showing 30-35% fewer critic calls and 47% total pipeline token reduction, while matching or exceeding CISC's and Self-Consistency's accuracy in nearly all settings

## Method

Given n sampled reasoning-trace/answer pairs for a question, VecCISC first groups traces by their distinct final answer (preserving the set of unique candidate answers), then embeds each group's traces (via OpenAI text-embedding-3-small) and clusters them within each answer group using either K-Means or Hierarchical Agglomerative Clustering (HAC, with K chosen per dataset-model pair via grid search on a holdout set). From each resulting cluster, a single representative trace is selected via a 'min-centroid' rule -- the trace whose embedding has the highest cosine similarity to (i.e. is closest to) the cluster centroid, on the reasoning that the least semantically deviant trace within a cluster is least likely to contain anomalous reasoning errors (compared against a random-trace-selection ablation). Only these cluster representatives (rather than all n traces) are passed to the critic LLM, which scores each with a verbalized 0-1 confidence rating, softmax-normalized (with a tunable temperature T) before the final answer is chosen via weighted majority vote, mirroring CISC's aggregation but over a smaller, curated candidate-trace set.

## Results

Across five models (GPT-4o mini, Llama 3.1 8B, Llama 3.3 70B, Qwen2.5 7B, Mistral 7B) and five datasets (AQuA-RAT, CommonsenseQA, ARC-Challenging, MMLU-Pro, GPQA), VecCISC+KMeans reduces the number of critic-LLM calls by an average 34.68% and VecCISC+HAC by 30.2% versus vanilla CISC; across the entire pipeline (including the initial self-consistency sampling stage), VecCISC+KMeans averages a 17.34% and VecCISC+HAC a 15.1% reduction in total LLM calls. Since the critic-LLM stage accounts for 77% of total token usage in the pipeline (being the most token-heavy component), these call reductions translate to substantial token savings: VecCISC+KMeans reduces critic-stage token usage by 36.2% and VecCISC+HAC by 31.69%, and averaged across the entire pipeline (sampling plus critic stages), both variants reduce total token usage by 47%. The min-centroid representative-selection strategy specifically drives lower token usage than random cluster-trace selection on 60% (KMeans) to 68% (HAC) of model-dataset combinations, confirming it selects higher-quality, typically shorter reasoning traces rather than arbitrary ones. Accuracy results (best-of-10 and average-of-10 runs) show VecCISC+KMeans and VecCISC+HAC consistently match or exceed both plain CISC and Self-Consistency across nearly all model-dataset combinations -- e.g. VecCISC+HAC records the best average accuracy on all combinations except two (AQuA-RAT/Mistral 7B and CommonsenseQA/GPT-4o-mini, where VecCISC+KMeans is best) -- so the token/cost reduction comes with no accuracy penalty and in several cases a modest improvement. As an ablation, VecCISC (random) -- randomly sampling K traces per answer group instead of clustering -- significantly underperforms both CISC and plain Self-Consistency, directly demonstrating that the clustering step (not merely reducing the number of critic calls) is responsible for the method's accuracy preservation.

## Limitations

The clustering and confidence-scoring approach as instantiated requires access to token-level generation from the LLM to compute reasoning-trace embeddings and prompts, and (as stated in the paper's own limitations section) the broader 'think-twice' framework this builds on is only applicable to white-box LLMs, limiting reach for fully closed API-only models where reasoning traces or internals are unavailable; the paper's own related-work discussion also notes it does not address the separate need for candidate *answer* selection strategies for weighted majority voting beyond the trace-clustering step itself, an open direction it leaves unaddressed. A general-purpose (not domain- or benchmark-fine-tuned) embedding model was deliberately chosen for adaptability, which the paper flags as a design tradeoff versus potentially higher-fidelity but less general domain-specific embeddings.

## Why it matters here

- **overthinking**: Indirectly relevant to test-time compute efficiency: this targets the cost of the aggregation/verification stage of parallel test-time scaling (critic-LLM calls for confidence scoring), not single-trace reasoning length, but shares this archive's recurring theme that expensive per-sample verification or scoring signals can be reduced by first filtering out redundant or low-quality candidates via a cheap similarity/clustering signal, complementary to methods like STOP and STEP that make similar filtering decisions from internal model states rather than external embeddings.

## Entities

- **Concepts**: think-twice paradigm, Confidence-Informed Self-Consistency (CISC), reasoning-trace embedding clustering, min-centroid representative selection, [weighted majority voting](../../../../wiki/concepts/weighted-majority-voting.md)
- **Methods**: VecCISC (+KMeans / +HAC), Confidence-Informed Self-Consistency (CISC, baseline), [Self-Consistency (SC, baseline)](../../../../wiki/methods/self-consistency-sc-baseline.md), VecCISC (random), ablation
- **Datasets**: [AQuA-RAT](../../../../wiki/datasets/aqua-rat.md), [CommonsenseQA](../../../../wiki/datasets/commonsenseqa.md), ARC-Challenging, [MMLU-Pro](../../../../wiki/datasets/mmlu-pro.md), [GPQA](../../../../wiki/datasets/gpqa.md)

Tags: `test-time-scaling`, `self-consistency`, `confidence-calibration`, `clustering`, `inference-cost-reduction`

## Abstract

A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted majority voting necessitates calling a critic LLM on each candidate’s reasoning trace to produce the answer’s confidence score. This secondary series of LLM calls greatly increases the overhead and cost of weighted majority voting, despite its potential performance benefits. To reduce this expense, we propose VecCISC, a lightweight, adaptive framework that uses a measure of semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic. To ensure adequate experimental thoroughness, we evaluated VecCISC on five challenging, widely-adopted datasets spanning the domains of mathematics, chemistry, biology, commonsense reasoning, and the humanities. Our results demonstrate that VecCISC reduces the total token usage by 47%, while maintaining or exceeding the accuracy of CISC.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1305`
