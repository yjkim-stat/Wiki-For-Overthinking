<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# DisCO: Reinforcing Large Reasoning Models with Discriminative Constrained Optimization

- **Authors**: _unknown_
- **Venue**: NeurIPS 2025
- **Published**: 2025-01-01
- **Source**: virtualsite
- **Link**: <https://neurips.cc/virtual/2025/poster/114995>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## In one line

DisCO replaces GRPO's group-relative advantage objective with a discriminative-learning objective (raising positive-answer scores, lowering negative-answer scores) using non-clipping surrogates and constrained KL optimization, eliminating GRPO's question-level difficulty bias and entropy instability, and beating GRPO/DAPO by 6-7% on math reasoning benchmarks.

## Problem

Group Relative Policy Optimization (GRPO), the RL method behind DeepSeek-R1-style training of large reasoning models, has an inherent question-level difficulty bias arising from its group-relative advantage function under binary rewards, and suffers entropy instability from its clipping-based surrogate objective.

## Contributions

- an analysis identifying GRPO's inherent question-level difficulty bias and its connection to discriminative supervised learning
- DisCO, a discriminative, non-clipping, KL-constrained RL objective for reasoning-model fine-tuning
- 7%/6% average gains over GRPO/DAPO across six math-reasoning benchmarks with a 1.5B model, plus improved training stability

## Method

Analyzes GRPO's objective under binary rewards, identifying the difficulty-bias mechanism and a connection to traditional discriminative learning in supervised settings; introduces Discriminative Constrained Optimization (DisCO), which (1) replaces the group-relative objective with a discriminative objective defined by a scoring function, (2) abandons clipping-based surrogates in favor of non-clipping RL surrogate objectives used as scoring functions, and (3) enforces the KL-divergence constraint via a constrained-optimization approach rather than clipping, also incorporating techniques for data imbalance (more negative than positive generated answers).

## Results

On enhancing mathematical reasoning of SFT-finetuned models, DisCO significantly outperforms GRPO and its improved variants such as DAPO, with average gains of 7% over GRPO and 6% over DAPO across six benchmark tasks for a 1.5B model; DisCO eliminates GRPO's difficulty bias and yields long, stable training dynamics by avoiding clipping-induced entropy instability.

## Limitations

Not stated in the fetched abstract beyond the 1.5B-model scale tested; generalization to larger model scales is not discussed in the excerpt retrieved.

## Why it matters here

- **overthinking**: Indirectly relevant: this is a training-algorithm improvement over GRPO (removing difficulty bias, stabilizing entropy) rather than a direct intervention on reasoning length, but since GRPO-family training is the mechanism by which most reasoning models acquire their (often overlong) reasoning behavior, a more stable, less-biased RL objective is upstream infrastructure that length-aware or efficiency-aware reward shaping (as used in several overthinking-mitigation papers) builds on.

## Entities

- **Concepts**: question-level difficulty bias in GRPO, discriminative learning for RL fine-tuning, constrained KL-divergence optimization
- **Methods**: Discriminative Constrained Optimization (DisCO), Group Relative Policy Optimization (GRPO, baseline), [DAPO (baseline)](../../../../wiki/methods/dapo-baseline.md)
- **Datasets**: _none recorded_

Tags: `reinforcement-learning`, `GRPO`, `large-reasoning-models`, `training-stability`

## Abstract

Abstract The recent success and openness of DeepSeek-R1 have brought widespread attention to Group Relative Policy Optimization (GRPO) as a reinforcement learning method for large reasoning models (LRMs). In this work, we analyze the GRPO objective under a binary reward setting and reveal an inherent limitation of question-level difficulty bias arising from its group relative advantage function. We also identify a connection between GRPO and traditional discriminative methods in supervised learning. Motivated by these insights, we introduce a new Discriminative Constrained Optimization (DisCO) framework for reinforcing LRMs, grounded in the principle of discriminative learning: increasing the scores of positive answers while decreasing those of negative ones. The main differences between DisCO and GRPO and its recent variants are: (1) it replaces the group relative objective with a discriminative objective defined by a scoring function; (2) it abandons clipping-based surrogates in favor of non-clipping RL surrogate objectives used as scoring functions; (3) it employs a simple yet effective constrained optimization approach to enforce the KL divergence constraint. As a result, DisCO offers notable advantages over GRPO and its variants: (i) it completely eliminates difficulty bias by adopting discriminative objectives; (ii) it addresses the entropy instability in GRPO and its variants through the use of non-clipping scoring functions and a constrained optimization approach, yielding long and stable training dynamics; (iii) it allows the incorporation of advanced discriminative learning techniques to address data imbalance, where a significant number of questions have more negative than positive generated answers during training. Our experiments on enhancing the mathematical reasoning capabilities of SFT-finetuned models show that DisCO significantly outperforms GRPO and its improved variants such as DAPO, achieving average gains of 7\% over GRPO and 6\% over DAPO across six benchmark tasks for a 1.5B model.

---

Record id: `title:ec9090a2d1f7fb05`
