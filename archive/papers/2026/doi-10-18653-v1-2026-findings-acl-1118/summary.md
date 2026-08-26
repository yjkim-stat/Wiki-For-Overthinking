<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models

- **Authors**: Yingzhi Mao, Chunkang Zhang, Junxiang Wang, Xinyan Guan, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1118/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1118.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1118
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) achieve strong performance on complex multi-step reasoning, yet they still exhibit severe safety failures such as harmful content generation. Existing methods often apply coarse-grained constraints over the entire reasoning trajectories, which can undermine reasoning capability while failing to address the root causes of unsafe behavior. In this work, we uncover a previously underexplored failure mode in LRMs, termed Self-Jailbreak, where models initially recognize the harmful intent of a query, but override this judgment during subsequent reasoning steps, ultimately generating unsafe outputs. Such a phenomenon reveals that LRMs are capable of recognizing harm, while safety failures primarily arise from reasoning steps. Motivated by this finding, we propose Chain-of-Guardrail (CoG), a trajectory-level training framework that mitigates Self-Jailbreak via targeted, step-level interventions while maintaining reasoning ability. Experiments across multiple safety and reasoning benchmarks indicate that CoG achieves a favorable balance between safety and reasoning performance compared with existing approaches.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1118`
