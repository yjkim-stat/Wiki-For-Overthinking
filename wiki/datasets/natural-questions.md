# Natural Questions

<!-- auto:begin -->

An open-domain question-answering dataset of real search queries, used in this archive as a retrieval-QA workload rather than as a reasoning benchmark. One source pairs it with HotpotQA as the two query sets for measuring per-query latency and energy in edge RAG; another places it with CRAG on the out-of-distribution side of a split whose in-distribution half is HotpotQA and HaluEval. Its single-hop character against HotpotQA's multi-hop one is what both uses rely on.

- **Kind**: dataset
- **Also called**: NQ
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [Length Penalty](../concepts/length-penalty.md), [Llama-3.2-1B](../models/llama-3-2-1b.md), [Overthinking](../concepts/overthinking.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG](../../archive/papers/2026/arxiv-2608-19535/summary.md) — Measures retrieval-augmented generation stage by stage on an edge SoC and shows that context compression pays only inside a bounded rate window, because the compressor runs on the same chip and its own latency and energy must be subtracted from the savings.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
