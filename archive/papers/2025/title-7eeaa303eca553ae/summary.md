<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/119802>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## In one line

Shows that scaling chain-of-thought length can hurt math reasoning past a domain-dependent optimum, and proposes a self-improvement method that teaches a model to pick the shortest correct response under varying reasoning efforts.

## Problem

Test-time scaling research generally assumes longer chains-of-thought help reasoning, but it was unclear whether excessively long CoTs could actively hurt performance, and whether there is a domain-dependent optimal reasoning length rather than 'longer is always better'.

## Contributions

- Shows that excessively scaling chain-of-thought length can impair reasoning performance on mathematical tasks in certain domains, rather than only saturating.
- Finds that the optimal scaled-length distribution differs across domains.
- Proposes a Thinking-Optimal Scaling strategy: seed data with varying response-length distributions teaches the model different reasoning efforts, then the model self-improves by selecting its shortest correct response across additional problems under different reasoning efforts.
- Self-improved 32B models built on Qwen2.5-32B-Instruct outperform other distillation-based 32B o1-like models and match the teacher model QwQ-32B-Preview.

## Method

Thinking-Optimal Scaling first fine-tunes the model on a small seed set of responses with varying length distributions so it learns to adopt different reasoning efforts (i.e., produce shorter or longer CoTs) for a given problem. The model then generates responses under these different reasoning efforts on additional problems and self-improves by selecting, for each problem, its shortest response that is still correct, training on that selection.

## Results

Self-improved models built on Qwen2.5-32B-Instruct outperform other distillation-based 32B o1-like models across various math benchmarks and achieve performance on par with the teacher model QwQ-32B-Preview that produced the seed data; specific benchmark accuracy figures are not given in the abstract.

## Limitations

The abstract does not name the specific math benchmarks used, nor give exact accuracy numbers versus QwQ-32B-Preview or the compared distilled models; it also does not quantify how much shorter the selected responses are.

## Why it matters here

- **overthinking**: Directly on-topic: the paper's central finding is that scaling CoT length past a domain-specific optimum degrades math reasoning accuracy (an explicit demonstration of overthinking), and it proposes a concrete training method (Thinking-Optimal Scaling, selecting the shortest correct response) to make a model stop at the right reasoning length rather than always thinking longer.

## Entities

- **Concepts**: optimal scaled length distribution, shortest correct response selection, domain-dependent reasoning effort
- **Methods**: Thinking-Optimal Scaling, self-improvement via shortest-correct-response selection, seed data with varying length distributions
- **Datasets**: various math benchmarks (unspecified names in abstract)

Tags: `overthinking`, `chain-of-thought-length`, `test-time-compute`, `self-improvement`, `math-reasoning`

## Abstract

Abstract Recent studies have shown that making a model spend more time thinking through longer Chain of Thoughts (CoTs) enables it to gain significant improvements in complex reasoning tasks. While current researches continue to explore the benefits of increasing test-time compute by extending the CoT lengths of Large Language Models (LLMs), we are concerned about a potential issue hidden behind the current pursuit of test-time scaling: Would excessively scaling the CoT length actually bring adverse effects to a model's reasoning performance? Our explorations on mathematical reasoning tasks reveal an unexpected finding that scaling with longer CoTs can indeed impair the reasoning performance of LLMs in certain domains. Moreover, we discover that there exists an optimal scaled length distribution that differs across different domains. Based on these insights, we propose a Thinking-Optimal Scaling strategy. Our method first uses a small set of seed data with varying response length distributions to teach the model to adopt different reasoning efforts for deep thinking. Then, the model selects its shortest correct response under different reasoning efforts on additional problems for self-improvement. Our self-improved models built upon Qwen2.5-32B-Instruct outperform other distillation-based 32B o1-like models across various math benchmarks, and achieve performance on par with the teacher model QwQ-32B-Preview that produces the seed data.

---

Record id: `title:7eeaa303eca553ae`
