<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Probing and steering biology across Boltz-1s trunk-diffusion boundary

- **Authors**: Piotr Jedryszek, Tongmeng Xie, Adam Winnifrith, Alexander Hasson, Weronika Ślesak, George Wicks, Toby Winnifrith, Oliver M. Crook
- **Venue**: q-bio.QM
- **Published**: 2026-08-11
- **Source**: arxiv
- **Link**: <https://arxiv.org/abs/2608.11475>
- **PDF**: <https://arxiv.org/pdf/2608.11475v1>
- **Topics**: reasoning-interpretability
- **Relevance score**: reasoning-interpretability 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

AlphaFold3-class structure predictors pair a representational trunk, which processes sequence and context, with a diffusion module, which generates atomic coordinates. How biological information changes as it crosses this architectural boundary remains poorly understood. We analyze per-residue activations from the Pairformer trunk and diffusion module of Boltz-1 using linear probes, sparse autoencoders (SAEs), and causal interventions. From the trunk, both geometry (secondary structure, disorder) and sequence chemistry (amino-acid identity, signal peptides, disulfide-bond annotations) are linearly decodable. In the diffusion module, the two diverge. Secondary structure transfers essentially unchanged, whereas sequence chemistry is strongly attenuated. We then test whether decodable directions can steer the model, intervening on the final trunk single representation that conditions the diffusion module. Helix and coil directions change predicted structure dose-dependently against matched-norm random controls, but a beta-strand direction that is highly predictive (F1 =0.82) produces no measurable increase in strand content: linear decodability does not imply causal influence at the site we tested. The same probes also score markedly lower against sparse SwissProt annotations than against dense DSSP labels, because unannotated residues that the model gets right are charged as false positives; such scores are therefore lower bounds. Finally, supervised probes outscore single SAE features wherever a label already exists. We release the trained trunk and diffusion SAEs, Boltz-1 per-residue activations, and the analysis code.

---

Record id: `arxiv:2608.11475`
