# GLM-4.6

<!-- auto:begin -->

GLM-4.6 is used in these sources as one of several frontier models evaluated on hard math benchmarks rather than as a subject of methodological study: PaCoRe reports comparison figures against frontier models including this one when showing an 8B model with massively-parallel test-time compute can surpass GPT-5 on HMMT 2025, and AMO-Bench separately evaluates it among 36 models on its original hard-problem set.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [benchmark saturation](../concepts/benchmark-saturation.md), [Claude-Opus-4.5](claude-opus-4-5.md), [DeepSeek-R1](deepseek-r1.md), [Gemini-3-Pro](gemini-3-pro.md), [GPT-5](gpt-5.md), [HMMT 2025](../datasets/hmmt-2025.md), [HMMT25](../datasets/hmmt25.md), [Kimi-K2-Thinking](kimi-k2-thinking.md), [MATH500](../datasets/math500.md), [o3-mini](o3-mini.md), [o4-mini](o4-mini.md), [Qwen3-235B-A22B-Thinking-2507](qwen3-235b-a22b-thinking-2507.md)

## Appears in

- [PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1253/summary.md) — PaCoRe (Parallel Coordinated Reasoning) decouples test-time compute scaling from a fixed context window by running rounds of massively parallel reasoning trajectories, compacting each trajectory's conclusion into a short message, and RL-training the model to synthesize (not just vote on) these messages into better subsequent exploration -- letting an 8B model reach 94.5% on HMMT 2025 by scaling effective test-time compute to ~2 million tokens, surpassing GPT-5's 93.2%.
- [AMO-Bench: Large Language Models Still Struggle in High School Math Competitions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-101/summary.md) — AMO-Bench is a 50-problem, IMO-difficulty-or-harder, entirely original math benchmark built to avoid the saturation and memorization issues of AIME24/25, on which even the best of 36 evaluated LLMs (Gemini-3-Pro) reaches only 63.1% accuracy, model performance grows near-linearly with the logarithm of output length (still-unsaturated evidence that test-time scaling keeps paying off), and a manual failure analysis finds brute-force enumeration and improper strategy selection -- reasoning deficiency, not missing math knowledge -- as the dominant error modes.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
