<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression

- **Authors**: Mengting Ai, Jingrui He, Yue Guo
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.01631>
- **PDF**: <https://arxiv.org/pdf/2608.01631v1>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, reasoning-training 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

KV cache compression is commonly evaluated by final-answer accuracy, implicitly assuming that preserving the answer also preserves the reasoning that supports it. We test this assumption for large reasoning models and show that it can fail: under compression, correct answers and the validity of their visible supporting rationales can be preserved at different rates. We study this failure with a controlled fixed-trace replay protocol, which holds reasoning content fixed and isolates whether compression preserves usable information from an already available trace. We evaluate ten token-eviction KV compression methods and one quantization method on three models across mathematical reasoning, scientific QA, clinical calculation, and long-context retrieval. We measure final accuracy, answer-chain consistency, and perturbation faithfulness. Across tasks, token-eviction methods can preserve competitive final-answer accuracy while substantially degrading chain support or perturbation faithfulness. We call this the answer-evidence gap. A coverage-preserving quantization control is substantially less affected, suggesting that the failure is tied less to KV memory reduction itself than to losing access to parts of the reasoning trace. Code is available at https://github.com/famous-blue-raincoat/Safe_KV_Compress.

---

Record id: `arxiv:2608.01631`
