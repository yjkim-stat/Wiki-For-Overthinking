# Qwen3-32B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AMC23](../datasets/amc23.md), [Chain-of-thought faithfulness](../concepts/chain-of-thought-faithfulness.md), [Chain-of-thought monitorability](../concepts/chain-of-thought-monitorability.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [gpt-oss-120b](gpt-oss-120b.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [MMLU](../datasets/mmlu.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](../methods/qwen3-8b.md), [QwQ-32B](../methods/qwq-32b.md)

## Appears in

- [Risky Business: Measuring The Faithfulness-Safety Tension](../../archive/papers/2026/arxiv-2608-03745/summary.md) — Introduces HazMart (77 hand-written agentic shopkeeper scenarios) and Targeted Reasoning Replacement, a search-and-replace edit of a model's own reasoning trace, and shows that models which follow their traces more faithfully also follow tampered unsafe traces more often, with two anti-correlated residual-stream directions in QwQ-32B that can be steered independently.
- [When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1080/summary.md) — DTSR (Dynamic Thought Sufficiency in Reasoning) is a training-free early-exit framework where the model itself, at each reflection signal ('Wait', 'Alternatively', etc.), evaluates from a third-person perspective whether its own chain-of-thought so far is sufficient to answer, exiting once a self-assessed sufficiency score crosses a threshold, cutting reasoning length 28.9-34.9% with near-zero accuracy loss across Qwen3-8B/14B/32B and five benchmarks, outperforming NoThinking, NOWAIT, and DEER while also cutting inference latency 25-40% (unlike DEER, which reduces length but increases latency).

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
