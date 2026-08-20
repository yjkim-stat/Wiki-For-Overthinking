<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling

- **Authors**: Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat, Soumyabrata Pal, Ramasuri Narayanam, Dinesh Manocha
- **Venue**: cs.AI
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10928>
- **PDF**: <https://arxiv.org/pdf/2608.10928v1>
- **Topics**: reasoning-faithfulness, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.50, test-time-scaling 0.62

## In one line

Injects a retrieved solved problem, with its full worked solution, into the middle of a reasoning model's own thinking trace at each step boundary, using the model's current intermediate answer as the retrieval query.

## Problem

Sequential test-time scaling extends a trace by prompting the model to keep going ('Wait', 'Think more'), and beyond a point this stops helping and starts hurting: longer traces show increased uncertainty, repetitive cycling, drift from the original problem, and error compounding, so the extra compute amplifies a mistake rather than correcting it. Existing retrieval does not address this. RAG and in-context learning retrieve once before reasoning begins and leave the context static; the dynamic methods that do interleave retrieval with thinking target factual knowledge rather than solved examples that act as procedural scaffolds.

## Contributions

- In-trace retrieval of complete solved exemplars at every reasoning step, rather than facts before reasoning starts
- Use of the model's elicited intermediate answer as the retrieval query, in place of the raw reasoning text
- An analysis showing in-trace exemplars lower the predictive entropy of the generated answer relative to sequential scaling
- A budget accounting under which the method has strictly fewer generation tokens than the baseline it beats

## Method

At each step boundary the framework closes the thinking block, appends a final-answer delimiter to elicit an intermediate answer, and uses that answer -- not the raw trace -- as the retrieval query. The reason is stated directly: a raw reasoning step is exploratory and full of verbose hypotheses, self-corrections and backtracking, so using it as a dense query injects semantic noise; the intermediate answer reflects the model's current belief state instead. The test query and that answer are jointly encoded with E5-Large, the nearest neighbour is found by cosine similarity over a FAISS index, and the retrieved entry -- the exemplar problem together with its step-by-step solution -- is formatted and appended to the trace with a continuation prompt, after which thinking resumes. Step boundaries are triggered by the model emitting its own stop token before the budget is exhausted, the same signal budget forcing uses; models that generate continuously get an insertion forced at a fixed token interval instead. The example bank is the synthetic portion of NuminaMath-1.5 under quality filters, 309,609 entries, decontaminated in two stages -- exact-match removal, then cosine-similarity filtering that drops any entry above 0.90 similarity to an evaluation instance -- with a post-hoc audit confirming no test query retains a corpus neighbour above the threshold. The budget control is the design's strongest feature: exemplar tokens count against the thinking budget identically to generated tokens, so at any budget the method has strictly fewer of its own tokens than sequential scaling does, and any gain cannot be extra compute. Five models from 1.5B to 8B, four benchmarks, three seeds, temperature 0.6, and two retrieval baselines beyond sequential scaling: static input-level ICL, and random per-step retrieval.

## Results

Improvement over sequential test-time scaling in every model-by-benchmark cell, and the size tracks difficulty: small on GSM-8K and MATH-500, largest on AIME 2025, reaching +13.4 points for Qwen3-1.7B. The budget curves are the more interesting result. Sequential scaling improves with more thinking tokens and then degrades: on AIME 2025 with Qwen3-1.7B it plateaus around 22 percent at 8K tokens and does not improve at 32K, while ThinkRetrieve climbs steadily to 35.6; on GSM-8K with DeepSeek-R1-Distill-Qwen-1.5B it collapses from 83 to 52 percent by 22K tokens while ThinkRetrieve holds 84. Across all five models and every benchmark the retrieval-augmented curve is monotone increasing or flat where the sequential one turns over. The mechanism analysis reports that in-trace exemplars measurably reduce the predictive entropy and uncertainty of the generated answer relative to sequential scaling, which is the paper's account of why procedural scaffolding beats thinking longer. The qualitative case shows both methods reaching the same wrong intermediate estimate on a MATH-500 probability problem, with self-reflection failing to catch it and a retrieved near-miss problem supplying the contrast that exposes the miscount.

## Limitations

No limitations section in the material read. What a reader should weigh first is the retrieval encoder: the related-work section cites a result that structurally faithful retrieval over mathematics is hard with off-the-shelf encoders, and the method then uses an off-the-shelf E5-Large, with the encoder choice relegated to an ablation. Second, decontamination is by cosine similarity at 0.90 and the audit reports maximum retained similarities of 0.898 and 0.891 -- immediately below the cut, with mean retained similarities of 0.866 and 0.845, which the paper attributes to the structural density of synthetic math corpora rather than leakage, and defends with an answer-distinct retrieval control rather than with a lower threshold. Third, the headline gains sit on AIME 2025, which is 30 problems, so +13.4 is four problems even at three seeds. Fourth, three of the four benchmarks share the same NuminaMath bank and the fourth uses its own training split, so 'adapts to different example banks' rests on one swap, and nothing here tests a domain where a bank of solved problems does not exist. Finally, the entropy reduction is offered as the explanation of the gain but is measured alongside it rather than manipulated, so it is a correlate of the improvement and not shown to cause it.

## Why it matters here

- **reasoning-faithfulness**: The intermediate answer elicited at each step boundary is the same probe the archive's early-exit and change-point work uses, deployed here as a retrieval query rather than a stopping signal. That makes this a third use of one measurement, and it inherits the same caveat the archive attaches to the others: what is probed is the model's current answer, not the reasoning that produced it, so a stable intermediate answer licenses no claim about the trace beneath it.
- **reasoning-training**: The example bank supplies at inference what supervised fine-tuning on reasoning traces supplies in the weights, and the archive already holds the result that 1,000 curated traces are enough to install the behaviour. This is the training-free counterpart, and its failure curve is informative for the training side too: what degrades under sequential scaling is not knowledge but the trace's ability to stay on the problem.
- **test-time-scaling**: The cleanest budget control in this archive's scaling cluster -- retrieved tokens are charged against the same budget as generated ones, so the method spends strictly fewer of its own tokens than the baseline it beats. And it supplies a measured instance of the diminishing-returns phenomenon the archive keeps citing: sequential scaling collapsing from 83 to 52 percent as the budget grows is a stronger statement of 'thinking longer is not thinking better' than anything else here, because it is a decline rather than a plateau.

## Entities

- **Concepts**: test-time scaling, in-trace retrieval, procedural scaffolding, [predictive entropy](../../../../wiki/concepts/predictive-entropy.md), error compounding, [reasoning drift](../../../../wiki/concepts/reasoning-drift.md), budget forcing, intermediate answer probing, [in-context learning](../../../../wiki/concepts/in-context-learning.md)
- **Methods**: [retrieval-augmented generation](../../../../wiki/methods/retrieval-augmented-generation.md), [dense retrieval](../../../../wiki/methods/dense-retrieval.md), FAISS, [budget forcing](../../../../wiki/methods/budget-forcing.md), [self-reflection](../../../../wiki/methods/self-reflection.md), [decontamination](../../../../wiki/methods/decontamination.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME 2025](../../../../wiki/datasets/aime-2025.md), [SciQ](../../../../wiki/datasets/sciq.md), NuminaMath

Tags: `test-time-scaling`, `retrieval`, `in-context-learning`, `entropy`, `efficient-reasoning`

## Abstract

Large Reasoning Models (LRMs) improve performance by allocating additional inference-time compute to generate extended chain-of-thought reasoning. However, recent studies reveal that sequential test-time scaling often yields diminishing or even negative returns, as longer traces exhibit increased uncertainty, error compounding, and drift from the original problem. We propose ThinkRetrieve, a test-time scaling framework that augments the reasoning traces of LRMs with dynamically retrieved solved examples at each reasoning step. Given an external corpus of problems paired with step-by-step solutions, ThinkRetrieve retrieves relevant exemplars at each intermediate step and injects them directly into the thinking trace, providing the model with guidance on how to reason rather than merely what facts are relevant. Experiments across five reasoning models (1.5B--8B parameters) on GSM-8K, MATH-500, AIME 2025, and SciQ demonstrate that ThinkRetrieve consistently improves accuracy over standard test-time scaling, with relative gains of up to $60\%$ on AIME 2025.

---

Record id: `arxiv:2608.10928`
