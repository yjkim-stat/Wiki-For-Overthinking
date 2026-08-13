<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

- **Authors**: Björn Engdahl, Adrian Kosowski, Jan Chorowski, Zuzanna Stamirowska, Przemysław Uznański, Junlin Jiang, Rohan Phadke, Remigiusz Kinas, Richard Zhong
- **Venue**: cs.NE
- **Published**: 2026-08-10
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.09888>
- **PDF**: <https://arxiv.org/pdf/2608.09888v1>
- **Topics**: reasoning-faithfulness
- **Relevance score**: reasoning-evaluation 0.25, reasoning-faithfulness 0.50, reasoning-training 0.25

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verbalizing its intermediate reasoning. We evaluate the model on the public ARC-AGI-1 evaluation set and use controlled ARC-like interventions to study what it learns from demonstrations, how consistently it applies an inferred transformation, and which concepts remain difficult. A 150M-parameter configuration reaches 29.5% pass@2 at a computed inference cost of \$0.0007 per task. This operating point breaks through the previously reported ARC-AGI-1 cost-accuracy Pareto frontier, establishing a new state of the art in benchmark cost efficiency.

---

Record id: `arxiv:2608.09888`
