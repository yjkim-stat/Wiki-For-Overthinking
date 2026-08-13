<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Thought-Level Beam Search for Reasoning

- **Authors**: Lijie Yang, Hongyin Luo, Jiawei Zhao, Tri Dao, Ravi Netravali
- **Venue**: cs.AI
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08020>
- **PDF**: <https://arxiv.org/pdf/2608.08020v2>
- **Topics**: reasoning-training
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.25, reasoning-training 0.40, test-time-scaling 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Test-time compute scaling is a primary driver of performance in large reasoning models (LRMs), but extreme inefficiency bounds current approaches, shifting the critical question from \emph{how much} compute to spend, to \emph{where} to allocate it. We formalize test-time reasoning as a constrained compute allocation problem over partial trajectories. Under a fixed hardware budget, existing paradigms fail to actively allocate the compute to the most promising partial progress: traditional parallel sampling treats traces independently and induces severe memory bottlenecks, while subtractive pruning starves hardware and fails to actively and sufficiently shift the output distribution. To overcome this dichotomy, we introduce Gambit, an inference algorithm that executes \emph{thought-level beam search}. By periodically pruning unpromising trajectories and immediately branching from high-quality prefixes, Gambit dynamically concentrates compute onto the most promising reasoning traces via a light-weight scorer probing hidden states while maintaining continuous high hardware utilization. Extensive evaluations across multiple models and benchmarks demonstrate that Gambit strictly dominates existing baselines. Under identical hardware constraints, our method yields up to a +6.7\% absolute accuracy gain on HMMT-24 and +3.3\% on AIME-25 over pruning baselines, delivers $>2\times$ higher throughput on trace completion, and reduces total token consumption by up to 68.5\% relative to standard parallel sampling.

---

Record id: `arxiv:2608.08020`
