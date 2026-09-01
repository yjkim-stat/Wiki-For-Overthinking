# Llama3.1-8B-Instruct

<!-- auto:begin -->

Llama3.1-8B-Instruct is a backbone model used in this archive by ARISE, which combines Monte Carlo Tree Search with a Bayesian risk-value function for knowledge-augmented reasoning (at substantially higher inference cost), and by GrACE, which teaches the model to emit a calibrated confidence score during generation itself to weight self-consistency voting and drive early stopping. Note: this entity's name differs only in capitalization/spacing from 'LLaMA-3.1-8B-Instruct' recorded elsewhere in the archive from a different set of sources -- possibly the same model under two spellings, not merged here.

- **Kind**: model
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [2WikiMultihopQA](../datasets/2wikimultihopqa.md), [AIME 2024](../datasets/aime-2024.md), [AIME 2025](../datasets/aime-2025.md), [AMC23](../datasets/amc23.md), [DAPO (baseline)](../methods/dapo-baseline.md), [DeepScaler (training)](../methods/deepscaler-training.md), [DeepSeek-R1-distilled models (comparison)](deepseek-r1-distilled-models-comparison.md), [GRPO (baseline)](../methods/grpo-baseline.md), [HMMT25](../datasets/hmmt25.md), [HotpotQA](../datasets/hotpotqa.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [MuSiQue](../datasets/musique.md), [OlympiadBench](../datasets/olympiadbench.md), [Qwen2.5-7B-Instruct](qwen2-5-7b-instruct.md), [Qwen3-4B-Base](qwen3-4b-base.md), [Qwen3-8B-Base](qwen3-8b-base.md), [SciQ](../datasets/sciq.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.
- [Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-237/summary.md) — MINER recovers training signal from 'positive homogeneous' (PH) prompts -- where all sampled RLVR rollouts are already correct and GRPO-style advantage collapses to zero, wasting the rollout budget -- by converting the policy's own per-token uncertainty (negative log-likelihood) into an intrinsic reward that reinforces under-confident-but-correct reasoning paths, combined with token-level focal credit assignment and adaptive advantage calibration, achieving up to +4.58 Pass@1 and +6.66 Pass@K over GRPO with zero extra rollouts or inference cost.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
