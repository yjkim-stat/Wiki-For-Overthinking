<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think Better, Not Longer: Token-Level Marginal Utility for Efficient Reasoning in Large Reasoning Models

- **Authors**: Jiawei Li, Yang Gao, Huashan Sun, Chong Feng
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1386/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1386.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1386
- **Topics**: overthinking
- **Relevance score**: overthinking 0.73

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While Large Reasoning Models (LRMs) have demonstrated remarkable capabilities through explicit Chain-of-Thought (CoT) generation, they frequently suffer from “overthinking”. In this work, we bridge this gap by introducing Token-level Marginal Utility, which quantifies the per-token log-probability gain of the ground-truth answer. Leveraging this dense supervision signal, we propose MUTO (Marginal Utility Guided Thinking Optimization), a unified training framework designed to synthesize concise reasoning chains. Rather than relying only on coarse trajectory-level length control, MUTO identifies tokens that reduce the model’s likelihood of the correct answer and penalizes such negative-utility reasoning, yielding concise yet effective CoT trajectories. Experiments on DeepSeek-R1-Distill-Qwen backbones (1.5B and 7B) across six math reasoning benchmarks show that MUTO yields a markedly better efficiency-accuracy Pareto frontier. It reduces average token usage by 87.1% at 1.5B while improving accuracy by 2.3%, and cuts tokens by 80.2% at 7B with only -0.1% accuracy change, achieving the best length-normalized accuracy among baselines.

---

Record id: `doi:10.18653/v1/2026.acl-long.1386`
