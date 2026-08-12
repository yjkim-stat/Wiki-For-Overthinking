<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Latent Thought Credit: Multi-Answer Credit Assignment for Latent Reasoning

- **Authors**: Xuyang Zhao, Liting Zhang, Zichen Xu, Yong Chen, Wenjia Zeng, Shiwan Zhao, Qicheng Li
- **Venue**: cs.AI
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01593>
- **PDF**: <https://arxiv.org/pdf/2608.01593v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Latent reasoning allows language models to carry out intermediate reasoning in continuous latent representations rather than fully externalizing it as discrete chains of thought. However, assigning credit to such latent thoughts from answer-only rewards is difficult: a single final answer mixes thought quality with answer-sampling noise. We propose \textbf{Latent Thought Credit (LTC)}, a hierarchical credit-assignment framework for latent reasoning. For each prompt, LTC samples multiple latent thoughts, fixes the context after each thought, and estimates thought-level expected reward by averaging rewards over multiple answers generated from that fixed context. LTC uses thought-level advantages to optimize the latent-thought phase, answer-level advantages to optimize the answer phase, and an advantage-weighted thought-matching objective that helps the policy reproduce high-credit latent thoughts. We instantiate LTC in a GRPO-style on-policy training framework and evaluate it across mathematical reasoning and STEM multiple-choice tasks. LTC achieves the best average accuracy among the compared methods, while ablations and fixed-context diagnostics show that multi-answer estimation reduces reward-estimation error and mitigates ambiguous or incorrect thought-level credit.

---

Record id: `arxiv:2608.01593`
