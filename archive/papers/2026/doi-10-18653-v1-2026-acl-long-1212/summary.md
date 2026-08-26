<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning Fails Where Step Flow Breaks

- **Authors**: Xiaoyu Xu, Yulan Pan, Xiaosong Yuan, Zhihong Shen, Minghao Su, Yuanhao Su, Xiaofeng Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1212/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1212.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1212
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) that generate long chains of thought now perform well on multi-step math, science, and coding tasks. However, their behavior is still unstable and hard to interpret, and existing analysis tools struggle with such long, structured reasoning traces. We introduce Step-Saliency, which pools attention–gradient scores into step-to-step maps along the question–thinking–summary trajectory. Across several models, Step-Saliency reveals two recurring information-flow failures: Shallow Lock-in, where shallow layers over-focus on the current step and barely use earlier context, and Deep Decay, where deep layers gradually lose saliency on the thinking segment and the summary increasingly attends to itself and the last few steps. Motivated by these patterns, we propose StepFlow, a saliency-inspired test-time intervention that adjusts shallow saliency patterns measured by Step-Saliency via Odds-Equal Bridge and adds a small step-level residual in deep layers via Step Momentum Injection. StepFlow improves accuracy on math, science, and coding tasks across multiple LRMs without retraining, indicating that repairing information flow can recover part of their missing reasoning performance.

---

Record id: `doi:10.18653/v1/2026.acl-long.1212`
