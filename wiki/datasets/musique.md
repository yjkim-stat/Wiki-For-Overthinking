# MuSiQue

<!-- auto:begin -->

A multi-hop question-answering benchmark used to evaluate knowledge-augmented and recursive test-time-scaling reasoning methods, including as one of the hardest benchmarks in a comparison of recursion operators (GROW/PRUNE/BRANCH) and as one of the three multi-hop QA datasets ARISE's risk-adaptive Monte Carlo Tree Search is evaluated on, where its difficulty produces the largest relative gains over vanilla RAG among the three benchmarks tested.

- **Kind**: dataset
- **Also called**: MuSiQue, MusiQue
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BBEH](bbeh.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [HLE](hle.md), [HotpotQA](hotpotqa.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [Omni-MATH](omni-math.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [SuperGPQA](supergpqa.md)

## Appears in

- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
