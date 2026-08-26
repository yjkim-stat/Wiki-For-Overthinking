<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Rhombus: Incentivizing Coordination in Parallel Thinking through Reinforcement Learning

- **Authors**: Ziyuan Nan, Qi Yi, Di Huang, Yutong Wu, Guanhua Huang, Xue Gong, Kejiao Li, Yuhao Jiang, Chenchen Zhang, Zenan Xu, Xing Hu, Bo Zhou
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1956/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1956.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1956
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Parallel thinking offers a promising avenue for scaling test-time compute in Large Language Models (LLMs), enabling them to explore diverse solution paths simultaneously before aggregating them into a final answer. However, coordinating the exploration and aggregation stages remains challenging, as simple aggregation techniques often incur information loss, failing to preserve the subtle, decision-relevant signals generated during exploration. To overcome this, we propose Rhombus, a parallel thinking framework that explicitly incentivizes coordination between components via end-to-end reinforcement learning. Rhombus employs multiple parallel Proposers to generate compact, decision-focused reasoning cues and a central Synthesizer to integrate them into final predictions, utilizing co-training under a shared task reward to align their interaction. Across challenging mathematical reasoning benchmarks, Rhombus improves accuracy by 6.0% over long chain-of-thought baselines while reducing wall-clock latency by 39.4% under matched token budgets. Our work demonstrates that explicit communication optimization is essential for realizing the accuracy and efficiency gains of parallel reasoning.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1956`
