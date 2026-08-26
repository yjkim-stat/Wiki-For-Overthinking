<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# FoE: Forest of Errors Makes the First Solution the Best in Large Reasoning Models

- **Authors**: Kehan Jiang, Haonan Dong, Zhaolu Kang, Zhengzhou Zhu, Guojie Song
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1128/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1128.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1128
- **Topics**: overthinking
- **Relevance score**: overthinking 0.62

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recent Large Reasoning Models (LRMs) like DeepSeek-R1 have demonstrated remarkable success in complex reasoning tasks, exhibiting human-like patterns in exploring multiple alternative solutions. Upon closer inspection, however, we uncover a surprising phenomenon: The First is The Best, where alternative solutions are not merely suboptimal but potentially detrimental. This observation challenges widely accepted test-time scaling laws, leading us to hypothesize that errors within the reasoning path scale concurrently with test time. Through comprehensive empirical analysis, we characterize errors as a forest-structured Forest of Errors (FoE) and conclude that FoE makes the First the Best, which is underpinned by rigorous theoretical analysis. Leveraging these insights, we propose RED, a self-guided efficient reasoning framework comprising two components: I) Refining First, which suppresses FoE growth in the first solution; and II) Discarding Subs, which prunes subsequent FoE via dual-consistency. Extensive experiments across five benchmarks and six backbone models demonstrate that RED outperforms eight competitive baselines, achieving performance gains of up to 19.0% while reducing token consumption by 37.7% 70.4%. Moreover, comparative experiments on FoE metrics shed light on how RED achieves effectiveness.

---

Record id: `doi:10.18653/v1/2026.acl-long.1128`
