<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning

- **Authors**: Nathanaël Carraz Rakotonirina, Ren Pang, Neha Anna John, Michael Bohlke-Schneider, Momchil Hardalov
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.622/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.622.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.622
- **Topics**: overthinking
- **Relevance score**: overthinking 0.67

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

The reasoning capabilities of large language models (LLMs) have improved substantially through increased test-time computation, typically in the form of intermediate tokens known as chain-of-thought (CoT). However, CoT often becomes unnecessarily long, increasing computation costs without improving accuracy and sometimes even degrading performance, a phenomenon known as “overthinking”. We propose a multi-stage efficient reasoning method that combines supervised fine-tuning—via rejection sampling or reasoning trace reformatting—with reinforcement learning using an adaptive length penalty. We introduce a lightweight reward function that penalizes tokens generated after the first correct answer, encouraging the model to perform self-verification only when beneficial. We conduct a holistic evaluation across seven diverse reasoning tasks, analyzing the accuracy–response length trade-off. Our approach reduces response length by an average of 28% for 8B models and 40% for 32B models, while incurring only minor performance drops of 1.6 and 2.5 points, respectively. Despite its conceptual simplicity, it achieves a better trade-off than more complex state-of-the-art efficient reasoning methods, scoring 76.6 on the area under the Overthinking-Adjusted Accuracy curve (AUCOAA)—5 points above the base model and 2.5 points above the second-best approach.

---

Record id: `doi:10.18653/v1/2026.findings-acl.622`
