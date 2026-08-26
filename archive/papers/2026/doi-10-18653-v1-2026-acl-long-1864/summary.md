<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# AdaMix: Adaptive Mixing for Short and Long Reasoning Adapters

- **Authors**: Hao Luo, Xiao Yan, Xinyan Li, Qiming Zeng, Yuhao Lin, Shanshan Feng, Hao Wang, Jiawei Jiang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-long.1864/>
- **PDF**: <https://aclanthology.org/2026.acl-long.1864.pdf>
- **DOI**: 10.18653/v1/2026.acl-long.1864
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by generating detailed Chain-of-Thought (CoT) reasoning. However, they tend to apply a uniform, computation-intensive deep reasoning strategy to all problems, leading to unnecessary overhead on simple tasks. This significantly hinders their efficiency in real-world applications. While existing methods have improved reasoning efficiency to some extent, they still face critical challenges such as conflicting objectives, limited adaptability. To address these limitations, we propose AdaMix, an adaptive reasoning framework via decoupled optimization. To mitigate optimization conflicts, AdaMix first constructs two specialized adapters: an efficiency-oriented short adapter and an accuracy-oriented long adapter. It then incorporates a difficulty-aware routing model that assesses problem complexity to predict a reasoning intensity coefficient. This coefficient is used to dynamically interpolate a mixed adapter from the two base adapters, enabling fine-grained reasoning control. Our experiment demonstrates that our AdaMix reduces the average response length of DeepSeek-R1-Distill-Qwen-7B by 54.9% while improving accuracy by up to 4.8% on five mathematical datasets, thus indicating a favorable accuracy-efficiency trade-off.

---

Record id: `doi:10.18653/v1/2026.acl-long.1864`
