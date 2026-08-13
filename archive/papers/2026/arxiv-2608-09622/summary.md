<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search

- **Authors**: Youssef A. Elhagrasy, Ian Hill, André Ivanov
- **Venue**: cs.AI
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09622>
- **PDF**: <https://arxiv.org/pdf/2608.09622v1>
- **DOI**: 10.1109/TR.2026.3722801
- **Topics**: test-time-scaling
- **Relevance score**: test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reliability qualification of advanced semiconductor devices requires sequential stress decisions that balance characterization objectives against multiple competing failure mechanisms. Current practice relies on static test plans derived from population-level acceleration models, which cannot adapt to per-unit variability or real-time degradation observations. This paper presents a closed-loop adaptive test planning framework that formulates reliability qualification as a partially observable sequential decision problem and solves it using Monte Carlo tree search for seed-action simulators (MCTS-SA) coupled with extended Kalman filter (EKF) belief-state estimation. The framework models stochastic, per-device variability in bias temperature instability (BTI), electromigration (EM), and time-dependent dielectric breakdown (TDDB), and treats stress selection as a constrained sequential optimization, i.e., to maximize the probability of successful degradation characterization while respecting catastrophic failure constraints. Under the experimental assumptions used here (discrete stress actions, proxy damage observability, and cumulative degradation without recovery), we believe this to be a novel application of tree-search-based adaptive test planning to multi-mechanism reliability qualification. Across 5,000 planning iterations, the characterization yield (CY) improves from 20% in the first 500 iterations to over 54% in the final 500, with 39% cumulative success, while the best successful test sequence terminates with EM and TDDB damage fractions DEM=0.564 and DTDDB=0.537, well within safety margins. These results demonstrate that sequential Bayesian planning can synthesize damage-aware test policies that significantly outperform non-adaptive strategies for reliability qualification under competing failure modes.

---

Record id: `arxiv:2608.09622`
