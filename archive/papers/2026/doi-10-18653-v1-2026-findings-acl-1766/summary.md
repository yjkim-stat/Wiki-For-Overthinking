<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness

- **Authors**: Hossam Amer, Maryam Dialameh, Hossein Rajabzadeh, Walid Ahmed, Weiwei Zhang, Yang Liu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1766/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1766.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1766
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Scaling training compute, measured in FLOPs, has long been shown to improve the accuracy of large language models, yet training remains resource-intensive. Prior work shows that increasing test-time compute (TTC)—for example through iterative sampling—can allow smaller models to rival or surpass much larger ones at lower overall cost. We introduce TTC-aware training, where an intermediate checkpoint and a corresponding TTC configuration can together match or exceed the accuracy of a fully trained model while requiring substantially fewer training FLOPs. Building on this insight, we propose an early stopping algorithm that jointly selects a checkpoint and TTC configuration to minimize training compute without sacrificing accuracy. To make this practical, we develop an efficient TTC evaluation method that avoids exhaustive search, and we formalize a break-even bound that identifies when increased inference compute compensates for reduced training compute. Experiments demonstrate up to 92% reductions in training FLOPs while maintaining and sometimes remarkably improving accuracy. These results highlight a new perspective for balancing training and inference compute in model development, enabling faster deployment cycles and more frequent model refreshes.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1766`
