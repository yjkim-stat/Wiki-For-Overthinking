<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Safety Cost of Steering Vectors Is Separable and Reducible

- **Authors**: Yuxiao Li, Gjergji Kasneci
- **Venue**: cs.CL
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08383>
- **PDF**: <https://arxiv.org/pdf/2608.08383v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## In one line

Shows that the part of a steering vector which breaks a model's refusal behaviour is a separate direction from the part that produces the intended behavioural effect, and learns that direction by constrained optimization so it can be ablated without losing the steering.

## Problem

Steering vectors are adopted because they are cheap -- one direction in activation space, computed from a small contrastive dataset, applied at inference with no retraining. But injecting one degrades safety: a vector built for a behaviourally unrelated purpose raises compliance with harmful requests, and no effective mitigation existed. The obvious fix does not work. Cosine similarity with the standard refusal direction predicts the degradation, yet ablating that direction from the steering vector fails to restore safety, because refusal is mediated by several mechanistically independent directions and the canonical one is not necessarily the one a given vector is damaging. Isolating the responsible component therefore cannot be done from any known direction, and making the model merely more cautious buys safety with false refusals.

## Contributions

- The safety-degrading and effect-relevant components of a steering vector are geometrically separable, and in several configurations partially competing
- CAST, a post-hoc constrained optimization that learns the direction to ablate rather than assuming a known one
- A differentiable refusal proxy -- KL restricted to refusal-indicative tokens -- that makes safety optimizable without a non-differentiable judge
- Generalization to three jailbreak families never seen during optimization

## Method

The sanitized vector is the original with a learned subspace projected out, renormalized to the original length; the main experiments use a rank-1 approximation, so one unit direction is learned. Three objectives are in tension and are handled as a constrained problem rather than a weighted sum. The safety loss uses a differentiable stand-in for refusal: rather than full KL, it measures divergence restricted to a small set of refusal-indicative tokens, weighted by the base model's own probabilities so the quantity is dominated by refusal tokens the unsteered model would actually produce, and so that distributional shifts on non-refusal tokens -- which may be exactly the steering effect worth keeping -- are not penalized. Because that divergence can go negative, minimizing it does not merely restore refusal to baseline but can strengthen it past baseline when the other constraints permit. The effect constraint preserves the full output distribution of the originally steered model on prompts where the target behaviour is active, and the false-refusal constraint penalizes any increase in refusal on benign prompts with its tolerance set to exactly zero. The Lagrangian is solved by primal-dual updates: the direction moves by gradient descent while the two dual variables rise when their constraint is violated and decay when it is satisfied, so only the tolerances need setting by hand. Training uses small symmetric multipliers because in that regime the model's response is approximately first-order in the multiplier, which makes the safety-interfering component easier to isolate. Evaluated on Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct and Qwen2.5-14B-Instruct, on the three most reliably steerable alignment behaviours -- corrigibility, power-seeking, self-awareness -- with the direction learned against three template attacks and tested additionally on three optimization-based and adaptive ones it never saw.

## Results

The negative result on the obvious baseline is the most useful part. Steering raises attack success rate on all three models, with worst-case increases exceeding 63 percent on Qwen-7B; ablating the standard refusal direction recovers at most about 8 points of mean ASR and leaves worst-case ASR largely unchanged on two of the three models -- 61.4 against 63.5 on Qwen-7B, 51.4 against 51.2 on Llama-8B, which is no recovery at all. CAST instead brings mean ASR below the unsteered baseline on both Qwen models (15.7 against a 24.5 baseline on 7B, 7.5 against 9.0 on 14B) and to within one point on Llama-8B. Broken out across the full multiplier range and all seven attacks individually -- 108 configurations -- no attack exceeds 4.2 points above the unsteered baseline after sanitization, the largest positive deviation is 4.6, and in more than two-thirds of cases the sanitized vector is actively safer than not steering at all. That holds on the three held-out attack families, so the learned direction captures a shared mechanism rather than an artifact of the templates it was fitted on. The separability claim is measured, not assumed: the sanitized vector's behavioural shift relative to the original averages 104.9 percent on Qwen-7B and 112.6 percent on Llama-8B, meaning removal of the safety-degrading direction typically *increases* the intended effect, which the paper reads as the two components being partially competing rather than merely separable. The one systematic attenuation is Qwen-14B under positive steering at about 75 percent, with its average across conditions at 87.6. False refusal does not pay for it: no measurable increase on general instruction-following prompts, Qwen models within about 1 percent on the harder borderline set, and Llama-8B's worst case around 3 to 4 points. The failure modes differ by family in a way a single-direction account would not predict -- both Qwen models degrade in the positive steering direction, consistent with directional alignment to the refusal direction, while Llama-8B degrades under both directions.

## Limitations

The paper is explicit that the Lagrangian relaxation is nonconvex, so there is no guarantee of global optimality or exact feasibility, and reports that the constraints are satisfied only to close approximation. Three more a reader should weigh. The main results use a rank-1 subspace while the paper's own motivation is that refusal is higher-dimensional; the higher-rank study is a later section rather than the headline. The effect tolerance is chosen empirically as the smallest value that lets safety return to baseline while retaining the steering effect, so the trade-off point is tuned per setting rather than derived. And the direction is learned per model, per behaviour and per layer, which makes this a post-hoc correction applied to each vector before deployment rather than a property of the model -- the paper says as much in calling it a recipe, but the framing 'safety cost is reducible' is easily read as stronger. On measurement: both ASR and false-refusal rate come from LLM judges, which this archive treats as an instrument with its own reliability, and the training multipliers are small enough for the first-order approximation the method leans on while evaluation runs to 1.5.

## Why it matters here

- **reasoning-interpretability**: A clean instance of the archive's standing finding that how well a direction detects a property licenses no claim about what intervening on it does. Here the standard refusal direction demonstrably mediates refusal and its cosine similarity with a steering vector *predicts* the safety damage -- and ablating it recovers almost nothing, leaving worst-case ASR unchanged on two of three models. The direction that must be removed has to be learned bottom-up against the intervention's own objective, and it turns out to be partially opposed to the behavioural effect rather than merely orthogonal to it. That is a sharper statement than the archive currently holds: not only does a detection direction fail to transfer to intervention, the correct intervention direction is one no detector had named.

## Entities

- **Concepts**: steering vector, refusal direction, safety degradation, false refusal, [superposition](../../../../wiki/concepts/superposition.md), constrained optimization, [jailbreak](../../../../wiki/concepts/jailbreak.md), [representation versus readout](../../../../wiki/concepts/representation-versus-readout.md), activation space
- **Methods**: [activation steering](../../../../wiki/methods/activation-steering.md), [contrastive activation addition](../../../../wiki/methods/contrastive-activation-addition.md), [ablation](../../../../wiki/methods/ablation.md), primal-dual optimization, KL divergence, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), [GCG](../../../../wiki/methods/gcg.md), AutoDAN, [PAIR](../../../../wiki/methods/pair.md)
- **Datasets**: JailbreakBench, Alpaca, [XSTest](../../../../wiki/datasets/xstest.md)

Tags: `steering`, `safety`, `activation-engineering`, `jailbreak`, `interpretability`

## Abstract

Steering vectors are a lightweight tool for controlling LLM behavior. However, emerging evidence shows that steering vectors can unintentionally compromise a model's safety mechanisms and increase compliance with harmful requests, while no effective mitigation yet exists. In this work, we show that this safety degradation arises from a separable component in the vector that disrupts the model's safety mechanisms but contributes little to the steering objective. We identify and remove this safety-degrading component, formulating the task as a constrained optimization problem solved through primal-dual updates, subject to preserving the intended steering effect and bounding false refusal. The resulting solution is both interpretable and surgical: the optimization recovers a single direction whose ablation from the steering vector restores model safety with minimal utility cost. Across models, steering behaviors, and attack suites, including unseen attacks types, our method substantially reduces steering-induced safety degradation while preserving the original steering effect with minimal impact on false refusal. Our method offers a post-hoc correction to steering vectors that mitigates their safety cost, and more broadly, it provides a general recipe for applying activation-level model interventions without paying a safety tax.

---

Record id: `arxiv:2608.08383`
