<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning

- **Authors**: Yongchan Kwon, Shang Zhu, Federico Bianchi, Kaitlyn Zhou, James Zou
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.1456/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.1456.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.1456
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

The ability of large language models (LLMs) to follow user instructions is central to their reliability, safety, and usefulness. While prior studies assess instruction adherence in the model’s main responses, we argue that it is also critical for large reasoning models (LRMs) to follow user instructions throughout their reasoning process. Reasoning instruction following makes LRMs more controllable and transparent, while reducing risks of undesirable shortcuts, hallucinations, or reward hacking within reasoning traces. To evaluate this dimension, we introduce ReasonIF, a systematic benchmark for assessing reasoning instruction following. ReasonIF includes six categories of instruction prompts, spanning multilingual reasoning, and length control. Across many open-source LRMs including GPT-OSS, Qwen3, and DeepSeek-R1, we find substantial failures in reasoning instruction adherence: the highest instruction following score (IFS) remains below 0.25, meaning that fewer than 25% of reasoning traces comply with the given instructions. Notably, as task difficulty increases, reasoning instruction following degrades further. We also explore two strategies to enhance reasoning instruction fidelity: (1) multi-turn reasoning and (2) Reasoning Instruction Finetuning (RIF) using synthetic data. RIF improves the IFS of GPT-OSS-20B from 0.11 to 0.27, indicating measurable progress but leaving ample room for improvement. We hope this work draws attention to reasoning-level instruction adherence as an underexplored but critical aspect of model alignment, and helps pave the way toward more controllable, interpretable, and trustworthy reasoning models.

---

Record id: `doi:10.18653/v1/2026.findings-acl.1456`
