# benchmark saturation

<!-- auto:begin -->

Benchmark saturation -- top models scoring so high on a benchmark (e.g. AIME24/25 exceeding 90%) that it can no longer distinguish further reasoning progress -- is the problem AMO-Bench is built to avoid, via original, IMO-difficulty-or-harder problems on which even the best model reaches only 63.1%; DARG addresses the same underlying problem differently, by perturbing an existing benchmark's extracted reasoning graph to generate new items at controlled complexity levels rather than authoring new problems from scratch.

- **Kind**: concept
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [Claude-Opus-4.5](../models/claude-opus-4-5.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3.2-Speciale](../models/deepseek-v3-2-speciale.md), [Gemini-3-Pro](../models/gemini-3-pro.md), [GLM-4.6](../models/glm-4-6.md), [HMMT25](../datasets/hmmt25.md), [Kimi-K2-Thinking](../models/kimi-k2-thinking.md), [MATH500](../datasets/math500.md), [o3-mini](../models/o3-mini.md), [o4-mini](../models/o4-mini.md), [reasoning graph](reasoning-graph.md), [reasoning graph extraction](../methods/reasoning-graph-extraction.md)

## Appears in

- [AMO-Bench: Large Language Models Still Struggle in High School Math Competitions](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-101/summary.md) — AMO-Bench is a 50-problem, IMO-difficulty-or-harder, entirely original math benchmark built to avoid the saturation and memorization issues of AIME24/25, on which even the best of 36 evaluated LLMs (Gemini-3-Pro) reaches only 63.1% accuracy, model performance grows near-linearly with the logarithm of output length (still-unsaturated evidence that test-time scaling keeps paying off), and a manual failure analysis finds brute-force enumeration and improper strategy selection -- reasoning deficiency, not missing math knowledge -- as the dominant error modes.
- [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](../../archive/papers/2024/title-f4deea1ce7836f59/summary.md) — A benchmark-construction framework that extracts the reasoning graph behind each item in an existing benchmark and perturbs it to generate new test items at controlled complexity levels, then measures how 15 LLMs degrade as complexity rises.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
