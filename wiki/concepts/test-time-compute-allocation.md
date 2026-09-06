# test-time compute allocation

<!-- auto:begin -->

Test-time compute allocation means deciding, per query, how much inference-time compute or reasoning effort to spend. The RTL-optimization source (ARES) raises an LLM agent's per-call reasoning effort only after progress on a task stalls, reporting normalized dollar cost alongside a power-area-delay figure of merit; 'Strategic Scaling of Test-Time Compute' instead formulates the allocation across queries as a bandit-learning problem, so harder queries receive more compute and easier ones less.

- **Kind**: concept
- **Also called**: Test-Time Compute Allocation, test-time compute allocation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2025](../datasets/aime-2025.md), [DeepSeek-R1](../models/deepseek-r1.md), [DeepSeek-V3](../models/deepseek-v3.md), [GLM-4.5-Air](../models/glm-4-5-air.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [Kimi-K2-Thinking](../models/kimi-k2-thinking.md), [LiveCodeBench](../datasets/livecodebench.md), [MATH500](../datasets/math500.md), [Qwen3-32B-Thinking](../models/qwen3-32b-thinking.md)

## Appears in

- [Thinking effort aligns between humans and reasoning models in abductive reasoning](../../archive/papers/2026/arxiv-2609-01867/summary.md) — Measures whether reasoning models spend tokens on the same items humans spend time on, using a forced-choice abductive task where item difficulty cannot be read off formal structure, and finds a significant per-item correlation in all eight models tested.
- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach](../../archive/papers/2026/title-de00054e3faab991/summary.md) — Formulates test-time compute allocation across queries as a bandit learning problem so that harder queries get more compute and easier ones get less.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
