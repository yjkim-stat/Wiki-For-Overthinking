<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# When Is Thinking Enough? Early Exit via Sufficiency Assessment for Efficient Reasoning

- **Authors**: Yang Xiang, Yixin Ji, Ruotao Xu, Dan Qiao, Zheming Yang, Juntao Li, Min Zhang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1080/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1080.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1080
- **Topics**: overthinking
- **Relevance score**: overthinking 0.75

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models (LRMs) have achieved remarkable performance in complex reasoning tasks, driven by their powerful inference-time scaling capability.However, LRMs often suffer from overthinking, which results in substantial computational redundancy and significantly reduces efficiency.Early-exit methods aim to mitigate this issue by terminating reasoning once sufficient evidence has been generated, yet existing approaches mostly rely on handcrafted or empirical indicators that are unreliable and impractical.In this work, we introduce Dynamic Thought Sufficiency in Reasoning (DTSR), a novel framework for efficient reasoning that enables the model to dynamically assess the sufficiency of its chain-of-thought (CoT) and determine the optimal point for early exit.Inspired by human metacognition, DTSR operates in two stages: (1) Reflection Signal Monitoring, which identifies reflection signals as potential cues for early exit, and (2) Thought Sufficiency Check, which evaluates whether the current CoT is sufficient to derive the final answer.Experimental results on the Qwen3 models show that DTSR reduces reasoning length by 28.9%–34.9% with minimal performance loss, effectively mitigating overthinking.We further discuss overconfidence in LRMs and self-evaluation paradigms, providing valuable insights for early-exit reasoning.

---

Record id: `doi:10.18653/v1/2026.acl-long.1080`
