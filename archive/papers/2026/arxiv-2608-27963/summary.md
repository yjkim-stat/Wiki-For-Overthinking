<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# SABER: Stability-Aware Early Exit for LLM Reasoning via Adversarial Branch Probing

- **Authors**: Wanli Cheng, Haiya Xiang, Juntao Li, Hongling Wang, Wenliang Chen
- **Venue**: cs.AI
- **Published**: 2026-08-31
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.27963>
- **PDF**: <https://arxiv.org/pdf/2608.27963>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) achieve strong reasoning capabilities, yet long-chain reasoning becomes inefficient once the intermediate answer stabilizes across reasoning steps: additional reasoning yields little marginal benefit while incurring substantial inference cost. Existing early-exit methods based on confidence or entropy poorly capture reasoning stability, while consistency-based approaches rely on multi-step trajectory agreement, requiring sequential evaluations that delay exit. To better balance efficiency and reliability, we propose SABER, a training-free framework for stability-aware early exit via adversarial branch probing. SABER constructs simple yet effective semantic perturbations around intermediate reasoning states to form adversarial branches, and applies lightweight probing to estimate their likely final outcomes without full trajectory rollouts. When the probed outcomes remain consistent across branches, SABER exits early; otherwise, it continues reasoning. Experiments across multiple reasoning benchmarks and model architectures show that SABER reduces reasoning token consumption by 30.2\%--39.8\% on average while maintaining competitive accuracy with full-length reasoning.

---

Record id: `arxiv:2608.27963`
