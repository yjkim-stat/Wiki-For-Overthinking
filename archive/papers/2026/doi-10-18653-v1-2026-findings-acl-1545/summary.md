<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# PACE: Prefix-Protected and Difficulty-Aware Compression for Efficient Reasoning

- **Authors**: Ruixiang Feng, Yuntao Wen, Silin Zhou, Ke Shi, Yifan Wang, Ran Le, Zhenwei An, Zongchao Chen, Chen Yang, Guangyue Peng, Yiming Jia, Dongsheng Wang, Tao Zhang, Lisi Chen, Yang Song, Shen Gao, Shuo Shang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1545/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1545.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1545
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Language Reasoning Models (LRMs) achieve strong performance by scaling test-time computation but often suffer from “overthinking”, producing excessively long reasoning traces that increase latency and memory usage. Existing LRMs typically enforce conciseness with uniform length penalties, which over-compress crucial early deduction steps at the sequence level and indiscriminately penalize all queries at the group level. To solve these limitations, we propose PACE, a dual-level framework for prefix-protected and difficulty-aware compression under hierarchical supervision. At the sequence level, prefix-protected optimization employs decaying mixed rollouts to maintain valid reasoning paths while promoting conciseness. At the group level, difficulty-aware penalty dynamically scales length constraints based on query complexity, maintaining exploration for harder questions while curbing redundancy on easier ones. Extensive experiments on DeepSeek-R1-Distill-Qwen (1.5B/7B) demonstrate that PACE achieves a substantial reduction in token usage (up to 55.7%) while simultaneously improving accuracy (up to 4.1%) on math benchmarks, with generalization ability to code, science, and general domains.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1545`
