<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs

- **Authors**: Qibin Wang, Pu Zhao, Shaohan Huang, Fangkai Yang, Lu Wang, Furu Wei, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1291/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1291.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1291
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time scaling (TTS) has gained widespread attention for enhancing LLM reasoning. Existing approaches such as Best-of-N and majority voting are limited as their performance depends on the quality of candidate responses, making them unable to produce a correct solution when all candidates are incorrect. Parallel self-refinement, generating multiple candidates and synthesizing a refined answer conditioned on them, offers a promising alternative, but the underlying mechanism driving its effectiveness remains obscure. To bridge this gap in understanding, we introduce a new metric, the Refinement Gap, designed to quantify the relative improvement of self-refinement beyond majority voting. We show that the Refinement Gap exhibits a clear scaling trend with model size and is only weakly correlated with the base capability. Based on this discovery, we propose Generative Self-Refinement (GSR), a parallel test-time scaling framework that transfers the refinement policy from larger teacher models with higher refinement gap into smaller students. Crucially, GSR jointly trains a single model to generate strong candidates and refine a better final answer based on these candidates. Experimental results demonstrate that our method achieves state-of-the-art performance across five mathematical benchmarks over other parallel aggregation methods, while the learned refinement skill transfers across multiple model scales and families and exhibits robust generalization to an out-of-distribution domain.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1291`
