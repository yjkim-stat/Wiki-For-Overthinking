# BrUMO'25

<!-- auto:begin -->

BrUMO'25 is a hard, 30-question competition-math benchmark used alongside AIME'24, AIME'25 and HMMT'25 as an Olympiad-difficulty evaluation set. 'Ranking Reasoning LLMs under Test-Time Scaling' uses it as one of four benchmarks (20 models, 80 sampled trials each) to test low-budget ranking-method stability, finding Bayes_R0@1 the best-agreeing low-budget method against the gold-standard ranking on it (Kendall's tau_b 0.779-0.858). 'Cut Your Losses!' evaluates its STOP path-pruning method on it under a standardized avg@8|64 protocol alongside AIME24/25, HMMT25 and GPQA-Diamond, though without a BrUMO'25-specific number broken out from the aggregate result.

- **Kind**: dataset
- **Also called**: BRUMO25
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [DeepSeek-R1-0528-Qwen3-8B](../models/deepseek-r1-0528-qwen3-8b.md), [DeepSeek-R1-Distill-Qwen-1.5B](../models/deepseek-r1-distill-qwen-1-5b.md), [DeepSeek-R1-Distill-Qwen-7B](../models/deepseek-r1-distill-qwen-7b.md), [GPQA-Diamond](gpqa-diamond.md), [gpt-oss-120b](../models/gpt-oss-120b.md), [GPT-OSS-20B](../models/gpt-oss-20b.md), [HMMT25](hmmt25.md), [LIMO-v2](limo-v2.md), [Phi-4](../models/phi-4.md), [Qwen3-4B](../models/qwen3-4b.md), [ZebraLogic](zebralogic.md)

## Appears in

- [Ranking Reasoning LLMs under Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1544/summary.md) — Formalizes ranking reasoning LLMs under test-time scaling as inference over a dense response tensor of repeated stochastic trials, compares 72 ranking methods (paired-comparison, IRT, voting, graph/spectral) across 20 models and four Olympiad math benchmarks, and finds Bayes_R0@N (Bayesian mean with an empirical greedy-decoding prior) is the most stable low-budget ranking method -- though its greedy prior can introduce systematic bias when greedy and stochastic sampling disagree.
- [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-876/summary.md) — STOP (Super TOken for Pruning) is a lightweight, LoRA-based module that reads a frozen LRM's cached KV states via a single learnable [STOP] token to score and prune futile parallel-reasoning paths early -- at negligible inference overhead (0.59% latency) -- and is shown, via a proposed four-way taxonomy of path-pruning signal generators, to dominate external-signal and non-learnable internal-signal baselines in both accuracy and compute across model scales 1.5B-20B.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
