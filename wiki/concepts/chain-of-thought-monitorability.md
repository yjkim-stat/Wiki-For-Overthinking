# Chain-of-thought monitorability

<!-- auto:begin -->

Whether a model's reasoning trace can be watched to catch misbehaviour before it acts - which the archive's sources split into two prerequisites, neither of them guaranteed. Risky Business treats monitorability as depending on faithfulness and in tension with safety: an agent must follow its trace closely enough for the trace to predict what it does, yet a model that follows its trace perfectly also executes tampered unsafe reasoning, which their Targeted Reasoning Replacement edit inserts across 77 HazMart scenarios. The trace-stealing paper attacks the other prerequisite, access: the encrypted chain-of-thought blocks returned by the Anthropic, OpenAI and Google APIs are interchangeable across sessions, users and models within one provider, and a weaker sibling model used as a decryption oracle recovers the hidden traces verbatim - so a trace withheld from the user is not thereby unreadable. The sources keep this distinct from faithfulness, which asks whether the trace reflects the computation rather than whether anyone can see it.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [Chain-of-thought faithfulness](chain-of-thought-faithfulness.md), [gpt-oss-120b](../methods/gpt-oss-120b.md), [MMLU](../datasets/mmlu.md), [Qwen3-8B](../datasets/qwen3-8b.md), [QwQ-32B](../methods/qwq-32b.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [Stealing Reasoning Traces from Proprietary LLM APIs](../../archive/papers/2026/arxiv-2608-09867/summary.md) — Shows that the encrypted chain-of-thought blocks returned by Anthropic, OpenAI and Google APIs are interchangeable across sessions, users and models within a provider, and uses a weaker sibling model as a decryption oracle to recover hidden reasoning traces verbatim.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
