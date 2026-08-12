<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection

- **Authors**: Yibo Yan, Shen Wang 0005, Jiahao Huo, Hang Li 0007, Boyan Li, Jiamin Su, Xiong Gao, Yifan Zhang 0004, Tianlong Xu, Zhendong Chu, Aoxiao Zhong, Kun Wang 0042, Hui Xiong 0001, Philip S. Yu, Xuming Hu, Qingsong Wen
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.findings-acl.1217>
- **DOI**: 10.18653/V1/2026.FINDINGS-ACL.1217
- **Topics**: reasoning-evaluation, reasoning-training
- **Relevance score**: reasoning-evaluation 0.50

## In one line

Benchmarks multimodal models on detecting and categorizing errors in K-12 math solutions collected from real student interactions, with the best model about 10% behind human experts.

## Problem

Multimodal math benchmarks focus on problem-solving ability, leaving a gap on more complex scenarios such as error detection — finding a mistake in someone else's work is a different competence from producing correct work.

## Contributions

- Formulation of multimodal error detection as an evaluation task
- ErrorRadar, the first benchmark for it, with error step identification and error categorization sub-tasks
- 2,500 multimodal K-12 math problems from real student interactions with expert annotation and error-category metadata
- Evaluation of open- and closed-source MLLMs against educational expert evaluators, with the best model around 10% behind humans

## Method

The paper formulates multimodal error detection as a task and introduces ErrorRadar to assess it, over two sub-tasks: error step identification and error categorization. It consists of 2,500 high-quality multimodal K-12 mathematical problems collected from real-world student interactions in an educational organization, with expert annotation and metadata including problem type and error category. Real student errors are the design choice that matters — they are the error distribution that actually occurs, rather than synthetic perturbations.

## Results

Both open-source and closed-source representative MLLMs are evaluated against educational expert evaluators. Challenges remain: GPT-4o, the best-performing model, is still around 10% behind human evaluation.

## Limitations

The abstract text available ends mid-sentence at the headline comparison. 'Around 10% behind' is not specified as absolute or relative, and the human reference is expert evaluators whose count and agreement are not given. Data comes from one educational organization, so the error distribution is specific to that population. K-12 level bounds the reasoning difficulty.

## Why it matters here

- **reasoning-evaluation**: Error detection is the evaluation task that matters most for the verifier and process-supervision lines this archive tracks, because a process reward model is doing exactly this job. A benchmark with real student errors and expert labels gives those methods an external reference instead of self-generated perturbations, and the ~10% gap to human experts is a concrete ceiling. It joins ErrorRadar's neighbours in this drain — VisAidMath, MathSight, SciVQR — as the fourth multimodal reasoning benchmark, and it is the only one whose labels come from naturally occurring mistakes.

## Entities

- **Concepts**: [error detection](../../../../wiki/concepts/error-detection.md), process evaluation, [multimodal reasoning](../../../../wiki/concepts/multimodal-reasoning.md), [verification](../../../../wiki/concepts/verification.md), [construct validity](../../../../wiki/concepts/construct-validity.md), human baseline
- **Methods**: ErrorRadar, error step identification, error categorization, expert annotation
- **Datasets**: ErrorRadar

Tags: `benchmark`, `error detection`, `multimodal`, `math reasoning`, `human baseline`

## Abstract

As the field of Multimodal Large Language Models (MLLMs) continues to evolve, their potential to handle mathematical reasoning tasks is promising, as they can handle multimodal questions via cross-modal understanding capabilities compared to text-only LLMs. Current mathematical benchmarks predominantly focus on evaluating MLLMs’ problem-solving ability, yet there is a crucial gap in addressing more complex scenarios such as error detection, for enhancing reasoning capability in complicated settings. To fill this gap, we formally formulate the new task — multimodal error detection, and introduce ErrorRadar, the first benchmark designed to assess MLLMs’ capabilities in such a task. ErrorRadar evaluates two sub-tasks: error step identification and error categorization, providing a framework for evaluating MLLMs’ complex mathematical reasoning ability. It consists of 2,500 high-quality multimodal K-12 mathematical problems, collected from real-world student interactions in an educational organization, with expert-based annotation and metadata such as problem type and error category. Through extensive experiments, we evaluated both open-source and closed-source representative MLLMs, benchmarking their performance against educational expert evaluators. Results indicate challenges still remain, as GPT-4o with best model performance is still around 10% behind human evaluation

---

Record id: `doi:10.18653/v1/2026.findings-acl.1217`
