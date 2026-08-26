<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# S2O: Early Stopping for Sparse Attention via Online Permutation

- **Authors**: Yu Zhang, Songwei Liu, Chenqian Yan, Linsheng, Beichen Ning, Fangmin Chen, Xing Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.351/>
- **PDF**: <https://aclanthology.org/2026.acl-long.351.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.351
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Attention scales quadratically with sequence length, fundamentally limiting long-context inference.Existing block-granularity sparsification can reduce latency, but coarse blocks impose an intrinsic sparsity ceiling, making further improvements difficult even with carefully engineered designs.We present S2O, which performs early stopping for sparse attention via online permutation.Inspired by virtual-to-physical address mapping in memory systems, S2O revisits and factorizes FlashAttention execution, enabling inference to load non-contiguous tokens rather than a contiguous span in the original order.Motivated by fine-grained structures in attention heatmaps, we transform explicit permutation into an online, index-guided, discrete loading policy; with extremely lightweight preprocessing and index-remapping overhead, it concentrates importance on a small set of high-priority blocks.Building on this importance-guided online permutation for loading, S2O further introduces an early-stopping rule: computation proceeds from high to low importance; once the current block score falls below a threshold, S2O terminates early and skips the remaining low-contribution blocks, thereby increasing effective sparsity and reducing computation under a controlled error budget.As a result, S2O substantially raises the practical sparsity ceiling.On Llama-3.1-8B under a 128K context, S2O reduces single-operator MSE by 3.82× at matched sparsity, and reduces prefill compute density by 3.31× at matched MSE; meanwhile, it preserves end-to-end accuracy and achieves 7.51× attention and 3.81× end-to-end speedups.

---

Record id: `doi:10.18653/v1/2026.acl-long.351`
