<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# "Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders

- **Authors**: Adelaide Danilov, Aria Nourbakhsh, Oleksandr Marchenko Breneur, Salima Lamsiyah
- **Venue**: cs.CL
- **Published**: 2026-08-08
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.07852>
- **PDF**: <https://arxiv.org/pdf/2608.07852v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

How a language model internally represents who is speaking, the Assistant, an assigned roleplay persona, or a narrated story character, remains underexplored. We study speaker representations using a dataset of user-expressed emotional text and corresponding model responses. We decompose three generation settings (Assistant, Roleplay, and Story) into sparse autoencoder features extracted at turn-boundary and pronoun-token positions and selected through a filtering pipeline for different depths. We characterize each surviving feature through its steering effects and activation distribution. Our main finding is that the Assistant and roleplay personas are not independent alternatives: personas retain the Assistant-associated feature core while progressively differentiating from it across layers, starting from operational machinery towards behavioral and stylistic features. Meanwhile, generated story characters lack the Assistant-associated core. Both Story and Roleplay can be distinguished from the Assistant with Immersive Simulation Mode. However, the Assistant can sometimes enter or slowly drift into it even in the default setting.

---

Record id: `arxiv:2608.07852`
