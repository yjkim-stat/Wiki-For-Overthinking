<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs

- **Authors**: Vu Duc Anh, Nhat M. Hoang, Do Xuan Long, Cong-Duy Nguyen, Ponhvoan Srey, Luu Anh Tuan
- **Venue**: cs.CL
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11573>
- **PDF**: <https://arxiv.org/pdf/2608.11573v1>
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.57

## In one line

Trains self-correction as a step-level preference problem -- preferring a detect-and-repair continuation over the continuation that would follow if the error went unaddressed -- after first initialising with ordinary step-level preference optimisation, and finds that correcting more often and detecting more errors both anti-correlate with accuracy.

## Problem

Self-correction remains unreliable in language models, and the supervised approaches to it suffer distribution shift and behaviour collapse, which biases a model toward following correction templates rather than selectively revising real errors. What is missing is a training signal that makes the correction contingent on there actually being an error, rather than on the surface form of a correction.

## Contributions

- A step-level self-correction preference objective whose rejected branch is the continuation the model would produce if the error went unaddressed, making the signal contingent on an error rather than on a correction template.
- A teacher-free construction of 8,416 correction pairs from an existing step preference dataset by splicing rejected steps onto correct prefixes, plus a teacher-rationale variant for comparison.
- A direct measurement that self-correction rate and error recall are both anti-correlated with reasoning accuracy across methods and across backbones.
- An initialisation ablation showing that staging step-level preference optimisation before the self-correction stage beats joint training and plain RL by 2 to 4 points.
- Out-of-domain evaluation on two benchmarks where the prior step-preference method degrades on several backbones and this one does not.

## Method

A reasoning trajectory is typed: each step is a solution step, an error-detection step, or a fixed step that replaces the flawed one. Stage one is the existing Step-DPO objective -- a preference between a correct and an incorrect next step given the same prefix -- used purely as initialisation to establish step-level reasoning. Stage two is the contribution: given a correct prefix followed by an incorrect step, the preferred continuation is a self-corrected one and the rejected continuation is the next step the model would have produced had the error stood, both scored against a frozen reference in the usual DPO form. Two variants differ in what the corrected continuation contains. The teacher-free variant concatenates an explicit error-detection signal with the corrected step. The teacher-assisted variant inserts a GPT-4o-generated explanation of why the previous step was wrong between the signal and the correction. Data is built from the 10K Step-DPO set by appending each rejected step to the prefix to manufacture an erroneous state, giving 8,416 pairs with no external resource; the rationale variant adds the teacher explanations. Self-correction behaviour in generated responses is identified automatically by a fixed list of signal phrases, extended by the authors with explicit ones such as 'The previous step is incorrect.'

## Results

Seven backbones from 7B to 14B, greedy decoding, in-domain MATH and GSM8K, out-of-domain GK2023 and OCW; one-sided McNemar's test against Step-DPO on the in-domain sets only, since the authors judge the OOD sets too small to power it. Averaged over seven backbones the teacher-free variant adds 1.11 points on MATH and 0.69 on GSM8K over the base, and the rationale variant 1.36 and 0.87 -- small margins, and only a subset are marked significant. The out-of-domain picture is where the two methods separate: Step-DPO degrades on some backbone-benchmark pairs (GK2023 on one, OCW on the 14B model, minus 1.5), while both new variants maintain or improve everywhere; the largest gains are 10.9 on GK2023 and 8.8 on OCW for a math-specialised backbone, and 8.1 on OCW for a 7B one. Gains shrink on the newer backbones (Qwen3-8B, Llama-3.1-8B-Instruct, Qwen2.5-14B-Instruct), which the authors attribute to those models already self-correcting more before training. The most useful result is the behavioural one. Against two prior supervised self-correction methods on a shared backbone, the new methods score higher on both MATH and GSM8K (51.0 and 51.7 against 48.5 and 48.7) while having markedly lower self-correction rates (28.8 and 23.9 against 45.3 and 46.5) and lower error recall (33.2 and 35.9 against 49.9 and 54.6) -- so correcting more often and detecting more errors both go the wrong way relative to accuracy. The same dissociation appears within the method's own backbones: two of five see their self-correction rate fall after training while reasoning accuracy rises. The initialisation ablation is clean and shows the stage is load-bearing: against the full pipeline's 55.6 MATH and 87.9 GSM8K on one model, dropping the initialisation gives 53.1 and 87.3, joint training instead of staging gives 53.3 and 84.1, and replacing the staged design with plain RL gives 53.3 and 83.6; on the instruct backbone the pattern repeats with a 4.1-point MATH loss for no initialisation.

## Limitations

The authors state three: the rationale variant depends on a stronger teacher and can propagate its biases and errors; the evaluation is mathematical reasoning, where step boundaries are naturally well defined, and generalisation to open-ended settings such as writing is untested; and only 7B-to-14B models are examined. Reader-visible additions: the in-domain effect sizes are around one point averaged over seven backbones, with significance marked on some cells and absent on others, so the in-domain claim rests on a pattern of small wins rather than on any single result; the out-of-domain benchmarks where the gains are large are exactly the ones the authors declare too small for a significance test. Self-correction rate and error recall are measured by matching an author-extended list of signal phrases, so both the behavioural metrics and the training data's chosen continuations are defined by the same lexical convention -- a model that corrects without using one of those phrases is invisible to the measurement. The erroneous states are manufactured by splicing a rejected step onto a correct prefix rather than sampled from the model's own failures, so the errors the model is trained to detect are drawn from a preference dataset rather than from its own distribution. No decoding variance is reported; everything is greedy, single-run.

## Why it matters here

- **test-time-scaling**: Self-correction is inference-time compute spent on revision, and this paper measures the thing the archive most needs measured about it: how often a model announces a correction is anti-correlated with whether the corrections help. Against two prior methods on a shared backbone it scores higher on both mathematics benchmarks (51.0 and 51.7 against 48.5 and 48.7) while self-correcting at 28.8 and 23.9 percent against 45.3 and 46.5, and recalling fewer errors (33.2 and 35.9 against 49.9 and 54.6); two of its own backbones lower their correction rate after training while getting better. So revision tokens are not a compute knob that pays by volume -- a method that raises the correction rate is buying template-following, and the useful quantity is selectivity. That is the same shape as the archive's finding that a local behavioural metric can be driven to its ceiling by a worse generation. The training construction is what makes selectivity trainable: the preference is between a repair and the continuation that would have followed had the error stood, so the signal exists only where an error does. The gains also shrink on the newer backbones, which the authors attribute to those models already self-correcting -- consistent with the archive's pattern that inference-time revision methods are worth most where the base policy does least of it unprompted. The out-of-domain results are the largest (10.9 and 8.8 points) and are exactly the ones the authors decline to test for significance.

## Entities

- **Concepts**: self-correction, step-level preference optimization, [error detection](../../../../wiki/concepts/error-detection.md), [process reward](../../../../wiki/concepts/process-reward.md), behavior collapse, [distribution shift](../../../../wiki/concepts/distribution-shift.md), [out-of-distribution generalization](../../../../wiki/concepts/out-of-distribution-generalization.md), [teacher-student gap](../../../../wiki/concepts/teacher-student-gap.md)
- **Methods**: SFS-DPO, SFS-DPO-R, Step-DPO, [DPO](../../../../wiki/methods/dpo.md), [supervised fine-tuning](../../../../wiki/methods/supervised-fine-tuning.md), LEMMA, S2R, McNemar's test
- **Datasets**: [MATH](../../../../wiki/datasets/math.md), [GSM8K](../../../../wiki/datasets/gsm8k.md), Gaokao2023, OCWCourses, MetaMath, MMIQC

Tags: `self-correction`, `step-dpo`, `preference-optimization`, `error-detection`, `math-reasoning`

## Abstract

Achieving effective self-correction, where models verify and correct their own mistakes, remains a fundamental challenge for large language models (LLMs). In this work, we propose Self-Fix Step-DPO (SFS-DPO), a reinforcement learning based, two-stage framework for step-level self-verification and self-correction. The first stage strengthens step-level reasoning via step-level preference optimization, while the second stage explicitly trains models to self-verify and self-correct. We further introduce a teacher-assisted variant, SFS-DPO-R, which incorporates explanatory rationales for error verification to provide stronger corrective signals. Comprehensive in-domain and out-of-domain evaluations across multiple LLMs demonstrate that SFS-DPO and SFS-DPO-R consistently outperform prior step-level training baselines. Our analysis further reveals improvements in self-correction frequency and effectiveness, highlighting the importance of strengthening step-level reasoning for robust performance.

---

Record id: `arxiv:2608.11573`
