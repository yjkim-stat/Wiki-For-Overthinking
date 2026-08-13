<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Safety Cost of Steering Vectors Is Separable and Reducible

- **Authors**: Yuxiao Li, Gjergji Kasneci
- **Venue**: cs.CL
- **Published**: 2026-08-09
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.08383>
- **PDF**: <https://arxiv.org/pdf/2608.08383v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Steering vectors are a lightweight tool for controlling LLM behavior. However, emerging evidence shows that steering vectors can unintentionally compromise a model's safety mechanisms and increase compliance with harmful requests, while no effective mitigation yet exists. In this work, we show that this safety degradation arises from a separable component in the vector that disrupts the model's safety mechanisms but contributes little to the steering objective. We identify and remove this safety-degrading component, formulating the task as a constrained optimization problem solved through primal-dual updates, subject to preserving the intended steering effect and bounding false refusal. The resulting solution is both interpretable and surgical: the optimization recovers a single direction whose ablation from the steering vector restores model safety with minimal utility cost. Across models, steering behaviors, and attack suites, including unseen attacks types, our method substantially reduces steering-induced safety degradation while preserving the original steering effect with minimal impact on false refusal. Our method offers a post-hoc correction to steering vectors that mitigates their safety cost, and more broadly, it provides a general recipe for applying activation-level model interventions without paying a safety tax.

---

Record id: `arxiv:2608.08383`
