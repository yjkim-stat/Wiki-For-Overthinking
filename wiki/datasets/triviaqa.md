# TriviaQA

<!-- auto:begin -->

TriviaQA is a knowledge-QA benchmark used in this archive's compute-optimal-scaling-of-skills study, where knowledge-based QA is shown to be capacity-hungry (versus code generation being data-hungry) even after controlling for skill-relevant pretraining data, and by GrACE's generative confidence-elicitation method, which uses an on-the-fly calibrated confidence score to weight self-consistency voting and drive early stopping.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [2WikiMultihopQA](2wikimultihopqa.md), [BigCodeBench](bigcodebench.md), [HotpotQA](hotpotqa.md), [HumanEval](humaneval.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [LoRA fine-tuning](../methods/lora-fine-tuning.md), [MathQA](mathqa.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MuSiQue](musique.md), [Natural Questions (NQ)](natural-questions-nq.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [SciQ](sciq.md)

## Appears in

- [Compute Optimal Scaling of Skills: Knowledge vs Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-688/summary.md) — Shows that compute-optimal scaling (the optimal trade-off between parameter count and training tokens) is skill-dependent -- knowledge-based QA is capacity-hungry while code generation is data-hungry -- a fundamental difference that persists even after controlling for the proportion of skill-relevant pretraining data, and demonstrates that a misspecified validation set can bias the estimated compute-optimal parameter count by up to 50%.
- [GrACE: A Generative Approach to Better Confidence Elicitation and Efficient Test-Time Scaling in Large Language Models](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1069/summary.md) — GrACE teaches an LLM to output a discriminative, calibrated confidence score during generation itself -- via the similarity between the last hidden state and a learned embedding for a special <CNF> token, trained against k-fold-binned accuracy targets -- eliminating the separate evaluation stage post-generation methods require, and uses this on-the-fly confidence to weight self-consistency voting and drive early-stopping, improving test-time-scaling accuracy by up to 3.3% while cutting required samples by more than half in many cases.
- [Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1712/summary.md) — Verbal-R3 shows that rewriting retrieved documents into 'Verbal Annotations' -- analytic narratives that explicitly state the logical connection between a query and a document, distilled from GPT-OSS-120B into a lightweight 1.5B/3B Verbal Reranker -- substantially improves RAG accuracy over both raw context injection and stylistic paraphrasing, and pairs this with a relevance-guided test-time-scaling method that allocates search-trajectory budget toward high-relevance-scored queries, beating Search-R1 by up to 18% F1 while cutting reranker calls ~45-54%.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
