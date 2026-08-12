<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning

- **Authors**: Zhaoxin Yu, Qi Shen, Hengli Li, Zhaowei Zhang, Song-Chun Zhu, Chi Zhang, Zilong Zheng
- **Venue**: cs.LG
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02585>
- **PDF**: <https://arxiv.org/pdf/2608.02585v1>
- **Topics**: reasoning-faithfulness, test-time-scaling
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.25, test-time-scaling 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Optimization-based latent reasoning improves large language model outputs by optimizing instance-specific continuous states at test time while keeping model parameters frozen. Existing methods, however, typically connect these states to the reasoning trajectory through decoded tokens, making sequence-level credit assignment indirect and obscuring how latent updates shape subsequent reasoning. We introduce GradCuit (gradient through circuit), which inserts optimizable latent states at a selected Transformer layer between the hidden representations of the prompt and the generated continuation. Causal self-attention provides every continuation-token log-probability with a differentiable path to every preceding latent state through the remaining Transformer blocks, enabling reward-weighted gradients from the entire continuation to be assigned directly to the latents. Across five instruction-tuned backbones, three reasoning benchmarks, and two answer formats, GradCuit achieves an average accuracy of 64.5%, outperforming chain-of-thought prompting by 6.6 percentage points and the strongest competing method by 2.4 points. GradCuit also demonstrates greater robustness: across seven learning-rate settings, it consistently outperforms LatentSeek while reducing the standard deviation of accuracy from 1.53 to 0.82, and even its random-walk variant remains competitive with LatentSeek. For interpretability, token-level gradient attribution reveals that latent influence concentrates on reasoning-connector tokens, while layer analysis identifies early-to-middle Transformer layers as the most effective optimization space. By directly optimizing internal reasoning from outcome feedback, GradCuit opens a new axis of robust and interpretable test-time scaling, where LLMs adapt how they reason rather than merely regenerate, sample, or rerank outputs.

---

Record id: `arxiv:2608.02585`
