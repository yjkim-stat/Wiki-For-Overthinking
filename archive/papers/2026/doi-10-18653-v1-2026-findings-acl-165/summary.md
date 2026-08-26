<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models

- **Authors**: Tingyun li, Zishang Jiang, Jinyi Han, Xinyi Wang, Sihang Jiang, Han Xia, Zhaoqian Dai, Ma Shuguang, Fei Yu, Jiaqing Liang, Yanghua Xiao
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.165/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.165.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.165
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models rely on long chain-of-thought to achieve strong performance, but applying such reasoning uniformly incurs high computational cost. Existing efficiency-oriented methods attempt to shorten or mix reasoning strategies, yet often degrade reasoning capability. We identify the root cause as sequence-level coupling between efficiency incentives and correctness optimization, which implicitly penalizes long but correct reasoning trajectories. To address this issue, we propose Adaptive Dual-Process Thinking (ADaPT), a token-level dual-process framework that explicitly decouples efficiency and correctness signals during training. ADaPT introduces a mode-selection token to control fast and slow reasoning, applying efficiency-related rewards exclusively to this token to avoid penalizing correct long reasoning while encouraging efficiency when appropriate. Moreover, ADaPT enables precise and continuous control over the efficiency–performance trade-off at inference time: by adjusting the generation probability of the mode-selection token, a single trained model can smoothly move along the efficiency–performance Pareto frontier. Extensive experiments demonstrate that ADaPT significantly reduces inference cost while maintaining strong reasoning performance across multiple benchmarks.

---

Record id: `doi:10.18653/v1/2026.findings-acl.165`
