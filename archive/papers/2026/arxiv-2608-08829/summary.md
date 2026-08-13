<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models

- **Authors**: Muhammad Faishal Adly Nelwan, Alfan Farizki Wicaksono
- **Venue**: cs.CL
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08829>
- **PDF**: <https://arxiv.org/pdf/2608.08829v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.57

## In one line

Shows that which layers a steering vector should be injected at is a property of the individual input rather than of the task, that a greedy per-input rule reaches the exhaustive optimum for structural reasons, and that a label-free predictor trained to imitate that rule recovers most of the oracle at deployment.

## Problem

Activation steering fixes its injection layers globally per behaviour and treats the remaining choices -- which layers, and how many -- as configuration. Both are hard for the same reason: the right answer depends on the input. A global layer set leaves gains unrealised on the instances where steering has room to act, and at higher layer counts it over-steers the saturated ones into fluency collapse. Per-instance selection has a catch that makes it look undeployable: every method that can find the best layers scores candidate subsets by steered forward passes judged against the gold answer, which does not exist at inference.

## Contributions

- A per-instance oracle over layer subsets establishing that the best layers change from input to input, with a permutation control
- A structural account of why a greedy top-K-by-single-layer-effect rule matches the exhaustive joint optimum: near-collinear mid-band vectors, negligible synergy, and padding
- A label-free deployable recipe -- a prompt-embedding layer ranker, a direction classifier, and an adaptive gate on how many layers to steer
- A mechanistic reading, direction over magnitude, that unifies global-rule corruption, high-K collapse, an unflippable ceiling and a cross-model dissociation

## Method

Steering follows contrastive activation addition with last-token injection at every generation step across a selected subset of layers. Three gold-aware references bracket what selection can achieve: an exhaustive per-instance oracle enumerable to three layers, a greedy per-instance rule that takes the layers of largest individual effect, and an in-sample global oracle that picks the best fixed set per cell and applies it unchanged to every input. None is deployable, because all score candidates against the gold answer; they serve as ceilings and as the training target. The deployable recipe replaces each with something label-free. Ranking is a single-hidden-layer network over a 25-dimensional PCA of an unsteered prompt embedding, trained listwise to reproduce each training input's distribution of per-layer effects, so one embedding pass yields the ranking. Direction is inferred by a logistic regression on the same features, which orients the push rather than sizing it and costs no extra forward pass. Depth is decided by an adaptive gate that walks the ranked prefix from one layer upward, scores each step's short steered pass against the inferred direction, and halts on a lift plateau, a floor on the yes/no mass, or an abrupt mass drop -- with all six constants set a priori rather than tuned on the evaluation set. Evaluated on Llama-3-8B-Instruct and Aya-Expanse-8B over six binary persona traits, with the primary metric the shift in gold-answer probability under a restricted yes/no softmax and a secondary rationale-perplexity guard against over-steering. Inputs where the base model already assigns near-certainty are separated as saturated, and per-instance claims are read on the remaining steerable stratum.

## Results

The best layers are a property of the input: an input's own oracle layers beat those of a different same-sign input in all twelve cells. The greedy rule then matches the exhaustive joint optimum -- statistically indistinguishable on 15 of 24 configurations on the full test set, with the oracle's margin at or below about 2.6 points everywhere and under one point on most cells -- and the paper explains why rather than reporting it as luck. The layers that carry effect sit in a narrow mid-band whose vectors are near-collinear (mean pairwise cosine 0.65 and 0.61, adjacent pairs 0.92), so neighbours substitute for one another; two-layer synergy is a few thousandths of the metric against single-layer effects two orders larger, and correlates *negatively* with vector cosine; and the exhaustive optimum pads a third of its three-layer picks on one model and 61 percent on the other with a do-nothing bottom layer, so joint search reaches for a third active layer only when one helps. Over-steering turns out to be dose-graded and extremely concentrated: of 942 severe events, 97 percent fall in a single trait-model cell, growing from 30 at three layers to 624 at five with a median perplexity inflation of 810 points. Attributing those events by selector, the global oracle carries 227 and the fixed-depth greedy rule 76, while each adaptively gated variant carries exactly one -- so the pathology belongs to a fixed aggressive dose, not to any particular picker. The deployable recipe recovers 93 percent of the exhaustive steerable lift on Llama-3-8B-Instruct and 65 percent on Aya-Expanse-8B, exceeds the gold-aware global oracle on five of six tasks on the first model despite having no labels, and never drives a trait-model cell below its unsteered baseline -- where the global rules do, on four cells and eight cells respectively. Counting behavioural flips on the generated answer, the per-instance rules corrupt no answer at any depth while the global oracle climbs from 12 corruptions at one layer to 249 at five, going net negative there. And the ceiling is stated plainly: of 206 strongly opposed inputs, 155 are flipped by no selector at all, the exhaustive oracle included.

## Limitations

The paper marks its own boundaries carefully, which is unusual and worth noting: the cross-model dissociation is called provisional and the magnitude gap explicitly not a precise figure, and the unflippable ceiling is presented as a limit of the static-coefficient steering paradigm rather than of the selector. What a reader should add is scope. The behaviour space is six persona traits posed as binary yes/no multiple choice, which is a narrow probe -- the primary metric is a two-way probability shift, and nothing here tests steering that must survive open-ended generation beyond a 200-token rationale used as a fluency guard. Two 8B models, and the two disagree enough that the headline recovery figure is 93 percent on one and 65 on the other, with the gap traced to 80 percent of the second model's inputs being saturated so that the prize per instance is smaller for any method. The gate's six constants are set a priori and a large configuration sweep places the deployed setting within about one point of the best, which is good practice, but the sweep is on the same corpus. Finally, the greedy rule's structural match to the joint optimum rests on the mid-band collinearity measured on these two models, and the paper is clear that this is what makes the oracle learnable -- so on an architecture whose effective layers were not near-substitutes, the whole argument would need re-establishing.

## Why it matters here

- **reasoning-interpretability**: Sharpens the archive's standing finding that a direction's quality as a detector says nothing about its effect as an intervention, by adding the axis nobody here had varied: *where* the direction is applied. The same vector at different layers produces effects that differ enough that an input's own layers beat another input's oracle layers in every cell, and the paper's summary -- direction over magnitude, meaning which layers carry the vector and hence which way the push points dominates how hard it is pushed -- means a steering result reported at a fixed layer is a measurement of that layer choice as much as of the direction. It also supplies the archive's first controlled account of over-steering: fluency collapse is content crowding rather than norm inflation, the final-layer residual norm stays flat while the output degenerates to a content-free attractor, and 97 percent of severe events fall in one trait-model cell. Read with the constrained-ablation entry from the same day, the two agree that safe steering is a selection problem -- one selects the direction, the other selects the site -- and neither is solved by the canonical direction.

## Entities

- **Concepts**: steering vector, layer selection, per-instance intervention, over-steering, fluency collapse, [detection versus control](../../../../wiki/concepts/detection-versus-control.md), saturation, Shapley value, sub-additivity
- **Methods**: [activation steering](../../../../wiki/methods/activation-steering.md), [contrastive activation addition](../../../../wiki/methods/contrastive-activation-addition.md), [logistic regression](../../../../wiki/methods/logistic-regression.md), [principal component analysis](../../../../wiki/methods/pca.md), listwise ranking, [beam search](../../../../wiki/methods/beam-search.md), adaptive gating
- **Datasets**: Anthropic Persona

Tags: `steering`, `interpretability`, `layer-selection`, `deployment`, `over-steering`

## Abstract

Activation steering edits the behaviour of a frozen language model by adding a learned vector to its residual stream, and current practice fixes the injection layers globally per task. We argue that the best layers are an instance-level decision, and we make per-instance, multi-layer selection both well understood and deployable. On two open-weight 8B models and six binary persona traits, a per-instance oracle over layer subsets shows that the best layers vary from one input to the next: on most trait-model pairs, no fixed global layer set recovers the per-instance benefit. A greedy rule that ranks layers by single-layer marginal effect recovers nearly all of the oracle's benefit, but both must score candidate layers against the gold answer, so neither can run at deployment; the rule instead becomes the target a prompt-only predictor is trained to reproduce. Our deployable recipe needs no label at inference: a per-instance layer ranker read off the prompt embedding, a classifier that infers the steering direction, and an adaptive gate that scores short steered passes against that inferred direction and steers no more layers than necessary. The recipe recovers most of the oracle's lift (the bulk on the stronger model, a clear majority on the harder one), never drives any trait-model pair below its unsteered alignment baseline on average, and largely avoids the fluency collapse that strong global selection incurs at higher layer counts. A mechanistic account, "direction over magnitude", explains the behavioural flip under a mis-directed global set, the output collapse from steering too many layers, and the ceiling of unsteerable inputs.

---

Record id: `arxiv:2608.08829`
