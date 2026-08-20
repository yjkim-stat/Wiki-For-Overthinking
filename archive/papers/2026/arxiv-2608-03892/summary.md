<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition

- **Authors**: Michal Mráz, Justin Shenk
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03892>
- **PDF**: <https://arxiv.org/pdf/2608.03892v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## In one line

Trains a difference-of-means direction on short- versus long-horizon answer continuations and steers along it, shifting binary temporal choices, moving the monetary indifference threshold on an untrained task by a factor of 56 at a ten-year delay, and changing a planning benchmark — with matched-norm random controls and an unusually candid account of what the direction may actually encode.

## Problem

Many deployed model outputs implicitly encode intertemporal preferences — advice about planning, finance, health, education and policy all trade near-term actions against delayed outcomes — and it is unclear whether that preference is a measurable internal quantity or an opaque side effect of pretraining and instruction tuning. The distinction matters for safety as well as for control: temporal preference is one ingredient in long-horizon planning and reward-seeking, and a model that internally optimizes over a different horizon than the one it presents to users would be hard to evaluate from outputs alone.

## Contributions

- A clean separation between readout and intervention, made explicit as a methodological commitment: probe accuracy is treated as evidence that the training contrast is linearly accessible, not as evidence that the direction isolates temporal horizon, and the intervention deliberately does not use the probe family that maximizes classification accuracy
- Two datasets crossing the same construct differently — one with overt time markers, one encoding horizon only through semantic contrasts — with the second used exclusively for cross-domain evaluation
- A generalization test on a structurally distinct task the direction was never trained on: monetary intertemporal choice with a quantitatively measurable indifference threshold
- An aggregate summary of that threshold, the area-equivalent indifference multiplier, defined as a log-axis average over sparse and unevenly sampled multiplier grids
- Matched-norm random-orthogonal controls at every layer, and residual-norm diagnostics reporting the intervention size relative to unsteered activations

## Method

For each temporal-choice question, short-term and long-term continuations are teacher-forced as two labelled examples, and the direction at a layer is the difference between the mean hidden states of the two classes, pooled over answer tokens. Comparison readouts — logistic regression, whitened logistic regression, and a whitened difference-of-means variant — are fitted on the same features for diagnostic purposes only. Steering adds a signed multiple of the normalized direction to the residual stream at the last prompt token and at every decode step, swept over seven layers spanning the middle-to-late part of a 64-layer model and over strengths from zero to plus or minus 128, with the perturbation norm therefore equal to the coefficient and the largest setting amounting to 36 to 63 percent of the unsteered residual norm. Three evaluations follow: held-out binary temporal choices with the two options presented in randomized order, a monetary grid of eight amount multipliers by twelve delays by eight scale factors that separates numeric proportions from absolute dollar amounts and uses day-count delay labels to avoid calendar semantics, and a real-world travel-planning benchmark scored by a commonsense constraint pass rate chosen because the benchmark's other metrics sit at ceiling or floor.

## Results

The construct is linearly accessible: probes reach 99.0 percent on the explicit holdout and 77 to 83.5 percent on the implicit set they were never trained on, with the difference-of-means family used for steering slightly the weakest classifier of the four — which the paper flags rather than hides, since it declines to pick the intervention by classification accuracy. Steering causally moves binary choices across every layer explored, with the proportion selecting the long-term option running from 0.33 to 0.82 on the explicit test set and 0.46 to 0.81 on the implicit one as the coefficient sweeps from negative to positive. The generalization result is the strongest in the paper: a direction trained only on binary temporal-horizon answers shifts monetary intertemporal choice on a task with a different format, moving the geometric-mean indifference multiplier from 2.67 unsteered to 8.34 under negative steering and 1.12 under positive at one layer, with the parsed later-choice rate moving from 54.7 to 36.3 and 80.4 percent. The effect is delay-dependent rather than uniform — the median ratio of negative-steer to positive-steer indifference across delays is 4.90, and at a ten-year delay it exceeds 56, so negative steering makes the model demand more than fifty-six times the delayed reward that positive steering accepts. On the planning benchmark the effect is real but non-monotonic and modest: moderate positive steering raises the commonsense pass rate above baseline while negative steering degrades it and the largest positive setting also degrades it, which the authors attribute to that magnitude pushing generation far enough off-distribution that coherence deteriorates. Matched-norm random orthogonal vectors produce smaller and inconsistently signed movement in both the binary and monetary experiments.

## Limitations

The limitations section is exemplary and should be read as part of the result. The construct-validity concern is stated first and is the sharpest: short-term and long-term continuations also differ in abstraction, urgency, strategic scope and proactive-versus-reactive framing, so if those correlated features dominate, the intervention is steering a broader short/long answer register rather than an isolated temporal-horizon variable — and the monetary transfer shows intertemporal preference is involved without identifying the direction's semantic basis. The intervention is large at the strongest settings, and residual-norm diagnostics calibrate its size without proving unrelated capabilities are preserved; the authors note that an intervention shifting time preference while degrading factuality or coherence would be unsafe rather than useful. Scope is one model family and size, a small set of prompt templates, and thinking-disabled decoding. No prompting baseline is reported, so it is unknown whether simply instructing the model to think short- or long-term produces similar changes. Matched-norm comparisons against the other probe families' steering directions are named as missing, so whether this direction is uniquely useful for intervention is open. And the planning evidence is called weaker than the monetary result because the aggregate metric is indirect and does not identify which checks change.

## Why it matters here

- **reasoning-interpretability**: This is the archive's steering caution applied correctly by the authors themselves, and the contrast with the inverted-steering result is instructive. Where that work shows discriminability licenses no claim about the sign of an intervention, this paper builds in the same separation from the start — probe accuracy is treated as evidence the contrast is accessible, the intervention deliberately does not use the best classifier, and matched-norm random-orthogonal controls are run at every layer. That is what the archive's randomized-control finding asks for, done in advance rather than in response. The generalization test is the strongest evidence type here: a direction trained on binary answer continuations moves a quantitatively measured indifference threshold on a task with a different format by a factor exceeding 56 at long delays, which is much harder to explain by surface features than a within-format effect. And the paper is candid that this does not identify what the direction encodes — short and long continuations differ in abstraction, urgency and framing as well as in horizon — which is exactly the confound this archive's probing results usually leave unstated. The non-monotonic capability result carries a practical warning: the same steering that improves a planning metric at moderate strength degrades it at large strength, so a steering effect measured at one magnitude does not extrapolate.

## Entities

- **Concepts**: [steering vector](../../../../wiki/concepts/steering-vector.md), linear probe, [detection versus control](../../../../wiki/concepts/detection-versus-control.md), [construct validity](../../../../wiki/concepts/construct-validity.md), activation steering, intertemporal preference, long-horizon planning, [causal intervention](../../../../wiki/concepts/causal-intervention.md), [randomized control](../../../../wiki/concepts/randomized-control.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md)
- **Methods**: [contrastive activation addition](../../../../wiki/methods/contrastive-activation-addition.md), [difference-of-means probe](../../../../wiki/methods/difference-of-means-probe.md), [logistic regression](../../../../wiki/methods/logistic-regression.md), [linear probe](../../../../wiki/methods/linear-probe.md), [activation steering](../../../../wiki/methods/activation-steering.md)
- **Datasets**: TravelPlanner

Tags: `steering`, `interpretability`, `temporal preference`, `planning`, `linear probes`

## Abstract

We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, and a TravelPlanner capability benchmark. The central result is that temporal-horizon directions can be identified with simple contrastive linear probes and then used for steering to induce large, bidirectional preference changes. On an out-of-distribution monetary choice task that varies reward size and delay, steering strongly shifts the model's indifference threshold between smaller-sooner and larger-later rewards in both directions. We further show improvements on a planning-related capability metric under moderate temporal steering. These results suggest that model intertemporal preferences are measurable and steerable, which is relevant for AI systems that give advice involving delayed costs and benefits, and for safety questions about long-horizon planning.

---

Record id: `arxiv:2608.03892`
