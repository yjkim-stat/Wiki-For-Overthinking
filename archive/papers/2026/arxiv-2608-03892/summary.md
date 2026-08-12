<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition

- **Authors**: Michal Mráz, Justin Shenk
- **Venue**: cs.AI
- **Published**: 2026-08-04
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.03892>
- **PDF**: <https://arxiv.org/pdf/2608.03892v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, and a TravelPlanner capability benchmark. The central result is that temporal-horizon directions can be identified with simple contrastive linear probes and then used for steering to induce large, bidirectional preference changes. On an out-of-distribution monetary choice task that varies reward size and delay, steering strongly shifts the model's indifference threshold between smaller-sooner and larger-later rewards in both directions. We further show improvements on a planning-related capability metric under moderate temporal steering. These results suggest that model intertemporal preferences are measurable and steerable, which is relevant for AI systems that give advice involving delayed costs and benefits, and for safety questions about long-horizon planning.

---

Record id: `arxiv:2608.03892`
