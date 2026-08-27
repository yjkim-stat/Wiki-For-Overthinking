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

## In one line

Recasts iterative refinement, decomposition and repeated sampling as three recursion operators (GROW, PRUNE, BRANCH) over a shared reasoning-trace primitive, compares them under a paired protocol across 3 frontier models and 5 benchmarks, and finds BRANCH wins mainly because it recovers answers a single pass never emitted at all.

## Problem

Test-time reasoning methods (iterative refinement, decomposition, repeated sampling) are each introduced on their own benchmarks, models and grading code, so practitioners cannot tell which buys the most accuracy at equal compute, or why -- and comparisons across long-running shared-endpoint runs are corrupted by unpaired scoring when infrastructure failures are silently treated as model errors.

## Contributions

- a unified formulation of additive (GROW), reductive (PRUNE) and search-based (BRANCH) test-time recursion over a reasoning trace, built on a shared solving primitive with an explicit finalization retry for budget-exhausted generations
- a controlled 14-cell comparison (5 benchmarks x 3 models x 4 methods, 49,327 graded items) under a paired scoring protocol, showing BRANCH wins 12/14 cells
- a mechanistic account that BRANCH's advantage is driven substantially by recovery of budget-exhausted (empty) outputs rather than marginalization over reasoning paths, evidenced by a 0.72 correlation between gain and baseline empty-output rate
- two negative results: adaptive per-item operator routing is not supported at this granularity, and unpaired scoring against a shared, intermittently-failing endpoint was shown to invert one of the paper's own findings

## Method

Defines a shared primitive solve(x,c) -- one model call with optional prior context -- with an explicit finalization retry when the model's hidden deliberation exhausts its token budget and returns empty content. Builds three recursion operators on top of it: GROW (re-solve with the previous attempt in context, halt on answer stability, cap 3 rounds), PRUNE (decompose into ordered sub-questions, solve each with prior answers in context, recompose), and BRANCH (N=5 independent samples at temperature 0.7, plurality vote over normalized answers, empty samples excluded). Evaluates all three plus a single-pass CoT baseline on 3 frontier reasoning models (DeepSeek-V4-Pro, MiniMax-M3, Qwen3.6-plus) across 5 benchmarks (MuSiQue, HLE, BBEH, SuperGPQA, Omni-MATH) -- 14 model x benchmark cells, 49,327 graded items, 151,876 model calls -- using a paired protocol that deduplicates retried items, excludes (rather than penalizes) unrecoverable transport failures, and scores every operator only on the item set every operator resolved.

## Results

BRANCH improves accuracy in all 14 cells (mean +5.98 points, median +6.47, range +0.66 to +13.50) and is the strict best operator in 12 of 14, tying in one and losing in one (SuperGPQA on Qwen3.6-plus, where GROW and BRANCH tie at +2.33/+2.34). GROW averages +2.18 but is negative on DeepSeek-V4-Pro for MuSiQue (-1.25) and BBEH (-2.50). PRUNE averages +0.94, ranging -2.17 to +4.00. BRANCH's gain correlates strongly (r=0.72, n=14) with the baseline's rate of empty, budget-exhausted outputs -- DeepSeek-V4-Pro alone returns empty content on 51.2% of HLE items under a single pass because its hidden deliberation exhausts a 16,000-token budget before emitting a visible answer; sampling 5 times converts this from a near-coin-flip into a minority event and roughly halves the empty-output rate in every cell where truncation occurs. The two cells BRANCH does not strictly win are both on Qwen3.6-plus, the one model that never produced an empty completion in this study. An adaptive per-item operator router is not supported by the data: BRANCH is best in all 5 DeepSeek-V4-Pro and all 5 MiniMax-M3 cells, so a router trained on these outcomes would learn a nearly constant policy. Cost: GROW averages 2.23 calls/item, PRUNE 4.04, BRANCH 4.85 (vs. 1 for the baseline); GROW returns +1.77 accuracy points per extra call, BRANCH +1.55, PRUNE +0.31 -- so BRANCH wins on achievable accuracy, not per-call efficiency, and its fixed N=5 with no early stopping is called out as an easy inefficiency to remove. Unpaired scoring on the authors' own data reversed a finding: Qwen3.6-plus on HLE looked like it dropped from 14.20% (baseline) to 11.20% (BRANCH) until item-level pairing showed BRANCH is actually +0.66 once the 172 (vs. 131) items lost to proxy read-timeouts are excluded rather than scored wrong.

## Limitations

BRANCH's selection is an unweighted majority vote; the paper records but does not use a per-item agreement ratio, and notes verifier- or confidence-weighted selection is strictly more expressive and the largest gap versus the state of the art. No significance tests are reported; a single 200-item cell's accuracy carries a roughly ±7-point 95% interval, so small effects in the BBEH and Omni-MATH cells are called provisional. The HLE grader (letter/string extraction) is a stated lower bound relative to an LLM judge. Omni-MATH was not run on Qwen3.6-plus. A 50-item pilot that preceded the full runs showed a task-dependent pattern of operator effectiveness that motivated the routing hypothesis and did not survive contact with the full-scale data, illustrating that small-n pilots at this cost regime can support a conclusion the full data contradicts.

## Why it matters here

- **overthinking**: Directly relevant to non-termination: it identifies budget-exhausted, empty-content outputs (a model's hidden deliberation consuming its entire token budget with nothing visible to show for it -- up to 51.2% of items on one benchmark/model pair) as the dominant failure mode single-pass reasoning faces, and shows that most of repeated sampling's benefit on long-reasoning models is recovering from that failure rather than marginalizing over correct reasoning paths. This reframes 'spend more test-time compute' as substantially a fix for a pathological non-termination/truncation problem rather than a pure accuracy-quality tradeoff, and its paired-scoring methodology is a caution for any efficiency study run against a shared or rate-limited endpoint.

## Entities

- **Concepts**: recursion operator, budget-exhausted output / truncation recovery, paired evaluation protocol, answer stability halting, hidden deliberation stream
- **Methods**: GROW (additive recursion), PRUNE (reductive/decomposition recursion), BRANCH (search/self-consistency recursion), [chain-of-thought baseline](../../../../wiki/methods/chain-of-thought-baseline.md)
- **Datasets**: [MuSiQue](../../../../wiki/datasets/musique.md), [HLE](../../../../wiki/datasets/hle.md), [BBEH](../../../../wiki/datasets/bbeh.md), [SuperGPQA](../../../../wiki/datasets/supergpqa.md), [Omni-MATH](../../../../wiki/datasets/omni-math.md)

Tags: `test-time-compute`, `self-consistency`, `decomposition`, `truncation`, `token-budget`, `evaluation-methodology`

## Abstract

Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an agent's reasoning trace: GROW, which deepens a single reasoning path; PRUNE, which decomposes and recomposes the problem; and BRANCH, which samples alternative reasoning paths and selects among them. We evaluate all three operators against a single-pass chain-of-thought baseline under a shared harness with identical prompts, token budgets, and grading code. Across five benchmarks and three frontier models, comprising 14 model-benchmark settings, 49,327 graded items, and 151,876 model calls, BRANCH improves accuracy in all 14 settings by an average of 5.98 percentage points and is the best-performing operator in 12. In contrast, GROW yields a mean gain of 2.18 points and degrades performance in two settings, while PRUNE improves accuracy by 0.94 points on average. Analysis shows that BRANCH's advantage arises not only from exploring multiple reasoning paths, but also from recovering from truncation: its gains strongly correlate with the baseline rate of empty, budget-exhausted outputs (r = 0.72). These results weaken the hypothesis that different problems require routing among test-time reasoning operators; at this level of abstraction, repeated branching is consistently dominant. Finally, we show that unpaired evaluation and treating scoring-pipeline failures as model errors can materially change, and even reverse, comparative conclusions, motivating paired scoring as a standard protocol for test-time-compute evaluation.

---

Record id: `arxiv:2608.23956`
