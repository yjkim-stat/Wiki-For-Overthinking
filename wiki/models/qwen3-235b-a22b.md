# Qwen3-235B-A22B

<!-- auto:begin -->

Qwen3-235B-A22B is a large mixture-of-experts reasoning model (235B total / 22B active parameters) used as an evaluated model across several reasoning-trace analysis papers, including Thought Injection (testing whether injected reasoning snippets causally change final answers), RFMDataset (revealing failure modes in mathematical proof reasoning), TRACE (decomposing reasoning traces into sub-thought progression graphs), and AlgBench (testing algorithmic understanding).

- **Kind**: model
- **Also called**: Qwen3-235B
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 5

**Related**: [adaptive test-time compute](../concepts/adaptive-test-time-compute.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [ASDiv](../datasets/asdiv.md), [Claude-3.7-Sonnet-Thinking](claude-3-7-sonnet-thinking.md), [Compute-optimal inference](../concepts/compute-optimal-inference.md), [DeepSeek-R1](deepseek-r1.md), [DeepSeek-R1-0528](deepseek-r1-0528.md), [DeepSeek-R1-Distill-Llama-70B](deepseek-r1-distill-llama-70b.md), [DeepSeek-V3.2-Speciale](deepseek-v3-2-speciale.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GPQA](../datasets/gpqa.md), [GPT-o1](gpt-o1.md), [gpt-o3](gpt-o3.md), [gpt-oss-120b](gpt-oss-120b.md), [greedy decoding](../methods/greedy-decoding.md), [GSM8K](../datasets/gsm8k.md), [MATH500](../datasets/math500.md), [Overthinking](../concepts/overthinking.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3-32B](qwen3-32b.md), [Qwen3-8B](qwen3-8b.md), [Qwen3 family (0.6B-235B-A22B)](qwen3-family-0-6b-235b-a22b.md), [Self-Consistency](../methods/self-consistency.md), [SimpleQA](../datasets/simpleqa.md)

## Appears in

- [Reasoning Traces Shape Outputs but Models Won’t Say So](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1986/summary.md) — Thought Injection causally inserts synthetic reasoning snippets into an LRM's <think> trace and shows the injected reasoning reliably changes the model's final answer, but when asked to explain the change, models disclose the injected influence in under 10% of extreme-hint cases -- instead fabricating unrelated, aligned-appearing explanations whose activations systematically align with sycophancy-related directions.
- [Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-582/summary.md) — RFMDataset uses 200 manually-curated mathematical proof problems and a 10-category fine-grained error taxonomy (judged by LLM-as-a-judge, validated against human labels) to reveal that even top reasoning models (GPT-o1/o3, Claude-3.7-Sonnet-Thinking, Qwen3-235B, DeepSeek-R1) achieve under 20-60% proof accuracy, dominated by logical violation, hidden assumption, vague argument, and incomplete proof failures that self-reflection prompting only modestly improves.
- [Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days Later”? Towards Structural Understanding of LLM Overthinking](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-773/summary.md) — TRACE decomposes reasoning traces into sub-thoughts and labeled progression graphs across 14 thinking models and 6 domains, finding thinking helps only within a narrow middle ground (5-20x more compute wasted on simple tasks with no gain, and no benefit at all once model scale exceeds ~4-8B or task difficulty exceeds representational capacity), identifies two overthinking-driving thought-progression patterns (Explorer, Late Landing), and redefines overthinking structurally as continuation past the point where marginal return per sub-thought drops below a threshold.
- [AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1885/summary.md) — AlgBench replaces problem-centric algorithmic benchmarks (which conflate multiple algorithms per problem and risk contamination) with 3,000 expert-curated, contamination-free problems each isolating exactly one of 27 algorithms under a six-category taxonomy, finding LRMs handle non-optimized/Euclidean-structured algorithms well (up to 92%) but collapse on global-optimization tasks like dynamic programming (~49%), that model-parameter scaling barely helps in exactly those weak categories, and that 'strategic over-shifts' -- models abandoning a correct algorithmic design mid-execution -- are specifically triggered by necessary low-entropy tokens (numeric constants, structural delimiters) that standard maximum-entropy RL training penalizes as if they were uncertain, unproductive continuations.
- [Adaptive Thinking: Large Language Models Know When to Think in Latent Space](../../archive/papers/2026/title-cc91145094e2b147/summary.md) — Sonata predicts a query's self-consistency from the last-layer hidden state at prefill and uses that prediction to set the thinking budget before the model starts reasoning.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
