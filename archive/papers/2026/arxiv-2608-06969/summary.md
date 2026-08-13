<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Finding Usable Weight Mechanisms with Tiled SVD

- **Authors**: Ash Manvi, Samreena Tajreen
- **Venue**: cs.AI
- **Published**: 2026-08-07
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.06969>
- **PDF**: <https://arxiv.org/pdf/2608.06969v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

The dominant approach to mechanistic interpretability trains proxy dictionaries such as sparse autoencoders and labels features from max-activating text. The best such atlases identify con- cepts, but that identity lives in the learned dictionary rather than in the network weights them- selves. We propose extracting mechanism mounts directly from linear sites by column-tiled SVD: each mount is a triple (v,u,σ) read as trigger, write, and strength. Identity is the weight rule. We evaluate mounts with a pre-registered suite judged on full-write energy lift rather than tile-local lift. On Gemma-2-2B with WikiText-2 (16,384-token subsample), all seven linear maps are scored: residual writes (mlp.down, attn.o) receive full A/B/C with steer after post-sublayer RMSNorm and pass 52/52 site-layers; other maps receive A/B only (mlp.gate/attn.q/attn.k/effective mlp.up/attn.v 26/26 each). Aggregate: 182/182 GO. We release library code, the corpus builder, the experiment entrypoint, and unit tests.

---

Record id: `arxiv:2608.06969`
