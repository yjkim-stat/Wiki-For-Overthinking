<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008733>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

FROST uses attention weights to identify and prune sentence-level 'reasoning outliers' from a reasoning model's chain of thought, reporting an average 69.68% token reduction and 26.70% accuracy gain over the base model on four maths benchmarks.

## Problem

Reasoning models emit long chains of thought whose length is not matched to the difficulty of the question, raising cost and, the authors argue, reliability. Existing efficiency methods act through prompting (TALE), supervised fine-tuning (DRP) or reinforcement learning (SelfBudgeter, ThinkLess); what was open is whether the model's own attention signal identifies which parts of a trajectory can be dropped without losing the steps the answer depends on.

## Contributions

- The notion of a reasoning outlier: a sentence in a chain of thought that attention marks as uncritical to the answer
- An attention-based mechanism that removes such outliers at sentence granularity without retraining the model
- A theoretical argument that the pruning preserves reasoning capacity while eliminating outliers
- Evaluation on four maths benchmarks with two reasoning models reporting 69.68% average token reduction and 26.70% average accuracy gain over the base model, plus direct attention-statistic evidence (15.97% lower max infinity norm, 91.09% lower average kurtosis)

## Method

FROST introduces the notion of a reasoning outlier: a sentence in the reasoning trajectory that attention weights mark as uncritical to the downstream answer. It scores segments of the chain of thought using attention and removes the outliers at sentence granularity, yielding a shorter trajectory. The paper argues theoretically that the pruning preserves the model's reasoning capacity while removing outliers, and measures the effect on attention statistics directly (maximum infinity norm and kurtosis of the attention distribution) as evidence that the outliers being removed are the ones the notion names. It is applied to off-the-shelf reasoning models rather than requiring retraining.

## Results

Evaluated on GSM8K, MATH500, AIME24 and Minerva with Phi-4-Reasoning and GPT-OSS-20B, against TALE (prompt-based), DRP (SFT-based), SelfBudgeter (RL-based), ThinkLess (RL-based) and the base models. Headline: an average 69.68% reduction in token usage and a 26.70% improvement in accuracy over the base model. Per-benchmark with Phi-4-Reasoning: GSM8K 93.11% at 154.33 tokens; MATH500 59.80% at 344.37 tokens; AIME24 26.67% at 899.80 tokens; Minerva 27.16% at 401.19 tokens. On attention-outlier metrics FROST reduces the maximum infinity norm by 15.97% and the average kurtosis by 91.09% relative to the base model.

## Limitations

The authors state the method is restricted to mathematical reasoning tasks while reasoning models also target domains such as coding, and that FROST may still occasionally prune low-attention but important reasoning steps, which is their own explanation for why its accuracy is not best against every baseline on every benchmark. That caveat qualifies the headline: the 26.70% figure is an average improvement measured against the base model, not against the strongest competing efficiency method, and the paper concedes it does not lead all baselines on accuracy. A reader should also weigh the absolute scores, which are modest for a dedicated reasoning model (59.80% on MATH500, 26.67% on AIME24, i.e. roughly two of twenty-four problems), so the comparison rests on how the base configuration was decoded, which the supplied material does not pin down.

## Why it matters here

- **overthinking**: On-topic and directly about the accuracy/length tradeoff. FROST is a training-free intervention that shortens a chain of thought after the fact using the model's own attention, which places it on a different axis from the RL and prompting methods it compares against (TALE, ThinkLess, SelfBudgeter, DRP) and makes it applicable to models the group cannot retrain. Two things are worth carrying into the topic: the claim that accuracy rises rather than falls as 69.68% of tokens are removed, which if it holds is evidence that a substantial fraction of a long chain is not merely wasteful but actively harmful; and the authors' own concession that pruning sometimes drops low-attention but important steps, which is the failure mode any attention-based stopping criterion inherits. The comparison baseline for the 26.70% accuracy figure is the base model rather than the best competitor, so it does not establish FROST as the strongest method.

## Entities

- **Concepts**: reasoning outliers, [efficient reasoning](../../../../wiki/concepts/efficient-reasoning.md), chain-of-thought pruning, attention as a saliency signal, [token budget](../../../../wiki/concepts/token-budget.md), attention kurtosis / infinity norm
- **Methods**: FROST, attention-weight pruning, TALE, [DRP](../../../../wiki/methods/drp.md), [SelfBudgeter](../../../../wiki/methods/selfbudgeter.md), [ThinkLess](../../../../wiki/methods/thinkless.md), [Phi-4-Reasoning](../../../../wiki/methods/phi-4-reasoning.md), [GPT-OSS-20B](../../../../wiki/methods/gpt-oss-20b.md)
- **Datasets**: [GSM8K](../../../../wiki/datasets/gsm8k.md), [MATH500](../../../../wiki/datasets/math500.md), [AIME24](../../../../wiki/datasets/aime-2024.md), [Minerva](../../../../wiki/datasets/minerva.md)

Tags: `overthinking`, `efficient-reasoning`, `chain-of-thought`, `attention`, `token-reduction`, `math-reasoning`, `training-free`

---

Record id: `title:e2cdfd631cb4eda0`
