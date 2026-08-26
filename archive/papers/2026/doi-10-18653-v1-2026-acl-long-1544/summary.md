<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Ranking Reasoning LLMs under Test-Time Scaling

- **Authors**: Mohsen Hariri, Michael Hinczewski, Jing Ma, Vipin Chaudhary
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1544/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1544.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1544
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time scaling evaluates reasoning LLMs by sampling multiple outputs per prompt, but ranking models in this regime remains underexplored. We formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library that implements statistical ranking methods such as paired-comparison models, item response theory (IRT) models, voting rules, and graph- and spectral-based methods. Across 20 reasoning models on four Olympiad-style math benchmarks (AIME’24, AIME’25, HMMT’25, and BrUMO’25; up to N = 80 trials), most full-trial rankings agree closely with the Bayesian gold standard Bayes_𝒰@80 (mean Kendall’s τ_b = 0.93–0.95), and 19–34 methods recover exactly the same ordering. In the single-trial regime, the best methods reach τ_b ≈ 0.86.Using greedy decoding as an empirical prior (Bayes_R₀@N) reduces variance at N = 1 by 16–52%, but can bias rankings when greedy and stochastic sampling disagree. These results identify reliable ranking methods for both high- and low-budget test-time scaling. We release Scorio as an open-source library at https://github.com/mohsenhariri/scorio.

---

Record id: `doi:10.18653/v1/2026.acl-long.1544`
