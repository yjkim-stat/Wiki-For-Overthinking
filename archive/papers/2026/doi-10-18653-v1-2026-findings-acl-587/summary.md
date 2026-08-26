<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation

- **Authors**: Wei-Rui Chen, Vignesh Kothapalli, Ata Fatahibaarzi, Hejian Sang, Shao Tang, Qingquan Song, Zhipeng Wang, Muhammad Abdul-Mageed
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.587/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.587.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.587
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Distilling the capabilities from a large reasoning model (LRM) to a smaller student model often involves training on substantial amounts of reasoning data. However, knowledge distillation (KD) over lengthy sequences with prompt (P), chain-of-thought (CoT), and answer (A) sections makes the process computationally expensive. In this work, we investigate how the allocation of supervision across different sections (P, CoT, A) affects student performance. Our analysis shows that selective KD over only the CoT tokens can be effective when the prompt and answer information is encompassed by it. Building on this insight, we establish a truncation protocol to quantify computation-quality tradeoffs as a function of sequence length. We observe that beyond a specific length, longer training sequences provide marginal returns for downstream performance but require substantially higher memory and FLOPs. To this end, training on only the first 50% of tokens of every training sequence can retain, on average, ≈91% of full-sequence performance on math benchmarks while reducing training time, memory usage, and FLOPs by about 50% each. Codes are available at https://github.com/weiruichen01/distilling-the-essence.

---

Record id: `doi:10.18653/v1/2026.findings-acl.587`
