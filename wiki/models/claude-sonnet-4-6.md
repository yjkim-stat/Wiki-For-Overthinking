# Claude Sonnet 4.6

<!-- auto:begin -->

A Claude model appearing in this archive only inside panels. It is one of 21 judges in the large-scale LLM-as-a-judge reliability evaluation, whose findings -- exact-match agreement overstating chance-corrected discrimination by 34 to 41 points across every judge and provider, and test-retest reliability coexisting with severe position bias -- are reported over the panel rather than per model. It also appears in the reasoning-trace extraction work, both in the cross-model compatibility map and as the model shown reasoning over a synthetic persona's private data while handling a flight-booking task, which is one of that paper's two illustrative leakage examples. Neither source reports a capability result attributed to it.

- **Kind**: model
- **Also called**: Claude Sonnet 4.6
- **Topics**: [reasoning-evaluation](../topics/reasoning-evaluation.md), [reasoning-faithfulness](../topics/reasoning-faithfulness.md)
- **Sources**: 2

**Related**: [chain of thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Claude Haiku 4.5](claude-haiku-4-5.md), [Claude Sonnet 4.5](claude-sonnet-4-5.md), [construct validity](../concepts/construct-validity.md), [DeepSeek-V3.2](deepseek-v3-2.md), [Gemini-2.5-Flash](gemini-2-5-flash.md), [Gemini-3.1-Pro](gemini-3-1-pro.md), [Gemini-3.5-Flash](gemini-3-5-flash.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [gpt-5.6-luna](gpt-5-6-luna.md), [GPT-5.6-Sol](gpt-5-6-sol.md), [GPT-5.6 Terra](gpt-5-6-terra.md), [GPT-5-mini](gpt-5-mini.md), [Humanity's Last Exam](../datasets/humanity-s-last-exam.md), [Kimi-K2.5](kimi-k2-5.md), [knowledge distillation](../methods/knowledge-distillation.md), [Llama-3.3-70B](llama-3-3-70b.md), [LLM-as-a-judge](../methods/llm-as-a-judge.md), [meta-evaluation](../concepts/meta-evaluation.md), [monitorability](../concepts/monitorability.md), [MT-Bench](../datasets/mt-bench.md), [o4-mini](o4-mini.md), [persistent semantic entity](../concepts/persistent-semantic-entity.md), [position bias](../concepts/position-bias.md), [prompt injection](../concepts/prompt-injection.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted reasoning blocks major providers return to clients are interchangeable across sessions, users and models within a provider, and measures four consequences of that interchangeability -- distillation, third-party secret extraction, hazardous-content exposure and monitor-invisible prompt injection -- before responsible disclosure closed it.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](../../archive/papers/2026/local-504cc53656b06ab4/summary.md) — Evaluates 21 LLM judges across three benchmarks and three protocols over ~541,000 judgments, and shows the field's standard validation metric — exact-match agreement — overstates chance-corrected discrimination by 34-41 points universally, while high test-retest reliability can coexist with severe position bias.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
