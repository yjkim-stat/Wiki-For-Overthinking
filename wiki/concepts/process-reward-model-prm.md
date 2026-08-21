# process reward model (PRM)

<!-- auto:begin -->

A reward model that scores the intermediate steps of a reasoning trace, not just the final answer, used to guide test-time search (pruning bad branches, expanding promising ones) rather than only to rank complete solutions. 'What If We Allocate Test-Time Compute Adaptively?' replaces uniform compute allocation with PRM-guided pruning/expansion; TaTToo trains a table-grounded, tool-verified PRM specifically for tabular reasoning search. Note: same concept as the archive's separately-tracked 'process reward model' entry -- not merged.

- **Kind**: concept
- **Also called**: PRM, process reward model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](../datasets/aime-2024.md), [MATH500](../datasets/math500.md), [Monte Carlo Tree Search](../methods/monte-carlo-tree-search.md), [process reward model](../methods/process-reward-model.md)

## Appears in

- [What If We Allocate Test-Time Compute Adaptively?](../../archive/papers/2026/title-892443a8a7093b83/summary.md) — Replaces uniform test-time compute allocation with a process-reward-model-guided framework that adaptively prunes, expands and selects reasoning trajectories per problem.
- [TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning](../../archive/papers/2026/title-983af40bdcebe387/summary.md) — TaTToo trains a table-grounded, tool-verified process reward model that supervises test-time-scaling search for large reasoning models on tabular reasoning tasks.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
