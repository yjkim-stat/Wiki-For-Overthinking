<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models

- **Authors**: _unknown_
- **Venue**: ICLR 2026
- **Published**: 2026-01-01
- **Source**: virtualsite
- **Link**: <https://iclr.cc/virtual/2026/poster/10008460>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## In one line

Plan-and-Budget decomposes queries into sub-questions and allocates test-time token budgets by estimated complexity, using a theoretical model of reasoning as sequential sub-questions to reduce both overthinking and underthinking.

## Problem

LLM inference for complex reasoning is computationally inefficient: models exhibit overthinking, generating verbose and tangential reasoning even for simple queries, while prior fixes that enforce fixed token budgets can instead cause underthinking on harder problems. The authors trace this to unclear problem-solving strategies rather than to reasoning length itself.

## Contributions

- BAM (Budget Allocation Model), a theoretical model of reasoning as a sequence of sub-questions with varying uncertainty
- E3, a metric capturing the tradeoff between correctness and computation efficiency
- Plan-and-Budget, a model-agnostic test-time framework that decomposes queries into sub-questions and allocates token budgets by estimated complexity via adaptive scheduling

## Method

Plan-and-Budget decomposes a complex query into sub-questions and allocates a token budget to each based on its estimated complexity, using an adaptive scheduling procedure grounded in the BAM theoretical model, which treats reasoning as a sequence of sub-questions of varying uncertainty. The E3 metric is introduced to jointly score correctness and computational efficiency.

## Results

Plan-and-Budget achieves up to 70% accuracy gains, 39% token reduction, and a 193.8% improvement in the E3 metric across a range of tasks and models. It raises the efficiency of a smaller model (DS-Qwen-32B) to match that of a larger model (DS-LLaMA-70B) without retraining.

## Limitations

_not recorded_

## Why it matters here

- **overthinking**: Directly targets the paper's central tradeoff: it formalizes overthinking and underthinking as failures of budget allocation across sub-questions of differing uncertainty, and proposes a test-time, model-agnostic method (Plan-and-Budget) to allocate reasoning budget by estimated complexity rather than a fixed cap.

## Entities

- **Concepts**: [overthinking](../../../../wiki/concepts/overthinking.md), [underthinking](../../../../wiki/concepts/underthinking.md), budget allocation model, sub-question decomposition, correctness-efficiency tradeoff
- **Methods**: BAM (Budget Allocation Model), [Plan-and-Budget](../../../../wiki/methods/plan-and-budget.md), E3 metric, adaptive scheduling
- **Datasets**: _none recorded_

Tags: `overthinking`, `underthinking`, `test-time-scaling`, `budget-allocation`, `reasoning-efficiency`

## Abstract

Abstract Large Language Models (LLMs) have achieved remarkable success in complex reasoning tasks, but their inference remains computationally inefficient. We observe a common failure mode in many prevalent LLMs, overthinking, where models generate verbose and tangential reasoning traces even for simple queries. Recent work has tried to mitigate this by enforcing fixed token budgets, however, this can lead to underthinking, especially on harder problems. Through empirical analysis, we identify that this inefficiency often stems from unclear problem-solving strategies. To formalize this, we develop a theoretical model, BAM (Budget Allocation Model), which models reasoning as a sequence of sub-questions with varying uncertainty, and introduce the E3 metric to capture the trade-off between correctness and computation efficiency. Building on theoretical results from BAM, we propose Plan-and-Budget, a model-agnostic, test-time framework that decomposes complex queries into sub-questions and allocates token budgets based on estimated complexity using adaptive scheduling. Plan-and-Budget improves reasoning efficiency across a range of tasks and models, achieving up to 70% accuracy gains, 39% token reduction, and 193.8% improvement in E3. Notably, it improves the efficiency of a smaller model (DS-Qwen-32B) to match the efficiency of a larger model (DS-LLaMA-70B), demonstrating Plan-and-Budget’s ability to close performance gaps without retraining. Our code is available at https://github.com/junhongmit/P-and-B.

---

Record id: `title:f0073c841a41fca9`
