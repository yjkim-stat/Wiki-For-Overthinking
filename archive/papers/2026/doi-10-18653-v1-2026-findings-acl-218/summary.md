<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Finding RELIEF: Shaping Reasoning Behavior without Reasoning Supervision via Belief Engineering

- **Authors**: Chak Tou Leong, Dingwei Chen, Heming Xia, Qingyu Yin, Sunbowen Lee, Jian Wang, Wenjie Li
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.218/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.218.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.218
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) have achieved remarkable success through step-by-step chains of thought, yet they often suffer from excessive redundancy or unfaithful reasoning. Existing methods for shaping LRM behavior typically rely on reinforcement learning or fine-tuning with gold-standard reasoning traces, a paradigm that is both computationally expensive and difficult to scale. In this paper, we reveal that LRMs possess latent reasoning beliefs that internally track their own reasoning traits, which can be captured through simple logit probing without specialized training. Building on this insight, we propose Reasoning Belief Engineering (RELIEF), a simple yet effective framework that shapes LRM behavior by aligning the model’s self-concept with a target belief blueprint. Crucially, RELIEF completely bypasses the need for reasoning-trace supervision. It internalizes desired traits by fine-tuning on synthesized, self-reflective QA pairs that affirm the target belief. Extensive experiments on efficiency and faithfulness tasks demonstrate that RELIEF matches or outperforms behavior-supervised and preference-based baselines while requiring significantly lower training costs. Our analysis further validates that shifting a model’s reasoning belief effectively shapes its actual behavior.

---

Record id: `doi:10.18653/v1/2026.findings-acl.218`
