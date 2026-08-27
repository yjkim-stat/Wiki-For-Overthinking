# Qwen3-30B-A3B

<!-- auto:begin -->

An open-weight (mixture-of-experts) reasoning model used across sources as an evaluation/generator subject: named among frontier models compared for parallel-reasoning behavior in Parason, and as one of the three model-benchmark settings (alongside Qwen3-8B and QwQ-32B) on which Reflection Steering's training-free activation-space intervention is evaluated, reducing thinking tokens 16.9% on average without harming accuracy.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC](../datasets/amc.md), [AMC23](../datasets/amc23.md), [ARC-C](../datasets/arc-c.md), [BBH](../datasets/bbh.md), [critical-path latency](../concepts/critical-path-latency.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [GPQA-D](../datasets/gpqa-d.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GPT-5.5](gpt-5-5.md), [GSM8K](../datasets/gsm8k.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-14B](qwen3-14b.md), [Qwen3-8B](../methods/qwen3-8b.md), [QwQ-32B](../methods/qwq-32b.md)

## Appears in

- [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](../../archive/papers/2026/arxiv-2608-24658/summary.md) — Parason distinguishes two forms of parallel reasoning -- AND-branch Subtask Parallelism and OR-branch Trial Parallelism -- shows Trial Parallelism dominates on hard reasoning traces, and trains models to convert sequential CoT into grammar-structured parallel trajectories that a real inference engine executes for ~1.7x wall-clock speedup with competitive accuracy.
- [Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference](../../archive/papers/2026/arxiv-2608-25542/summary.md) — Reflection Steering is a training-free activation-space intervention that isolates reflection-associated computation from general reasoning via PCA-purified, orthogonalized steering directions calibrated per layer, cutting thinking tokens by 16.9% on average across six model-benchmark settings with accuracy statistically equivalent to the raw model.
- [The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1239/summary.md) — Identifies a two-stage 'Reasoning Dynamics' structure in LRM chains-of-thought -- a Pre-RCP Active Reasoning stage where thinking length and content length compensate for each other, followed by a Post-RCP Converged Reasoning stage where the semantic trajectory has stabilized and further thinking is redundant -- defines the boundary as the instance-specific Reasoning Completion Point (RCP), and builds RCPD, an online detector (monitoring the rank of the </think> token) that truncates post-RCP overthinking, cutting tokens up to 44% while preserving or improving accuracy-per-token across four models and three benchmarks.
- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
