<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Real-Time Visual Attribution Streaming in Thinking Model

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/62671>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

vStream trains a lightweight linear estimator to predict counterfactual ablation effects of image regions from cached attention features, so a multimodal reasoning model's visual grounding can be displayed while it reasons rather than recomputed afterwards, at 0.024 s per 10 tokens against 1.9-2.8 s for causal baselines.

## Problem

Multimodal thinking models generate long reasoning traces over an image — writing code from a screenshot, solving an image-based math problem — and those traces are supposed to be grounded in visual evidence. Verifying that they are is the difficulty. Faithful causal attribution methods require repeated backward passes or input perturbations, which cost seconds per token span and scale linearly with trace length, so they run only after generation and fail on long traces. Raw attention maps are available instantly but carry no causal guarantee that the attended region is what the output depends on. The paper notes that as chains grow longer, reasoning models increasingly lean on language priors rather than visual evidence, so without a usable verification tool the interpretability that a visible reasoning trace seems to offer is unverified.

## Contributions

- An amortized formulation of visual attribution: learn once to predict counterfactual ablation effects from attention features, instead of recomputing causal attribution per query with backward passes or perturbations.
- Semantic region unitization via agglomerative clustering over DINOv3 features, attributing to 16-128 coherent regions rather than pixels or patch tokens.
- A linear estimator with only L x H parameters trained on about 2,000 examples to maximize Pearson correlation with attention-masking ground truth.
- Streaming attribution with asynchronous attention caching, so grounding evidence is shown while the model reasons rather than after it finishes, with overhead constant in trace length.
- Evaluation across five task categories and four thinking models showing LDS comparable to exhaustive causal baselines (0.70-0.72 vs 0.64-0.71) at 0.024 s per 10 tokens versus 1.9-2.8 s, up to 117x faster.
- Cross-task generalization measurements showing 75-90% retention and full recovery from mixed-category training.

## Method

vStream is an amortized attribution framework with four parts. Semantic region unitization: the image is partitioned into K disjoint semantically coherent regions (typically 16-128) covering objects, text and background, by agglomerative clustering over DINOv3 self-supervised features, so attribution targets regions rather than pixels or patch tokens. Attention feature extraction: for each (reasoning span, region) pair, cross-attention weights are pooled over the span and the region across all 32 layers and 36 heads, producing a 1,152-dimensional feature vector. Linear amortized estimator: a linear model with only L x H parameters is trained on about 2,000 examples to predict the counterfactual ablation effect from those attention features, with ground truth obtained by attention masking and the objective being to maximize Pearson correlation between predictions and targets. Streaming inference: attention is cached asynchronously during generation and attributions are computed in parallel with token generation, with spatial refinement from DINO attention maps, so attribution is emitted alongside the trace at near-zero added overhead. The design point is that faithfulness is learned once, offline, instead of being recomputed per query by brute force.

## Results

Evaluated on four multimodal thinking models — Qwen3-VL-8B-Thinking, GLM-4.1V-9B-Thinking, MiMo-VL-7B, Cosmos-Reason1-7B — over five task categories: math (MathVista, MathVerse, OlympiadBench), science (ScienceQA, AI2D), document (DocVQA, ChartMimic), code (WebSight) and general (GQA, COCO, ReferIt). Faithfulness by Linear Datamodeling Score averages 0.72 for Qwen3-VL and 0.70 for each of the other three, against 0.64-0.71 for gradient- and perturbation-based baselines; predicted versus actual ablation effects reach R^2 = 0.65. Top-5 log-probability drop is 0.98-1.02 across models. Latency per 10 tokens: vStream 0.024 +/- 0.002 s, versus TAM 1.90 +/- 1.13 s, AttnLRP 2.60 +/- 1.04 s and InputGrad 2.80 +/- 1.06 s — reported as up to 117x speedup, and vStream's overhead is constant in trace length while the baselines grow linearly and hit out-of-memory on extended reasoning. Cross-task transfer retains 75-90% of in-domain performance (in-domain LDS 0.70-0.74) for most category pairs, and training on a mixture recovers the full 0.72. The estimator saturates at about 2,000 training examples, roughly 4.5 hours on a single GPU, with 1,000 examples already giving over 90% of peak.

## Limitations

Stated: ambiguity in visual references, where a model cites the correct object while attending elsewhere; hallucination and disconnected reasoning, where the model produces a plausible narrative with no actual visual support; degraded performance on dense text and small objects needing fine-grained attribution; inability to ground purely symbolic reasoning steps that have no visual anchor; dependence on model architecture, since an estimator trained on one architecture may not transfer to a substantially different design; and degradation under feature distribution shift beyond the training domain. Beyond the stated: the ground truth the estimator is trained and scored against is attention masking, so the reported faithfulness measures agreement with one particular ablation operator rather than with the model's true causal dependence, and R^2 = 0.65 means roughly a third of the variance in ablation effect is unexplained. The linear estimator also requires a per-model training run, so the 4.5 GPU-hours is a per-architecture cost rather than a one-off.

## Why it matters here

- **overthinking**: Tangential. The paper matched on 'thinking model' and does operate on multimodal reasoning models with long traces, but it proposes no method for controlling reasoning length and does not treat reasoning length as a cost to be managed. Its efficiency claims — 0.024 s versus 1.9-2.8 s per 10 tokens, 117x, constant rather than linear overhead — are about the cost of computing an attribution over a trace, not about the cost of producing the trace, so they should not be filed alongside test-time compute results. One observation does bear on the topic and is worth keeping: the authors motivate the work by noting that as reasoning traces extend to thousands of tokens, models increasingly rely on language priors rather than visual evidence, and that baseline causal attribution methods run out of memory on extended reasoning. That is a claim about a failure mode of long reasoning — drift away from the evidence as the trace grows — and if the group wants to study whether extra thinking degrades grounding rather than merely costing tokens, a per-span grounding measure that is cheap enough to run over a whole long trace is the instrument that would make the question answerable. The paper does not itself run that experiment, and nothing here is evidence about the accuracy/length tradeoff. Keep as a methods pointer, not as a result for this topic.

## Entities

- **Concepts**: Visual attribution, Amortized explanation, Faithfulness, Counterfactual ablation, Attention as a feature signal, Multimodal thinking models, Streaming interpretability, Language-prior drift in long reasoning traces
- **Methods**: vStream, amortized attribution, semantic region unitization, DINOv3 features, agglomerative clustering, linear amortized estimator, attention masking ablation, Linear Datamodeling Score, InputGrad, AttnLRP, TAM, Qwen3-VL-8B-Thinking, GLM-4.1V-9B-Thinking, MiMo-VL-7B, Cosmos-Reason1-7B
- **Datasets**: [MathVista](../../../../wiki/datasets/mathvista.md), [MathVerse](../../../../wiki/datasets/mathverse.md), [OlympiadBench](../../../../wiki/datasets/olympiadbench.md), [ScienceQA](../../../../wiki/datasets/scienceqa.md), [AI2D](../../../../wiki/datasets/ai2d.md), DocVQA, ChartMimic, WebSight, [GQA](../../../../wiki/datasets/gqa.md), COCO, ReferIt

Tags: `multimodal`, `visual-attribution`, `interpretability`, `faithfulness`, `attention`, `thinking-models`, `long-reasoning-traces`, `streaming`, `tangential`

---

Record id: `title:503ded235751878b`
