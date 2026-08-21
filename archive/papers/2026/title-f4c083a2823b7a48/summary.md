<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Optimal Self-Consistency for Efficient Reasoning with Large Language Models

- **Authors**: _unknown_
- **Venue**: ICML 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://icml.cc/virtual/2026/poster/61225>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Analyses the scaling behaviour of self-consistency sampling as mode estimation, derives power-law error decay in the number of samples, and introduces Blend-ASC, a hyperparameter-free scheme that reallocates a fixed sample budget across questions.

## Problem

Self-consistency draws k chain-of-thought samples per question and returns the majority answer. It reliably improves accuracy but costs k full generations per question, which is prohibitive at dataset scale, and there has been no unified account of how its accuracy scales with k or of how sample-efficient its many adaptive variants actually are. Fixed-allocation schemes spend the same budget on a question the model already answers unanimously and on one where it is split, which is where most of the waste lies.

## Contributions

- A treatment of self-consistency as empirical mode estimation, connecting it to mode estimation and voting theory.
- Derivation and empirical validation of power-law scaling for self-consistency error in the number of samples across datasets.
- A sample-efficiency analysis covering both fixed-allocation and dynamic-allocation self-consistency schemes.
- Blend-ASC, a dynamic sample-allocation variant that is hyperparameter-free and fits an arbitrary sample budget.
- Empirical result that Blend-ASC matches vanilla self-consistency using 4.8x fewer samples on average, beating fixed- and dynamic-allocation baselines.

## Method

Self-consistency is cast as empirical mode estimation, i.e. a majority vote over the model's answer distribution, which lets the paper import results from mode estimation and voting theory. Error is governed by the margin between the most frequent answer and the runner-up; for broad classes of dataset the margin distribution behaves like m^(-1/2) near zero, and this yields a power-law decay of SC error in the number of samples, which the paper derives and then validates empirically across datasets. The same framework is used to compare fixed-allocation sampling against dynamic-allocation schemes that stop sampling a question once its answer looks settled. Blend-ASC is the proposed dynamic-allocation method: it distributes samples across questions during inference according to how undecided each currently is, so easy questions are cut off early and the saved samples go to contested ones. Unlike prior adaptive variants it has no hyperparameters to tune and accepts an arbitrary total sample budget, so it can be dropped into an existing self-consistency pipeline at whatever budget is available.

## Results

Blend-ASC reaches the accuracy of vanilla self-consistency with 4.8x fewer samples on average, and outperforms both fixed-allocation and dynamic-allocation baselines (including Adaptive Self-Consistency and PPR-1v1) across model-dataset combinations. Evaluated on GSM8K, MATH, MMLU and GPQA-Diamond with Llama-3.2-3B, Qwen-2.5-Math-7B and Qwen-2.5-32B. The predicted power-law scaling of self-consistency error in the sample count is empirically validated on these datasets. Note that the arXiv v1 listing of this work reported 6.8x rather than 4.8x; the later version and the ICML page both state 4.8x, so the smaller figure is the one to cite.

## Limitations

The method and its guarantees assume answers can be aggregated by majority vote, and the authors state they do not apply to tasks where aggregation is unnatural or ill-defined, such as open-ended generation. Tight bounds for datasets where most of the model's samples are wrong are not obtained: the authors say this requires an infeasible combinatorial analysis and leave it to future work — which matters because the low-margin regime is exactly where extra samples are being spent. The reported savings are relative to vanilla SC at matched accuracy, so the absolute cost still scales with the budget the user chooses. Models tested are 3B-32B; no frontier-scale or long-CoT reasoning model appears in the evaluation, and the m^(-1/2) margin-distribution assumption underpinning the power law is a claim about dataset classes rather than something checked per benchmark.

## Why it matters here

- **overthinking**: Directly on topic, on the parallel axis of test-time compute rather than the sequential one. Overthinking usually gets framed as a single trace being too long; this paper frames the same waste as too many samples spent on a question the model has already effectively decided. The power-law result gives a concrete shape to the diminishing return of adding samples, so 'more test-time compute' has a predicted, and empirically checked, payoff curve rather than an assumed one. The 4.8x figure is a measurement of how much of vanilla self-consistency's budget is spent past the point of usefulness, which is the parallel-sampling analogue of a chain that keeps going after the answer is settled. Blend-ASC's stopping signal is the margin between the top two answers, which is a different quantity from the token-level confidence that sequential early-exit methods use, and being hyperparameter-free makes it comparable across budgets. The stated inapplicability to open-ended generation bounds how far this transfers: the group's non-verifiable tasks are outside it.

## Entities

- **Concepts**: self-consistency, [test-time compute scaling](../../../../wiki/concepts/test-time-compute-scaling.md), sample efficiency, dynamic sample allocation, answer margin, power-law scaling, mode estimation, majority voting, compute budget allocation across questions
- **Methods**: Blend-ASC, self-consistency (SC), Adaptive Self-Consistency (ASC), Early-Stopping Self-Consistency, PPR-1v1, empirical mode estimation, chain-of-thought prompting
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH](../../../../wiki/datasets/math.md), [MMLU](../../../../wiki/datasets/mmlu.md), [GPQA-Diamond](../../../../wiki/datasets/gpqa-diamond.md)

Tags: `self-consistency`, `test-time compute`, `sample efficiency`, `adaptive sampling`, `majority voting`, `scaling law`, `efficient reasoning`, `chain-of-thought`

---

Record id: `title:f4c083a2823b7a48`
