# LoRA fine-tuning

<!-- auto:begin -->

A parameter-efficient fine-tuning method used across sources as a lightweight alternative to full fine-tuning: applied to internalize temporal-reasoning self-reflection behavior (TISER) into smaller open models, and referenced (per another archived source) as a technique compared against full fine-tuning for few-step diffusion language model distillation.

- **Kind**: method
- **Also called**: Low-Rank Adaptation
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [AIME 2024](../datasets/aime-2024.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](deepseek-r1-distill-qwen-7b.md), [GPQA](../datasets/gpqa.md), [GPT-4o](../models/gpt-4o.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [MATH500](../datasets/math500.md), [MathQA](../datasets/mathqa.md), [Mistral 7B](../models/mistral-7b.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [Qwen3-8B](qwen3-8b.md), [SciQ](../datasets/sciq.md), [TriviaQA](../datasets/triviaqa.md)

## Appears in

- [OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models](../../archive/papers/2026/arxiv-2608-02942/summary.md) — OPTD trains a few-step diffusion language model by sampling partial decoding states from the student's own inference trajectory and letting a frozen teacher verify, per state, the longest set of future token releases that can be committed jointly without changing the teacher's rollout outcome.
- [Learning to Reason Over Time: Timeline Self-Reflection for Improved Temporal Reasoning in Language Models](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-1358/summary.md) — TISER (Temporal Self-Reflective Prompting) extends chain-of-thought into a four-stage test-time-scaling pipeline -- reasoning, explicit timeline construction, iterative self-reflection, then answer generation -- for temporal reasoning, and fine-tuning smaller open models (Mistral-7B, Qwen2.5-7B) on TISER-formatted synthetic traces lets them match or beat GPT-4o on in-domain and out-of-distribution temporal reasoning benchmarks.
- [CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-industry-152/summary.md) — CAT (Confidence-Adaptive Thinking) uses self-certainty -- the KL divergence of a reasoning trajectory's per-token predictive distribution from uniform, an intrinsic model signal requiring no external labels -- to build preference pairs and a confidence-weighted preference-optimization loss (CWPO) that compresses reasoning on problems the model is confident about while preserving deliberation on uncertain ones, beating three efficient-reasoning baselines (OverThink, DAST, ConCISE) on accuracy-at-compression across three LRMs and three benchmarks.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
