<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Pru-CoT: Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought

- **Authors**: Han Liu, Shuotian Ma, Hui Li, Xiaotong Zhang, Fenglong Ma, Hong Yu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1684/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1684.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1684
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Knowledge distillation has emerged as a pivotal paradigm for transferring the superior reasoning capabilities of Large Reasoning Models (LRMs) to efficient student models. However, the raw Chain-of-Thought (CoT) trajectories are often verbose and redundant, which dilutes the underlying logic and hinders effective knowledge distillation for student models. Although recent work has focused on pruning CoT to streamline these reasoning paths, existing local heuristic methods often fail to capture global causal logic due to rigid rules and limited search spaces, while global heuristic approaches incur substantial computational costs. To address these issues, we propose Pru-CoT (Pruning Chain-of-Thought), a framework that aims to extract the essential logical structure from reasoning chains. Pru-CoT implements a step-level importance assessment via global optimization on a frozen student large language model (LLM), quantifying the gradient-based causal contribution of each component. Guided by these important signals, the framework performs fidelity-constrained pruning, utilizing an LLM-driven process to synthesize concise, logically coherent narratives. Extensive experiments on mathematical reasoning benchmarks demonstrate that models trained with Pru-CoT not only achieve superior accuracy but also generate significantly more compact reasoning paths compared to those trained on raw verbose data.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1684`
