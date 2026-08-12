<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs

- **Authors**: Iaroslav Chelombitko, Ekaterina Chelombitko, Mika Hämäläinen
- **Venue**: cs.CL
- **Published**: 2026-08-03
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.02486>
- **PDF**: <https://arxiv.org/pdf/2608.02486v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Open-source LLMs reliably name Zeus, Jupiter, and Thor, but recover their counterparts in less-represented traditions like Finnish, Slavic, Egyptian, or Chinese mythology far less consistently. We ask where inside the model this cultural default is produced. On a parallel cross-cultural substrate of Thompson-motif entities, we instrument 18 open-source LLMs from 8 architecture families with linear probing, logit lens, activation patching, and output extraction. The residual stream cleanly distinguishes cultures, well above a name-string baseline, yet the decoder collapses culturally-specific tokens onto dominant-tradition ones. The failure is at readout, not at representation. Asking the same question in the target culture's native language versus English produces failures that cluster within language but decouple across language: the decoder is gated on prompt language. We release a per-entity (probe, output) decomposition framework, a citation-anchored cross-cultural ground truth, a within- versus cross-mode correlation test for language-conditioned readout, and per-entity predictions for all 18 models.

---

Record id: `arxiv:2608.02486`
