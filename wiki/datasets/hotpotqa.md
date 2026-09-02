# HotpotQA

<!-- auto:begin -->

HotpotQA is the archive's multi-hop question-answering leg, and it is where reasoning length gets counted in steps rather than in tokens. CoSMo trains and evaluates on it as in-distribution data (with HaluEval, against Natural Questions and CRAG out-of-distribution), reporting a 3.3-point accuracy gain at 28.7% fewer segments and roughly 2.9 segments on average - but its unit is segments, not tokens, and only the SFT-only ablation gives a token figure (19%). It is evaluated on multi-hop QA precisely because its method needs ground-truth hop counts to set a target, which math and code benchmarks do not annotate. Atom of Thoughts also names it as its multi-hop leg alongside BBH, MMLU and LongBench, but the archive could recover only the qualitative claim that performance improves as budget grows, with no numbers.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 4

**Related**: [2WikiMultihopQA](2wikimultihopqa.md), [accuracy-efficiency tradeoff](../concepts/accuracy-efficiency-tradeoff.md), [BBH (Big-Bench Hard)](bbh-big-bench-hard.md), [DeepSeek-R1-distilled models (comparison)](../concepts/deepseek-r1-distilled-models-comparison.md), [GRPO](../methods/grpo.md), [Length Penalty](../concepts/length-penalty.md), [LLaMA-3.1-8B-Instruct](../models/llama-3-1-8b-instruct.md), [MMLU](mmlu.md), [Monte Carlo Tree Search (MCTS)](../methods/monte-carlo-tree-search-mcts.md), [MuSiQue](musique.md), [Natural Questions](natural-questions.md), [Natural Questions (NQ)](natural-questions-nq.md), [Overthinking](../concepts/overthinking.md), [PopQA](popqa.md), [Qwen2.5-3B-Instruct](../models/qwen2-5-3b-instruct.md), [Qwen2.5 7B](../models/qwen2-5-7b.md), [Qwen2.5-7B-Instruct](../models/qwen2-5-7b-instruct.md), [supervised fine-tuning](../concepts/supervised-fine-tuning.md), [TriviaQA](triviaqa.md)

## Appears in

- [ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search](../../archive/papers/2025/doi-10-18653-v1-2025-acl-long-538/summary.md) — ARISE combines Monte Carlo Tree Search with a Bayesian Risk-Value function -- estimating each reasoning-state node's risk from the policy model's own likelihood of regenerating the original question given that state -- to guide retrieval-augmented multi-hop reasoning, outperforming SOTA knowledge-augmented-reasoning baselines by up to 23.10% and RAG-equipped DeepSeek-R1-distilled LRMs by up to 25.37%, while making explicit that its search-based gains come at substantially higher inference-time cost.
- [Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1712/summary.md) — Verbal-R3 shows that rewriting retrieved documents into 'Verbal Annotations' -- analytic narratives that explicitly state the logical connection between a query and a document, distilled from GPT-OSS-120B into a lightweight 1.5B/3B Verbal Reranker -- substantially improves RAG accuracy over both raw context injection and stylistic paraphrasing, and pairs this with a relevance-guided test-time-scaling method that allocates search-trajectory budget toward high-relevance-scored queries, beating Search-R1 by up to 18% F1 while cutting reranker calls ~45-54%.
- [Atom of Thoughts for Markov LLM Test-Time Scaling](../../archive/papers/2025/title-0393ca4ca3f4fb8c/summary.md) — Atom of Thoughts reframes multi-step LLM reasoning as a Markov process of decomposing a question into independent atomic subquestions and contracting them into an answer-equivalent simplified question, removing the need to carry accumulated historical context and serving as a plug-in for existing test-time scaling methods.
- [Short Chains, Deep Thoughts: Balancing Reasoning Efficiency and Intra-Segment Capability via Split-Merge Optimization](../../archive/papers/2026/title-0bf980e6919c2982/summary.md) — CoSMo restructures reasoning chains by merging redundant segments and splitting logical gaps, then trains with RL against a segment-count budget rather than a token budget.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
