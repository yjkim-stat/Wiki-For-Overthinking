# chain-of-thought baseline

<!-- auto:begin -->

The single-pass chain-of-thought generation against which test-time-scaling and adaptive-reasoning methods are compared: one model call producing one reasoning trace and one answer, with no recursion, resampling, or per-task configuration search. Sources use it as the zero-extra-compute reference point that recursion operators (GROW/PRUNE/BRANCH) and adaptive plugins (e.g. picking prompt format, temperature, and step count per task) are measured against.

- **Kind**: method
- **Also called**: Chain-of-Thought (baseline), CoT baseline, single-pass CoT
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [adaptive reasoning](../concepts/adaptive-reasoning.md), [BBEH](../datasets/bbeh.md), [Best-of-N (baseline)](best-of-n-baseline.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [GPQA](../datasets/gpqa.md), [HLE](../datasets/hle.md), [LogiQA](../datasets/logiqa.md), [MuSiQue](../datasets/musique.md), [Omni-MATH](../datasets/omni-math.md), [SuperGPQA](../datasets/supergpqa.md), [TruthfulQA](../datasets/truthfulqa.md)

## Appears in

- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [AdaReasoner: Adaptive Reasoning Enables More Flexible Thinking](../../archive/papers/2025/title-b12c09d1a21e70d0/summary.md) — AdaReasoner is an RL-trained, model-agnostic plugin that picks a per-task reasoning configuration - prompt instruction format, decoding temperature and number of reasoning steps - instead of using one fixed prompting setup for every task.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
