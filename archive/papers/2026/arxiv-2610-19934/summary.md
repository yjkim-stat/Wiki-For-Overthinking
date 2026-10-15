<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# To Reason but Not to Stop: Understanding and Recovering Pruned Large Reasoning Models

- **Authors**: Minh-Anh Nguyen, Nguyen T. Ha Lan, Xiyan Fu, Dung D. Le, Wei Lu
- **Venue**: cs.CL
- **Published**: 2026-10-14
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2610.19934>
- **PDF**: <https://arxiv.org/pdf/2610.19934v1>
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Weight pruning can degrade the accuracy of large reasoning models (LRMs), yet it remains unclear whether it damages reasoning itself. We find that much of this degradation stems from a failure to stop rather than to reason. As sparsity increases, pruned LRMs increasingly fail to terminate within the token budget, often after the correct answer has appeared in their reasoning, instead falling into repetitive loops, even though they still recognize where the dense model would stop. We further find that the hidden-state difference between terminating and looping continuations is consistent across pruned checkpoints, suggesting a shared direction associated with committing to an answer. Building on this, we propose Termination-Guided Activation Steering (TGAS), a training-free method that adds this direction to the residual stream at inference time. Across six LRMs, three pruning pipelines, and math and code benchmarks, TGAS improves termination and overall accuracy while reducing repetitive reasoning and generation length, showing that this failure is actionable.

---

Record id: `arxiv:2610.19934`
