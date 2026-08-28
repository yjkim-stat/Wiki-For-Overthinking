# MuSiQue

<!-- auto:begin -->

A multi-hop question-answering benchmark used to evaluate knowledge-augmented and recursive test-time-scaling reasoning methods, including as one of the hardest benchmarks in a comparison of recursion operators (GROW/PRUNE/BRANCH) and as one of the three multi-hop QA datasets ARISE's risk-adaptive Monte Carlo Tree Search is evaluated on, where its difficulty produces the largest relative gains over vanilla RAG among the three benchmarks tested.

- **Kind**: dataset
- **Also called**: MuSiQue, MusiQue
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [2WikiMultihopQA](2wikimultihopqa.md), [BBEH](bbeh.md), [chain-of-thought baseline](../methods/chain-of-thought-baseline.md), [deepseek-v4-pro](../models/deepseek-v4-pro.md), [HLE](hle.md), [HotpotQA](hotpotqa.md), [Llama3.1-8B-Instruct](../models/llama3-1-8b-instruct.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [Natural Questions (NQ)](natural-questions-nq.md), [Omni-MATH](omni-math.md), [PopQA](popqa.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [SuperGPQA](supergpqa.md), [TriviaQA](triviaqa.md)

## Appears in

- [Recursive Agentic Reasoning](../../archive/papers/2026/arxiv-2608-23956/summary.md) — Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.
- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1712/summary.md) — Verbal-R3 shows that rewriting retrieved documents into 'Verbal Annotations' -- analytic narratives that explicitly state the logical connection between a query and a document, distilled from GPT-OSS-120B into a lightweight 1.5B/3B Verbal Reranker -- substantially improves RAG accuracy over both raw context injection and stylistic paraphrasing, and pairs this with a relevance-guided test-time-scaling method that allocates search-trajectory budget toward high-relevance-scored queries, beating Search-R1 by up to 18% F1 while cutting reranker calls ~45-54%.
- [Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1052/summary.md) — Self-Correcting RAG reformulates retrieval-augmented generation as constrained optimization: a Multi-dimensional Multiple-choice Knapsack Problem (MMKP) selects a diverse, non-redundant, token-budget-respecting document context (replacing greedy top-k), and an NLI-guided Monte Carlo Tree Search explores reasoning trajectories at inference time, penalizing branches whose generated claims contradict retrieved evidence -- improving average EM/F1 (37.1/45.8) and retrieval recall@5 (72.0%) over strong RAG baselines across six QA datasets while cutting the contradiction rate to 0.04.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
