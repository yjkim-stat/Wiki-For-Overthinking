<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AutoL2S: Auto Long-Short Reasoning for Efficient Large Language Models

- **Authors**: Feng Luo, Yu-Neng Chuang, Guanchu Wang, Hoang Anh Duy Le, Shaochen Zhong, Hongyi Liu, Jiayi Yuan, Yang Sui, Vladimir Braverman, Vipin Chaudhary, Xia Hu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.831/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.831.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.831
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Reasoning-capable large language models (LLMs) achieve strong performance on complex tasks but often exhibit overthinking after distillation, generating unnecessarily long chain-of-thought (CoT) reasoning even for simple inputs and incurring high inference cost. However, naively shortening reasoning length can degrade reasoning accuracy, as concise reasoning may be insufficient for certain inputs and lacks explicit supervision. We propose Auto Long-Short Reasoning (AutoL2S), a distillation framework that empowers non-reasoning LLMs to think thoroughly but only when necessary. AutoL2S first learns a lightweight switching token with verified long-short CoTs to enable instance-wise long-short reasoning selection. Then it leverages long-short reasoning rollouts induced by switching tokens within a GRPO-style loss to improve reasoning efficiency while maintaining accuracy. Experiments demonstrate that AutoL2S effectively reduces reasoning length up to 71% with minimal accuracy loss, yielding markedly better trade-off in token length and inference time while preserving accuracy. The code is available at https://github.com/amandaluof/AutoL2S.

---

Record id: `doi:10.18653/v1/2026.findings-acl.831`
