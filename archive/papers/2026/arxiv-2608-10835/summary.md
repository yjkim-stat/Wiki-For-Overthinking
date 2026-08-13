<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations

- **Authors**: Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca, Ethan Fetaya, Yftah Ziser, Gal Chechik, Haggai Maron
- **Venue**: cs.CV
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10835>
- **PDF**: <https://arxiv.org/pdf/2608.10835v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Vision-Language Models (LVLMs) achieve impressive visual reasoning and dialogue capabilities, yet frequently hallucinate content unsupported by the visual input. Effective mitigation requires token-level localization, enabling targeted intervention without discarding the entire response. Existing detectors require expensive full-model fine-tuning, rely on external verifiers that ignore the model's generation process, or reduce internal signals to isolated features and hand-crafted statistics, discarding spatial, sequential, and relational structure. We introduce \textbf{UniProbe}, a lightweight, unified, learnable detector that models a frozen LVLM's heterogeneous computational trace from a single forward pass. UniProbe constructs a directed graph over image patches, query tokens, and generated tokens, with attention weights encoding their relations. It processes this trace with alternating structure-aware modules: a GNN for relational evidence, a ViT for 2-D visual geometry, and a GRU for response order. Interleaving them allows spatial, relational, and sequential evidence to interact throughout the detector. We further develop a streaming variant for hallucination-aware decoding, which detects and resamples hallucinated tokens during generation, and a self-adaptation strategy aligning the detector with the LVLM's own generations. Across diverse LVLM backbones, UniProbe achieves state-of-the-art token-level and object-hallucination detection. During decoding, it reduces object hallucinations by up to 55\% at $1.06\times$ the latency of standard generation.

---

Record id: `arxiv:2608.10835`
