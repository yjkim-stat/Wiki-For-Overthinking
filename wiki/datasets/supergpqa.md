# SuperGPQA

<!-- auto:begin -->

A large, broad-domain multiple-choice science-question dataset used as a source pool in the archive: TRAAC references it as part of its evaluation suite, and OptimalThinkingBench draws its 72-domain OverthinkingBench questions from SuperGPQA before filtering for unambiguous, easy items.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [AdaptThink](../methods/adaptthink.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [AIME 2026](aime-2026.md), [BBEH](bbeh.md), [BBH](bbh.md), [BBH (Big-Bench Hard)](bbh-big-bench-hard.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [DAPO-Math-17K](dapo-math-17k.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GPQA-Diamond](gpqa-diamond.md), [GRPO](../methods/grpo.md), [HLE](hle.md), [HMMT 2025](hmmt-2025.md), [LC-R1](../methods/lc-r1.md), [MMLU-Pro](mmlu-pro.md), [MuSiQue](musique.md), [Omni-MATH](omni-math.md), [OverthinkingBench](overthinkingbench.md), [Self-Certainty](../concepts/self-certainty.md), [Test-Time Scaling](../concepts/test-time-scaling.md), [TokenSkip](../methods/tokenskip.md)

## Appears in

- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](../../archive/papers/2026/arxiv-2608-04001/summary.md) — A framework paper that formalizes test-time scaling as budgeted inference over a model's implicit prefix tree, splits it into three structural regimes (single-trajectory, leaf-level, prefix-level), replaces scalar repeated-sampling metrics with a discovery-stability profile that Pass@k and its relatives are coordinates of, specifies exact-replay versus distributional reproducibility, and releases 1,948,821 full reasoning traces with token-level alternatives and two verifier signals.
- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [Think Right: Learning to Mitigate Under-Over Thinking via Adaptive, Attentive Compression](../../archive/papers/2025/local-da3fbe3617acc5f8/summary.md) — TRAAC is an online GRPO-based RL method that prunes a reasoning model's chain-of-thought using attention scores from the </think> token and calibrates how aggressively it prunes based on estimated problem difficulty, so it thinks less on easy problems and more on hard ones.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
