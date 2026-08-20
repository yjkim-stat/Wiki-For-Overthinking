<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Your Reasoning Model is Secretly a Reward Model - Optimization-Free Verification from Experience

- **Authors**: Zhenwen Liang, Ruosen Li, Yujun Zhou 0002, Linfeng Song, Dian Yu 0001, Xinya Du, Haitao Mi, Dong Yu 0001
- **Venue**: ACL
- **Published**: 2026-01-01
- **Source**: dblp
- **Link**: <https://doi.org/10.18653/v1/2026.acl-long.788>
- **DOI**: 10.18653/V1/2026.ACL-LONG.788
- **Topics**: reasoning-training
- **Relevance score**: reasoning-training 0.50

## In one line

Verifies correctness without training by comparing a reasoning trace's start-to-end hidden-state delta against two class centroids built from labelled experience.

## Problem

Assessing output quality is hard in high-branching settings where one prompt yields many plausible candidates. Existing verifiers work on surface text — reward models, LLM judges, majority voting — or on token-probability confidence proxies. The former is swayed by stylistic artifacts, the latter is often miscalibrated.

## Contributions

- Hidden states as a third verification signal, distinct from surface text and token-probability confidence
- The finding that correct and incorrect solutions differ geometrically in hidden-state trajectories
- Clue, a training-free non-parametric verifier using a start-to-end activation delta and two class centroids
- Selection and reranking gains on AIME 24/25, GPQA and WebInstruct-verified, including 56.7% to 70.0% on AIME 24 with a 1.5B model

## Method

A third information source is studied: hidden states, for binary correctness verification on tasks with a reliable success/failure signal such as deterministic checkers or reference-grounded answers. Correct and incorrect solutions are found to differ geometrically in their hidden-state trajectories. Clue summarizes each trace by an activation delta — the difference between hidden states at the start and end of the explicit reasoning span — and predicts correctness by comparing that delta to two class centroids computed from labelled experience. It is training-free and non-parametric, which is the point: minimal modeling assumptions isolate the signal rather than fitting it.

## Results

Across math (AIME 24/25), scientific QA (GPQA) and a multi-domain benchmark (WebInstruct-verified), Clue improves selection and reranking, with the strongest gains on smaller or less-calibrated models. On AIME 24 with a 1.5B model, accuracy rises from 56.7% (majority@64) to 70.0% (top-maj@16).

## Limitations

Requires labelled experience to compute the centroids, so it is not label-free, and it needs white-box hidden-state access. The headline comparison changes both the method and the sample budget — majority@64 against top-maj@16 — so the reported gain bundles a verification improvement with a 4x reduction in samples rather than isolating either. Gains concentrate on smaller or less-calibrated models, leaving the frontier case weaker.

## Why it matters here

- **reasoning-training**: Offers a reward signal that requires no reward model, which matters to this topic because reward-model calibration is the recurring failure in the verifier line. A non-parametric centroid comparison over activation deltas is about as assumption-light as a verifier gets, and its strongest gains on poorly calibrated models are consistent with it substituting for exactly what those models lack. It is also the third paper in this drain reading correctness off residual-stream geometry, with arxiv:2608.05660 and acl-long.2073, and the three disagree on representation — full trajectory, displacement-plus-location, start-to-end delta — while all outperforming single-layer probing. That the crudest of the three works this well is the finding worth following up.

## Entities

- **Concepts**: [verification](../../../../wiki/concepts/verification.md), [calibration](../../../../wiki/concepts/calibration.md), [residual stream](../../../../wiki/concepts/residual-stream.md), [reasoning trajectory](../../../../wiki/concepts/reasoning-trajectory.md), activation delta, best-of-n, [answer stabilization](../../../../wiki/concepts/answer-stabilization.md), pass-k
- **Methods**: Clue, [majority voting](../../../../wiki/methods/majority-voting.md), [best-of-n](../../../../wiki/methods/best-of-n.md), reward model, [LLM-as-a-judge](../../../../wiki/methods/llm-as-a-judge.md), centroid classification, [activation probing](../../../../wiki/methods/activation-probing.md)
- **Datasets**: [AIME 24](../../../../wiki/datasets/aime-2024.md), [AIME 25](../../../../wiki/datasets/aime-2025.md), [GPQA](../../../../wiki/datasets/gpqa.md), WebInstruct-verified

Tags: `verification`, `hidden states`, `training-free`, `reranking`, `calibration`

## Abstract

Assessing the quality of Large Language Model (LLM) outputs becomes especially challenging in high-branching settings, where a single prompt yields many plausible candidates. Existing verifiers typically operate on the surface text (e.g., reward models, LLM judges, majority voting) or on confidence proxies derived from token probabilities, both of which can be brittle: the former can be influenced by stylistic artifacts, while the latter is often miscalibrated. In this paper, we study a third source of information—the model’s hidden states—for binary correctness verification in tasks with a reliable success/failure signal (e.g., deterministic checkers or reference-grounded answers). We find that correct and incorrect solutions exhibit measurable geometric differences in their hidden-state trajectories. To isolate this signal with minimal modeling assumptions, we introduce C LUE (Clustering and Experience-based Verification) , a training-free, non-parametric verifier. C LUE summarizes each reasoning trace by an activation delta —the difference between hidden states at the start and end of the explicit reasoning span— and predicts correctness by comparing this delta to two class centroids computed from labeled experience. Across math (AIME 24/25), scientific QA (GPQA), and a multi-domain benchmark (WebInstruct-verified), C LUE improves selection and reranking

---

Record id: `doi:10.18653/v1/2026.acl-long.788`
