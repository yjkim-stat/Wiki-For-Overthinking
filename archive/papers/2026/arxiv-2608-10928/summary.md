<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling

- **Authors**: Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat, Soumyabrata Pal, Ramasuri Narayanam, Dinesh Manocha
- **Venue**: cs.AI
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10928>
- **PDF**: <https://arxiv.org/pdf/2608.10928v1>
- **Topics**: reasoning-faithfulness, reasoning-training, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.50, test-time-scaling 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) improve performance by allocating additional inference-time compute to generate extended chain-of-thought reasoning. However, recent studies reveal that sequential test-time scaling often yields diminishing or even negative returns, as longer traces exhibit increased uncertainty, error compounding, and drift from the original problem. We propose ThinkRetrieve, a test-time scaling framework that augments the reasoning traces of LRMs with dynamically retrieved solved examples at each reasoning step. Given an external corpus of problems paired with step-by-step solutions, ThinkRetrieve retrieves relevant exemplars at each intermediate step and injects them directly into the thinking trace, providing the model with guidance on how to reason rather than merely what facts are relevant. Experiments across five reasoning models (1.5B--8B parameters) on GSM-8K, MATH-500, AIME 2025, and SciQ demonstrate that ThinkRetrieve consistently improves accuracy over standard test-time scaling, with relative gains of up to $60\%$ on AIME 2025.

---

Record id: `arxiv:2608.10928`
