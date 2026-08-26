<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Compute Optimal Scaling of Skills: Knowledge vs Reasoning

- **Authors**: Nicholas Roberts, Niladri S. Chatterji, Sharan Narang, Mike Lewis, Dieuwke Hupkes
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2025.findings-acl.688/>
- **PDF**: <https://aclanthology.org/2025.findings-acl.688.pdf>
- **DOI**: 10.18653/v1/2025.findings-acl.688
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Scaling laws are a critical component of the LLM development pipeline, most famously as a way to forecast training decisions such as ‘compute-optimally’ trading-off parameter count and dataset size, alongside a more recent growing list of other crucial decisions. In this work, we ask whether compute-optimal scaling behaviour can be skill-dependent. In particular, we examine knowledge and reasoning-based skills such as knowledge-based QA and code generation, and we answer this question in the affirmative: scaling laws are skill-dependent. Next, to understand whether skill-dependent scaling is an artefact of the pretraining datamix, we conduct an extensive ablation of different datamixes and find that, also when correcting for datamix differences, knowledge and code exhibit fundamental differences in scaling behaviour. We conclude with an analysis of how our findings relate to standard compute-optimal scaling using a validation set, and find that a misspecified validation set can impact compute-optimal parameter count by nearly 50%, depending on its skill composition.

---

Record id: `doi:10.18653/v1/2025.findings-acl.688`
