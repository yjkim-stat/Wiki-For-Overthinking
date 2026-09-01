# LIMO-v2

<!-- auto:begin -->

LIMO-v2 is a curated long-CoT reasoning distillation dataset used in these sources as source/comparison data: CoRD applies its collaborative step-wise decoding to reprocess LIMO-v2's question set (alongside LIMO-v1 and S1k-1.1), showing student models trained on CoRD-processed LIMO-v2 outperform those trained on the original curated dataset; the ranking-reasoning-LLMs paper's own cited note does not name LIMO-v2 specifically.

- **Kind**: dataset
- **Topics**: [overthinking](../topics/overthinking.md)
- **Sources**: 2

**Related**: [AIME 2024](aime-2024.md), [AIME 2025](aime-2025.md), [HMMT25](hmmt25.md), [Phi-4](../models/phi-4.md), [Qwen3-4B](../models/qwen3-4b.md), [s1k-1.1](s1k-1-1.md)

## Appears in

- [Ranking Reasoning LLMs under Test-Time Scaling](../../archive/papers/2026/doi-10-18653-v1-2026-acl-long-1544/summary.md) — Formalizes ranking reasoning LLMs under test-time scaling as inference over a dense response tensor of repeated stochastic trials, compares 72 ranking methods (paired-comparison, IRT, voting, graph/spectral) across 20 models and four Olympiad math benchmarks, and finds Bayes_R0@N (Bayesian mean with an empirical greedy-decoding prior) is the most stable low-budget ranking method -- though its greedy prior can introduce systematic bias when greedy and stochastic sampling disagree.
- [Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding](../../archive/papers/2026/doi-10-18653-v1-2026-findings-acl-1867/summary.md) — CoRD reframes long-CoT reasoning distillation from post-hoc curation (each teacher generates a complete trajectory, then the best one is picked) to step-wise collaborative decoding: heterogeneous teacher LRMs propose candidate next reasoning steps in a shared, prompt-guided step format, a meta-prover scores each candidate by the predictive perplexity of the ground-truth answer given that step, and beam search retains the top-B partial trajectories -- producing higher-quality composite reasoning data than either post-hoc curation or a GPT-mini-based post-hoc integrator, and distilling student models whose 32B version, trained on CoRD data from heterogeneous teachers, actually surpasses every individual teacher's own Pass@1 on AIME24/25.

<!-- auto:end -->

## Notes

_Anything below the marker above is yours. It is never overwritten._
