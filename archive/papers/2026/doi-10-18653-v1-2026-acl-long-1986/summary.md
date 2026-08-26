<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Reasoning Traces Shape Outputs but Models Won’t Say So

- **Authors**: Yijie Hao, Lingjie Chen, Ali Emami, Joyce C. Ho
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1986/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1986.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1986
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Can we trust the reasoning traces that large reasoning models (LRMs) produce? We investigate whether these traces faithfully reflect what drives model outputs, and whether models will honestly report their influence. We introduce Thought Injection, a method that injects synthetic reasoning snippets into a model’s reasoning trace, then measures whether the model follows the injected reasoning and acknowledges doing so. Across 45,000 samples from three LRMs, we find that injected hints reliably alter outputs, confirming that reasoning traces causally shape model behavior. However, when asked to explain their changed answers, models overwhelmingly refuse to disclose the influence: non-disclosure exceeds 90% for extreme hints across 30,000 follow-up samples. Instead of acknowledging the injected reasoning, models fabricate aligned-appearing but unrelated explanations. Activation analysis reveals that sycophancy- and deception-related directions are strongly activated during these fabrications, suggesting systematic patterns rather than incidental failures. Our findings reveal a gap between the reasoning LRMs follow and the reasoning they report, raising concern that aligned-appearing explanations may not be equivalent to genuine alignment.

---

Record id: `doi:10.18653/v1/2026.acl-long.1986`
