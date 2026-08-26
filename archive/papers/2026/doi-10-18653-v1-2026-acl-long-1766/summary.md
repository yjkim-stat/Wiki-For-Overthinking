<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Think How to Think: Mitigating Overthinking with Autonomous Difficulty Cognition in Large Reasoning Models

- **Authors**: Yongjiang Liu, Haoxi Li, Xiaosong Ma, Jie Zhang, Song Guo
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1766/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1766.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1766
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Recent Large Reasoning Models (LRMs) excel at complex reasoning tasks but often suffer from overthinking, generating overly long and redundant reasoning trajectories. To explore its essence, our empirical analysis reveals that LRMs are primarily limited to recognizing task properties (i.e., difficulty levels) like humans before solving the problem, leading to a one-size-fits-all reasoning strategy. This observation motivates a fundamental question: Can we explicitly bootstrap such ability to alleviate overthinking in LRMs? To this end, we propose Think-How-to-Think (TH2T), a novel two-stage fine-tuning strategy that progressively inspires LRMs’ difficulty cognition and redundancy cognition of LRMs. Specifically, we first inject Difficulty Dypnosis into output prefixes as cues for global, prospective reasoning strategy selection, stimulating the model’s sharper sensitivity to task complexity and adaptive control of reasoning depth. Then, we incorporate Redundancy Hypnosis into in-progress reasoning steps, which serve as local, retrospective signals for behavior correction by identifying and eliminating superfluous reasoning detours. Experiments across 7B/14B/32B models demonstrate that TH2T significantly reduces inference costs by over 70% on easy tasks and 40% on complex ones without compromising performance. The resultant models exhibit a nascent ability for difficulty-aware reasoning, effectively mitigating behaviors like excessive reflection and looping, thereby paving the way for more cognitively efficient LRMs.

---

Record id: `doi:10.18653/v1/2026.acl-long.1766`
