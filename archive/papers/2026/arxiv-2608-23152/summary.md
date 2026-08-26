<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation

- **Authors**: Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty
- **Venue**: cs.CL
- **Published**: 2026-08-24
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.23152>
- **PDF**: <https://arxiv.org/pdf/2608.23152v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

FIRE splits counterspeech generation into two sub-2B Qwen3-1.7B agents -- one that classifies the hate category, names the target group, writes a reasoning trace and triggers a web search for evidence, one that writes the reply -- with specialization coming from a contrastively-trained 22M retrieval encoder over annotated examples rather than from fine-tuning.

## Problem

Automated counterspeech work has emphasised stylistic control while treating hate speech as homogeneous, but a rebuttal that works against a stereotype does not work against a conspiracy theory. Existing datasets pair input to output or annotate tone, and carry no hate-category label, reasoning trace or evidence mapping, so a model cannot ground its reply in the specific nature of the abuse.

## Contributions

- FactualCS, 4,784 instances annotated with hate category, target group, reasoning trace, retrieval query and supporting evidence, developed through a piloted multi-stage protocol with guidelines for the ambiguous category boundaries.
- A five-way hate taxonomy (misinformation, stereotype, conspiracy, dehumanizing, non-factual) mapped to targeted counterspeech styles.
- A two-agent framework in which sub-2B agents obtain specialization from a contrastively-trained retrieval memory instead of fine-tuning, cutting peak VRAM 75% against monolithic 8B baselines at comparable latency.
- Component ablations isolating what each part buys, with the analyst agent the largest contributor (36.0% Factual Score, 27.7% Category Accuracy).

## Method

Counterspeech generation is formulated as conditional generation of a reply c together with latent auxiliary variables Z = category x target group x reasoning trace x search query x evidence, from hate speech h alone. Two agents, both Qwen3-1.7B and neither fine-tuned: a Hatespeech Analyst identifies type, target and reasoning and triggers a web search when factual claims are detected; a Counterspeech Generator writes the reply from those outputs plus retrieved examples and evidence. Specialization comes entirely from a memory module -- every annotated training instance contributes a record, and a 22M encoder trained with a supervised contrastive loss (temperature tau, positives = same hate type) maps hate speech to embeddings so that same-type instances cluster; at inference the top-k most similar entries within each hate type give a type-level score. The accompanying dataset, FactualCS, has 4,784 instances annotated by six annotators through a 500-instance pilot, disagreement adjudication, and formalised guidelines covering the boundaries the pilot found hardest (stereotype versus misinformation, dehumanizing versus other non-factual hate).

## Results

Across 28 baseline configurations, FIRE is best on nine of thirteen metrics. Semantic: BERTScore 0.886, METEOR 0.247, CoSIM 0.574, with ROUGE-1 0.294, ROUGE-2 0.071, ROUGE-L 0.197. Safety and quality: Toxicity 0.016 (11.1% lower than the best baseline), Repetition Rate 0.118 (7.1% lower), Novelty 0.730 (9.1% higher), Diversity 0.873 (1.3% higher). Strategy and factuality: Category Accuracy 0.702 (11.1% higher), Factual Score 0.969 (12.2% higher). Efficiency: sequentially activating two 1.7B agents cuts peak VRAM by 75% (about 4GB against about 16GB for monolithic 8B models) at comparable end-to-end latency. Ablations: removing web search drops Factual Score 0.969 -> 0.832 (-14.1%) and Category Accuracy to 0.664; removing memory drops Category Accuracy to 0.599 (-14.5%) and CoSIM 0.574 -> 0.490 (-14.6%), with Repetition Rate rising 0.118 -> 0.152; removing the Hatespeech Analyst -- a single pass with the same tool and memory access -- costs 36.0% Factual Score and 27.7% Category Accuracy, the largest effect of any component. Human study: 30 expert annotators ranked paired responses on four criteria, with FIRE win rates of 0.86-0.93 against LLaMA-3.1-8B-Instruct (SFT), 0.94-0.97 against HiPPrO, and 0.96-0.98 against CoARL.

## Limitations

Noticed by the reader, as the paper states no limitations section in the body read: (a) all baseline comparisons involve a system with web-search access against baselines whose access is not described as equivalent, and the ablation shows search alone is worth 14.1% of Factual Score, so part of the headline factuality gain may be a tooling difference rather than a framework one; (b) Factual Score, Category Accuracy and the other automatic metrics are computed against FactualCS annotations produced by the same authors, so the evaluation and the training signal share a definition of the five categories; (c) the human study samples one seed with 30 annotators and reports win rates without agreement statistics or confidence intervals; (d) the memory holds every annotated training instance, so 'not fine-tuned' understates the dependence on labelled data -- specialization is moved from weights into a retrieval index built from the same annotations; (e) both agents are the same 1.7B checkpoint, so no result separates multi-agent decomposition from simply running two passes; (f) the ethics statement acknowledges that generated counterspeech may misconvey intended meaning and that no fully operational counterspeech system exists, which bears on deployment claims.

## Why it matters here

- **overthinking**: Does not bear on the topic. The paper entered the archive on the keywords 'efficient reasoning' and 'reasoning trace', but its efficiency axis is memory footprint -- two sequentially activated 1.7B agents holding about 4GB peak VRAM against about 16GB for a monolithic 8B model, at comparable latency -- not the length of a reasoning trajectory. The reasoning trace here is an annotated field in a dataset used to ground generation, not an object whose length is measured or controlled. Nothing measures tokens spent, no budget is varied, and no accuracy-efficiency tradeoff in the archive's sense is reported. Treat as a scoring false positive: 'efficient reasoning' is a phrase the topic's keyword list cannot distinguish between compute-per-parameter efficiency and reasoning-length efficiency, and this is the former.

## Entities

- **Concepts**: Multi-Agent Decomposition, Retrieval Memory, Supervised Contrastive Learning, Evidence Grounding, Counterspeech Generation, Hate Category Taxonomy, Tool-Augmented Generation
- **Methods**: FIRE (Factuality Informed Multi-Agent REasoning Framework), Supervised contrastive encoder training, Top-k type-level retrieval, Web search tool invocation, CoARL, HiPPrO, DialoGPT, GPS
- **Datasets**: FactualCS (4,784 instances, introduced here)

Tags: `counterspeech`, `hate speech`, `multi-agent`, `retrieval memory`, `evidence grounding`, `small models`, `off-topic`

## Abstract

Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

---

Record id: `arxiv:2608.23152`
