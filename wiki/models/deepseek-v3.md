# DeepSeek-V3

<!-- auto:begin -->

DeepSeek-V3 is used in these sources as one of many evaluated LRMs/LLMs rather than a subject of study: Rt-LRM includes it among 26 models in a unified truthfulness/safety/efficiency red-teaming benchmark finding over 60% of samples exhibit overthinking (more than double the clean-input token count) under attack, and BloomEval's cited note does not name DeepSeek-V3 specifically.

- **Kind**: model
- **Also called**: DeepSeek v3
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [DeepSeek-R1](deepseek-r1.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [Grok-3](grok-3.md), [GSM8K](../datasets/gsm8k.md), [Kimi-k1.5](kimi-k1-5.md), [MATH](../datasets/math.md), [o1](o1.md), [o3-mini](o3-mini.md), [Omni-MATH](../datasets/omni-math.md), [OpenAI o1-mini](openai-o1-mini.md), [Qwen3-Max](qwen3-max.md), [s1-32B](s1-32b.md)

## Appears in

- [Red Teaming Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1034/summary.md) — Rt-LRM is a unified 30-task benchmark evaluating large reasoning models along truthfulness, safety and efficiency, testing both CoT-hijacking (direct interference with the reasoning process) and prompt-induced impacts (jailbreaks or overthinking triggers); across 26 models it finds LRMs are consistently less trustworthy than their own base LLMs, that explicit reasoning can amplify safety risk and inefficiency under attack, and that over 60% of tested samples exhibit overthinking (more than double the clean-input token count) across most models.
- [BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1262/summary.md) — BloomEval maps each step of an LRM's reasoning trace onto Bloom's six-level cognitive taxonomy (Remember through Create) via a Cognitive Hierarchy Trace (CHT), defining structural anomalies -- hierarchy break (reasoning never reaches the required cognitive level), hierarchy jump (skipping intermediate levels), and overthinking (invoking cognitive operations exceeding what the task needs) -- and finds these anomalies are common even in *correct* answers (e.g. Grok-3 shows a 0.185 hierarchy-jump rate on correct answers), demonstrating that answer accuracy alone cannot detect incoherent or wasteful reasoning structure.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
