<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Validating LLM-as-a-Judge Systems under Rating Indeterminacy

- **Authors**: Luke Guerdan, Solon Barocas, Kenneth Holstein, Hanna Wallach, Zhiwei Steven Wu, Alexandra Chouldechova
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: local
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Shows that when a rating task admits several defensible interpretations, forcing raters to pick one answer biases LLM-as-a-judge validation so badly that the selected judge can be up to 31% worse than the one chosen by asking raters for the set of all plausible ratings.

## Problem

Validating a judge system means collecting several human ratings per item and aggregating them into a single gold label. But many rating criteria admit multiple valid readings of the same item — a response can be reasonably called toxic or not, helpful or not, depending on how the instruction is interpreted — a condition the paper names rating indeterminacy. Nearly all such tasks use forced-choice elicitation, requiring each rater to select exactly one rating. Humans and LLMs resolve that forced choice differently, and the standard validation pipeline has no way to represent the difference, so what looks like judge error may be interpretive divergence and vice versa.

## Contributions

- The concept of rating indeterminacy, distinguished from ordinary rater disagreement: not noise about a single correct answer, but several ratings each defensible under a different valid reading of the criteria.
- A formal framework connecting measures of judge-system performance to the choice of human-judge agreement metric, rating elicitation scheme and aggregation scheme, showing how they interact.
- A theoretical account of how forced-choice elicitation biases validation when humans and judges break ties differently.
- Multi-label 'response set' elicitation as the alternative: raters select every rating corresponding to a plausible interpretation, and judge agreement is measured against that set.
- Empirical demonstration across 11 real-world rating tasks and 9 commercial LLMs that standard forced-choice validation selects substantially suboptimal judge systems.

## Method

Rating tasks are modelled so that each item has a set of ratings admissible under some valid interpretation of the criteria, rather than one latent true rating. Two elicitation schemes are compared. Forced choice, the status quo, instructs each rater to select exactly one rating per item; multiple raters are then collected and aggregated into a per-item gold label, typically by majority or a soft label. Response-set elicitation instead instructs each rater to select all ratings that correspond to a plausible interpretation of the item. The framework then relates judge-selection decisions under each scheme to the underlying admissible sets, allowing the bias introduced by forced choice to be characterized theoretically rather than only observed. Empirically, 11 real-world rating tasks spanning conditions such as toxic language, factuality and helpfulness are rated under both schemes, and 9 commercial LLM judges are validated under each; the judge system that each validation approach would select is then compared on its actual performance measured against response-set ratings.

## Results

The headline is a selection error rather than a measurement error: standard forced-choice validation selects judge systems that perform as much as 31% worse than those selected by response-set validation, with a further reported gap of 28% in the analysis. The mechanism is that humans and LLMs resolve indeterminacy differently when forced to choose one rating, so agreement computed on forced-choice labels rewards a judge for matching an arbitrary human tie-break rather than for correctly identifying the admissible set. Because the effect operates through which judge is chosen, it is invisible to the usual diagnostics: a validation pipeline can report reasonable-looking agreement and still have picked the wrong system. The paper's conclusion is that measuring human-judge agreement against response-set ratings is essential for selecting performant judge systems whenever indeterminacy is present, and it closes with concrete recommendations for validation practice.

## Limitations

The paper does not carry a standalone limitations section; its scoping is done in the related-work discussion, where it positions itself as examining how the human rating process affects meta-evaluation rather than factors such as prompt formatting that other work covers. What a reader should weigh: the response-set scheme shifts cost and burden onto annotation — raters must enumerate plausible interpretations rather than pick one, which is harder to instruct and to quality-control, and the paper does not report the additional annotation cost. The 11 tasks are general rating tasks such as toxicity, factuality and helpfulness rather than reasoning-specific ones, so the magnitude of the effect on tasks with objectively checkable answers is not established. And the framework's central move — treating an item as having a set of admissible ratings — requires deciding which interpretations count as valid, which is itself a judgement the paper formalizes but does not eliminate.

## Why it matters here

- **reasoning-evaluation**: The second half of the judge-validity problem this topic now tracks, and it operates at a different layer than the first. The large-scale judge audit in this archive shows that the standard agreement metric overstates a judge's discrimination by 34-41 points and that reproducibility can mask bias; this paper shows that even a correctly computed agreement score can select the wrong judge, because the human labels it is computed against were produced by a forced choice that humans and LLMs make differently. Together they say judge validation fails at both ends — the metric and the ground truth. For this archive the practical question is how much of it transfers. Several archived papers use judges for labels that look determinate — is this reasoning step correct, does this trace acknowledge the injected cue, did this trajectory collapse — where a single right answer plausibly exists and indeterminacy should be milder than for helpfulness or toxicity. But two archived label sets are visibly interpretive: the classification of a correction as reactive versus proactive, and the five-way taxonomy of reasoning-collapse modes. Those are exactly the shape this paper describes, they were collected by forced choice from a single judge, and the up-to-31% selection penalty is the reason to treat conclusions resting on them as provisional. The response-set method is also directly adoptable at small scale for this group's own annotation.

## Entities

- **Concepts**: rating indeterminacy, LLM as a judge, forced-choice elicitation, response set elicitation, gold label aggregation, human-judge agreement, [construct validity](../../../../wiki/concepts/construct-validity.md), [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), inter-rater disagreement
- **Methods**: [LLM as a judge](../../../../wiki/methods/llm-as-a-judge.md), response set elicitation, forced-choice elicitation, soft label aggregation
- **Datasets**: 11 real-world rating tasks, 9 commercial LLM judges

Tags: `llm-as-a-judge`, `evaluation`, `validity`, `annotation`, `meta-evaluation`, `rating indeterminacy`

## Abstract

The LLM-as-a-judge paradigm, in which a judge LLM system replaces human raters in rating the outputs of other generative AI (GenAI) systems, plays a critical role in scaling and standardizing GenAI evaluations. To validate such judge systems, evaluators assess human--judge agreement by first collecting multiple human ratings for each item in a validation corpus, then aggregating the ratings into a single, per-item gold label rating. For many items, however, rating criteria may admit multiple valid interpretations, so a human or LLM rater may deem multiple ratings "reasonable" or "correct". We call this condition rating indeterminacy. Problematically, many rating tasks that contain rating indeterminacy rely on forced-choice elicitation, whereby raters are instructed to select only one rating for each item. In this paper, we introduce a framework for validating LLM-as-a-judge systems under rating indeterminacy. We draw theoretical connections between different measures of judge system performance under different human--judge agreement metrics, and different rating elicitation and aggregation schemes. We demonstrate that differences in how humans and LLMs resolve rating indeterminacy when responding to forced-choice rating instructions can heavily bias LLM-as-a-judge validation. Through extensive experiments involving 11 real-world rating tasks and 9 commercial LLMs, we show that standard validation approaches that rely upon forced-choice ratings select judge systems that are highly suboptimal, performing as much as 31% worse than judge systems selected by our approach that uses multi-label "response set" ratings to account for rating indeterminacy. We conclude with concrete recommendations for more principled approaches to LLM-as-a-judge validation.

---

Record id: `local:17fe90fcd8710387`
