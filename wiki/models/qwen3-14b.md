# Qwen3-14B

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [GPQA-D](../datasets/gpqa-d.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](../methods/qwen3-8b.md)

## Appears in

- [When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1080/summary.md) — DTSR (Dynamic Thought Sufficiency in Reasoning) is a training-free early-exit framework where the model itself, at each reflection signal ('Wait', 'Alternatively', etc.), evaluates from a third-person perspective whether its own chain-of-thought so far is sufficient to answer, exiting once a self-assessed sufficiency score crosses a threshold, cutting reasoning length 28.9-34.9% with near-zero accuracy loss across Qwen3-8B/14B/32B and five benchmarks, outperforming NoThinking, NOWAIT, and DEER while also cutting inference latency 25-40% (unlike DEER, which reduces length but increases latency).
- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1239/summary.md) — Identifies a two-stage 'Reasoning Dynamics' structure in LRM chains-of-thought -- a Pre-RCP Active Reasoning stage where thinking length and content length compensate for each other, followed by a Post-RCP Converged Reasoning stage where the semantic trajectory has stabilized and further thinking is redundant -- defines the boundary as the instance-specific Reasoning Completion Point (RCP), and builds RCPD, an online detector (monitoring the rank of the </think> token) that truncates post-RCP overthinking, cutting tokens up to 44% while preserving or improving accuracy-per-token across four models and three benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
