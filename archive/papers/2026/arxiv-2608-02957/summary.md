<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Inverted Detection and Control in Steering Vectors

- **Authors**: Max Torop, Aria Masoomi, Jennifer Dy
- **Venue**: cs.LG
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02957>
- **PDF**: <https://arxiv.org/pdf/2608.02957v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Finds directions that are highly discriminative for a concept and aligned with its positive examples yet reliably steer the model the opposite way, characterizes them geometrically as spoofing the concept's absence downstream, and turns that characterization into a training-free test that fixes the sign — improving a standard steering pipeline in 27 of 30 experiments.

## Problem

Steering vectors rest on the linear representation hypothesis: if texts exhibiting a concept are linearly separable from those that do not, then translating a representation toward the positive half-space should promote the concept and away from it should suppress. Detection and control are thereby assumed to be the same thing, and the assumption is what licenses picking a steering direction by its discriminability — which is exactly what the foundational method does when it selects the most discriminative attention heads. Prior work had noted anti-steerable examples, but treated them as input-specific failures attributed to spurious correlations and low discriminability, so nothing challenged the assumption for vectors that discriminate well.

## Contributions

- Identifying inverted-steering vectors: directions with high discriminability and strong alignment to positive examples that induce the opposite behaviour consistently in aggregate across inputs, rather than on a minority subset
- A definition that separates them from ordinary steering vectors by three measurable properties — discriminability, effect size, and the sign of the monotonic relationship between steer factor and concept score
- A geometric account: steering any discriminative direction spoofs the concept's presence in the steered head, but ordinary vectors spoof presence in downstream discriminative heads while inverted ones spoof absence
- The inner-product response and its summary, the representation response, with a concentration bound establishing that the quantity is reliably estimable from finite samples
- A resulting spoof score that classifies a direction from forward passes alone — no generation, no judge model, no ground-truth positive and negative responses — and a targeted sign flip that uses it to repair a detection-based steering pipeline

## Method

For an attention head, the steering vector is the mean-difference between positive-class and negative-class final-token head representations, and its discriminability is the area under the ROC curve of the inner product with that direction. A vector is classified by sweeping the steer factor over more than 40 values, pruning factors at which output degrades, and computing effect size together with the Spearman correlation between steer factor and concept score; a strongly negative correlation with a large effect marks an inverted vector. The geometric analysis steers one candidate head and records, at the final question token before any generation, how the inner product between downstream head representations and their own concept directions changes; normalized by the natural variability of that downstream quantity this gives the inner-product response, and its best linear coefficient in the steer factor gives the representation response. Averaging the latter over discriminative downstream heads yields the spoof score. The intervention modifies Inference Time Intervention: for the top-k most discriminative heads it normally steers, the sign is flipped for any head whose spoof score is negative. Three instruction-tuned models and five concepts are evaluated in a multiple-choice setting scored by logits and an open-ended setting scored by a judge model, on a single 48GB GPU.

## Results

Inverted vectors are systematic rather than incidental: three are mined per model-concept pair across 15 pairs, giving 45 alongside 45 ordinary ones, and they achieve high discriminability while showing strongly negative monotonicity — one example reaches an AUC of 0.97 with a Spearman correlation of -1 between steer factor and concept score. That combination is the paper's central claim, and it falsifies the working assumption directly: alignment with positive representations does not determine the sign of the steering effect. The spoof score separates the two classes from representation-level measurements alone, with an AUC of 0.91 and 81% accuracy at a threshold of zero, computed without training, generation or judge scoring. Applied as a sign correction to the standard pipeline it improves 27 of 30 experiments, with gains from 0.9% to 138%. The largest case is diagnostic of how bad the untreated failure is: on corrigibility in one model, the standard method's promotion score is 1.50 against an unsteered baseline of 1.75 — steering the concept moves it backwards — and the corrected version reaches 3.57. Improvements hold on both promotion and suppression across all behaviours in two of three models; in the third, 7 of 10 improve and the paper leaves the remaining three to further investigation rather than smoothing over them. The authors read this as an explanation for the variability in steering efficacy reported across model-concept pairs in prior work: some selected vectors were inducing the opposite of the intended effect.

## Limitations

The paper states its scope: it studies translation-based steering vectors specifically, in order to isolate the inverted phenomenon, and does not evaluate more complex or optimized steering pipelines, with affine and non-linear interventions named as future work. What a reader should add: the evidence covers three open models and five concepts, with vectors mined only from attention-head outputs, so whether the phenomenon appears at other steering sites is untested. The spoof-score classifier is 81% accurate at the natural threshold, which is useful but leaves roughly one head in five misclassified, and the three experiments that did not improve are unexplained. Concept scoring in the open-ended setting relies on a judge model, and degradation is controlled by a heuristic threshold rather than measured directly. The concentration bound is asymptotic in the usual sense and its assumptions — bounded head inputs, non-degenerate downstream variance — are argued to hold in practice rather than verified per case.

## Why it matters here

- **reasoning-interpretability**: This is the sharpest statement in the archive of a distinction it keeps needing: what a direction detects and what intervening on it does are separate facts, and here they come apart in sign, not merely in magnitude. A vector with AUC 0.97 for a concept — near-perfect detection — moves the model away from that concept when pushed toward it. That is a stronger version of the archive's cultural-decoding result, where a probe reads what generation does not emit, and of the vision-language audit where a signal provably tracks the image and still buys nothing at the selection layer. Read together the three say that discriminability licenses no causal claim at all. The methodological contribution is equally transferable and cheap: the representation response measures what an intervention does to downstream representations from forward passes alone, at the final token before generation, with no judge and no labelled responses. That is a way to check an intervention's direction before spending anything on generating and scoring text — which the archive's other steering and probing work does not do, and which the 138% case shows is not optional.

## Entities

- **Concepts**: [steering vector](../../../../wiki/concepts/steering-vector.md), [linear representation hypothesis](../../../../wiki/concepts/linear-representation-hypothesis.md), detection versus control, [representation versus readout](../../../../wiki/concepts/representation-versus-readout.md), linear probe, [causal intervention](../../../../wiki/concepts/causal-intervention.md), [attention head](../../../../wiki/concepts/attention-head.md), concept direction, representation response, activation steering
- **Methods**: inverted-steering vector, Inference Time Intervention, ITI-RRF, [activation steering](../../../../wiki/methods/activation-steering.md), mean-difference probe, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), [contrastive activation addition](../../../../wiki/methods/contrastive-activation-addition.md)
- **Datasets**: [TruthfulQA](../../../../wiki/datasets/truthfulqa.md), Model-Written Evaluations

Tags: `steering vectors`, `interpretability`, `activation steering`, `causal intervention`, `control`

## Abstract

Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-control phenomenon in which some highly discriminative SVs that are aligned with positive representations can consistently promote the opposite behavior. We refer to such vectors as inverted-steering vectors (ISVs). We provide a geometric characterization of ISVs' effects, finding that steering along these directions systematically pushes representations in discriminative downstream heads as if the concept were absent, even prior to decoding. Motivated by this analysis, we propose an approach for distinguishing ISVs without requiring generation or associated response scoring. This enables targeted sign flips, which we use to improve a foundational detection-based steering pipeline via Inference Time Intervention (ITI). Our approach improves results in 27/30 experiments, ranging from +0.9% to +138%. We evaluate our findings on Gemma 3 12B, Qwen 2.5 14B, and Olmo 3 7B across 5 concepts.

---

Record id: `arxiv:2608.02957`
