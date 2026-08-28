# o4-mini

<!-- auto:begin -->

o4-mini is cited in this archive by EchoCoT, a security study showing its hidden chain-of-thought (and that of other black-box reasoning models) can be recovered near-verbatim through ordinary API tool-calling, because reasoning state must persist across tool calls within a turn, and by REST's multi-question stress test of large reasoning models.

- **Kind**: model
- **Also called**: O4-mini
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [ARC-C](../datasets/arc-c.md), [BBH](../datasets/bbh.md), [benchmark saturation](../concepts/benchmark-saturation.md), [Claude-Opus-4.5](claude-opus-4-5.md), [DeepScaleR-1.5B](deepscaler-1-5b.md), [DeepSeek-R1](deepseek-r1.md), [deepseek-v4-flash](deepseek-v4-flash.md), [Direct Prompting](../methods/direct-prompting.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [GLM-5.2](glm-5-2.md), [GPQA-Diamond](../datasets/gpqa-diamond.md), [GSM8K](../datasets/gsm8k.md), [HMMT25](../datasets/hmmt25.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [LiveCodeBench](../datasets/livecodebench.md), [LiveCodeBench (v5)](../datasets/livecodebench-v5.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [OpenThoughts](../datasets/openthoughts.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-30B-A3B](qwen3-30b-a3b.md), [Qwen3.5-Plus](qwen3-5-plus.md)

## Appears in

- [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](../../archive/papers/2026/arxiv-2608-20055/summary.md) — A security study showing that the hidden chain-of-thought of a black-box reasoning model can be recovered near-verbatim through ordinary API tool-calling, because reasoning state must be retained across tool calls within a turn.
- [REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1296/summary.md) — REST (Reasoning Evaluation through Simultaneous Testing) concatenates multiple questions from an existing benchmark into a single prompt to stress-test LRMs' multi-context reasoning; across 30+ models and 9 benchmarks it finds even SOTA models like DeepSeek-R1 degrade substantially (e.g. -31.6% on AIME25), that the 'overthinking trap' is a primary cause, that Long2Short-trained models are more robust, and that REST reveals sharp performance gaps among models that look identical under traditional single-question evaluation.
- [AMO-Bench: Large Language Models Still Struggle in High School Math Competitions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-101/summary.md) — AMO-Bench is a 50-problem, IMO-difficulty-or-harder, entirely original math benchmark built to avoid the saturation and memorization issues of AIME24/25, on which even the best of 36 evaluated LLMs (Gemini-3-Pro) reaches only 63.1% accuracy, model performance grows near-linearly with the logarithm of output length (still-unsaturated evidence that test-time scaling keeps paying off), and a manual failure analysis finds brute-force enumeration and improper strategy selection -- reasoning deficiency, not missing math knowledge -- as the dominant error modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
