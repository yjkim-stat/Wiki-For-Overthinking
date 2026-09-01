<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Understanding LLM Reasoning for Abstractive Summarization

- **Authors**: Haohan Yuan, Haopeng Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.859/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.859.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.859
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## In one line

The first large-scale, systematic evaluation of 8 reasoning prompting strategies (across augmentation, organization, reflection paradigms) and 3 Large Reasoning Models on abstractive summarization across 8 datasets finds reasoning is not a panacea for this task -- there is a statistically significant quality-faithfulness trade-off, and increasing an LRM's internal reasoning budget does not reliably improve, and can actively reduce, factual consistency.

## Problem

Reasoning has substantially improved LLMs on analytical tasks (math, code generation, logical inference), but its value for abstractive summarization -- a fundamentally different task requiring information compression rather than derivation -- remains largely assumed rather than proven, and no prior systematic study has evaluated a broad range of reasoning strategies and models across diverse summarization settings.

## Contributions

- the first large-scale, systematic evaluation of reasoning strategies (8 prompting methods across three paradigms, plus 3 LRMs) applied to abstractive summarization across 8 diverse datasets and multiple evaluation dimensions
- identification of a statistically significant quality-faithfulness trade-off: explicit reasoning strategies tend to improve reference-based quality at the cost of factual faithfulness, while implicit LRM reasoning shows the opposite pattern
- evidence that LLM-as-judge (G-Eval) systematically overestimates faithfulness relative to human evaluation and underweights the completeness-conciseness trade-off, cautioning against relying solely on LLM judges for faithfulness assessment in summarization
- demonstration, via both a GPT-5 'think ability' ablation and a cross-model Gemini 2.5 Flash thinking-budget validation, that increasing internal reasoning depth does not reliably improve summarization and can actively reduce factual faithfulness (over-thinking as creative gap-filling rather than faithful compression)

## Method

Establishes a unified evaluation framework covering three reasoning paradigms and 8 explicit prompting strategies: Augmentation-based (CoT, Extract-to-Abstract/E2A, Question-Answer-Guided/QAG, Cited-Summarization/Cite), Organization-based (Decomposition/Deco, Plan-then-Write/Plan), and Reflective (Iterative-Refine/IR, Self-Consistency/SC, adapted with a rubric-based judge for summarization), each formalized as generating an augmentation/organization/reflection signal that conditions the final summary generation. Benchmarks these explicit methods (applied to GPT-4.1) against a Vanilla single-pass baseline and against three Large Reasoning Models (o1, o3, GPT-5) that reason implicitly and internally rather than via explicit prompting. Evaluates across 8 datasets spanning four task-type/domain groups (Short-Form: CNN/DM, SAMSum, Reddit, WikiHow; Long-Form: ArXiv, Multi-News, BookSum; Table-to-Text: SciGen), using 100-instance subsets per dataset, in both 0-shot and 2-shot settings. Metrics span reference-based quality (ROUGE, BERTScore), factual faithfulness (SummaC, AlignScore), LLM-as-judge (G-Eval: completeness, conciseness, faithfulness), and a human evaluation using the same rubric as G-Eval to check LLM-judge calibration. Additionally runs a controlled ablation varying GPT-5's internal 'think ability' hyperparameter (reasoning depth) on three representative datasets, and a separate controlled validation on Gemini 2.5 Flash varying its internal thinking-token budget directly, to test whether the same trend generalizes beyond the GPT model family.

## Results

Reasoning is not a panacea: a simple Vanilla prompt often matches or surpasses complex reasoning strategies, particularly in the 2-shot setting, where Vanilla becomes highly competitive against every explicit method for reference-based quality; explicit reasoning's advantage on ROUGE/BERTScore largely disappears once a few in-context examples are provided. A statistically significant quality-faithfulness trade-off is found (BERTScore vs. AlignScore correlation r=-0.685, p=0.014): explicit reasoning methods (SC, IR, QAG, Plan, CoT) cluster in a high-BERTScore (85-86)/low-to-mid-AlignScore (60-62) region, while LRMs cluster in a lower-BERTScore (82-84)/higher-AlignScore region, with GPT-5 at the extreme (highest faithfulness); Vanilla is a notable outlier, achieving both strong BERTScore and above-average AlignScore. SC and IR achieve the best reference-based summary quality across most settings (SC leads on short-form datasets like CNN/DM and SAMSum; IR performs best on long-form datasets like ArXiv and Multi-News), while LRMs (especially GPT-5) achieve the highest factual faithfulness overall, with the advantage clearest on long-form datasets. On table-to-text (SciGen), AlignScore approaches 98-100% across nearly all methods since structured tabular inputs make factual alignment easy to satisfy by construction; explicit methods like SC and IR lose faithfulness specifically when given 2-shot examples, while LRMs stay stable or slightly improve. LLM-as-judge (G-Eval) systematically overestimates faithfulness relative to human evaluation (G-Eval scores cluster 4.96-4.99 near-perfect across all systems, while human ratings range 3.98-4.42 and are far more discriminating) -- e.g. G-Eval rates GPT-5 and E2A nearly identically (and even slightly favors E2A), while humans rate GPT-5 substantially higher in faithfulness (4.42 vs. 3.98), and human evaluation reveals a clear completeness-conciseness trade-off G-Eval partly captures but underweights (GPT-5 is most complete/faithful but least concise at 3.17; E2A is most concise but loses content, 2.77 completeness). Summary abstractiveness is negatively correlated with both reference-based quality and factual faithfulness: Vanilla and Reflective methods are least abstract and achieve the highest ROUGE; Organization-based methods (Deco, Plan) are the most abstract and perform worst on both metrics; a qualitative case study shows Deco's chunk-based decomposition can over-generalize a document-specific conditional rule (applying a cooking-length instruction meant for one vegetable-cutting context to all pieces) while E2A's extraction bottleneck can omit a final necessary procedural step -- concrete evidence that reasoning pipelines fragmenting or filtering context risk having the model fill non-existent logical gaps or omit important information. Increasing internal reasoning depth does not reliably help and risks over-thinking: as GPT-5's 'think ability' hyperparameter increases, factual faithfulness (AlignScore, and more mildly SummaC) consistently declines while reference-based quality metrics stay stable, interpreted as the LRM 'over-thinking' -- generating creative gap-filling or elaboration instead of maintaining faithful compression of the source; the controlled Gemini 2.5 Flash validation (varying internal thinking-token budget directly rather than a qualitative 'think ability' setting) confirms this is not GPT-family-specific: increasing the thinking budget does not consistently improve any metric, and on ArXiv, ROUGE drops from 0.2284 at budget=0 to 0.1954 at budget=1024, with the best ROUGE on CNN/DM and SciGen achieved at a middle budget (256) rather than the largest one.

## Limitations

Evaluation uses 100-instance subsets per dataset rather than full test sets, a deliberate trade-off for breadth (8 datasets x 8 strategies x 3 LRMs) that the authors flag as needing verification on full splits in future work. The study focuses on English summarization; extension to multilingual or specialized-domain (legal, biomedical, clinical) settings is left to future research. Experiments use the GPT model family (GPT-4.1, o1, o3, GPT-5) as the primary testbed to control for confounding architectural/training differences, restricting fine-grained inspection of internal reasoning processes since these are closed-source APIs -- the paper's account of 'internal reasoning' relies on observed output behavior rather than internal mechanisms (e.g. attention weights), and verifying the same patterns on open-weight models is named as a valuable extension (partially addressed here by the separate Gemini 2.5 Flash validation, but that too is closed-source). Human evaluation, while used to validate automated-metric trends, does not scale to the full benchmark's size due to annotation cost. Resource-heavy reasoning strategies (QAG, SC, IR) require multiple generations, inherently trading inference cost for quality, and the paper does not conduct a fine-grained latency/cost analysis of this trade-off.

## Why it matters here

- **overthinking**: Core paper for this topic despite being outside the archive's usual math/code focus: it explicitly frames its central negative finding as a 'risk of over-thinking' and provides direct, controlled evidence (via two separate reasoning-budget ablations on two different model families) that more internal reasoning does not reliably improve task performance and can actively harm factual faithfulness -- extending the archive's overthinking-and-accuracy findings to a fundamentally different task domain (compression rather than derivation) where the failure mode manifests as creative gap-filling and hallucination rather than wasted tokens on a solved problem. Its finding that LLM-as-judge evaluation systematically overestimates faithfulness relative to humans is also methodologically important for any overthinking study relying on LLM-judged quality metrics.

## Entities

- **Concepts**: quality-faithfulness trade-off, over-thinking in summarization (creative gap-filling), explicit vs. implicit (in-model) reasoning, summary abstractiveness
- **Methods**: Chain-of-Thought (CoT), Extract-to-Abstract (E2A), Question-Answer Guided (QAG), Cited Summarization (Cite), Decomposition (Deco), Plan-then-Write (Plan), Iterative Refine (IR), Self-Consistency (SC, rubric-based selection), Vanilla (baseline)
- **Datasets**: CNN/DM, SAMSum, Reddit (TIFU), WikiHow, ArXiv, Multi-News, BookSum, SciGen

Tags: `overthinking`, `summarization`, `factual-faithfulness`, `reasoning-strategies`, `quality-faithfulness-tradeoff`

## Abstract

Reasoning has substantially improved Large Language Models (LLMs) on analytical tasks such as mathematics and code generation, but its value for abstractive summarization remains unclear. To address this gap, we adapt general reasoning strategies to the summarization setting and conduct a large-scale comparative study of 8 reasoning strategies and 3 Large Reasoning Models (LRMs) across 8 diverse datasets, evaluating both summary quality and factual faithfulness. Our results show that reasoning is not a universal solution and its effectiveness depends strongly on the strategy and the summarization setting. In particular, we find a trade-off between summary quality and factual faithfulness. Explicit reasoning strategies often improve reference-based quality, but may weaken factual grounding, whereas implicit reasoning in LRMs shows the opposite tendency. We further find that increasing an LRM’s internal reasoning budget does not reliably improve summarization and can even reduce factual consistency. These findings suggest that, for summarization, more reasoning is not always better. Effective reasoning should preserve faithful compression rather than induce over-elaboration.

---

Record id: `doi:10.18653/v1/2026.findings-acl.859`
