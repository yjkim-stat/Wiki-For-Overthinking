<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# NEAT: Neuron-Based Early Exit for Large Reasoning Models

- **Authors**: Kang Liu, YongKang Liu, Xiaocui Yang, Peidong Wang, Wen Zhang, Shi Feng, Yifei Zhang, Daling Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1231/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1231.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1231
- **Topics**: overthinking
- **Relevance score**: overthinking 0.70

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) often suffer from overthinking, a phenomenon in which redundant reasoning steps are generated after a correct solution has already been reached. Existing early reasoning exit methods primarily rely on output-level heuristics or trained probing models to skip redundant reasoning steps, thereby mitigating overthinking. However, these approaches typically require additional rollout computation or externally labeled datasets. In this paper, we propose NEAT, a Neuron-based Early reAsoning exiT framework that monitors neuron-level activation dynamics to enable training-free early exits, without introducing any additional test-time computation. NEAT identifies exit-associated neurons and tracks their activation patterns during reasoning to dynamically trigger early exit or suppress reflection, thereby reducing unnecessary reasoning while preserving solution quality. Experiments on four reasoning benchmarks across six models with different scales and architectures show that, for each model, NEAT achieves an average token reduction of 22% to 28% when averaged over the four benchmarks, while maintaining accuracy.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1231`
