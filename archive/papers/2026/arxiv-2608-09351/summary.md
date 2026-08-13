<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute

- **Authors**: Nikita Kozodoi, Zainab Afolabi, Jack Butler
- **Venue**: cs.LG
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09351>
- **PDF**: <https://arxiv.org/pdf/2608.09351v1>
- **Topics**: test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-training 0.25, test-time-scaling 0.57

## In one line

Asks whether a fixed inference budget buys more accuracy spent on varying the input than on varying the reasoning path, and finds paraphrase aggregation beats self-consistency on five of six benchmarks at matched compute.

## Problem

Every established test-time scaling method spends its budget on the output side -- self-consistency, Tree of Thoughts, self-refine all re-run the model on the same input. Input-side diversity draws on the same budget and is a direct competitor for where each additional inference call should go, but prior work applies rephrasing to one narrow task at a time and none benchmarks it against self-consistency at matched compute. What matters in deployment is accuracy per unit of compute, and that comparison had not been made.

## Contributions

- A matched-compute comparison of input-side against output-side diversity across six benchmarks and four task types
- Semantic TTA (paraphrase aggregation) shown to Pareto-dominate self-consistency on cost-effectiveness, with statistically significant gains
- Ablations over augmentation count, multi-modal strategies and base-model scale, locating the regime where the extra compute pays

## Method

Given a query and a model, TTA generates k transformed versions of the input, answers each independently, and majority-votes. Three augmentation strategies are compared against chain-of-thought prompting and self-consistency, all decoding at T = 0.75 from the same CoT template so only the diversity source differs. Semantic TTA prompts a model to produce k meaning-preserving rephrasings in a single call -- keeping augmentation overhead small relative to the k answer calls -- with explicit instructions to preserve answer choices, formatting requirements and image references so every variant stays answerable. Lexical TTA applies character-level noise instead: random swaps within words, insertions and deletions, and injected typos, at 5% probability per word capped at 10 perturbations, which needs no extra call and is therefore nearly free. Visual TTA perturbs the image while leaving the question fixed, with small-angle rotation and brightness and contrast shifts. The comparison is designed so semantic TTA is a strict extension of self-consistency -- it also samples at T = 0.75, so each answer carries the same output-side diversity plus input-side diversity on top, and any improvement at matched k is attributable to varying the input. Evaluated on MMLU, MMMLU (14 languages), MMMU, HLE, Math500 and IMDB Reviews, 400 randomly sampled examples each, with Claude 4.5 Haiku as the base model, k selected by grid search over {2, 4, 6} on a held-out sample disjoint from the evaluation subset, and Math500 answers checked by normalized string match followed by SymPy symbolic equivalence.

## Results

Semantic TTA gives the largest mean gain over single-call CoT at 1.80 percentage points, against 1.21 for lexical TTA and 0.92 for self-consistency, and beats self-consistency on five of six benchmarks. Per benchmark, semantic against self-consistency: MMMLU +2.75 vs +1.25 (CoT baseline 79.8%), Math500 +2.53 vs +1.01 (89.6%), MMMU +2.01 vs +1.01 (66.1%), MMLU +1.75 vs +1.50 (87.8%), HLE +0.75 vs -0.25 (3.0%), and IMDB where all three methods give exactly +1.00 on a 94.5% baseline. Paired t-tests over the pooled per-question gains put semantic TTA above single-call CoT at p < 0.01 and above self-consistency at p < 0.05, with a non-parametric bootstrap over n = 2,400 giving a 95% interval of [+0.88, +2.71] pp; lexical TTA beats CoT at p < 0.01 but its edge over self-consistency is only p = 0.058, and it is not distinguishable from semantic TTA at the 5% level. On cost, semantic TTA achieves the highest accuracy gain per extra dollar (133.11 pp) and per extra LLM call (0.403 pp) against self-consistency's 91.81 and 0.209. The augmentation-count result is the one that bears on the archive: semantic TTA peaks at k = 4.33 on average and, on Math500 extended to k = 10, peaks at k = 5 with diminishing returns after, while self-consistency keeps improving all the way to k = 10 and nearly catches semantic TTA there. Accuracy is non-monotone in k for both, with the paper attributing the dips to stochastic paraphrase generation and to odd-versus-even tie-breaking.

## Limitations

The paper is unusually direct about scope: it states that gains of 1-2 pp may not justify a 2-6x cost increase, and that TTA is most valuable when baseline accuracy is moderate (40-80%). Two of its six benchmarks fall outside that band and show it -- IMDB at 94.5% where all three methods return an identical +1.00, and HLE at 3.0% where a +0.75 pp gain on 400 examples is three questions. What a reader should add: the main results use one base model, so 'input diversity beats output diversity' is established for Claude 4.5 Haiku and the model-scale section is an ablation rather than a replication. The 1.8x cost-effectiveness figure in the abstract is not either of the two ratios the figure reports -- accuracy per dollar is 1.45x and per LLM call is 1.93x -- so the headline number should be traced to the intended denominator before quoting. k is chosen per dataset and method by grid search, which is the right protocol but means the reported k differs across arms of the comparison. And the crossing at k = 10 on Math500 undercuts the framing more than the paper says: if self-consistency catches up given enough samples, input diversity is buying convergence speed rather than a higher ceiling, which is a different claim from the one in the title.

## Why it matters here

- **test-time-scaling**: Sits directly against an archived result that a perturbation-based selection rule's apparent 31.8-point gain over majority voting in vision-language scaling was a decoding-format effect, recovered by a control spending the same short-answer budget on the unperturbed image. This paper runs the matched-compute comparison that one demanded and reports a real but much smaller input-side gain -- 1.80 against 0.92 mean pp -- which is what the archive should expect once the format confound is removed. It also refines the standing finding that extra samples strengthen whatever the aggregation rule already does: here the aggregation rule is unchanged and only the input varies, and the benefit saturates at k = 5 while self-consistency keeps climbing to k = 10, so input diversity reduces variance faster without raising the ceiling.

## Entities

- **Concepts**: test-time augmentation, input diversity, output diversity, [prompt sensitivity](../../../../wiki/concepts/prompt-sensitivity.md), matched compute, cost-effectiveness, variance reduction, answer aggregation
- **Methods**: [self-consistency](../../../../wiki/methods/self-consistency.md), [majority voting](../../../../wiki/methods/majority-voting.md), [chain-of-thought prompting](../../../../wiki/methods/chain-of-thought-prompting.md), paraphrasing, [test-time scaling](../../../../wiki/methods/test-time-scaling.md)
- **Datasets**: [MMLU](../../../../wiki/datasets/mmlu.md), MMMLU, MMMU, HLE, [MATH500](../../../../wiki/datasets/math500.md), IMDB Reviews

Tags: `test-time-scaling`, `augmentation`, `self-consistency`, `cost-efficiency`, `multimodal`

## Abstract

Test-time scaling improves LLM accuracy but multiplies inference cost, making the accuracy gained per unit of compute the metric that matters in deployment. Self-consistency is one of the established approaches, which spends this budget entirely on the output side by sampling repeated reasoning paths. We study Test-Time Augmentation (TTA), which extends self-consistency by also perturbing the input, aggregating predictions across transformed versions of the input, and ask whether input-side diversity converts compute into accuracy more efficiently than output-side diversity. We perform a systematic, matched-compute comparison: we evaluate three simple input-side strategies (semantic rephrasing, lexical perturbations, and visual transformations) across six datasets covering general and multilingual knowledge, mathematical reasoning, multi-modal question answering, and sentiment classification, against chain-of-thought prompting and self-consistency. Semantic rephrasing delivers consistent and statistically significant accuracy gains while Pareto-dominating self-consistency on cost-effectiveness, delivering roughly 1.8X more accuracy per dollar and outperforming it on five of six tasks. We further analyze the number of augmentations, multi-modal strategies, and base model scaling, finding that TTA is most cost-effective for mid-tier models where a stronger model is unavailable or too expensive. Our findings indicate that for current mid-tier LLMs, varying the input converts inference compute into accuracy more efficiently than varying the reasoning path alone. The TTA implementation is available at https://github.com/aws-samples/sample-genai-reflection-for-bedrock.

---

Record id: `arxiv:2608.09351`
