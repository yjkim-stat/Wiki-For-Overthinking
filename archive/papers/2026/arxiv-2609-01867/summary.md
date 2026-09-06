<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thinking effort aligns between humans and reasoning models in abductive reasoning

- **Authors**: Henry Arthur
- **Venue**: cs.CL
- **Published**: 2026-09-01
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2609.01867>
- **PDF**: <https://arxiv.org/pdf/2609.01867v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## In one line

Measures whether reasoning models spend tokens on the same items humans spend time on, using a forced-choice abductive task where item difficulty cannot be read off formal structure, and finds a significant per-item correlation in all eight models tested.

## Problem

Whether the number of tokens a reasoning model generates tracks human thinking effort has been tested mainly on deductive tasks such as syllogisms and relational reasoning. The paper's objection is that in those tasks difficulty is partly recoverable from the formal structure of the item, so a model that has learned which forms look hard can spend more tokens on them without doing more search, producing an alignment that is a shortcut rather than shared effort. Abduction has no such structure: the evidence underdetermines the conclusion by design, so difficulty arises only from searching over what each hypothesis would explain.

## Contributions

- Moves the human-model thinking-effort comparison to abductive reasoning, where item difficulty cannot be inferred from formal structure, removing the shortcut available in syllogistic and relational tasks.
- Reports a significant per-item correlation between reasoning tokens and human reaction time in all seven reasoning models and in the non-reasoning baseline, with a noise-ceiling estimate placing the strongest model at 35% of explainable RT variance.
- Shows the alignment extends to errors: humans fall below chance on the items models get wrong, and model-consensus accuracy tracks human accuracy at r = 0.668.
- Shows that averaging over stochastic decoding runs at the provider-recommended temperature raises alignment relative to greedy decoding in all three models retested, with a bootstrap criterion for how many runs are needed.

## Method

A forced-choice abductive task built from the ART dataset (Abductive Natural Language Inference, AI2, adapted from ROCStories): each item gives two observations and two candidate hypotheses, one of which better explains the pair. Items were filtered to those whose hypotheses differ by at most one word, duplicates removed, and 162 sampled with a fixed seed (160 main, 2 practice). 127 participants were recruited on Prolific and 120 retained after removing implausibly fast or slow responders; each saw one of four blocks of 40 items, with accuracy and reaction time recorded. Seven large reasoning models (DeepSeek-R1, Qwen3-235B-Thinking, Qwen3-32B-Thinking, GPT-OSS-20B, GPT-OSS-120B, GLM-4.5-Air, Kimi-K2-Thinking) and one non-reasoning baseline (DeepSeek-V3) were run through the OpenRouter API on a prompt mirroring the human instructions, with reasoning tokens counted from the <think>...</think> trace. The alignment measure is a Pearson partial correlation between log reasoning tokens and log mean human RT per item, residualising both on log prompt token count, because item length correlates strongly with RT (r = 0.669). Three models were then rerun with stochastic decoding at their provider-recommended temperatures and at temperature 2, aggregating many runs per item into a mean token cost and a majority-vote answer, with the number of runs fixed by a bootstrap convergence criterion.

## Results

Under greedy decoding all eight models correlate significantly with human effort after controlling for prompt length: GPT-OSS-120B r = 0.552, GPT-OSS-20B r = 0.41, Qwen3-235B-Thinking r = 0.359, DeepSeek-R1 r = 0.327, Kimi-K2-Thinking r = 0.303 (all p < .001), GLM-4.5-Air r = 0.263 (p < .001), Qwen3-32B-Thinking r = 0.229 (p = .002), and the non-reasoning DeepSeek-V3 r = 0.197 (p = .012), the weakest. The R1-vs-V3 gap does not reach significance (Fisher z = 1.23, p = .217), so the reasoning/non-reasoning advantage is numerical but not established at this sample size. Model size does not predict alignment: GPT-OSS-20B ranks second, above DeepSeek-R1 (671B) and Kimi-K2 (1T). Errors align too: mean human accuracy is 78.8%, but 82.5% on items DeepSeek-R1 answered correctly against 47.8% - below chance - on items it got wrong (point-biserial r = 0.53, p < .001); across models, per-item model-consensus accuracy and human accuracy correlate at partial r = 0.668, with human accuracy 48.7% on items at least 75% of models failed and 84.6% on items at least 75% answered correctly. Stochastic decoding at recommended temperatures raises alignment in all three models retested: GPT-OSS-20B 0.41 -> 0.55 (temp 1, converged at 19 runs, Steiger-Williams p < .001), Qwen3-32B 0.23 -> 0.32 (temp 0.6, converged at 18 runs, p < .05), DeepSeek-R1 0.32 -> 0.37 (temp 0.6, converged at 8 runs, not significant). Temperature 2 is worse than the recommended setting everywhere, and GPT-OSS-20B falls to 0.22 without converging in 25 runs. Against a noise ceiling from split-half reliability of human RTs (Spearman-Brown corrected r = .861), the strongest model explains R^2 = .303 of residualised item-level RT variance, or 35% of the explainable variance. The ensemble mean partial r of 0.42 under greedy decoding sits between the syllogism (0.43) and relational-reasoning (0.27) results of the prior work this replicates.

## Limitations

Stated by the author: effort increased correctness only on the hardest tercile of problems; all main analyses used each model's default reasoning-effort setting, a choice fixed a priori and analogous to telling a human in advance to expect easy, medium or hard items, so alignment might be stronger on a difficulty-calibrated dataset; only one form of abduction is tested (inference to the best explanation), leaving hypothesis generation uncovered; LLM outputs are prompt-sensitive and a different instruction wording could change the results; and although the shared error pattern argues against simple memorisation, ART items may have appeared in pretraining. Noticeable to the reader: the alignment is correlational and per-item, so it constrains what makes a problem expensive but says nothing about whether either system spends the right amount; the single non-reasoning control is one model, which is what leaves the reasoning-versus-non-reasoning comparison underpowered; and the stochastic-decoding gain is obtained by averaging many runs per item, so it describes an aggregate rather than the cost of any single generation the way a deployed model would produce it.

## Why it matters here

- **overthinking**: Supplies an external criterion for how long a problem should take, which this topic otherwise lacks. Work here judges reasoning length against accuracy or against an estimated minimum length; this paper judges it against how long people take on the same item, and finds the two track each other per item in every model tested, including a non-reasoning one. That bears directly on the premise separating waste from difficulty: if token count correlates with human reaction time after controlling for prompt length, then length is carrying difficulty information and not only redundancy, which is the same caution that stops length alone from being a measure of overthinking. The error result sharpens it - humans score below chance on the items models get wrong - so the expensive items are hard rather than mishandled. Two further points are usable: model size does not predict alignment, and decoding temperature does, with the provider-recommended setting beating both greedy and temperature 2. The limit to keep in view is that alignment says what makes an item expensive, not whether either system stops at the right time.

## Entities

- **Concepts**: thinking effort as token count, abductive reasoning, human-model behavioural alignment, reaction time as a measure of cognitive effort, noise ceiling, stochastic decoding, [test-time compute allocation](../../../../wiki/concepts/test-time-compute-allocation.md), item difficulty
- **Methods**: partial correlation of log reasoning tokens with log human reaction time, controlling for prompt length, point-biserial correlation of model correctness with human accuracy, bootstrap convergence criterion for the number of stochastic runs, Steiger-Williams test for dependent correlations, split-half noise ceiling with Spearman-Brown correction, majority-vote aggregation over stochastic decoding runs
- **Datasets**: ART (Abductive Natural Language Inference, AI2), ROCStories

Tags: `cognitive-modeling`, `human-alignment`, `abductive-reasoning`, `reasoning-tokens`, `reaction-time`, `decoding-strategy`, `overthinking`

## Abstract

A major question in cognitive modeling concerns the behavioral alignment between large language models and humans across linguistic and non-linguistic tasks. Unlike standard LLMs, large reasoning models (LRMs) are optimized with reinforcement learning from verifiable rewards, encouraging correct solutions to reasoning tasks rather than preference-aligned responses. Recent work (de Varda et al., 2025) investigates the cost of thinking in humans and LRMs by comparing human reaction times with model reasoning traces across a range of reasoning tasks. We isolate this alignment by turning to abductive reasoning: unlike deductive tasks, its difficulty cannot be inferred from formal structure and offers no shortcuts a model could exploit to mimic effort without genuine search, providing firmer ground for empirical claims of shared effort. We find further evidence of alignment between LRM and human reasoning effort, as well as evidence that models and humans tend to make similar errors. Finally, we show that decoding methods that let models explore multiple reasoning paths increase alignment in reasoning cost between humans and LRMs across the three models tested.

---

Record id: `arxiv:2609.01867`
