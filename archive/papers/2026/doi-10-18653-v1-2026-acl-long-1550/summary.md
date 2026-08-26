<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Memory efficiency and resource-rational encoding in sentence processing

- **Authors**: Weijie Xu, Brian Dillon, Richard Futrell
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1550/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1550.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1550
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

There is a growing consensus that, in order to serve as models of human language processing, language models (LMs) need to be constrained in their use of memory for context, the analogue to human working memory (WM). Here we take a novel yet simple approach to constraining WM in language models, in a way that reflects models of human cognition where memory is treated as a limited resource and deployed strategically. In order to capture this constraint on memory encoding, we inject noise into the hidden representations of Transformer-based LMs at tunable rates. Then we train the models with a hybrid objective, such that they learn to maximize the performance of next-word prediction subject to explicit constraints on the total encoding precision. We find that explicit WM constraints improve the model’s alignment with human reading times. More importantly, we find that the need to manage encoding precision reshapes the nature of the models’ context representations, making them more compressed and categorical. Our results show how resource-rational models of WM allocation can be implemented in neural models simply and successfully, and point to a dissociation between WM retrieval mechanisms and the underlying memory representations in models of human sentence processing.

---

Record id: `doi:10.18653/v1/2026.acl-long.1550`
