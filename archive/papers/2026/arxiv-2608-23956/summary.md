<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Recursive Agentic Reasoning

- **Authors**: Shengxin Zhang, Xiaomin Wu, Xiyang Wu, Jing Xie
- **Venue**: cs.AI
- **Published**: 2026-08-25
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.23956>
- **PDF**: <https://arxiv.org/pdf/2608.23956v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an agent's reasoning trace: GROW, which deepens a single reasoning path; PRUNE, which decomposes and recomposes the problem; and BRANCH, which samples alternative reasoning paths and selects among them. We evaluate all three operators against a single-pass chain-of-thought baseline under a shared harness with identical prompts, token budgets, and grading code. Across five benchmarks and three frontier models, comprising 14 model-benchmark settings, 49,327 graded items, and 151,876 model calls, BRANCH improves accuracy in all 14 settings by an average of 5.98 percentage points and is the best-performing operator in 12. In contrast, GROW yields a mean gain of 2.18 points and degrades performance in two settings, while PRUNE improves accuracy by 0.94 points on average. Analysis shows that BRANCH's advantage arises not only from exploring multiple reasoning paths, but also from recovering from truncation: its gains strongly correlate with the baseline rate of empty, budget-exhausted outputs (r = 0.72). These results weaken the hypothesis that different problems require routing among test-time reasoning operators; at this level of abstraction, repeated branching is consistently dominant. Finally, we show that unpaired evaluation and treating scoring-pipeline failures as model errors can materially change, and even reverse, comparative conclusions, motivating paired scoring as a standard protocol for test-time-compute evaluation.

---

Record id: `arxiv:2608.23956`
