<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Again! The Effect of Test-Time Compute on Preferences, Opinions, and Beliefs of Large Language Models

- **Authors**: George Kour, Itay Nakash, Michal Shmueli-Scheuer, Ateret Anaby Tavor
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-industry.45/>
- **PDF**: <https://aclanthology.org/2025.acl-industry.45.pdf>
- **DOI**: 10.18653/v1/2025.acl-industry.45
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Introduces POBs, a 20-topic Likert-scale benchmark for LLM preferences/opinions/beliefs on controversial topics, finding models consistently lean progressive-collectivist (with newer versions more strongly and less consistently so), and that adding reasoning or self-reflection prompting gives only limited improvement to reliability, neutrality, or consistency.

## Problem

As LLMs increasingly influence advice and decisions, it is unclear whether and how strongly they hold implicit subjective preferences, opinions and beliefs on controversial societal/personal topics, whether test-time-compute mechanisms (reasoning, self-reflection) that improve other tasks also reduce this bias, and whether models accurately self-report their own stances.

## Contributions

- POBs, a 20-topic Likert-scale benchmark with reference-free metrics (reliability, NNI, TCI) for auditing LLM subjective preferences, opinions and beliefs on controversial and personal-preference topics
- a finding that increasing test-time compute via reasoning and self-reflection prompting gives only limited, inconsistent improvement to neutrality/consistency and can reduce answer reliability
- identification of a consistent progressive-collectivist lean across evaluated models that strengthens (with reduced consistency) in newer versions within the same model family, and evidence that models underreport their own biases when asked to self-declare their stance

## Method

Builds POBs (Preference, Opinion, and Belief survey), 20 topics with 12-38 Likert-scale questions each, split into polar topics (two opposing extremes, e.g. 'AI Precautionary vs. Optimism,' scored on a -1 to 1 polarity scale) and non-polar topics (personal-preference areas with a 'Refused' option). Evaluates 10 open- and closed-source LLMs under three prompting strategies -- Direct, Reasoning (explicit chain-of-thought before answering), and Self-reflection (reconsidering an initial reasoned answer) -- computing three metrics: Reliability (average consistency of repeated (n=5) answers to the same question), the Non-Neutrality Index (NNI, average absolute polarity within a topic) and the Topical Consistency Index (TCI, 1 minus the standard deviation of average polarity across a topic's questions). Also introduces 'Declarative POBs,' a companion survey directly asking models to self-report their stance, to check self-report accuracy against POBs-inferred stances.

## Results

Increasing test-time compute (Reasoning, then Self-reflection) reduces reliability for most models -- e.g. LLaMA-3.3-70B-instruct's reliability is 0.99 (Direct) vs. 0.93 (Reflection); reliability degradation is not explained by invalid-response rates. NNI and TCI both show only limited, inconsistent improvement from added test-time compute (Table 2 shows roughly as many degradations as improvements across the 10 models moving Direct -> Reasoning -> Reflection). A strong negative correlation (r ~ -0.9, consistent across all three prompting strategies) exists between NNI and TCI: models expressing stronger opinions are also more inconsistent, an inherent tension between opinionation and stability. Across polar topics, models cluster into three patterns: consistent neutrality (e.g. individualism, religion), consistent opinionation (e.g. LGBTQ+, women's rights, environmentalism -- models lean progressive on these), and inconsistent opinionation (e.g. free speech, competitiveness). Aggregated ideological analysis (Progressivism-vs-Conservatism and Individualism-vs-Collectivism axes) shows most models cluster in the progressive-collectivist quadrant, with newer versions within the same model family showing stronger and more consistent progressive-collectivist lean than older versions -- the opposite of what one might expect from added alignment maturity. Models systematically underreport their own biases: Declarative POBs self-reported stances (starred in Figure 5) sit closer to neutral than the same models' POBs-inferred stances, particularly understating their progressivism. Opinion-shift analysis between Reasoning and Reflection shows GPT-4o has near-zero opinion change while LLaMA-3.2-3B shifts opinion (>1 polarity-point change) on 8% of questions, and more advanced versions within a family shift less than older ones.

## Limitations

No human baseline comparison exists -- the benchmark is intentionally reference-free, so results are relative rankings between models rather than a comparison to any 'correct' or population-representative stance. Prompting-strategy effects (Direct/Reasoning/Reflection) may not generalize to real-world system prompts or interaction patterns; instructing neutrality explicitly via system prompt was not tried. POBs is English-only with a fixed, LLM-generated question set that was not validated for balance/clarity by domain experts or human participants, so results should be read as relative comparisons rather than absolute measurements; the questions may also carry biases inherited from the LLM (Llama-3.3-70B-Instruct) used to generate them. The benchmark measures stated opinions and preferences, not whether a model's downstream recommendations or actions (e.g. actual advice given to a user) are consistent with those stated positions -- this transfer is explicitly left to future work. Whether training a model to be neutral on one topic generalizes to related or opposing topics is also unexplored.

## Why it matters here

- **overthinking**: Adjacent rather than central: it studies test-time compute's effect on a completely different axis (subjective neutrality/consistency of opinions) than accuracy-efficiency, but the direct finding that adding reasoning and self-reflection reduces answer reliability (more inconsistency, not less) is a concrete example of test-time compute making an undesirable property worse rather than better -- relevant as a caution that 'think more' is not a universally beneficial intervention, mirroring overthinking's core claim that additional reasoning can hurt rather than help on some classes of task.

## Entities

- **Concepts**: Non-Neutrality Index (NNI), Topical Consistency Index (TCI), reliability (response consistency under repeated sampling), opinion self-report underestimation
- **Methods**: Direct / Reasoning / Self-reflection prompting comparison, hierarchical clustering of topic correlations, Likert-scale polarity scoring
- **Datasets**: POBs (new, 20 topics), Declarative POBs (new, self-report companion survey)

Tags: `test-time-compute`, `bias`, `neutrality`, `self-reflection`, `benchmark`

## Abstract

As Large Language Models (LLMs) become deeply integrated into human life and increasingly influence decision-making, it’s crucial to evaluate whether and to what extent they exhibit subjective preferences, opinions, and beliefs. These tendencies may stem from biases within the models, which may shape their behavior, influence the advice and recommendations they offer to users, and potentially reinforce certain viewpoints. This paper presents the Preference, Opinion, and Belief survey (POBs), a benchmark developed to assess LLMs’ subjective inclinations across societal, cultural, ethical, and personal domains. We applied our benchmark to evaluate leading open- and closed-source LLMs, measuring desired properties such as reliability, neutrality, and consistency. In addition, we investigated the effect of increasing the test-time compute, through reasoning and self-reflection mechanisms, on those metrics. While effective in other tasks, our results show that these mechanisms offer only limited gains in our domain. Furthermore, we reveal that newer model versions are becoming less consistent and more biased toward specific viewpoints, highlighting a blind spot and a concerning trend.POBS: https://ibm.github.io/POBS

---

Record id: `doi:10.18653/v1/2025.acl-industry.45`
