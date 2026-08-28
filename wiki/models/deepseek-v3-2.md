# DeepSeek-V3.2

<!-- auto:begin -->

DeepSeek-V3.2 is used in these sources as an annotator/judge model rather than a subject of study: TRACE uses it (alongside Qwen3.5-Plus and KIMI-K2.5) as one of three LRMs annotating the safety of prompts, reasoning traces and responses. Timely Machine is a separate, unrelated source that happens to share this concept's promotion threshold but does not name DeepSeek-V3.2 specifically in its cited note.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME](../datasets/aime.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemma-4-E4B](gemma-4-e4b.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [Kimi-K2.5](kimi-k2-5.md), [MATH](../datasets/math.md), [Qwen3.5-Plus](qwen3-5-plus.md), [Qwen3-8B](qwen3-8b.md)

## Appears in

- [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](../../archive/papers/2026/arxiv-2608-24232/summary.md) — TRACE is a benchmark that extends LLM-safety evaluation from prompts and final responses to the reasoning traces of large reasoning models, with evidence-grounded annotations for each safety label.
- [Timely Machine: Awareness of Time Makes Test-Time Scaling Agentic](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-211/summary.md) — Timely Machine redefines test-time scaling in agentic settings as wall-clock time rather than token/generation length (since unpredictable tool-call latency decouples the two), introduces Timely-Eval to benchmark this, and trains Timely-RL (SFT cold-start + a sinusoidal time-utilization RL reward) so an 8B model learns to query elapsed time and dynamically size its reasoning to a time budget, beating much larger models' on-time completion rates and outperforming Qwen3-8B on all three general-reasoning benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
