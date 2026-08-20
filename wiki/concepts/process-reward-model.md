# process reward model

<!-- auto:begin -->

A reward model that scores the intermediate steps of a reasoning trace, used to guide test-time search rather than only rank finished answers. MetaStone-S1 shares one backbone between its policy and process-reward model; TaTToo trains a domain-specific PRM for tabular reasoning; JETTS benchmarks how well LLM-as-judge models substitute for a trained PRM in guiding test-time scaling, finding judges match outcome reward models but lag PRMs. Note: same concept as the archive's separately-tracked 'process reward model (PRM)' entry -- not merged.

- **Kind**: concept
- **Also called**: PRM, process reward model (PRM)
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [Monte Carlo Tree Search](../methods/monte-carlo-tree-search.md), [process reward model (PRM)](process-reward-model-prm.md), [test-time scaling](test-time-scaling.md)

## Appears in

- [Test-Time Scaling with Reflective Generative Model](../../archive/papers/2026/title-5ff343d0a198bd25/summary.md) — Proposes a reasoning model (MetaStone-S1) whose policy and process-reward model share one backbone, and which exposes selectable low/medium/high reasoning-effort modes that trade off thinking length against test-time performance, matching OpenAI o3-mini on math benchmarks at 32B parameters.
- [TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning](../../archive/papers/2026/title-983af40bdcebe387/summary.md) — TaTToo trains a table-grounded, tool-verified process reward model that supervises test-time-scaling search for large reasoning models on tabular reasoning tasks.
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](../../archive/papers/2025/title-ab80eef8a7c42e7c/summary.md) — JETTS is a benchmark evaluating how well LLM-as-judge models perform as evaluators guiding test-time-scaling methods -- response reranking, step-level beam search, and critique-based refinement -- across math, code and instruction-following.
- [ContextPRM: Leveraging Contextual Coherence for multi-domain Test-Time Scaling](../../archive/papers/2026/title-da31eb8bef16ddcc/summary.md) — Trains a process reward model that scores chain-of-thought coherence instead of domain knowledge, and uses it to weight votes among sampled reasoning chains for test-time scaling across math and non-math domains.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
