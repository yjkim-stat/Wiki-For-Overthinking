# HLE

<!-- auto:begin -->

HLE appears in this archive only as coverage of the hardest science and knowledge questions, and neither citing source reports a length or accuracy number on it. Statistical Early Stopping names GPQA and HLE as its science evaluation but reports its token savings on the four other sets - 63.30% (GSM-MC), 41.10% (UMWP), 68.15% (MiP) and 69.83% (MMLU) for the Maxwise rule, measured on ill-posed instances - so nothing is stated about what its stopping rules do on HLE. WebThinker lists HLE among GPQA, GAIA, WebWalkerQA and Glaive with only a qualitative claim of outperforming existing methods, and the archive files it as sharing no more than the 'large reasoning model' keyword. The group's pattern that token savings shrink on hard sets is therefore untested here rather than confirmed. The archive also holds this benchmark separately under its spelled-out name.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [BBEH](bbeh.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [Conformal Prediction](../methods/conformal-prediction.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [early stopping](../concepts/early-stopping.md), [GAIA](gaia.md), [GPQA](gpqa.md), [GPQA-Diamond](gpqa-diamond.md), [GSM8K](gsm8k.md), [MMLU](mmlu.md), [Omni-MATH](omni-math.md), [Overthinking](../concepts/overthinking.md), [SuperGPQA](supergpqa.md), [Test-Time Compute](../concepts/test-time-compute.md), [Uncertainty Quantification](../concepts/uncertainty-quantification.md)

## Appears in

- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [Statistical Early Stopping for Reasoning Models](../../archive/papers/2026/title-594984624acaa60d/summary.md) — Two statistical stopping rules monitor uncertainty-keyword arrivals inside a reasoning trace and halt generation on ill-posed or ambiguous queries, one with a finite-sample bound on the probability of halting too early on a well-posed query.
- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](../../archive/papers/2025/title-93df459afa09bdd6/summary.md) — WebThinker gives large reasoning models a Deep Web Explorer module and an Autonomous Think-Search-and-Draft strategy so they can search, navigate, and draft research reports interleaved with reasoning, trained via iterative online DPO, and it outperforms existing methods and strong proprietary systems on complex reasoning and report-generation benchmarks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
