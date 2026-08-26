<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations

- **Authors**: Bowen Zuo, Dongruo Zhou, Yinglun Zhu
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1754/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1754.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1754
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

While scaling test-time compute can substantially improve model performance, existing approaches either rely on static compute allocation or sample from fixed generation distributions.In this work, we introduce a test-time compute allocation framework that jointly adapts where computation is spent and how generation is performed. Our method begins with a warm-up phase that identifies easy queries and assembles an initial pool of question-response pairs from the test set itself. An adaptive phase then concentrates further computation on unresolved queries while reshaping their generation distributions through evolving in-context demonstrations—conditioning each generation on successful responses from semantically related queries rather than resampling from a fixed distribution.Experiments across math, coding, and reasoning benchmarks demonstrate that our approach consistently outperforms existing baselines while consuming substantially less inference-time compute.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1754`
