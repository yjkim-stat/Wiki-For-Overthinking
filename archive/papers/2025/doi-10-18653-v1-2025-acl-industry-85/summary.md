<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL

- **Authors**: Hyungjoo Chae, Dongjin Kang, Jihyuk Kim, Beong-woo Kwak, Sunghyun Park, Haeju Park, Jinyoung Yeo, Moontae Lee, Kyungjae Lee
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.acl-industry.85/>
- **PDF**: <https://aclanthology.org/2025.acl-industry.85.pdf>
- **DOI**: 10.18653/v1/2025.acl-industry.85
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

With the release of R1, a publicly available large reasoning model (LRM), researchers commonly train new LRMs by training language models on R1’s long chain-of-thought (CoT) inferences. While prior works show that LRMs’ capabilities can be reproduced through direct distillation, the continued reliance on the existing models (e.g., R1) remains a critical limitation in advancing the field.As a first step toward independent LRM development, this paper explores the possibility of constructing a long CoT dataset with LLMs that are not trained for inference-time scaling.To this end, we present the Long CoT Collection, a dataset of 100K CoT rationales annotated using existing short CoT LLMs. We develop a pipeline that induces o1’s novel reasoning strategies into short CoT LLMs, enabling them to think longer and introducing controllability over the thought budget to better manage the overthinking problem.Our extensive analyses validate that our dataset achieves quality comparable to—or slightly below—R1. Furthermore, our experiments demonstrate that training on our dataset not only strengthens general reasoning skills, but also provides a strong foundation for reinforcement learning—models initialized on our data achieve 2-3x larger gains with RLVR. We make the codes, datasets, and models publicly available at LINK.

---

Record id: `doi:10.18653/v1/2025.acl-industry.85`
