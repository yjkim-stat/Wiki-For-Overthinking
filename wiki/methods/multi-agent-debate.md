# Multi-Agent Debate

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: method
- **Also called**: multi-agent debate
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [BBH (Big-Bench Hard)](../datasets/bbh-big-bench-hard.md), [Chain-of-Thought (CoT, baseline)](chain-of-thought-cot-baseline.md), [Direct Prompting](direct-prompting.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [Llama-3.1-8B](../models/llama-3-1-8b.md), [majority voting / self-consistency](majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [MMLU-Pro](../datasets/mmlu-pro.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Self-Consistency](self-consistency.md), [self-refine](self-refine.md)

## Appears in

- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.
- [Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-srw-1/summary.md) — A systematic Pareto-front analysis of four test-time-scaling pipelines (self-consistency, self-refinement, debate, mixture-of-agents) across 34 configurations finds mixture-of-agents dominates the compute-accuracy frontier (+7.1pp over CoT at 15-20x compute, beating self-consistency and debate by 2.7pp/1.4pp at matched budgets), that debate should scale agents rather than rounds, that MoA is Pareto-optimal when proposer models outnumber layers by one, and that harder tasks benefit far more from added test-time compute than easy ones (+9.0pp vs. +2.2pp), while self-refinement underperforms even the plain chain-of-thought baseline throughout.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
