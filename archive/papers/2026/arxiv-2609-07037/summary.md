<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Disentangling Steering Vectors

- **Authors**: Takeru Hiramatsu, Kyohei Atarashi, Koh Takeuchi, Hisashi Kashima
- **Venue**: cs.LG
- **Published**: 2026-09-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2609.07037>
- **PDF**: <https://arxiv.org/pdf/2609.07037>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Activation steering has emerged as a lightweight, inference-time approach to control the behavior of Large Language Models (LLMs). However, traditional steering vectors used to intervene in LLMs' activations, such as those derived from the difference-in-means method, tend to entangle multiple semantic and stylistic concepts into a single composite direction, leading to unpredictable steering effects. Our core objective is to disentangle this composite direction into its constituent concepts. To this end, we propose Steering Vector Dissection, a framework to explicitly isolate individual and semantically consistent features from these composite directions. Specifically, we pair positive and negative activations and take their differences to generate a set of instance-level steering vectors, and train a dedicated Sparse Autoencoder (SAE) directly on them. Quantitative evaluations across two datasets, two models, and two intervention depths show that our method yields a set of semantically consistent basis vectors whose steering effects are mutually distinguishable. Furthermore, we show that this disentanglement enables precise control over model behaviors.

---

Record id: `arxiv:2609.07037`
