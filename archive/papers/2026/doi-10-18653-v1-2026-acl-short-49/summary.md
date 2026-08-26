<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Skill-Aware Data Selection and Fine-Tuning for Data-Efficient Reasoning Distillation

- **Authors**: Lechen Zhang, Yunxiang Zhang, Wei Hu, Lu Wang
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-short.49/>
- **PDF**: <https://aclanthology.org/2026.acl-short.49.pdf>
- **DOI**: 10.18653/v1/2026.acl-short.49
- **Topics**: overthinking
- **Relevance score**: overthinking 0.57

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large reasoning models such as DeepSeek-R1 and their distilled variants achieve strong performance on complex reasoning tasks. Yet, distilling these models often demands large-scale data for supervised fine-tuning (SFT), motivating the pursuit of data-efficient training methods. To address this, we propose a skill-centric distillation framework that efficiently transfers reasoning ability to weaker models with two components: (1) Skill-based data selection, which prioritizes examples targeting the student model’s weaker skills, and (2) Skill-aware fine-tuning, which encourages explicit skill decomposition during problem solving. With only 1,000 training examples selected from a 100K teacher-generated corpus, our method surpasses random SFT baselines by +1.6% on Qwen3-4B and +1.4% on Qwen3-8B across five mathematical reasoning benchmarks. Further analysis confirms that these gains concentrate on skills emphasized during training, highlighting the effectiveness of skill-centric training for efficient reasoning distillation.

---

Record id: `doi:10.18653/v1/2026.acl-short.49`
