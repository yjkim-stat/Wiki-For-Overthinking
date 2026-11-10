<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Entropy-Sparing for Efficient Reasoning

- **Authors**: Cong Jiang, Xiaofeng Zhang, Tom Ko, Zheng Zhang
- **Venue**: cs.CL
- **Published**: 2026-11-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2611.11901>
- **PDF**: <https://arxiv.org/pdf/2611.11901v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) produce explicit chains of thought to improve transparency, but they frequently overthink, generating long yet inefficient reasoning chains that inflate computational costs and risk introducing errors. While numerous reinforcement learning methods struggle to penalize verbosity to achieve conciseness, they typically apply the penalty uniformly across lengthy sequences, which leads to credit confounding, that is, the failure to distinguish essential reasoning steps from superfluous ones. In this paper, we study a measurable proxy for this confounding: high-entropy tokens that often coincide with surface transition points where reasoning re-enters verification. Based on this insight, we propose Adaptive Entropy-Sparing (AES), which selectively spares high-entropy tokens that occur before an efficient in-group reference, while penalizing overlength high-entropy suffix tokens associated with superfluous branching. Our AES thereby navigates the suppression-exploration trade-off, reducing overthinking while preserving average reasoning accuracy. We also present an entropy-length model that motivates why local uncertainty can serve as a proxy for future reasoning cost. Across eight reasoning benchmarks, AES reduces reasoning length by up to 52.9% while increasing mean accuracy by up to 3.8% over the base models, consistently outperforming existing efficiency-oriented methods. Our code is available at https://github.com/MobiusDai/AES.

---

Record id: `arxiv:2611.11901`
