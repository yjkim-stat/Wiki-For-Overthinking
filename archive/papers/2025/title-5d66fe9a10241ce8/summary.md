<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/115605>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

Shows that extending a reasoning model's thinking trace improves accuracy only up to a point and then declines from overthinking, and proposes sampling multiple independent short traces (parallel thinking) with majority vote as a more effective use of the same compute budget.

## Problem

Whether letting reasoning models 'think more' at test time via longer thinking traces truly improves reasoning, versus previous belief that extended thinking (prompted continuation, e.g. 'Wait') straightforwardly helps.

## Contributions

- Empirically shows a consistent non-monotonic pattern: extending thinking traces improves accuracy initially, then declines due to overthinking
- Explains the pattern with a simple probabilistic model: additional thinking increases output variance, creating an illusion of improved reasoning while undermining precision
- Argues observed gains from 'more thinking' are largely artifacts of the link between model uncertainty and the evaluation metric, not true reasoning improvement
- Proposes parallel thinking: generating multiple independent reasoning paths within the same inference budget and selecting the most consistent answer via majority vote
- Reports up to 20% higher accuracy for parallel thinking versus extended thinking at equal inference budget

## Method

Performs a detailed empirical study across multiple reasoning models and benchmarks of how accuracy changes as thinking traces are extended (e.g. via 'Wait' / 'Let me rethink' prompts). Builds a simple probabilistic model to explain why extended thinking raises output variance rather than genuinely improving reasoning. As an alternative test-time scaling strategy, proposes parallel thinking: sample multiple independent reasoning paths under the same total inference budget and pick the answer by majority vote (Best-of-N style), rather than lengthening a single chain.

## Results

Extended single-chain thinking shows an initial accuracy rise followed by decline (overthinking) across the models and benchmarks tested. Parallel thinking (majority vote over independent reasoning paths at equal inference budget) achieves up to 20% higher accuracy than extended thinking.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: A direct, central treatment of the topic: demonstrates the accuracy/reasoning-length curve is non-monotonic (gains then decline from overthinking) across models and benchmarks, gives a mechanistic (variance-based) explanation for why extended thinking looks helpful before it isn't, and proposes an explicit alternative — parallel thinking / majority vote — as a better way to spend a fixed test-time compute budget than lengthening a single chain.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [test-time scaling](../../../../wiki/concepts/test-time-scaling.md), output variance under extended thinking, parallel thinking, best-of-n sampling, majority voting
- **Methods**: parallel thinking, [best-of-n sampling](../../../../wiki/methods/best-of-n-sampling.md), [majority voting](../../../../wiki/methods/majority-voting.md), probabilistic model of output variance
- **Datasets**: _none recorded_

Tags: `overthinking`, `test-time-scaling`, `parallel-thinking`, `best-of-n`, `reasoning-length`, `output-variance`

## Abstract

Abstract Recent trends in test-time scaling for reasoning models (e.g., OpenAI o1, DeepSeek R1) have led to a popular belief that extending thinking traces using prompts like “Wait” or “Let me rethink” can improve performance. This raises a natural question: Does thinking more at test-time truly lead to better reasoning? To answer this question, we perform a detailed empirical study across models and benchmarks, which reveals a consistent pattern of initial performance improvements from additional thinking followed by a decline, due to "overthinking". To understand this non-monotonic trend, we consider a simple probabilistic model, which reveals that additional thinking increases output variance—creating an illusion of improved reasoning while ultimately undermining precision. Thus, observed gains from "more thinking" are not true indicators of improved reasoning, but artifacts stemming from the connection between model uncertainty and evaluation metric. This suggests that test-time scaling through extended thinking is not an effective way to utilize the inference thinking budget. Recognizing these limitations, we introduce an alternative test-time scaling approach, parallel thinking, inspired by Best-of-N sampling. Our method generates multiple independent reasoning paths within the same inference budget and selects the most consistent response via majority vote, achieving up to 20% higher accuracy compared to extended thinking. This provides a simple yet effective mechanism for test-time scaling of reasoning models.

---

Record id: `title:5d66fe9a10241ce8`
