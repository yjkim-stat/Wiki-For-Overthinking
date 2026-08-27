# Monte Carlo Tree Search (MCTS)

<!-- auto:begin -->

A search algorithm (select/expand/simulate/backpropagate) used across sources to guide test-time reasoning search: ARISE combines it with a Bayesian Risk-Value function (estimated from the policy model's own likelihood of regenerating the original question) to guide knowledge-augmented multi-hop reasoning, while SolverLLM uses a modified MCTS (with dynamic expansion, prompt backpropagation, and uncertainty backpropagation) to guide LLM-generated mathematical-optimization-problem formulations.

- **Kind**: method
- **Also called**: MCTS
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [HotpotQA](../datasets/hotpotqa.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [MuSiQue](../datasets/musique.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Test-Time Scaling](../concepts/test-time-scaling.md)

## Appears in

- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search](../../archive/papers/2025/title-e149fd58642147ea/summary.md) — SolverLLM is a training-free test-time-scaling framework that solves optimization problems by having an LLM generate mathematical formulations and translate them into solver-ready code, guided by a modified Monte Carlo Tree Search with dynamic expansion, prompt backpropagation, and uncertainty backpropagation.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
