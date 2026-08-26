<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ARM2: Adaptive Reasoning Model with Vision Understanding and Executable Code

- **Authors**: Jian Xie, Zhendong Chu, Aoxiao Zhong, Kai Zhang, Mingzhe Han, Xing Fan, Jialie Shen, Qingsong Wen
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1365/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1365.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1365
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) often suffer from the “over-thinking” problem, generating unnecessarily long reasoning on simple tasks. Some strategies have been proposed to mitigate this issue, such as length penalties or routing mechanisms, but they are typically heuristic and task-specific, lacking a general framework for adaptive reasoning. In this paper, we present ARM2, a unified model that adaptively balances reasoning performance and efficiency across multiple formats through a reinforcement learning framework augmented with length-aware optimization. Beyond conventional natural language inference, ARM2 integrates vision understanding, extending its applicability to multimodal. Moreover, ARM2 integrates executable code into reasoning, enabling substantial reductions in token cost while preserving task performance compared to long CoT. Experiments demonstrate that ARM2 achieves performance on par with traditional reasoning models trained with GRPO, while reducing token usage by over 70% on average. We further conduct extensive analyses to validate the effectiveness of ARM2 and the soundness of its design.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1365`
