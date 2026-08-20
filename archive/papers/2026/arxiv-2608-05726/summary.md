<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation

- **Authors**: Yuma Asato, Kiyoaki Shirai, Natthawut Kertkeidkachorn
- **Venue**: cs.CL
- **Published**: 2026-08-06
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.05726>
- **PDF**: <https://arxiv.org/pdf/2608.05726v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Measures an LLM judge's latent number bias by asking it to emit random numbers, then rectifies its scoring token probabilities against that measured bias.

## Problem

LLM judges tend to produce particular scores regardless of the evaluated text, a scoring bias that corrupts their use as evaluation metrics. Existing calibration methods do not isolate where the bias comes from.

## Contributions

- A random-number-generation probe that isolates an LLM's latent numerical bias independently of evaluated content
- Task-conditioned bias measurement by adding the downstream task definition to the probe prompt
- A token-probability rectification step applied at judging time
- Evidence that scoring bias varies across models, tasks and score ranges

## Method

The LLM is instructed to generate number tokens at random, and its latent numerical bias is identified as the deviation of the observed number distribution from uniform. Because a random-number request has no correct answer, any deviation is attributable to the model rather than to the content — that is what makes the measurement a clean bias probe. A definition of the downstream task the judge will be used for is added to the random-number prompt, yielding a task-specific latent bias. At evaluation time the token generation probabilities for a given input are rectified using the measured bias.

## Results

On four tasks — LLM alignment evaluation, summarization evaluation, Semantic Textual Similarity and Semantic Textual Relatedness — the method outperforms an undebiased LLM and previous calibration methods. Scoring bias is confirmed to vary across LLMs, tasks and score ranges.

## Limitations

No numeric margins in the abstract, and the models are not named. The method assumes a uniform distribution is the correct reference for a random-number request, which is a modelling choice rather than a fact about the intended judge behaviour. Rectification needs access to token generation probabilities, so it does not apply to judges behind APIs that do not expose logprobs. Bias varying by score range means a single measured distribution may not correct the tails.

## Why it matters here

- **reasoning-evaluation**: LLM judges are how much reasoning work gets scored once the answer is not a checkable string, so a bias in the judge is a bias in the field's measurements. The useful part for this archive is the probe rather than the fix: a random-number request has no correct answer, so deviation from uniform is a content-free estimate of the judge's prior, and it is cheap enough to run as a routine control. The finding that bias varies by score range matters most for reasoning evaluation, where scores cluster high and the compressed top of the scale is exactly where discrimination is needed.

## Entities

- **Concepts**: [calibration](../../../../wiki/concepts/calibration.md), scoring bias, [meta-evaluation](../../../../wiki/concepts/meta-evaluation.md), [judge reliability](../../../../wiki/concepts/judge-reliability.md), token probability rectification
- **Methods**: [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), random number generation probe, probability rectification, calibration
- **Datasets**: Semantic Textual Similarity, Semantic Textual Relatedness, summarization evaluation task, LLM alignment evaluation task

Tags: `llm-as-a-judge`, `calibration`, `scoring bias`, `evaluation`

## Abstract

Large Language Models (LLMs) are often used as evaluators of text quality, known as LLM-as-a-Judge, which can outperform conventional automatic evaluation metrics that rely on reference texts. However, LLM evaluators tend to generate particular scores regardless of the context of the evaluated text, which is known as scoring bias. This study proposes a novel method to mitigate this scoring bias. An LLM is instructed to randomly generate number tokens, and the latent numerical bias of the LLM is identified by measuring the deviation of the observed distribution of numbers from the uniform distribution. A definition of a downstream task, for which an LLM evaluator is used, is added to the prompts for random number generation to measure task-specific latent number bias. In the evaluation by an LLM, the token generation probabilities for a given input are rectified considering the LLM's latent number bias. Results of the experiment on four different tasks, evaluation of LLM alignment, evaluation of summarization, Semantic Textual Similarity, and Semantic Textual Relatedness, demonstrate that our proposed method outperforms the baselines, including an LLM without debiasing and previous calibration methods. In addition, it is confirmed that scoring bias varies across LLMs, tasks, and score ranges, indicating the importance of measuring latent number bias as the case may be.

---

Record id: `arxiv:2608.05726`
