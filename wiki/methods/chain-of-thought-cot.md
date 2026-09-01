# Chain-of-Thought (CoT)

<!-- auto:begin -->

Chain-of-Thought is used across sources both as a baseline prompting strategy and as a target of critical study: a systematic comparison of 8 prompting strategies finds plain CoT eventually dominates every other strategy for majority-vote test-time scaling under equal sampling budget, and Understanding LLM Reasoning for Abstractive Summarization includes CoT among its evaluated augmentation-based reasoning strategies, finding reasoning strategies trade off summary quality against factual faithfulness.

- **Kind**: method
- **Also called**: CoT
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [Direct Prompting](direct-prompting.md), [Gemini 2.5 Flash](../models/gemini-2-5-flash.md), [GPQA](../datasets/gpqa.md), [GPT-4.1](../models/gpt-4-1.md), [GPT-4o-mini](../models/gpt-4o-mini.md), [GPT-5](../models/gpt-5.md), [GSM-Hard](../datasets/gsm-hard.md), [GSM8K](../datasets/gsm8k.md), [LLaMA-3-8B-Instruct](../models/llama-3-8b-instruct.md), [majority voting / self-consistency](majority-voting-self-consistency.md), [MATH500](../datasets/math500.md), [Multi-Agent Debate](multi-agent-debate.md), [o1](../models/o1.md), [o3](../models/o3.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [self-refine](self-refine.md)

## Appears in

- [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1356/summary.md) — Systematically compares 8 prompting strategies under equal sampling budget for majority-vote test-time scaling across 6 LLMs x 6 benchmarks, finding plain Chain-of-Thought eventually dominates every more elaborate strategy as sampling time N grows -- because CoT has more easy/fewer hard questions and a flatter wrong-answer distribution -- and shows combining per-question difficulty-adaptive scaling with per-question optimal-strategy selection lifts GSM8K accuracy from 86.0% to 97.4% (Majority@10) and MATH-500 from 15.2% to 61.0%.
- [Understanding LLM Reasoning for Abstractive Summarization](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-859/summary.md) — The first large-scale, systematic evaluation of 8 reasoning prompting strategies (across augmentation, organization, reflection paradigms) and 3 Large Reasoning Models on abstractive summarization across 8 datasets finds reasoning is not a panacea for this task -- there is a statistically significant quality-faithfulness trade-off, and increasing an LRM's internal reasoning budget does not reliably improve, and can actively reduce, factual consistency.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
