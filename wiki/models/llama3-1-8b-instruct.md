# Llama3.1-8B-Instruct

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [HotpotQA](../datasets/hotpotqa.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MathQA](../datasets/mathqa.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [MuSiQue](../datasets/musique.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [SciQ](../datasets/sciq.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
