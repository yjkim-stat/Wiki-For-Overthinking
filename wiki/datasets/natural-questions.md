# Natural Questions

<!-- auto:begin -->

An open-domain question-answering dataset of real search queries, used in this archive as a retrieval-QA workload rather than as a reasoning benchmark. One source pairs it with HotpotQA as the two query sets for measuring per-query latency and energy in edge RAG; another places it with CRAG on the out-of-distribution side of a split whose in-distribution half is HotpotQA and HaluEval. Its single-hop character against HotpotQA's multi-hop one is what both uses rely on.

- **Kind**: dataset
- **Also called**: NQ
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 1

**Related**: [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [GRPO](../methods/grpo.md), [HotpotQA](hotpotqa.md), [Length Penalty](../concepts/length-penalty.md), [Overthinking](../concepts/overthinking.md), [retrieval-augmented generation](../methods/retrieval-augmented-generation.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md)

## Appears in

- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
