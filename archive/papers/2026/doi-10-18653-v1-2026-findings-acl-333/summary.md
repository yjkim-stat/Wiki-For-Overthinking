<!-- Generated from data/. Do not edit by hand: edits are overwritten on the next render. Put hand-written notes in the wiki instead. -->

# TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models

- **Authors**: Yi Zhao, Yajuan Peng, Cam-Tu Nguyen, Zuchao Li, Xiaoliang Wang, Xiaoming Fu, Hai Zhao
- **Venue**: ACL
- **Published**: unknown
- **Source**: anthology
- **Link**: <https://aclanthology.org/2026.findings-acl.333/>
- **PDF**: <https://aclanthology.org/2026.findings-acl.333.pdf>
- **DOI**: 10.18653/v1/2026.findings-acl.333
- **Topics**: overthinking
- **Relevance score**: overthinking 0.50

## Summary

_Not summarized yet. A task is queued under `data/queue/pending/`._

## Abstract

Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chains of thought but suffer from high inference latency due to autoregressive reasoning. Recent work explores using Small Reasoning Models (SRMs) to accelerate LRM inference, yet existing frameworks such as SpecReason adopt a polling-based design that repeatedly invokes the LRM for verification at every step. This approach is inefficient, as frequent LRM calls introduce a high computational overhead, and is unreliable, since the LRM as a judge is prone to errors. In this paper, we systematically characterize the capability boundaries of SRMs and identify three common types of reasoning risks: (1) path divergence, where SRMs lack the strategic ability to construct an initial plan, causing reasoning to deviate from the most probable path; (2) cognitive overload, where SRMs fail to solve particularly difficult steps; and (3) recovery inability, where SRMs lack robust self-reflection and error correction mechanisms. To address these challenges, we propose TrigReason, a trigger-based collaborative reasoning framework that replaces continuous polling with selective intervention. TrigReason delegates most reasoning to the SRM and activates LRM intervention only when necessary—during initial strategic planning (strategic priming trigger), upon detecting extraordinary overconfidence (cognitive offload trigger), or when reasoning falls into unproductive loops (intervention request trigger). The evaluation results on AIME24, AIME25, and GPQA-D indicate that TrigReason matches the accuracy of full LRMs and SpecReason, while offloading 1.70×–4.79× more reasoning steps to SRMs. Under edge–cloud conditions, TrigReason reduces latency by 43.9% and API cost by 73.3% compared to SpecReason.

---

Record id: `doi:10.18653/v1/2026.findings-acl.333`
