<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasMark: A Robust Watermark for Attributing LLM Reasoning Under Knowledge Distillation Attacks

- **Authors**: Peizhuo Lv, Ruihua Zhou, Yunpeng Li, Ruigang Liang, Xingshuo Han, XiaoFeng Wang, Wei Dong, Yuling Liu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.2185/>
- **PDF**: <https://aclanthology.org/2026.acl-long.2185.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.2185
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning-enhanced large language models rely on intermediate reasoning signals to solve complex, multi-step tasks, making reasoning behavior a valuable form of intellectual property. Meanwhile, knowledge distillation enables an adversary to replicate this behavior in a realistic black-box setting by repeatedly querying a deployed model on a target domain and training a local student to imitate its outputs, including reasoning traces. Existing LLM watermarks primarily operate on surface text and decoding-time token biases, and thus fail to provide reliable attribution of reasoning behavior once it is transferred through knowledge distillation. ReasMark entangles the watermark with the target-domain input distribution by selecting watermark tokens from high-frequency prompts, so distillation queries naturally activate it. It then embeds the watermark by score-conditioned losses that create a detectable reasoning-length gap for black-box verification. Comprehensive experiments across multiple LLMs, datasets, and distillation settings demonstrate that ReasMark consistently outperforms existing baselines while preserving task utility.

---

Record id: `doi:10.18653/v1/2026.acl-long.2185`
