# Phi-4

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [MATH](../datasets/math.md), [PRM800K](../datasets/prm800k.md), [Qwen3-1.7B](qwen3-1-7b.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-4B](qwen3-4b.md), [Qwen3-8B](qwen3-8b.md), [ScienceQA](../datasets/scienceqa.md), [StrategyQA](../datasets/strategyqa.md)

## Appears in

- [Ranking Reasoning LLMs under Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1544/summary.md) — Formalizes ranking reasoning LLMs under test-time scaling as inference over a dense response tensor of repeated stochastic trials, compares 72 ranking methods (paired-comparison, IRT, voting, graph/spectral) across 20 models and four Olympiad math benchmarks, and finds Bayes_R0@N (Bayesian mean with an empirical greedy-decoding prior) is the most stable low-budget ranking method -- though its greedy prior can introduce systematic bias when greedy and stochastic sampling disagree.
- [ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-536/summary.md) — ReProbe is a lightweight (<10M-parameter) transformer probe trained on a frozen LLM's internal states (hidden states, attention, logits) to predict step-level reasoning correctness, matching or exceeding Process Reward Models up to 810x larger for test-time-scaling verification, at 2.6-25x faster inference, and can be trained fully self-supervised (the model annotating its own reasoning) with no human labels or Monte Carlo rollouts.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
