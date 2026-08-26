<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs

- **Authors**: Siyi Li, Jiajun Shi, Shiwen Ni, Ge Zhang, Shuaimin Li, Shijian Wang, Zhoufutu Wen, Yizhi LI, Hamid Alinejad-Rokny, Jiaheng Liu, Min Yang, Wenhao Huang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.2077/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.2077.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.2077
- **Topics**: overthinking
- **Relevance score**: overthinking 0.40

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) have demonstrated strong performance by producing extended Chain-of-Thought (CoT) traces before answering. However, this paradigm often induces over-reasoning: redundant calculations and circular self-verification that increase computational cost without improving outcomes. Existing evaluations largely emphasize final accuracy or coarse token counts, and lack automated tools to separate essential logic from structural redundancy. We introduce CoTJudger, a graph-driven framework that quantifies reasoning efficiency by converting free-form CoTs into directed dependency graphs and extracting the Shortest Effective Path (SEP) needed to reach a correct solution. This yields an interpretable efficiency signal – how much of a CoT is necessary versus structurally redundant – that is comparable across models and tasks. Evaluating 21 LRMs, CoTJudger reveals pervasive redundancy and surfaces recurring failure modes, including verification obsession and compensatory redundancy. These results provide a practical metric for disentangling reasoning ability from computational waste, enabling more targeted evaluation and diagnosis of LRM efficiency.

---

Record id: `doi:10.18653/v1/2026.findings-acl.2077`
