# self-refine

<!-- auto:begin -->

Self-refine is iteratively revising a generated output using feedback, used as an outer-loop test-time-scaling strategy. In this archive, Decoding Time Verification (DTV) composes with a self-refine outer loop rather than substituting for it when translating code, and a systematic comparison of eight prompting strategies under equal sampling budget finds plain Chain-of-Thought eventually dominates self-refine and every other more elaborate strategy as the sampling budget grows.

- **Kind**: method
- **Also called**: Self-Refine
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [best-of-N](best-of-n.md), [Chain-of-Thought (CoT)](chain-of-thought-cot.md), [Direct Prompting](direct-prompting.md), [Gemma-4-E4B](../models/gemma-4-e4b.md), [GPQA](../datasets/gpqa.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3-8B-Instruct](../models/llama-3-8b-instruct.md), [majority voting / self-consistency](majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [Multi-Agent Debate](multi-agent-debate.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-4B-Instruct-2507](../models/qwen3-4b-instruct-2507.md)

## Appears in

- [Verifier-Guided Code Translation via Meta-Step Decoding](../../archive/papers/2026/arxiv-2605-17626/summary.md) — Decoding Time Verification (DTV) interleaves code generation with deterministic verifier calls (compiler, type checker) at structural boundaries, using structure-aware rollback and diagnostic feedback instead of post-hoc filtering, to translate code more accurately and more token-efficiently than resampling-based test-time scaling.
- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
