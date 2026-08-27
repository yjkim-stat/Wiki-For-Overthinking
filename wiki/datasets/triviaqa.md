# TriviaQA

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [BigCodeBench](bigcodebench.md), [HumanEval](humaneval.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [SciQ](sciq.md)

## Appears in

- [Compute Optimal Scaling of Skills: Knowledge vs Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-688/summary.md) — Shows that compute-optimal scaling (the optimal trade-off between parameter count and training tokens) is skill-dependent -- knowledge-based QA is capacity-hungry while code generation is data-hungry -- a fundamental difference that persists even after controlling for the proportion of skill-relevant pretraining data, and demonstrates that a misspecified validation set can bias the estimated compute-optimal parameter count by up to 50%.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
