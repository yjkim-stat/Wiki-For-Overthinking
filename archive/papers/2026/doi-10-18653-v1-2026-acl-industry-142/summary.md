<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for Efficient Reasoning

- **Authors**: Sanket Badhe, Deep Shah
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.acl-industry.142/>
- **PDF**: <https://aclanthology.org/2026.acl-industry.142.pdf>
- **DOI**: 10.18653/v1/2026.acl-industry.142
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Advanced reasoning typically requires Chain-of-Thought prompting, which is accurate but incurs prohibitive latency and substantial test-time inference costs. The standard alternative, fine-tuning smaller models, often sacrifices interpretability while introducing significant resource and operational overhead. To address these limitations, we introduce Prompt-Level Distillation (PLD). We extract explicit reasoning patterns from a Teacher model and organize them into a structured list of expressive instructions for the Student model’s System Prompt. Evaluated using Gemma-3 4B, PLD improved Macro F1 scores on StereoSet (57% to 90.0%) and Contract-NLI (67% to 83%), while increasing LogiQA accuracy to 70%. Similar results on Mistral Small 3.1 demonstrate cross-architecture generalizability, enabling these compact models to match frontier performance with negligible latency overhead. These expressive instructions render the decision-making process transparent, allowing for full human verification of logic, making this approach ideal for regulated industries such as law, finance, and content moderation, as well as high-volume use cases and edge devices.

---

Record id: `doi:10.18653/v1/2026.acl-industry.142`
