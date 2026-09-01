# DeepSeek-V3.2-Speciale

<!-- auto:begin -->

DeepSeek-V3.2-Speciale is used in these sources as a top-tier evaluated model on hard math benchmarks: AMO-Bench includes it among the top-tier models (alongside Gemini-3-Pro, Qwen3-Max-Thinking) forming a clear top performance tier on its 50 original hard problems, and AlgBench evaluates it among its frontier LRMs on the algorithm-centric benchmark, where it shows strong performance on non-optimized/Euclidean algorithms but the same global-optimization collapse pattern as other top models.

- **Kind**: model
- **Also called**: DeepSeek-v3.2-Speciale
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [benchmark saturation](../concepts/benchmark-saturation.md), [Claude-Opus-4.5](claude-opus-4-5.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-2.5-Pro](gemini-2-5-pro.md), [Gemini-3-Pro](gemini-3-pro.md), [GLM-4.6](glm-4-6.md), [gpt-o3](gpt-o3.md), [gpt-oss-120b](gpt-oss-120b.md), [HMMT25](../datasets/hmmt25.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Qwen3-235B-A22B](qwen3-235b-a22b.md)

## Appears in

- [AMO-Bench: Large Language Models Still Struggle in High School Math Competitions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-101/summary.md) — AMO-Bench is a 50-problem, IMO-difficulty-or-harder, entirely original math benchmark built to avoid the saturation and memorization issues of AIME24/25, on which even the best of 36 evaluated LLMs (Gemini-3-Pro) reaches only 63.1% accuracy, model performance grows near-linearly with the logarithm of output length (still-unsaturated evidence that test-time scaling keeps paying off), and a manual failure analysis finds brute-force enumeration and improper strategy selection -- reasoning deficiency, not missing math knowledge -- as the dominant error modes.
- [AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1885/summary.md) — AlgBench replaces problem-centric algorithmic benchmarks (which conflate multiple algorithms per problem and risk contamination) with 3,000 expert-curated, contamination-free problems each isolating exactly one of 27 algorithms under a six-category taxonomy, finding LRMs handle non-optimized/Euclidean-structured algorithms well (up to 92%) but collapse on global-optimization tasks like dynamic programming (~49%), that model-parameter scaling barely helps in exactly those weak categories, and that 'strategic over-shifts' -- models abandoning a correct algorithmic design mid-execution -- are specifically triggered by necessary low-entropy tokens (numeric constants, structural delimiters) that standard maximum-entropy RL training penalizes as if they were uncertain, unproductive continuations.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
