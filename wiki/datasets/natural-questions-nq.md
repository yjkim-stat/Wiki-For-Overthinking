# Natural Questions (NQ)

<!-- auto:begin -->

_No definition yet — a task is queued to write one._

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 3

**Related**: [2WikiMultihopQA](2wikimultihopqa.md), [BigCodeBench](bigcodebench.md), [HotpotQA](hotpotqa.md), [HumanEval](humaneval.md), [MBPP](mbpp.md), [MMLU](mmlu.md), [MuSiQue](musique.md), [PopQA](popqa.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [TriviaQA](triviaqa.md)

## Appears in

- [Compute Optimal Scaling of Skills: Knowledge vs Reasoning](../../archive/papers/2025/doi-10-18653-v1-2025-findings-acl-688/summary.md) — Shows that compute-optimal scaling (the optimal trade-off between parameter count and training tokens) is skill-dependent -- knowledge-based QA is capacity-hungry while code generation is data-hungry -- a fundamental difference that persists even after controlling for the proportion of skill-relevant pretraining data, and demonstrates that a misspecified validation set can bias the estimated compute-optimal parameter count by up to 50%.
- [Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1712/summary.md) — Verbal-R3 shows that rewriting retrieved documents into 'Verbal Annotations' -- analytic narratives that explicitly state the logical connection between a query and a document, distilled from GPT-OSS-120B into a lightweight 1.5B/3B Verbal Reranker -- substantially improves RAG accuracy over both raw context injection and stylistic paraphrasing, and pairs this with a relevance-guided test-time-scaling method that allocates search-trajectory budget toward high-relevance-scored queries, beating Search-R1 by up to 18% F1 while cutting reranker calls ~45-54%.
- [Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1052/summary.md) — Self-Correcting RAG reformulates retrieval-augmented generation as constrained optimization: a Multi-dimensional Multiple-choice Knapsack Problem (MMKP) selects a diverse, non-redundant, token-budget-respecting document context (replacing greedy top-k), and an NLI-guided Monte Carlo Tree Search explores reasoning trajectories at inference time, penalizing branches whose generated claims contradict retrieved evidence -- improving average EM/F1 (37.1/45.8) and retrieval recall@5 (72.0%) over strong RAG baselines across six QA datasets while cutting the contradiction rate to 0.04.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
