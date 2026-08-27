<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning

- **Authors**: Lam So, Canhui Wu, Han Lin
- **Venue**: cs.CL
- **Published**: 2026-08-26
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.25583>
- **PDF**: <https://arxiv.org/pdf/2608.25583v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning-oriented large language models often achieve strong problem-solving performance by generating long chains of thought, but this behavior substantially increases inference cost and latency. In contrast, instruction-tuned models tend to answer more concisely, yet often lack comparable reasoning ability. This accuracy-efficiency mismatch motivates a lightweight approach that combines the strengths of both models without full model retraining. In this paper, we propose GRIP (Granular Reward-guided Interpolation of Parameters), a reward-guided parameter interpolation framework for efficient reasoning. Given a reasoning model and an instruction model with identical architectures, GRIP assigns learnable interpolation ratios to individual modules and optimizes only these ratios while keeping both source models frozen. The interpolation ratios are trained with a reward signal that favors responses that are both correct and concise. Experiments show that GRIP achieves a better accuracy-efficiency trade-off than fixed or search-based merging baselines and further reveals module-wise fusion patterns associated with efficient reasoning.

---

Record id: `arxiv:2608.25583`
