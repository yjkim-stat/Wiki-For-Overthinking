<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# LEMUR: Latent Entropy-aware Multimodal Unlearning via Visual-anchored Reasoning Redirection

- **Authors**: Xinhao Zhong, Yuxia Qiao, Junhao Li, Hao Fang, Yi Sun, Bin Chen
- **Venue**: cs.LG
- **Published**: 2026-08-12
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11691>
- **PDF**: <https://arxiv.org/pdf/2608.11691v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-faithfulness 0.25, reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reinforcement-learning (RL) post-training equips multimodal large reasoning models (MLRMs) with exploratory chains of thought (CoT), substantially improving visual reasoning. However, we find that this capability introduces a distinct privacy vulnerability: even when a sensitive fact is successfully unlearned from the final answer, the model may still reproduce it in its reasoning trace. This leakage is substantially more pronounced in natively RL-trained MLRMs than in their non -reasoning base models, revealing a privacy risk that existing unlearning methods are not designed to address. We show that RL-induced exploration leaves sensitive content with a distinctive token-level entropy signature that is largely absent from base models. Based on this observation, we propose LEMUR, a fully training-free, inference-time unlearning framework for natively RL-trained multimodal models. LEMUR uses entropy dynamics as a control signal to identify when sensitive reasoning begins and when sanitization should stop. During this interval, it redirects the reasoning trajectory through entropy-modulated visual-anchor latent injection, replacing committed tokens with sanitized, probability-weighted embeddings re-grounded in the input image. Across diverse MLRMs, LEMUR consistently outperforms existing unlearning met hods in suppressing both reasoning-trace and answer leakage, while better preserving non-sensitive utility and output fluency. These results demonstrate that RL-induced entropy dynamics provide a distinctive signal for privacy leakage and that exploiting this signal enables effective training-free unlearning for reasoning-capable multimodal models.

---

Record id: `arxiv:2608.11691`
