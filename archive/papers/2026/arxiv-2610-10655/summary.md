<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Nullify: Null-Space Activation Steering for Training-Free LLM Unlearning

- **Authors**: Wei Zhai, Xiang Liu, Qiang Huang, Rui Qian, Lemao Liu, Ziwei Li, Ziqi Wang, Zhitao Huang, Dejing Dou
- **Venue**: cs.LG
- **Published**: 2026-10-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2610.10655>
- **PDF**: <https://arxiv.org/pdf/2610.10655>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Language Models (LLMs) inevitably internalize substantial amounts of sensitive or private information during pre-training, while LLM unlearning aims to selectively erase specific knowledge to prevent privacy leakage with minimal loss of model utility. However, existing methods struggle to balance forget quality with utility, and typically incur substantial computational costs due to parameter fine-tuning. To address this, we propose Nullify, a training-free, non-destructive activation steering method for LLM unlearning. Nullify employs steering vectors during inference to redirect privacy-related activations away from their memorized answers, while satisfying a null-space constraint that leaves retained-query activations essentially unaffected to maintain utility. Evaluations on TOFU and MUSE show that Nullify matches or surpasses established baselines in forget quality while achieving near-lossless preservation of model utility. By avoiding weight updates entirely, Nullify serves as an efficient, plug-and-play inference-time intervention framework.

---

Record id: `arxiv:2610.10655`
