<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/117041>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

Studies how often a verifier should be called during LLM generation, proposing a search algorithm that tunes verification granularity to trade off accuracy and compute in test-time scaling.

## Problem

In test-time scaling with verifiers, prior work verifies either only the final output or every individual step, without studying whether intermediate verification frequencies could do better; the effect of this granularity choice on accuracy and compute cost was unexamined.

## Contributions

- First systematic study of verification granularity (how often a verifier is invoked during generation) as a distinct axis of test-time scaling, beyond final-answer-only or per-step verification
- Introduces Variable Granularity Search (VG-Search), a unified algorithm generalizing beam search and Best-of-N sampling via a tunable granularity parameter g
- Shows that dynamically selecting g improves compute efficiency and scaling behavior across compute budgets, generator-verifier configurations, and task attributes
- Proposes adaptive VG-Search strategies achieving up to 3.1% accuracy gains over Beam Search and 3.6% over Best-of-N while reducing FLOPs by over 52%

## Method

Formalizes verification granularity as a tunable parameter g controlling how frequently a verifier is invoked during generation. Variable Granularity Search (VG-Search) generalizes beam search (fine granularity) and Best-of-N sampling (coarse granularity) as special cases of this parameter. Adaptive strategies then select g dynamically per compute budget, generator-verifier configuration, and task attribute.

## Results

Adaptive VG-Search achieves accuracy gains of up to 3.1% over Beam Search and 3.6% over Best-of-N, while reducing FLOPs by over 52%. Specific benchmark names and absolute accuracy numbers are not given in the abstract.

## Limitations

The abstract does not name the specific benchmarks, generator/verifier model pairs, or task domains used in the experiments; the paper focuses on search-time verification frequency rather than on the length of a single model's reasoning trace.

## Why it matters here

- **overthinking**: Addresses a different lever of test-time compute than reasoning-token length: it tunes how often an external verifier is called during parallel search (beam search / Best-of-N) rather than how long a single reasoning trace runs. It is relevant to the topic's test-time-compute-efficiency angle but does not discuss reasoning length, stopping a chain of thought, or over/underthinking within a single generation.

## Entities

- **Concepts**: verification granularity, beam search and Best-of-N as special cases of a granularity parameter, compute-efficiency in test-time scaling via verifier call frequency
- **Methods**: Variable Granularity Search (VG-Search), beam search, [Best-of-N sampling](../../../../wiki/methods/best-of-n-sampling.md)
- **Datasets**: _none recorded_

Tags: `test-time-scaling`, `verification`, `search`, `compute-efficiency`, `beam-search`

## Abstract

Abstract Test-time scaling (TTS) has proven effective in enhancing the reasoning capabilities of large language models (LLMs). Verification plays a key role in TTS, simultaneously influencing (1) reasoning performance and (2) compute efficiency, due to the quality and computational cost of verification. In this work, we challenge the conventional paradigms of verification, and make the first attempt toward systematically investigating the impact of verification granularity—that is, how frequently the verifier is invoked during generation, beyond verifying only the final output or individual generation steps. To this end, we introduce Variable Granularity Search (VG-Search), a unified algorithm that generalizes beam search and Best-of-N sampling via a tunable granularity parameter $g$. Extensive experiments with VG-Search under varying compute budgets, generator-verifier configurations, and task attributes reveal that dynamically selecting $g$ can improve the compute efficiency and scaling behavior. Building on these findings, we propose adaptive VG-Search strategies that achieve accuracy gains of up to 3.1\% over Beam Search and 3.6\% over Best-of-N, while reducing FLOPs by over 52\%. We will open-source the code to support future research.

---

Record id: `title:7409f584637723da`
