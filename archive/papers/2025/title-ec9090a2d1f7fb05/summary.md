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

Proposes DisCO, a discriminative constrained-optimization alternative to GRPO for RL-training of large reasoning models, that removes question-level difficulty bias and entropy instability, giving average gains of 7% over GRPO and 6% over DAPO on math reasoning benchmarks with a 1.5B model.

## Problem

GRPO, the RL method behind DeepSeek-R1-style training of large reasoning models, has an inherent question-level difficulty bias from its group relative advantage function and suffers entropy instability during training; the paper addresses how to fix these issues in the RL objective itself.

## Contributions

- Identifies a question-level difficulty bias inherent to GRPO's group relative advantage function under binary reward
- Draws a connection between GRPO and traditional discriminative methods in supervised learning
- Introduces DisCO, a discriminative constrained optimization framework replacing the group relative objective with a discriminative scoring-function objective
- Replaces clipping-based surrogates with non-clipping RL surrogate objectives used as scoring functions, addressing entropy instability
- Uses a constrained optimization approach to enforce the KL divergence constraint, and allows techniques for handling class imbalance in the positive/negative answer distribution

## Method

DisCO reframes RL fine-tuning of large reasoning models as a discriminative learning problem: instead of GRPO's group-relative advantage (which the authors show induces question-level difficulty bias), it defines a discriminative objective via a scoring function that increases scores of positive answers and decreases scores of negative ones. It replaces GRPO's clipping-based surrogate objectives with non-clipping surrogates used directly as scoring functions, which the authors argue stabilizes entropy during training, and enforces the KL divergence constraint via a constrained optimization approach rather than clipping.

## Results

On six benchmark tasks for mathematical reasoning with a 1.5B SFT-finetuned model, DisCO achieves average gains of 7% over GRPO and 6% over DAPO.

## Limitations

The abstract does not name the six benchmark tasks, and evaluation is limited to a 1.5B SFT-finetuned model; it does not discuss reasoning length, inference cost, or generalization to larger model scales.

## Why it matters here

- **overthinking**: Tangential. The paper is about the RL training objective used to fine-tune large reasoning models for accuracy on math benchmarks -- fixing difficulty bias and entropy instability in GRPO -- not about reasoning length, thinking budgets, or when a model should stop generating. It shares only the generic 'large reasoning model' keyword with the topic and does not address the accuracy/efficiency tradeoff of reasoning length or test-time compute allocation.

## Entities

- **Concepts**: group relative advantage, difficulty bias, discriminative learning, entropy instability in RL, KL-constrained optimization
- **Methods**: DisCO, GRPO (baseline), DAPO (baseline), discriminative constrained optimization
- **Datasets**: six benchmark tasks for mathematical reasoning (unspecified names)

Tags: `grpo`, `reinforcement-learning`, `discriminative-learning`, `difficulty-bias`, `not-reasoning-length`

## Abstract

Abstract The recent success and openness of DeepSeek-R1 have brought widespread attention to Group Relative Policy Optimization (GRPO) as a reinforcement learning method for large reasoning models (LRMs). In this work, we analyze the GRPO objective under a binary reward setting and reveal an inherent limitation of question-level difficulty bias arising from its group relative advantage function. We also identify a connection between GRPO and traditional discriminative methods in supervised learning. Motivated by these insights, we introduce a new Discriminative Constrained Optimization (DisCO) framework for reinforcing LRMs, grounded in the principle of discriminative learning: increasing the scores of positive answers while decreasing those of negative ones. The main differences between DisCO and GRPO and its recent variants are: (1) it replaces the group relative objective with a discriminative objective defined by a scoring function; (2) it abandons clipping-based surrogates in favor of non-clipping RL surrogate objectives used as scoring functions; (3) it employs a simple yet effective constrained optimization approach to enforce the KL divergence constraint. As a result, DisCO offers notable advantages over GRPO and its variants: (i) it completely eliminates difficulty bias by adopting discriminative objectives; (ii) it addresses the entropy instability in GRPO and its variants through the use of non-clipping scoring functions and a constrained optimization approach, yielding long and stable training dynamics; (iii) it allows the incorporation of advanced discriminative learning techniques to address data imbalance, where a significant number of questions have more negative than positive generated answers during training. Our experiments on enhancing the mathematical reasoning capabilities of SFT-finetuned models show that DisCO significantly outperforms GRPO and its improved variants such as DAPO, achieving average gains of 7\% over GRPO and 6\% over DAPO across six benchmark tasks for a 1.5B model.

---

Record id: `title:ec9090a2d1f7fb05`
