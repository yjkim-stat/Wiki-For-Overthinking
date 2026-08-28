# BBEH

<!-- auto:begin -->

A general many-hop reasoning benchmark used as one of several evaluation suites for test-time-compute methods; sources use it to compare recursion operators (GROW/PRUNE/BRANCH) and difficulty-aware entropy-shaping methods against a single-pass baseline. Sources do not define its construction beyond naming it a harder benchmark than BIG-Bench Hard.

- **Kind**: dataset
- **Also called**: BIG-Bench Extra Hard
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [ARES](../methods/ares.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [Difficulty-aware compute allocation](../concepts/difficulty-aware-compute-allocation.md), [GPQA](gpqa.md), [GSM8K](gsm8k.md), [HLE](hle.md), [MATH500](math500.md), [MathVerse](mathverse.md), [MathVision](mathvision.md), [MathVista](mathvista.md), [MMLU-Pro](mmlu-pro.md), [MMMU](mmmu.md), [MMMU-Pro](mmmu-pro.md), [MMStar](mmstar.md), [MuSiQue](musique.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5-VL](../methods/qwen2-5-vl.md), [Reasoning Trace Length](../concepts/reasoning-trace-length.md), [RLVR](../methods/rlvr.md), [SuperGPQA](supergpqa.md), [Token-Level Entropy](../concepts/token-level-entropy.md), [WeMath](wemath.md)

## Appears in

- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](../../archive/papers/2026/title-544eea46a2eb68c1/summary.md) — ARES trains multimodal reasoning models to spend exploration effort in proportion to problem difficulty, using sliding-window token entropy as the signal for when and how much to explore.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
