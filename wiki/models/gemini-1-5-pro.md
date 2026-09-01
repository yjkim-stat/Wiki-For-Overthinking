# Gemini-1.5-Pro

<!-- auto:begin -->

Gemini 1.5 Pro is used as an evaluated/reference model in SCOPE (Programming over Thinking, which replaces long natural-language reasoning chains with a two-stage multi-agent pipeline for multi-constraint planning) and in TRUTHFULVQA's evaluation of multimodal LLM truthfulness under misleading visual-linguistic prompts.

- **Kind**: model
- **Also called**: Gemini-1.5-Pro
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [Chain-of-Thought (CoT, baseline)](../methods/chain-of-thought-cot-baseline.md), [Claude-3.5-Sonnet](claude-3-5-sonnet.md), [Claude-3.7-Sonnet](claude-3-7-sonnet.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPT-4o](gpt-4o.md), [GPT-5](gpt-5.md), [gpt-o3](gpt-o3.md), [o4-mini](o4-mini.md)

## Appears in

- [Programming over Thinking: Efficient and Robust Multi-Constraint Planning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-2028/summary.md) — SCOPE replaces long natural-language reasoning chains for multi-constraint planning with a two-stage, multi-agent pipeline that infers a query's combination/constraint structure once and compiles it into reusable, deterministic solver functions (Combination/Filter/Deliver), reaching 93.1% success on TravelPlanner with GPT-4o (a 61.6-point gain over CoT) while cutting inference cost 1.4x and time 4.67x versus the best baseline.
- [When Slower Isn’t Truer: Inverse Scaling Law of Truthfulness in Multimodal Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-63/summary.md) — TRUTHFULVQA, a 5,000-image hierarchical human-annotated benchmark testing multimodal LLM truthfulness under progressively misleading visual-linguistic prompts, uncovers an inverse scaling law of truthfulness: slow-thinking (reasoning) MLLMs are consistently less truthful than their fast-thinking chat counterparts of the same family, and larger reasoning models show worse calibration despite generating more reasoning tokens.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
