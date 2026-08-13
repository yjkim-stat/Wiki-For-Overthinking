<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents

- **Authors**: Di Wu, Xiaohui Zhu
- **Venue**: cs.AI
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.10198>
- **PDF**: <https://arxiv.org/pdf/2608.10198v1>
- **Topics**: reasoning-evaluation
- **Relevance score**: reasoning-evaluation 0.40, reasoning-interpretability 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Latent-space communication allows heterogeneous vision-language model agents to exchange continuous representations without serializing visual and reasoning states into text. Vision Wormhole realizes this approach by translating visual features into a universal latent representation that can be consumed by another model, but every message is transported as a dense tensor of the same size regardless of its content. A fixed-capacity dense tensor therefore need not have a fixed effective information density: some messages may use only a small fraction of the available representational degrees of freedom. This observation suggests that the communication channel may be substantially compressible. We study its redundancy by fitting a post-hoc sparse autoencoder to frozen Vision Wormhole activations and measuring reconstruction, downstream utility, feature reuse, and token-level interventions across nine reasoning benchmarks. Relative to the original float32 transport, a uint16-index/float16-value sparse payload with k=4 active coefficients per token reduces the transmitted bytes by 128x. In a single-run evaluation, the seven-task non-AIME mean accuracy changes from 49.85% to 49.77%. The fitted 4096-element dictionary uses only 50 features, and task-level active sets have a mean pairwise Jaccard similarity of 0.906. These measurements establish strong post-hoc compressibility relative to the original transport, but do not yet isolate the incremental contribution of sparse coding from position selection, reduced precision, low-rank structure, or SAE optimization effects. The results motivate matched-payload comparisons and communication mechanisms whose payload adapts to the information used by each message.

---

Record id: `arxiv:2608.10198`
